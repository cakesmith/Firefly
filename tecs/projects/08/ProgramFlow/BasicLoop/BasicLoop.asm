// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
(BasicLoop.init.loop_start)
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
// push local 0
@0
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
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
// pop argument 0
@SP
AM=M-1
D=M
@ARG
A=M
M=D
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
// if-goto loop_start
@SP
AM=M-1
D=M
@BasicLoop.init.loop_start
D;JNE
// push local 0
@0
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
