// push constant 10
@10
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

// push constant 21
@21
D=A
@SP
M=M+1
A=M-1
M=D

// push constant 22
@22
D=A
@SP
M=M+1
A=M-1
M=D

// pop argument 2
@SP
AM=M-1
D=M
@ARG
A=M
A=A+1
A=A+1
M=D

// pop argument 1
@SP
AM=M-1
D=M
@ARG
A=M
A=A+1
M=D

// push constant 36
@36
D=A
@SP
M=M+1
A=M-1
M=D

// pop this 6
@SP
AM=M-1
D=M
@THIS
A=M
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
M=D

// push constant 42
@42
D=A
@SP
M=M+1
A=M-1
M=D

// push constant 45
@45
D=A
@SP
M=M+1
A=M-1
M=D

// pop that 5
@SP
AM=M-1
D=M
@THAT
A=M
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
M=D

// pop that 2
@SP
AM=M-1
D=M
@THAT
A=M
A=A+1
A=A+1
M=D

// push constant 510
@510
D=A
@SP
M=M+1
A=M-1
M=D

// pop temp 6
@SP
AM=M-1
D=M
@R5
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
M=D

// push local 0
@LCL
A=M
D=M
@SP
M=M+1
A=M-1
M=D

// push that 5
@5
D=A
@THAT
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

// push argument 1
@ARG
A=M+1
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

// push this 6
@6
D=A
@THIS
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D

// push this 6
@6
D=A
@THIS
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

// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D

// push temp 6
@11
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

