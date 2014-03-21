// Bootstrap code
@256
D=A
@SP
M=D
@Sys.init
0;JMP
// ***
// FibonacciElement
// compiled on Friday March 14, 2014
// ***
// Begin hardcode
// ***
//
(call)
//
@R13
D=M
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
// function Main.fibonacci nLocals: 0
(Main.fibonacci)
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
// push constant 2
@2
D=A
@SP
M=M+1
A=M-1
M=D
// lt
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=0
@Main.fibonacci.lt.0
D;JLT
@SP
A=M-1
M=1
(Main.fibonacci.lt.0)
@SP
A=M-1
M=M-1
// if-goto Main.IF_TRUE
@SP
AM=M-1
D=M
@Main.IF_TRUE
D;JNE
// goto Main.IF_FALSE
@Main.IF_FALSE
0;JMP
(Main.IF_TRUE)
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
// return
@return
0;JMP
(Main.IF_FALSE)
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
// push constant 2
@2
D=A
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
// call Main.fibonacci nArgs: 1
@Main.fibonacci.return.0
D=A
@R13
M=D
@1
D=A
@R14
M=D
@Main.fibonacci.call.0
D=A
@R15
M=D
@call
0;JMP
(Main.fibonacci.call.0)
@Main.fibonacci
0;JMP
(Main.fibonacci.return.0)
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
// push constant 1
@1
D=A
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
// call Main.fibonacci nArgs: 1
@Main.fibonacci.return.1
D=A
@R13
M=D
@1
D=A
@R14
M=D
@Main.fibonacci.call.1
D=A
@R15
M=D
@call
0;JMP
(Main.fibonacci.call.1)
@Main.fibonacci
0;JMP
(Main.fibonacci.return.1)
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// return
@return
0;JMP
// function Sys.init nLocals: 0
(Sys.init)
// push constant 4
@4
D=A
@SP
M=M+1
A=M-1
M=D
// call Main.fibonacci nArgs: 1
@Sys.init.return.0
D=A
@R13
M=D
@1
D=A
@R14
M=D
@Sys.init.call.0
D=A
@R15
M=D
@call
0;JMP
(Sys.init.call.0)
@Main.fibonacci
0;JMP
(Sys.init.return.0)
(Sys.WHILE)
// goto Sys.WHILE
@Sys.WHILE
0;JMP
