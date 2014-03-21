// Bootstrap code
@256
D=A
@SP
M=D
@Sys.init
0;JMP
// ***
// StaticsTest
// compiled on Friday March 14, 2014
// ***
// Begin hardcode
// ***
//
(call)
//
@SP
M=M+1
A=M-1
M=D
@LCL
D=M
@SP
M=M+1
A=M-1
M=D
@ARG
D=M
@SP
M=M+1
A=M-1
M=D
@THIS
D=M
@SP
M=M+1
A=M-1
M=D
@THAT
D=M
@SP
M=M+1
A=M-1
M=D
@SP
D=M
@ARG
M=D
@R14
D=M
@ARG
M=M-D
@5
D=A
@ARG
M=M-D
@SP
D=M
@LCL
M=D
@R15
A=M
0;JMP
//
(return)
//
@LCL
D=M
@R15
M=D
@5
A=D-A
D=M
@R14
M=D
@SP
A=M-1
D=M
@ARG
A=M
M=D
D=A+1
@SP
M=D
@R15
AM=M-1
D=M
@THAT
M=D
@R15
AM=M-1
D=M
@THIS
M=D
@R15
AM=M-1
D=M
@ARG
M=D
@R15
AM=M-1
D=M
@LCL
M=D
@R14
A=M
0;JMP
// function Class2.set nLocals: 0
(Class2.set)
// push argument 0
@0
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// pop static 0
@SP
AM=M-1
D=M
@Class2.static.0
M=D
// push argument 1
@1
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// pop static 1
@SP
AM=M-1
D=M
@Class2.static.1
M=D
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// return
@return
0;JMP
// function Class2.get nLocals: 0
(Class2.get)
// push static 0
@Class2.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// push static 1
@Class2.static.1
D=M
@SP
M=M+1
A=M-1
M=D
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// return
@return
0;JMP
// function Class1.set nLocals: 0
(Class1.set)
// push argument 0
@0
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// pop static 0
@SP
AM=M-1
D=M
@Class1.static.0
M=D
// push argument 1
@1
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// pop static 1
@SP
AM=M-1
D=M
@Class1.static.1
M=D
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// return
@return
0;JMP
// function Class1.get nLocals: 0
(Class1.get)
// push static 0
@Class1.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// push static 1
@Class1.static.1
D=M
@SP
M=M+1
A=M-1
M=D
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// return
@return
0;JMP
// function Sys.init nLocals: 0
(Sys.init)
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// push constant 8
@8
D=A
@SP
M=M+1
A=M-1
M=D
// call Class1.set nArgs: 2
@2
D=A
@R14
M=D
@Class1.set
D=A
@R15
M=D
@Sys.init.return.0
D=A
@call
0;JMP
(Sys.init.return.0)
// pop temp 0
@SP
AM=M-1
// push constant 23
@23
D=A
@SP
M=M+1
A=M-1
M=D
// push constant 15
@15
D=A
@SP
M=M+1
A=M-1
M=D
// call Class2.set nArgs: 2
@2
D=A
@R14
M=D
@Class2.set
D=A
@R15
M=D
@Sys.init.return.1
D=A
@call
0;JMP
(Sys.init.return.1)
// pop temp 0
@SP
AM=M-1
// call Class1.get nArgs: 0
@0
D=A
@R14
M=D
@Class1.get
D=A
@R15
M=D
@Sys.init.return.2
D=A
@call
0;JMP
(Sys.init.return.2)
// call Class2.get nArgs: 0
@0
D=A
@R14
M=D
@Class2.get
D=A
@R15
M=D
@Sys.init.return.3
D=A
@call
0;JMP
(Sys.init.return.3)
(Sys.Sys.init.WHILE)
// goto Sys.Sys.init.WHILE
@Sys.Sys.init.WHILE
0;JMP
