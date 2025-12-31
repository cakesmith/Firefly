import os
from collections import namedtuple

from Toolkit.LookAhead import LookAhead
from Toolkit.functions import flatten, scanpattern, loctoline

import PetriEmitter

class vmcommand(namedtuple('vmcommand', ('command', 'segment', 'index', 'loc'))):
    def __new__(cls, command, segment=None, index=None, loc=None):
        return super(vmcommand, cls).__new__(cls, command, segment, index, loc)
        
class VMParser:

    def __init__(self, programdir, input_extension=".vm"):

        self.emitter = PetriEmitter.PetriEmitter()
        
        self.countlines = 0

        dirname = os.path.dirname(programdir)
        _, self.progname = os.path.split(dirname)
            
        inputfilenames = [os.path.join(programdir, name) for name in os.listdir(programdir) if name.endswith(input_extension)]
        
        self.results = []
        
        for inputfile, self.filename, self.classname in [(open(f), f, os.path.basename(os.path.splitext(f)[0])) for f in inputfilenames]:
            
            try:
                self.results.extend(list(self.parse(inputfile.read())))
                    
            except Exception as exc:
                args = exc.args
                
                if not args:
                    arg0 = ''
                else:
                    arg0 = args[0]
                
                if isinstance(arg0, str):                    
                    arg0 += "\nIn file: { %s } " % self.filename

                exc.args = flatten((arg0, args[1:]))
                raise
                
        print ("commands parsed: %d" % len(self.results))
        
    def _tokenize(text):
        
        zeroargs = "add", "sub", "neg", "lt", "eq", "gt", "and", "or", "not", "return"
        onearg   = "label", "goto", "if-goto"
        twoargs  = "function", "call", "push", "pop"
        
        allcommands = flatten((zeroargs, onearg, twoargs))
        
        line_comment    = r"(?P<line_comment>//.*\n)"
        block_comment   = r"(?P<block_comment>\/\*[^*]*\*+([^/][^*]*\*+)*\/)"
        whitespace      = r"(?P<whitespace>\s+)"
        identifier      = r"(?P<identifier>[^\s]+)"
        
        master_pat = "|".join((line_comment, block_comment, identifier, whitespace))
        
        ignore_types = "line_comment", "block_comment", "whitespace"
        
        # use a generator comprehension to pull matches one at a time.
        
        matches = ((scanmatch.value, scanmatch.loc) for scanmatch in scanpattern(master_pat, text, ignore_types))
        
        for token, loc in matches:
            
            if token in zeroargs:
                yield vmcommand(command=token, loc=loc)
                next
                
            elif token in onearg:
                command = token
                try:
                    segment, _ = next(matches)
                    if segment in allcommands:
                        raise Exception("\"%s\" expects one argument on line %d" % (command, loctoline(text)(loc)))
                except StopIteration:
                    raise Exception("Unexpected end of file on line %d" % loctoline(text)(loc))
                yield vmcommand(command, segment, loc=loc)
                
            elif token in twoargs:
                command = token
                try:
                    segment, _ = next(matches)
                    index, _ = next(matches)
                    
                    #~ print("{%s} {%s} {%s}" % (command, segment, index))
                    
                    if (segment in allcommands) or (index in allcommands):
                        raise Exception("\"%s\" expects two arguments on line %d" % (command, loctoline(text)(loc)))
                        
                except StopIteration:
                    raise Exception("Unexpected end of file on line %d" % loctoline(text)(loc))
                
                if index.isdigit():
                    yield vmcommand(command, segment, int(index), loc)
                else:
                    raise Exception("expected int on line %d: %s" % (loctoline(text)(loc), index))
            
            else:
                raise Exception("Unknown command %s on line %d" % (token, loctoline(text)(loc)))
                
    def parse(self, text):
        
        arithcommands = [ "add", "sub", "neg", "lt", "eq", "gt", "and", "or", "not" ]
        
        self.line = loctoline(text)
        commands = LookAhead(VMParser._tokenize(text))

        def process(vmc):
            command = vmc.command
                
            if command == "if-goto":
                return self.emitter.ifgoto(vmc)
                    
            elif command == "return":
                return self.emitter.ret(vmc)
                    
            elif command in arithcommands:
                return self.arithmetic(vmc)
                    
            elif command == "label":
                return self.emitter.label(vmc)
                
            elif command == "goto":
                return self.emitter.goto(vmc)
                
            elif command == "function":
                return self.emitter.function(vmc)
                
            elif command == "call":
                return self.emitter.call(vmc)
                
            elif command == "push":
                return self.push(vmc)
                
            elif command == "pop":
                return self.pop(vmc)
                
            else:
                raise Exception("Unknown command: %s" % command)
            
        for vmc in commands:
            result = process(vmc)
            yield vmc, result

    def arithmetic(self, vmc):
        # """Handle arithmetic commands: add, sub, neg, lt, eq, gt, and, or, not"""
        cmd = vmc.command
        
        if cmd == "add":
            return self.emitter.add(vmc)
        elif cmd == "sub":
            return self.emitter.sub(vmc)
        elif cmd == "neg":
            return self.emitter.neg(vmc)
        elif cmd == "lt":
            return self.emitter.lt(vmc)
        elif cmd == "eq":
            return self.emitter.eq(vmc)
        elif cmd == "gt":
            return self.emitter.gt(vmc)
        elif cmd == "and":
            return self.emitter.and_op(vmc)
        elif cmd == "or":
            return self.emitter.or_op(vmc)
        elif cmd == "not":
            return self.emitter.not_op(vmc)
        else:
            raise Exception("unknown arithmetic cmd %s" % cmd)
        
    def push(self, vmc):
        # """Handle push command"""
        segment = vmc.segment
        index = vmc.index
        
        if segment == "constant":
            return self.emitter.push_constant(vmc)
        elif segment == "local":
            return self.emitter.push_local(vmc)
        elif segment == "argument":
            return self.emitter.push_argument(vmc)
        elif segment == "this":
            return self.emitter.push_this(vmc)
        elif segment == "that":
            return self.emitter.push_that(vmc)
        elif segment == "pointer":
            return self.emitter.push_pointer(vmc)
        elif segment == "temp":
            return self.emitter.push_temp(vmc)
        elif segment == "static":
            return self.emitter.push_static(vmc)
        else:
            raise Exception("unrecognized segment %s" % segment)
        
    def pop(self, vmc):
        # """Handle pop command"""
        segment = vmc.segment
        index = vmc.index
        
        if segment == "local":
            return self.emitter.pop_local(vmc)
        elif segment == "argument":
            return self.emitter.pop_argument(vmc)
        elif segment == "this":
            return self.emitter.pop_this(vmc)
        elif segment == "that":
            return self.emitter.pop_that(vmc)
        elif segment == "pointer":
            return self.emitter.pop_pointer(vmc)
        elif segment == "temp":
            return self.emitter.pop_temp(vmc)
        elif segment == "static":
            return self.emitter.pop_static(vmc)
        else:
            raise Exception("unrecognized segment %s" % segment)

        
if __name__ == "__main__":
    vm = VMParser('tecs/projects/07/MemoryAccess/BasicTest')
    
