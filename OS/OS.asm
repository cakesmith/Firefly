// Bootstrap code
@256
D=A
@SP
M=D
@Sys.init
0;JMP
// ***
// OS
// compiled on Thursday March 20, 2014
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
@R14
D=M
@5
D=D+A
@SP
D=M-D
@ARG
M=D
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
//
(lt)
//
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=0
@LT.TRUE
D;JLT
@SP
A=M-1
M=1
(LT.TRUE)
@SP
A=M-1
M=M-1
@R14
A=M
0;JMP
//
(gt)
//
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=0
@GT.TRUE
D;JGT
@SP
A=M-1
M=1
(GT.TRUE)
@SP
A=M-1
M=M-1
@R14
A=M
0;JMP
//
(eq)
//
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=0
@EQ.TRUE
D;JEQ
@SP
A=M-1
M=1
(EQ.TRUE)
@SP
A=M-1
M=M-1
@R14
A=M
0;JMP
// {line: 5}
// function Output.init nLocals: 1
(Output.init)
@SP
AM=M+1
A=A-1
M=0
// {line: 18}
// call Output.initMap nArgs: 0
@0
D=A
@R14
M=D
@Output.initMap
D=A
@R15
M=D
@Output.init.call.0
D=A
@call
0;JMP
(Output.init.call.0)
// {line: 23}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 29}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 34}
// pop static 10
@SP
AM=M-1
D=M
@Output.static.10
M=D
// {line: 40}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 45}
// pop static 9
@SP
AM=M-1
D=M
@Output.static.9
M=D
// {line: 47}
// return
@return
0;JMP
// {line: 52}
// function Output.initMap nLocals: 1
(Output.initMap)
@SP
AM=M+1
A=A-1
M=0
// {line: 58}
// push constant 127
@127
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 71}
// call Array.new nArgs: 1
@1
D=A
@R14
M=D
@Array.new
D=A
@R15
M=D
@Output.initMap.call.0
D=A
@call
0;JMP
(Output.initMap.call.0)
// {line: 76}
// pop static 8
@SP
AM=M-1
D=M
@Output.static.8
M=D
// {line: 82}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 88}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 94}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 100}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 106}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 112}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 118}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 124}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 130}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 136}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 142}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 148}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 161}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.1
D=A
@call
0;JMP
(Output.initMap.call.1)
// {line: 166}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 172}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 178}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 184}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 190}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 196}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 202}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 208}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 214}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 220}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 226}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 232}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 238}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 251}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.2
D=A
@call
0;JMP
(Output.initMap.call.2)
// {line: 256}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 262}
// push constant 33
@33
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 268}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 274}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 280}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 286}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 292}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 298}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 304}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 310}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 316}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 322}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 328}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 341}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.3
D=A
@call
0;JMP
(Output.initMap.call.3)
// {line: 346}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 352}
// push constant 34
@34
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 358}
// push constant 54
@54
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 364}
// push constant 54
@54
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 370}
// push constant 20
@20
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 376}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 382}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 388}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 394}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 400}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 406}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 412}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 418}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 431}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.4
D=A
@call
0;JMP
(Output.initMap.call.4)
// {line: 436}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 442}
// push constant 35
@35
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 448}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 454}
// push constant 18
@18
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 460}
// push constant 18
@18
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 466}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 472}
// push constant 18
@18
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 478}
// push constant 18
@18
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 484}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 490}
// push constant 18
@18
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 496}
// push constant 18
@18
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 502}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 508}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 521}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.5
D=A
@call
0;JMP
(Output.initMap.call.5)
// {line: 526}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 532}
// push constant 36
@36
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 538}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 544}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 550}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 556}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 562}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 568}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 574}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 580}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 586}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 592}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 598}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 611}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.6
D=A
@call
0;JMP
(Output.initMap.call.6)
// {line: 616}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 622}
// push constant 37
@37
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 628}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 634}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 640}
// push constant 35
@35
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 646}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 652}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 658}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 664}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 670}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 676}
// push constant 49
@49
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 682}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 688}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 701}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.7
D=A
@call
0;JMP
(Output.initMap.call.7)
// {line: 706}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 712}
// push constant 38
@38
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 718}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 724}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 730}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 736}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 742}
// push constant 54
@54
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 748}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 754}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 760}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 766}
// push constant 54
@54
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 772}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 778}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 791}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.8
D=A
@call
0;JMP
(Output.initMap.call.8)
// {line: 796}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 802}
// push constant 39
@39
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 808}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 814}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 820}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 826}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 832}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 838}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 844}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 850}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 856}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 862}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 868}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 881}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.9
D=A
@call
0;JMP
(Output.initMap.call.9)
// {line: 886}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 892}
// push constant 40
@40
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 898}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 904}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 910}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 916}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 922}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 928}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 934}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 940}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 946}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 952}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 958}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 971}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.10
D=A
@call
0;JMP
(Output.initMap.call.10)
// {line: 976}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 982}
// push constant 41
@41
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 988}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 994}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1000}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1006}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1012}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1018}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1024}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1030}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1036}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1042}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1048}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1061}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.11
D=A
@call
0;JMP
(Output.initMap.call.11)
// {line: 1066}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 1072}
// push constant 42
@42
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1078}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1084}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1090}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1096}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1102}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1108}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1114}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1120}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1126}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1132}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1138}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1151}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.12
D=A
@call
0;JMP
(Output.initMap.call.12)
// {line: 1156}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 1162}
// push constant 43
@43
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1168}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1174}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1180}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1186}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1192}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1198}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1204}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1210}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1216}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1222}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1228}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1241}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.13
D=A
@call
0;JMP
(Output.initMap.call.13)
// {line: 1246}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 1252}
// push constant 44
@44
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1258}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1264}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1270}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1276}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1282}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1288}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1294}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1300}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1306}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1312}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1318}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1331}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.14
D=A
@call
0;JMP
(Output.initMap.call.14)
// {line: 1336}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 1342}
// push constant 45
@45
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1348}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1354}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1360}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1366}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1372}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1378}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1384}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1390}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1396}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1402}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1408}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1421}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.15
D=A
@call
0;JMP
(Output.initMap.call.15)
// {line: 1426}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 1432}
// push constant 46
@46
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1438}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1444}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1450}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1456}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1462}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1468}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1474}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1480}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1486}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1492}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1498}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1511}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.16
D=A
@call
0;JMP
(Output.initMap.call.16)
// {line: 1516}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 1522}
// push constant 47
@47
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1528}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1534}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1540}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1546}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1552}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1558}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1564}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1570}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1576}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1582}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1588}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1601}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.17
D=A
@call
0;JMP
(Output.initMap.call.17)
// {line: 1606}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 1612}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1618}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1624}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1630}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1636}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1642}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1648}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1654}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1660}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1666}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1672}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1678}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1691}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.18
D=A
@call
0;JMP
(Output.initMap.call.18)
// {line: 1696}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 1702}
// push constant 49
@49
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1708}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1714}
// push constant 14
@14
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1720}
// push constant 15
@15
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1726}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1732}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1738}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1744}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1750}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1756}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1762}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1768}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1781}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.19
D=A
@call
0;JMP
(Output.initMap.call.19)
// {line: 1786}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 1792}
// push constant 50
@50
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1798}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1804}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1810}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1816}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1822}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1828}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1834}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1840}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1846}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1852}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1858}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1871}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.20
D=A
@call
0;JMP
(Output.initMap.call.20)
// {line: 1876}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 1882}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1888}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1894}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1900}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1906}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1912}
// push constant 28
@28
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1918}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1924}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1930}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1936}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1942}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1948}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1961}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.21
D=A
@call
0;JMP
(Output.initMap.call.21)
// {line: 1966}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 1972}
// push constant 52
@52
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1978}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1984}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1990}
// push constant 28
@28
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1996}
// push constant 26
@26
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2002}
// push constant 25
@25
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2008}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2014}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2020}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2026}
// push constant 60
@60
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2032}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2038}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2051}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.22
D=A
@call
0;JMP
(Output.initMap.call.22)
// {line: 2056}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 2062}
// push constant 53
@53
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2068}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2074}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2080}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2086}
// push constant 31
@31
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2092}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2098}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2104}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2110}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2116}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2122}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2128}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2141}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.23
D=A
@call
0;JMP
(Output.initMap.call.23)
// {line: 2146}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 2152}
// push constant 54
@54
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2158}
// push constant 28
@28
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2164}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2170}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2176}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2182}
// push constant 31
@31
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2188}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2194}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2200}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2206}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2212}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2218}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2231}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.24
D=A
@call
0;JMP
(Output.initMap.call.24)
// {line: 2236}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 2242}
// push constant 55
@55
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2248}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2254}
// push constant 49
@49
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2260}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2266}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2272}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2278}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2284}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2290}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2296}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2302}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2308}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2321}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.25
D=A
@call
0;JMP
(Output.initMap.call.25)
// {line: 2326}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 2332}
// push constant 56
@56
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2338}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2344}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2350}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2356}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2362}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2368}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2374}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2380}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2386}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2392}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2398}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2411}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.26
D=A
@call
0;JMP
(Output.initMap.call.26)
// {line: 2416}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 2422}
// push constant 57
@57
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2428}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2434}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2440}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2446}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2452}
// push constant 62
@62
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2458}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2464}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2470}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2476}
// push constant 14
@14
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2482}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2488}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2501}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.27
D=A
@call
0;JMP
(Output.initMap.call.27)
// {line: 2506}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 2512}
// push constant 58
@58
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2518}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2524}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2530}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2536}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2542}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2548}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2554}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2560}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2566}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2572}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2578}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2591}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.28
D=A
@call
0;JMP
(Output.initMap.call.28)
// {line: 2596}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 2602}
// push constant 59
@59
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2608}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2614}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2620}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2626}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2632}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2638}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2644}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2650}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2656}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2662}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2668}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2681}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.29
D=A
@call
0;JMP
(Output.initMap.call.29)
// {line: 2686}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 2692}
// push constant 60
@60
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2698}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2704}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2710}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2716}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2722}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2728}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2734}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2740}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2746}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2752}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2758}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2771}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.30
D=A
@call
0;JMP
(Output.initMap.call.30)
// {line: 2776}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 2782}
// push constant 61
@61
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2788}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2794}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2800}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2806}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2812}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2818}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2824}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2830}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2836}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2842}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2848}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2861}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.31
D=A
@call
0;JMP
(Output.initMap.call.31)
// {line: 2866}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 2872}
// push constant 62
@62
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2878}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2884}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2890}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2896}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2902}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2908}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2914}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2920}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2926}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2932}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2938}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2951}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.32
D=A
@call
0;JMP
(Output.initMap.call.32)
// {line: 2956}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 2962}
// push constant 64
@64
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2968}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2974}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2980}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2986}
// push constant 59
@59
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2992}
// push constant 59
@59
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2998}
// push constant 59
@59
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3004}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3010}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3016}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3022}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3028}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3041}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.33
D=A
@call
0;JMP
(Output.initMap.call.33)
// {line: 3046}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 3052}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3058}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3064}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3070}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3076}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3082}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3088}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3094}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3100}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3106}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3112}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3118}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3131}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.34
D=A
@call
0;JMP
(Output.initMap.call.34)
// {line: 3136}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 3142}
// push constant 65
@65
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3148}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3154}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3160}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3166}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3172}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3178}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3184}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3190}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3196}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3202}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3208}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3214}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3227}
// call Output.create nArgs: 13
@13
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.35
D=A
@call
0;JMP
(Output.initMap.call.35)
// {line: 3232}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 3238}
// push constant 66
@66
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3244}
// push constant 31
@31
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3250}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3256}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3262}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3268}
// push constant 31
@31
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3274}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3280}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3286}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3292}
// push constant 31
@31
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3298}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3304}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3317}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.36
D=A
@call
0;JMP
(Output.initMap.call.36)
// {line: 3322}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 3328}
// push constant 67
@67
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3334}
// push constant 28
@28
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3340}
// push constant 54
@54
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3346}
// push constant 35
@35
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3352}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3358}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3364}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3370}
// push constant 35
@35
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3376}
// push constant 54
@54
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3382}
// push constant 28
@28
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3388}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3394}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3407}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.37
D=A
@call
0;JMP
(Output.initMap.call.37)
// {line: 3412}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 3418}
// push constant 68
@68
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3424}
// push constant 15
@15
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3430}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3436}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3442}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3448}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3454}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3460}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3466}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3472}
// push constant 15
@15
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3478}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3484}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3497}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.38
D=A
@call
0;JMP
(Output.initMap.call.38)
// {line: 3502}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 3508}
// push constant 69
@69
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3514}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3520}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3526}
// push constant 35
@35
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3532}
// push constant 11
@11
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3538}
// push constant 15
@15
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3544}
// push constant 11
@11
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3550}
// push constant 35
@35
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3556}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3562}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3568}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3574}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3587}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.39
D=A
@call
0;JMP
(Output.initMap.call.39)
// {line: 3592}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 3598}
// push constant 70
@70
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3604}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3610}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3616}
// push constant 35
@35
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3622}
// push constant 11
@11
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3628}
// push constant 15
@15
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3634}
// push constant 11
@11
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3640}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3646}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3652}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3658}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3664}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3677}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.40
D=A
@call
0;JMP
(Output.initMap.call.40)
// {line: 3682}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 3688}
// push constant 71
@71
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3694}
// push constant 28
@28
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3700}
// push constant 54
@54
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3706}
// push constant 35
@35
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3712}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3718}
// push constant 59
@59
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3724}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3730}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3736}
// push constant 54
@54
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3742}
// push constant 44
@44
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3748}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3754}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3767}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.41
D=A
@call
0;JMP
(Output.initMap.call.41)
// {line: 3772}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 3778}
// push constant 72
@72
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3784}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3790}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3796}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3802}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3808}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3814}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3820}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3826}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3832}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3838}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3844}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3857}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.42
D=A
@call
0;JMP
(Output.initMap.call.42)
// {line: 3862}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 3868}
// push constant 73
@73
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3874}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3880}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3886}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3892}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3898}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3904}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3910}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3916}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3922}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3928}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3934}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3947}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.43
D=A
@call
0;JMP
(Output.initMap.call.43)
// {line: 3952}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 3958}
// push constant 74
@74
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3964}
// push constant 60
@60
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3970}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3976}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3982}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3988}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3994}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4000}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4006}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4012}
// push constant 14
@14
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4018}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4024}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4037}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.44
D=A
@call
0;JMP
(Output.initMap.call.44)
// {line: 4042}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 4048}
// push constant 75
@75
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4054}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4060}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4066}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4072}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4078}
// push constant 15
@15
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4084}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4090}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4096}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4102}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4108}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4114}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4127}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.45
D=A
@call
0;JMP
(Output.initMap.call.45)
// {line: 4132}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 4138}
// push constant 76
@76
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4144}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4150}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4156}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4162}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4168}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4174}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4180}
// push constant 35
@35
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4186}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4192}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4198}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4204}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4217}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.46
D=A
@call
0;JMP
(Output.initMap.call.46)
// {line: 4222}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 4228}
// push constant 77
@77
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4234}
// push constant 33
@33
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4240}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4246}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4252}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4258}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4264}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4270}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4276}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4282}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4288}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4294}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4307}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.47
D=A
@call
0;JMP
(Output.initMap.call.47)
// {line: 4312}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 4318}
// push constant 78
@78
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4324}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4330}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4336}
// push constant 55
@55
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4342}
// push constant 55
@55
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4348}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4354}
// push constant 59
@59
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4360}
// push constant 59
@59
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4366}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4372}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4378}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4384}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4397}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.48
D=A
@call
0;JMP
(Output.initMap.call.48)
// {line: 4402}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 4408}
// push constant 79
@79
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4414}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4420}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4426}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4432}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4438}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4444}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4450}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4456}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4462}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4468}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4474}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4487}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.49
D=A
@call
0;JMP
(Output.initMap.call.49)
// {line: 4492}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 4498}
// push constant 80
@80
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4504}
// push constant 31
@31
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4510}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4516}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4522}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4528}
// push constant 31
@31
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4534}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4540}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4546}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4552}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4558}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4564}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4577}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.50
D=A
@call
0;JMP
(Output.initMap.call.50)
// {line: 4582}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 4588}
// push constant 81
@81
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4594}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4600}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4606}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4612}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4618}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4624}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4630}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4636}
// push constant 59
@59
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4642}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4648}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4654}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4667}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.51
D=A
@call
0;JMP
(Output.initMap.call.51)
// {line: 4672}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 4678}
// push constant 82
@82
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4684}
// push constant 31
@31
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4690}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4696}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4702}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4708}
// push constant 31
@31
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4714}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4720}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4726}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4732}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4738}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4744}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4757}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.52
D=A
@call
0;JMP
(Output.initMap.call.52)
// {line: 4762}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 4768}
// push constant 83
@83
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4774}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4780}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4786}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4792}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4798}
// push constant 28
@28
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4804}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4810}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4816}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4822}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4828}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4834}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4847}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.53
D=A
@call
0;JMP
(Output.initMap.call.53)
// {line: 4852}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 4858}
// push constant 84
@84
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4864}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4870}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4876}
// push constant 45
@45
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4882}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4888}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4894}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4900}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4906}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4912}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4918}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4924}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4937}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.54
D=A
@call
0;JMP
(Output.initMap.call.54)
// {line: 4942}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 4948}
// push constant 85
@85
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4954}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4960}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4966}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4972}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4978}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4984}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4990}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4996}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5002}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5008}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5014}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5027}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.55
D=A
@call
0;JMP
(Output.initMap.call.55)
// {line: 5032}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 5038}
// push constant 86
@86
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5044}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5050}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5056}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5062}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5068}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5074}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5080}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5086}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5092}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5098}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5104}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5117}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.56
D=A
@call
0;JMP
(Output.initMap.call.56)
// {line: 5122}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 5128}
// push constant 87
@87
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5134}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5140}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5146}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5152}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5158}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5164}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5170}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5176}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5182}
// push constant 18
@18
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5188}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5194}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5207}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.57
D=A
@call
0;JMP
(Output.initMap.call.57)
// {line: 5212}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 5218}
// push constant 88
@88
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5224}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5230}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5236}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5242}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5248}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5254}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5260}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5266}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5272}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5278}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5284}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5297}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.58
D=A
@call
0;JMP
(Output.initMap.call.58)
// {line: 5302}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 5308}
// push constant 89
@89
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5314}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5320}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5326}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5332}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5338}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5344}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5350}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5356}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5362}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5368}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5374}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5387}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.59
D=A
@call
0;JMP
(Output.initMap.call.59)
// {line: 5392}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 5398}
// push constant 90
@90
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5404}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5410}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5416}
// push constant 49
@49
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5422}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5428}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5434}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5440}
// push constant 35
@35
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5446}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5452}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5458}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5464}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5477}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.60
D=A
@call
0;JMP
(Output.initMap.call.60)
// {line: 5482}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 5488}
// push constant 91
@91
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5494}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5500}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5506}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5512}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5518}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5524}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5530}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5536}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5542}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5548}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5554}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5567}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.61
D=A
@call
0;JMP
(Output.initMap.call.61)
// {line: 5572}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 5578}
// push constant 92
@92
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5584}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5590}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5596}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5602}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5608}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5614}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5620}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5626}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5632}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5638}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5644}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5657}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.62
D=A
@call
0;JMP
(Output.initMap.call.62)
// {line: 5662}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 5668}
// push constant 93
@93
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5674}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5680}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5686}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5692}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5698}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5704}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5710}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5716}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5722}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5728}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5734}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5747}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.63
D=A
@call
0;JMP
(Output.initMap.call.63)
// {line: 5752}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 5758}
// push constant 94
@94
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5764}
// push constant 8
@8
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5770}
// push constant 28
@28
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5776}
// push constant 54
@54
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5782}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5788}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5794}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5800}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5806}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5812}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5818}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5824}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5837}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.64
D=A
@call
0;JMP
(Output.initMap.call.64)
// {line: 5842}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 5848}
// push constant 95
@95
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5854}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5860}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5866}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5872}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5878}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5884}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5890}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5896}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5902}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5908}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5914}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5927}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.65
D=A
@call
0;JMP
(Output.initMap.call.65)
// {line: 5932}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 5938}
// push constant 96
@96
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5944}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5950}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5956}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5962}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5968}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5974}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5980}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5986}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5992}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5998}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6004}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6017}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.66
D=A
@call
0;JMP
(Output.initMap.call.66)
// {line: 6022}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 6028}
// push constant 97
@97
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6034}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6040}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6046}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6052}
// push constant 14
@14
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6058}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6064}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6070}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6076}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6082}
// push constant 54
@54
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6088}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6094}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6107}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.67
D=A
@call
0;JMP
(Output.initMap.call.67)
// {line: 6112}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 6118}
// push constant 98
@98
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6124}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6130}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6136}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6142}
// push constant 15
@15
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6148}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6154}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6160}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6166}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6172}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6178}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6184}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6197}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.68
D=A
@call
0;JMP
(Output.initMap.call.68)
// {line: 6202}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 6208}
// push constant 99
@99
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6214}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6220}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6226}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6232}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6238}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6244}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6250}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6256}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6262}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6268}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6274}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6287}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.69
D=A
@call
0;JMP
(Output.initMap.call.69)
// {line: 6292}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 6298}
// push constant 100
@100
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6304}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6310}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6316}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6322}
// push constant 60
@60
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6328}
// push constant 54
@54
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6334}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6340}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6346}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6352}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6358}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6364}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6377}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.70
D=A
@call
0;JMP
(Output.initMap.call.70)
// {line: 6382}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 6388}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6394}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6400}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6406}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6412}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6418}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6424}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6430}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6436}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6442}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6448}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6454}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6467}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.71
D=A
@call
0;JMP
(Output.initMap.call.71)
// {line: 6472}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 6478}
// push constant 102
@102
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6484}
// push constant 28
@28
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6490}
// push constant 54
@54
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6496}
// push constant 38
@38
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6502}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6508}
// push constant 15
@15
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6514}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6520}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6526}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6532}
// push constant 15
@15
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6538}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6544}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6557}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.72
D=A
@call
0;JMP
(Output.initMap.call.72)
// {line: 6562}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 6568}
// push constant 103
@103
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6574}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6580}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6586}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6592}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6598}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6604}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6610}
// push constant 62
@62
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6616}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6622}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6628}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6634}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6647}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.73
D=A
@call
0;JMP
(Output.initMap.call.73)
// {line: 6652}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 6658}
// push constant 104
@104
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6664}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6670}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6676}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6682}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6688}
// push constant 55
@55
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6694}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6700}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6706}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6712}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6718}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6724}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6737}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.74
D=A
@call
0;JMP
(Output.initMap.call.74)
// {line: 6742}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 6748}
// push constant 105
@105
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6754}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6760}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6766}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6772}
// push constant 14
@14
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6778}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6784}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6790}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6796}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6802}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6808}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6814}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6827}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.75
D=A
@call
0;JMP
(Output.initMap.call.75)
// {line: 6832}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 6838}
// push constant 106
@106
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6844}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6850}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6856}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6862}
// push constant 56
@56
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6868}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6874}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6880}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6886}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6892}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6898}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6904}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6917}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.76
D=A
@call
0;JMP
(Output.initMap.call.76)
// {line: 6922}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 6928}
// push constant 107
@107
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6934}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6940}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6946}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6952}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6958}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6964}
// push constant 15
@15
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6970}
// push constant 15
@15
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6976}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6982}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6988}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6994}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7007}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.77
D=A
@call
0;JMP
(Output.initMap.call.77)
// {line: 7012}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 7018}
// push constant 108
@108
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7024}
// push constant 14
@14
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7030}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7036}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7042}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7048}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7054}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7060}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7066}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7072}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7078}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7084}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7097}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.78
D=A
@call
0;JMP
(Output.initMap.call.78)
// {line: 7102}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 7108}
// push constant 109
@109
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7114}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7120}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7126}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7132}
// push constant 29
@29
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7138}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7144}
// push constant 43
@43
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7150}
// push constant 43
@43
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7156}
// push constant 43
@43
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7162}
// push constant 43
@43
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7168}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7174}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7187}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.79
D=A
@call
0;JMP
(Output.initMap.call.79)
// {line: 7192}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 7198}
// push constant 110
@110
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7204}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7210}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7216}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7222}
// push constant 29
@29
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7228}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7234}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7240}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7246}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7252}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7258}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7264}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7277}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.80
D=A
@call
0;JMP
(Output.initMap.call.80)
// {line: 7282}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 7288}
// push constant 111
@111
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7294}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7300}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7306}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7312}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7318}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7324}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7330}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7336}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7342}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7348}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7354}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7367}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.81
D=A
@call
0;JMP
(Output.initMap.call.81)
// {line: 7372}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 7378}
// push constant 112
@112
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7384}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7390}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7396}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7402}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7408}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7414}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7420}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7426}
// push constant 31
@31
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7432}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7438}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7444}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7457}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.82
D=A
@call
0;JMP
(Output.initMap.call.82)
// {line: 7462}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 7468}
// push constant 113
@113
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7474}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7480}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7486}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7492}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7498}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7504}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7510}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7516}
// push constant 62
@62
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7522}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7528}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7534}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7547}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.83
D=A
@call
0;JMP
(Output.initMap.call.83)
// {line: 7552}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 7558}
// push constant 114
@114
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7564}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7570}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7576}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7582}
// push constant 29
@29
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7588}
// push constant 55
@55
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7594}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7600}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7606}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7612}
// push constant 7
@7
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7618}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7624}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7637}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.84
D=A
@call
0;JMP
(Output.initMap.call.84)
// {line: 7642}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 7648}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7654}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7660}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7666}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7672}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7678}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7684}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7690}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7696}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7702}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7708}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7714}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7727}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.85
D=A
@call
0;JMP
(Output.initMap.call.85)
// {line: 7732}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 7738}
// push constant 116
@116
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7744}
// push constant 4
@4
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7750}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7756}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7762}
// push constant 15
@15
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7768}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7774}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7780}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7786}
// push constant 54
@54
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7792}
// push constant 28
@28
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7798}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7804}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7817}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.86
D=A
@call
0;JMP
(Output.initMap.call.86)
// {line: 7822}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 7828}
// push constant 117
@117
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7834}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7840}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7846}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7852}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7858}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7864}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7870}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7876}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7882}
// push constant 54
@54
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7888}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7894}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7907}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.87
D=A
@call
0;JMP
(Output.initMap.call.87)
// {line: 7912}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 7918}
// push constant 118
@118
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7924}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7930}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7936}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7942}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7948}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7954}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7960}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7966}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7972}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7978}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7984}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7997}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.88
D=A
@call
0;JMP
(Output.initMap.call.88)
// {line: 8002}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 8008}
// push constant 119
@119
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8014}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8020}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8026}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8032}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8038}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8044}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8050}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8056}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8062}
// push constant 18
@18
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8068}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8074}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8087}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.89
D=A
@call
0;JMP
(Output.initMap.call.89)
// {line: 8092}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 8098}
// push constant 120
@120
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8104}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8110}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8116}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8122}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8128}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8134}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8140}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8146}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8152}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8158}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8164}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8177}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.90
D=A
@call
0;JMP
(Output.initMap.call.90)
// {line: 8182}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 8188}
// push constant 121
@121
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8194}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8200}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8206}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8212}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8218}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8224}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8230}
// push constant 62
@62
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8236}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8242}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8248}
// push constant 15
@15
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8254}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8267}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.91
D=A
@call
0;JMP
(Output.initMap.call.91)
// {line: 8272}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 8278}
// push constant 122
@122
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8284}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8290}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8296}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8302}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8308}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8314}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8320}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8326}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8332}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8338}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8344}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8357}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.92
D=A
@call
0;JMP
(Output.initMap.call.92)
// {line: 8362}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 8368}
// push constant 123
@123
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8374}
// push constant 56
@56
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8380}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8386}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8392}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8398}
// push constant 7
@7
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8404}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8410}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8416}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8422}
// push constant 56
@56
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8428}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8434}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8447}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.93
D=A
@call
0;JMP
(Output.initMap.call.93)
// {line: 8452}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 8458}
// push constant 124
@124
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8464}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8470}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8476}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8482}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8488}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8494}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8500}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8506}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8512}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8518}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8524}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8537}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.94
D=A
@call
0;JMP
(Output.initMap.call.94)
// {line: 8542}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 8548}
// push constant 125
@125
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8554}
// push constant 7
@7
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8560}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8566}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8572}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8578}
// push constant 56
@56
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8584}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8590}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8596}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8602}
// push constant 7
@7
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8608}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8614}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8627}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.95
D=A
@call
0;JMP
(Output.initMap.call.95)
// {line: 8632}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 8638}
// push constant 126
@126
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8644}
// push constant 38
@38
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8650}
// push constant 45
@45
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8656}
// push constant 25
@25
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8662}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8668}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8674}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8680}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8686}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8692}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8698}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8704}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8717}
// call Output.create nArgs: 12
@12
D=A
@R14
M=D
@Output.create
D=A
@R15
M=D
@Output.initMap.call.96
D=A
@call
0;JMP
(Output.initMap.call.96)
// {line: 8722}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 8728}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8730}
// return
@return
0;JMP
// {line: 8735}
// function Output.create nLocals: 1
(Output.create)
@SP
AM=M+1
A=A-1
M=0
// {line: 8741}
// push constant 11
@11
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8754}
// call Array.new nArgs: 1
@1
D=A
@R14
M=D
@Array.new
D=A
@R15
M=D
@Output.create.call.0
D=A
@call
0;JMP
(Output.create.call.0)
// {line: 8760}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 8766}
// push static 8
@Output.static.8
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 8775}
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
// {line: 8780}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 8785}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 8794}
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
// {line: 8800}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 8809}
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
// {line: 8815}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8820}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 8825}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 8834}
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
// {line: 8840}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 8849}
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
// {line: 8855}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8860}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 8865}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 8874}
// push argument 2
@2
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 8880}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 8889}
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
// {line: 8895}
// push constant 2
@2
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8900}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 8905}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 8914}
// push argument 3
@3
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 8920}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 8929}
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
// {line: 8935}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8940}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 8945}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 8954}
// push argument 4
@4
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 8960}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 8969}
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
// {line: 8975}
// push constant 4
@4
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8980}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 8985}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 8994}
// push argument 5
@5
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9000}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 9009}
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
// {line: 9015}
// push constant 5
@5
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9020}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 9025}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 9034}
// push argument 6
@6
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9040}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 9049}
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
// {line: 9055}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9060}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 9065}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 9074}
// push argument 7
@7
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9080}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 9089}
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
// {line: 9095}
// push constant 7
@7
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9100}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 9105}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 9114}
// push argument 8
@8
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9120}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 9129}
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
// {line: 9135}
// push constant 8
@8
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9140}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 9145}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 9154}
// push argument 9
@9
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9160}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 9169}
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
// {line: 9175}
// push constant 9
@9
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9180}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 9185}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 9194}
// push argument 10
@10
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9200}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 9209}
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
// {line: 9215}
// push constant 10
@10
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9220}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 9225}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 9234}
// push argument 11
@11
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9240}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 9246}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9248}
// return
@return
0;JMP
// {line: 9249}
// function Output.getMap nLocals: 0
(Output.getMap)
// {line: 9258}
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
// {line: 9264}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9271}
// lt
@Output.getMap.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Output.getMap.lt.0)
// {line: 9280}
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
// {line: 9286}
// push constant 126
@126
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9293}
// gt
@Output.getMap.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Output.getMap.gt.0)
// {line: 9298}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 9303}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 9309}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9315}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9318}
// not
@SP
A=M-1
M=!M
// {line: 9323}
// if-goto Output.getMap.if.0
@SP
AM=M-1
D=M
@Output.getMap.if.0
D;JNE
// {line: 9329}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9335}
// pop argument 0
@SP
AM=M-1
D=M
@ARG
A=M
M=D
// {line: 9336}
(Output.getMap.if.0)
// {line: 9341}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 9347}
// push pointer 1
@4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9353}
// push static 8
@Output.static.8
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9362}
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
// {line: 9367}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 9372}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 9381}
// push that 0
@0
D=A
@THAT
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9386}
// pop temp 2
@SP
AM=M-1
D=M
@R7
M=D
// {line: 9391}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 9397}
// push temp 2
@7
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9399}
// return
@return
0;JMP
// {line: 9400}
// function Output.moveCursor nLocals: 0
(Output.moveCursor)
// {line: 9409}
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
// {line: 9415}
// push constant 23
@23
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9422}
// lt
@Output.moveCursor.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Output.moveCursor.lt.0)
// {line: 9431}
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
// {line: 9437}
// push constant 64
@64
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9444}
// lt
@Output.moveCursor.lt.1
D=A
@R14
M=D
@lt
0;JMP
(Output.moveCursor.lt.1)
// {line: 9449}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 9454}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 9460}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9466}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9469}
// not
@SP
A=M-1
M=!M
// {line: 9474}
// if-goto Output.moveCursor.if.0
@SP
AM=M-1
D=M
@Output.moveCursor.if.0
D;JNE
// {line: 9483}
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
// {line: 9488}
// pop static 9
@SP
AM=M-1
D=M
@Output.static.9
M=D
// {line: 9497}
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
// {line: 9502}
// pop static 10
@SP
AM=M-1
D=M
@Output.static.10
M=D
// {line: 9508}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9521}
// call Output._print nArgs: 1
@1
D=A
@R14
M=D
@Output._print
D=A
@R15
M=D
@Output.moveCursor.call.0
D=A
@call
0;JMP
(Output.moveCursor.call.0)
// {line: 9526}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 9527}
(Output.moveCursor.if.0)
// {line: 9532}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 9534}
// return
@return
0;JMP
// {line: 9535}
// function Output.printChar nLocals: 0
(Output.printChar)
// {line: 9541}
// push static 10
@Output.static.10
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9547}
// push constant 64
@64
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9554}
// lt
@Output.printChar.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Output.printChar.lt.0)
// {line: 9559}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 9565}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9571}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9574}
// not
@SP
A=M-1
M=!M
// {line: 9579}
// if-goto Output.printChar.if.0
@SP
AM=M-1
D=M
@Output.printChar.if.0
D;JNE
// {line: 9588}
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
// {line: 9601}
// call Output._print nArgs: 1
@1
D=A
@R14
M=D
@Output._print
D=A
@R15
M=D
@Output.printChar.call.0
D=A
@call
0;JMP
(Output.printChar.call.0)
// {line: 9606}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 9612}
// push static 10
@Output.static.10
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9618}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9623}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 9628}
// pop static 10
@SP
AM=M-1
D=M
@Output.static.10
M=D
// {line: 9629}
(Output.printChar.if.0)
// {line: 9634}
// if-goto Output.printChar.goto.0
@SP
AM=M-1
D=M
@Output.printChar.goto.0
D;JNE
// {line: 9640}
// push static 9
@Output.static.9
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9646}
// push constant 23
@23
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9653}
// lt
@Output.printChar.lt.1
D=A
@R14
M=D
@lt
0;JMP
(Output.printChar.lt.1)
// {line: 9658}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 9664}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9670}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9673}
// not
@SP
A=M-1
M=!M
// {line: 9678}
// if-goto Output.printChar.if.1
@SP
AM=M-1
D=M
@Output.printChar.if.1
D;JNE
// {line: 9684}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9689}
// pop static 10
@SP
AM=M-1
D=M
@Output.static.10
M=D
// {line: 9695}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9700}
// pop static 9
@SP
AM=M-1
D=M
@Output.static.9
M=D
// {line: 9709}
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
// {line: 9722}
// call Output._print nArgs: 1
@1
D=A
@R14
M=D
@Output._print
D=A
@R15
M=D
@Output.printChar.call.1
D=A
@call
0;JMP
(Output.printChar.call.1)
// {line: 9727}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 9733}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9738}
// pop static 10
@SP
AM=M-1
D=M
@Output.static.10
M=D
// {line: 9739}
(Output.printChar.if.1)
// {line: 9744}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 9745}
(Output.printChar.goto.0)
// {line: 9747}
// return
@return
0;JMP
// {line: 9780}
// function Output._print nLocals: 8
(Output._print)
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
// {line: 9793}
// call Screen.getColor nArgs: 0
@0
D=A
@R14
M=D
@Screen.getColor
D=A
@R15
M=D
@Output._print.call.0
D=A
@call
0;JMP
(Output._print.call.0)
// {line: 9806}
// pop local 7
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
M=D
// {line: 9815}
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
// {line: 9828}
// call Output.getMap nArgs: 1
@1
D=A
@R14
M=D
@Output.getMap
D=A
@R15
M=D
@Output._print.call.1
D=A
@call
0;JMP
(Output._print.call.1)
// {line: 9834}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 9840}
// push static 10
@Output.static.10
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9846}
// push constant 8
@8
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9859}
// call Math.multiply nArgs: 2
@2
D=A
@R14
M=D
@Math.multiply
D=A
@R15
M=D
@Output._print.call.2
D=A
@call
0;JMP
(Output._print.call.2)
// {line: 9866}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 9872}
// push static 9
@Output.static.9
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9878}
// push constant 11
@11
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9891}
// call Math.multiply nArgs: 2
@2
D=A
@R14
M=D
@Math.multiply
D=A
@R15
M=D
@Output._print.call.3
D=A
@call
0;JMP
(Output._print.call.3)
// {line: 9899}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 9908}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9914}
// push constant 7
@7
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9919}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 9928}
// pop local 3
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
A=A+1
M=D
// {line: 9937}
// push local 2
@2
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9943}
// push constant 10
@10
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9948}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 9958}
// pop local 4
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
A=A+1
A=A+1
M=D
// {line: 9964}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9976}
// pop local 6
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
M=D
// {line: 9977}
(Output._print.while.0)
// {line: 9986}
// push local 2
@2
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9995}
// push local 6
@6
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10000}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 10009}
// push local 4
@4
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10016}
// lt
@Output._print.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Output._print.lt.0)
// {line: 10019}
// not
@SP
A=M-1
M=!M
// {line: 10024}
// if-goto Output._print.while.1
@SP
AM=M-1
D=M
@Output._print.while.1
D;JNE
// {line: 10030}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10041}
// pop local 5
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
M=D
// {line: 10042}
(Output._print.while.2)
// {line: 10051}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10060}
// push local 5
@5
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10065}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 10074}
// push local 3
@3
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10081}
// lt
@Output._print.lt.1
D=A
@R14
M=D
@lt
0;JMP
(Output._print.lt.1)
// {line: 10084}
// not
@SP
A=M-1
M=!M
// {line: 10089}
// if-goto Output._print.while.3
@SP
AM=M-1
D=M
@Output._print.while.3
D;JNE
// {line: 10095}
// push pointer 1
@4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10104}
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
// {line: 10113}
// push local 6
@6
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10118}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 10123}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 10132}
// push that 0
@0
D=A
@THAT
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10137}
// pop temp 2
@SP
AM=M-1
D=M
@R7
M=D
// {line: 10142}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 10148}
// push temp 2
@7
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10157}
// push local 5
@5
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10170}
// call Math.bit nArgs: 2
@2
D=A
@R14
M=D
@Math.bit
D=A
@R15
M=D
@Output._print.call.4
D=A
@call
0;JMP
(Output._print.call.4)
// {line: 10183}
// call Screen.setColor nArgs: 1
@1
D=A
@R14
M=D
@Screen.setColor
D=A
@R15
M=D
@Output._print.call.5
D=A
@call
0;JMP
(Output._print.call.5)
// {line: 10188}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 10197}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10206}
// push local 5
@5
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10211}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 10220}
// push local 2
@2
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10229}
// push local 6
@6
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10234}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 10247}
// call Screen.drawPixel nArgs: 2
@2
D=A
@R14
M=D
@Screen.drawPixel
D=A
@R15
M=D
@Output._print.call.6
D=A
@call
0;JMP
(Output._print.call.6)
// {line: 10252}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 10261}
// push local 5
@5
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10267}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10272}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 10283}
// pop local 5
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
M=D
// {line: 10285}
// goto Output._print.while.2
@Output._print.while.2
0;JMP
// {line: 10286}
(Output._print.while.3)
// {line: 10295}
// push local 6
@6
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10301}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10306}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 10318}
// pop local 6
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
M=D
// {line: 10320}
// goto Output._print.while.0
@Output._print.while.0
0;JMP
// {line: 10321}
(Output._print.while.1)
// {line: 10330}
// push local 7
@7
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10343}
// call Screen.setColor nArgs: 1
@1
D=A
@R14
M=D
@Screen.setColor
D=A
@R15
M=D
@Output._print.call.7
D=A
@call
0;JMP
(Output._print.call.7)
// {line: 10348}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 10350}
// return
@return
0;JMP
// {line: 10359}
// function Output.printString nLocals: 2
(Output.printString)
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
// {line: 10368}
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
// {line: 10381}
// call String.length nArgs: 1
@1
D=A
@R14
M=D
@String.length
D=A
@R15
M=D
@Output.printString.call.0
D=A
@call
0;JMP
(Output.printString.call.0)
// {line: 10388}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 10394}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10400}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 10401}
(Output.printString.while.0)
// {line: 10410}
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
// {line: 10419}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10426}
// lt
@Output.printString.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Output.printString.lt.0)
// {line: 10429}
// not
@SP
A=M-1
M=!M
// {line: 10434}
// if-goto Output.printString.while.1
@SP
AM=M-1
D=M
@Output.printString.while.1
D;JNE
// {line: 10443}
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
// {line: 10452}
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
// {line: 10465}
// call String.charAt nArgs: 2
@2
D=A
@R14
M=D
@String.charAt
D=A
@R15
M=D
@Output.printString.call.1
D=A
@call
0;JMP
(Output.printString.call.1)
// {line: 10478}
// call Output.printChar nArgs: 1
@1
D=A
@R14
M=D
@Output.printChar
D=A
@R15
M=D
@Output.printString.call.2
D=A
@call
0;JMP
(Output.printString.call.2)
// {line: 10483}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 10492}
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
// {line: 10498}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10503}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 10509}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 10511}
// goto Output.printString.while.0
@Output.printString.while.0
0;JMP
// {line: 10512}
(Output.printString.while.1)
// {line: 10514}
// return
@return
0;JMP
// {line: 10519}
// function Output.printInt nLocals: 1
(Output.printInt)
@SP
AM=M+1
A=A-1
M=0
// {line: 10525}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10538}
// call String.new nArgs: 1
@1
D=A
@R14
M=D
@String.new
D=A
@R15
M=D
@Output.printInt.call.0
D=A
@call
0;JMP
(Output.printInt.call.0)
// {line: 10544}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 10553}
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
// {line: 10562}
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
// {line: 10575}
// call String.setInt nArgs: 2
@2
D=A
@R14
M=D
@String.setInt
D=A
@R15
M=D
@Output.printInt.call.1
D=A
@call
0;JMP
(Output.printInt.call.1)
// {line: 10580}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 10589}
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
// {line: 10602}
// call Output.printString nArgs: 1
@1
D=A
@R14
M=D
@Output.printString
D=A
@R15
M=D
@Output.printInt.call.2
D=A
@call
0;JMP
(Output.printInt.call.2)
// {line: 10607}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 10609}
// return
@return
0;JMP
// {line: 10610}
// function Output.println nLocals: 0
(Output.println)
// {line: 10616}
// push static 9
@Output.static.9
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10622}
// push constant 23
@23
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10629}
// lt
@Output.println.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Output.println.lt.0)
// {line: 10634}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 10640}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10646}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10649}
// not
@SP
A=M-1
M=!M
// {line: 10654}
// if-goto Output.println.if.0
@SP
AM=M-1
D=M
@Output.println.if.0
D;JNE
// {line: 10660}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10665}
// pop static 10
@SP
AM=M-1
D=M
@Output.static.10
M=D
// {line: 10671}
// push static 9
@Output.static.9
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10677}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10682}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 10687}
// pop static 9
@SP
AM=M-1
D=M
@Output.static.9
M=D
// {line: 10688}
(Output.println.if.0)
// {line: 10693}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 10695}
// return
@return
0;JMP
// {line: 10696}
// function Output.backSpace nLocals: 0
(Output.backSpace)
// {line: 10702}
// push static 10
@Output.static.10
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10708}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10715}
// gt
@Output.backSpace.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Output.backSpace.gt.0)
// {line: 10720}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 10726}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10732}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10735}
// not
@SP
A=M-1
M=!M
// {line: 10740}
// if-goto Output.backSpace.if.0
@SP
AM=M-1
D=M
@Output.backSpace.if.0
D;JNE
// {line: 10746}
// push static 9
@Output.static.9
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10752}
// push static 10
@Output.static.10
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10758}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10763}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 10776}
// call Output.moveCursor nArgs: 2
@2
D=A
@R14
M=D
@Output.moveCursor
D=A
@R15
M=D
@Output.backSpace.call.0
D=A
@call
0;JMP
(Output.backSpace.call.0)
// {line: 10781}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 10782}
(Output.backSpace.if.0)
// {line: 10787}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 10789}
// return
@return
0;JMP
// {line: 10790}
// function Main.main nLocals: 0
(Main.main)
// {line: 10796}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10802}
// push constant 220
@220
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10808}
// push constant 511
@511
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10814}
// push constant 220
@220
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10827}
// call Screen.drawLine nArgs: 4
@4
D=A
@R14
M=D
@Screen.drawLine
D=A
@R15
M=D
@Main.main.call.0
D=A
@call
0;JMP
(Main.main.call.0)
// {line: 10832}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 10838}
// push constant 280
@280
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10844}
// push constant 90
@90
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10850}
// push constant 410
@410
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10856}
// push constant 220
@220
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10869}
// call Screen.drawRectangle nArgs: 4
@4
D=A
@R14
M=D
@Screen.drawRectangle
D=A
@R15
M=D
@Main.main.call.1
D=A
@call
0;JMP
(Main.main.call.1)
// {line: 10874}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 10880}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10893}
// call Screen.setColor nArgs: 1
@1
D=A
@R14
M=D
@Screen.setColor
D=A
@R15
M=D
@Main.main.call.2
D=A
@call
0;JMP
(Main.main.call.2)
// {line: 10898}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 10904}
// push constant 350
@350
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10910}
// push constant 120
@120
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10916}
// push constant 390
@390
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10922}
// push constant 219
@219
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10935}
// call Screen.drawRectangle nArgs: 4
@4
D=A
@R14
M=D
@Screen.drawRectangle
D=A
@R15
M=D
@Main.main.call.3
D=A
@call
0;JMP
(Main.main.call.3)
// {line: 10940}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 10946}
// push constant 292
@292
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10952}
// push constant 120
@120
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10958}
// push constant 332
@332
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10964}
// push constant 150
@150
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10977}
// call Screen.drawRectangle nArgs: 4
@4
D=A
@R14
M=D
@Screen.drawRectangle
D=A
@R15
M=D
@Main.main.call.4
D=A
@call
0;JMP
(Main.main.call.4)
// {line: 10982}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 10988}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10991}
// not
@SP
A=M-1
M=!M
// {line: 11004}
// call Screen.setColor nArgs: 1
@1
D=A
@R14
M=D
@Screen.setColor
D=A
@R15
M=D
@Main.main.call.5
D=A
@call
0;JMP
(Main.main.call.5)
// {line: 11009}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 11015}
// push constant 360
@360
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11021}
// push constant 170
@170
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11027}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11040}
// call Screen.drawCircle nArgs: 3
@3
D=A
@R14
M=D
@Screen.drawCircle
D=A
@R15
M=D
@Main.main.call.6
D=A
@call
0;JMP
(Main.main.call.6)
// {line: 11045}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 11051}
// push constant 280
@280
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11057}
// push constant 90
@90
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11063}
// push constant 345
@345
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11069}
// push constant 35
@35
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11082}
// call Screen.drawLine nArgs: 4
@4
D=A
@R14
M=D
@Screen.drawLine
D=A
@R15
M=D
@Main.main.call.7
D=A
@call
0;JMP
(Main.main.call.7)
// {line: 11087}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 11093}
// push constant 345
@345
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11099}
// push constant 35
@35
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11105}
// push constant 410
@410
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11111}
// push constant 90
@90
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11124}
// call Screen.drawLine nArgs: 4
@4
D=A
@R14
M=D
@Screen.drawLine
D=A
@R15
M=D
@Main.main.call.8
D=A
@call
0;JMP
(Main.main.call.8)
// {line: 11129}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 11135}
// push constant 140
@140
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11141}
// push constant 60
@60
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11147}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11160}
// call Screen.drawCircle nArgs: 3
@3
D=A
@R14
M=D
@Screen.drawCircle
D=A
@R15
M=D
@Main.main.call.9
D=A
@call
0;JMP
(Main.main.call.9)
// {line: 11165}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 11171}
// push constant 140
@140
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11177}
// push constant 26
@26
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11183}
// push constant 140
@140
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11189}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11202}
// call Screen.drawLine nArgs: 4
@4
D=A
@R14
M=D
@Screen.drawLine
D=A
@R15
M=D
@Main.main.call.10
D=A
@call
0;JMP
(Main.main.call.10)
// {line: 11207}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 11213}
// push constant 163
@163
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11219}
// push constant 35
@35
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11225}
// push constant 178
@178
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11231}
// push constant 20
@20
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11244}
// call Screen.drawLine nArgs: 4
@4
D=A
@R14
M=D
@Screen.drawLine
D=A
@R15
M=D
@Main.main.call.11
D=A
@call
0;JMP
(Main.main.call.11)
// {line: 11249}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 11255}
// push constant 174
@174
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11261}
// push constant 60
@60
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11267}
// push constant 194
@194
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11273}
// push constant 60
@60
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11286}
// call Screen.drawLine nArgs: 4
@4
D=A
@R14
M=D
@Screen.drawLine
D=A
@R15
M=D
@Main.main.call.12
D=A
@call
0;JMP
(Main.main.call.12)
// {line: 11291}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 11297}
// push constant 163
@163
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11303}
// push constant 85
@85
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11309}
// push constant 178
@178
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11315}
// push constant 100
@100
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11328}
// call Screen.drawLine nArgs: 4
@4
D=A
@R14
M=D
@Screen.drawLine
D=A
@R15
M=D
@Main.main.call.13
D=A
@call
0;JMP
(Main.main.call.13)
// {line: 11333}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 11339}
// push constant 140
@140
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11345}
// push constant 94
@94
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11351}
// push constant 140
@140
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11357}
// push constant 114
@114
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11370}
// call Screen.drawLine nArgs: 4
@4
D=A
@R14
M=D
@Screen.drawLine
D=A
@R15
M=D
@Main.main.call.14
D=A
@call
0;JMP
(Main.main.call.14)
// {line: 11375}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 11381}
// push constant 117
@117
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11387}
// push constant 85
@85
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11393}
// push constant 102
@102
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11399}
// push constant 100
@100
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11412}
// call Screen.drawLine nArgs: 4
@4
D=A
@R14
M=D
@Screen.drawLine
D=A
@R15
M=D
@Main.main.call.15
D=A
@call
0;JMP
(Main.main.call.15)
// {line: 11417}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 11423}
// push constant 106
@106
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11429}
// push constant 60
@60
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11435}
// push constant 86
@86
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11441}
// push constant 60
@60
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11454}
// call Screen.drawLine nArgs: 4
@4
D=A
@R14
M=D
@Screen.drawLine
D=A
@R15
M=D
@Main.main.call.16
D=A
@call
0;JMP
(Main.main.call.16)
// {line: 11459}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 11465}
// push constant 117
@117
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11471}
// push constant 35
@35
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11477}
// push constant 102
@102
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11483}
// push constant 20
@20
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11496}
// call Screen.drawLine nArgs: 4
@4
D=A
@R14
M=D
@Screen.drawLine
D=A
@R15
M=D
@Main.main.call.17
D=A
@call
0;JMP
(Main.main.call.17)
// {line: 11501}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 11507}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11509}
// return
@return
0;JMP
// {line: 11514}
// function Array.new nLocals: 1
(Array.new)
@SP
AM=M+1
A=A-1
M=0
// {line: 11523}
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
// {line: 11536}
// call Memory.alloc nArgs: 1
@1
D=A
@R14
M=D
@Memory.alloc
D=A
@R15
M=D
@Array.new.call.0
D=A
@call
0;JMP
(Array.new.call.0)
// {line: 11542}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 11551}
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
// {line: 11553}
// return
@return
0;JMP
// {line: 11558}
// function Array.dispose nLocals: 1
(Array.dispose)
@SP
AM=M+1
A=A-1
M=0
// {line: 11567}
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
// {line: 11572}
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// {line: 11578}
// push pointer 0
@3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 11591}
// call Memory.deAlloc nArgs: 1
@1
D=A
@R14
M=D
@Memory.deAlloc
D=A
@R15
M=D
@Array.dispose.call.0
D=A
@call
0;JMP
(Array.dispose.call.0)
// {line: 11596}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 11598}
// return
@return
0;JMP
// {line: 11603}
// function Memory.init nLocals: 1
(Memory.init)
@SP
AM=M+1
A=A-1
M=0
// {line: 11609}
// push constant 2048
@2048
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11614}
// pop static 0
@SP
AM=M-1
D=M
@Memory.static.0
M=D
// {line: 11620}
// push constant 16382
@16382
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11625}
// pop static 1
@SP
AM=M-1
D=M
@Memory.static.1
M=D
// {line: 11631}
// push constant 16383
@16383
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11636}
// pop static 3
@SP
AM=M-1
D=M
@Memory.static.3
M=D
// {line: 11642}
// push static 0
@Memory.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 11647}
// pop static 2
@SP
AM=M-1
D=M
@Memory.static.2
M=D
// {line: 11653}
// push static 0
@Memory.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 11659}
// push static 1
@Memory.static.1
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 11665}
// push static 0
@Memory.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 11670}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 11676}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11681}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 11694}
// call Memory.poke nArgs: 2
@2
D=A
@R14
M=D
@Memory.poke
D=A
@R15
M=D
@Memory.init.call.0
D=A
@call
0;JMP
(Memory.init.call.0)
// {line: 11699}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 11705}
// push static 0
@Memory.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 11711}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11716}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 11722}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11735}
// call Memory.poke nArgs: 2
@2
D=A
@R14
M=D
@Memory.poke
D=A
@R15
M=D
@Memory.init.call.1
D=A
@call
0;JMP
(Memory.init.call.1)
// {line: 11740}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 11742}
// return
@return
0;JMP
// {line: 11747}
// function Memory.peek nLocals: 1
(Memory.peek)
@SP
AM=M+1
A=A-1
M=0
// {line: 11753}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11759}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 11765}
// push pointer 1
@4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 11774}
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
// {line: 11783}
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
// {line: 11788}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 11793}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 11802}
// push that 0
@0
D=A
@THAT
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 11807}
// pop temp 2
@SP
AM=M-1
D=M
@R7
M=D
// {line: 11812}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 11818}
// push temp 2
@7
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 11820}
// return
@return
0;JMP
// {line: 11825}
// function Memory.poke nLocals: 1
(Memory.poke)
@SP
AM=M+1
A=A-1
M=0
// {line: 11831}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11837}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 11846}
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
// {line: 11855}
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
// {line: 11860}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 11865}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 11874}
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
// {line: 11880}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 11882}
// return
@return
0;JMP
// {line: 11903}
// function Memory.alloc nLocals: 5
(Memory.alloc)
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
// {line: 11912}
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
// {line: 11918}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11925}
// lt
@Memory.alloc.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Memory.alloc.lt.0)
// {line: 11934}
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
// {line: 11940}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11947}
// eq
@Memory.alloc.eq.0
D=A
@R14
M=D
@eq
0;JMP
(Memory.alloc.eq.0)
// {line: 11952}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 11957}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 11963}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 11969}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 11972}
// not
@SP
A=M-1
M=!M
// {line: 11977}
// if-goto Memory.alloc.if.0
@SP
AM=M-1
D=M
@Memory.alloc.if.0
D;JNE
// {line: 11983}
// push static 3
@Memory.static.3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 11985}
// return
@return
0;JMP
// {line: 11986}
(Memory.alloc.if.0)
// {line: 11991}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 11997}
// push static 2
@Memory.static.2
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12004}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 12013}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12019}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 12025}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12035}
// pop local 4
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
A=A+1
A=A+1
M=D
// {line: 12036}
(Memory.alloc.while.0)
// {line: 12045}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12051}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12058}
// eq
@Memory.alloc.eq.1
D=A
@R14
M=D
@eq
0;JMP
(Memory.alloc.eq.1)
// {line: 12061}
// not
@SP
A=M-1
M=!M
// {line: 12064}
// not
@SP
A=M-1
M=!M
// {line: 12069}
// if-goto Memory.alloc.while.1
@SP
AM=M-1
D=M
@Memory.alloc.while.1
D;JNE
// {line: 12078}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12091}
// call Memory.peek nArgs: 1
@1
D=A
@R14
M=D
@Memory.peek
D=A
@R15
M=D
@Memory.alloc.call.0
D=A
@call
0;JMP
(Memory.alloc.call.0)
// {line: 12099}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 12108}
// push local 2
@2
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12117}
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
// {line: 12124}
// eq
@Memory.alloc.eq.2
D=A
@R14
M=D
@eq
0;JMP
(Memory.alloc.eq.2)
// {line: 12129}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 12135}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12141}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12144}
// not
@SP
A=M-1
M=!M
// {line: 12149}
// if-goto Memory.alloc.if.1
@SP
AM=M-1
D=M
@Memory.alloc.if.1
D;JNE
// {line: 12158}
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
// {line: 12164}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12169}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 12178}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12184}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12189}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 12202}
// call Memory.poke nArgs: 2
@2
D=A
@R14
M=D
@Memory.poke
D=A
@R15
M=D
@Memory.alloc.call.1
D=A
@call
0;JMP
(Memory.alloc.call.1)
// {line: 12207}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 12216}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12218}
// return
@return
0;JMP
// {line: 12219}
(Memory.alloc.if.1)
// {line: 12224}
// if-goto Memory.alloc.goto.0
@SP
AM=M-1
D=M
@Memory.alloc.goto.0
D;JNE
// {line: 12233}
// push local 2
@2
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12242}
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
// {line: 12249}
// gt
@Memory.alloc.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Memory.alloc.gt.0)
// {line: 12254}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 12260}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12266}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12269}
// not
@SP
A=M-1
M=!M
// {line: 12274}
// if-goto Memory.alloc.if.2
@SP
AM=M-1
D=M
@Memory.alloc.if.2
D;JNE
// {line: 12283}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12292}
// push local 2
@2
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12297}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 12303}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12308}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 12317}
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
// {line: 12322}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 12331}
// pop local 3
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
A=A+1
M=D
// {line: 12340}
// push local 3
@3
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12349}
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
// {line: 12362}
// call Memory.poke nArgs: 2
@2
D=A
@R14
M=D
@Memory.poke
D=A
@R15
M=D
@Memory.alloc.call.2
D=A
@call
0;JMP
(Memory.alloc.call.2)
// {line: 12367}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 12376}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12385}
// push local 2
@2
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12394}
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
// {line: 12399}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 12405}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12410}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 12423}
// call Memory.poke nArgs: 2
@2
D=A
@R14
M=D
@Memory.poke
D=A
@R15
M=D
@Memory.alloc.call.3
D=A
@call
0;JMP
(Memory.alloc.call.3)
// {line: 12428}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 12437}
// push local 3
@3
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12443}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12448}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 12450}
// return
@return
0;JMP
// {line: 12451}
(Memory.alloc.if.2)
// {line: 12456}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 12457}
(Memory.alloc.goto.0)
// {line: 12466}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12472}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 12481}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12487}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12492}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 12505}
// call Memory.peek nArgs: 1
@1
D=A
@R14
M=D
@Memory.peek
D=A
@R15
M=D
@Memory.alloc.call.4
D=A
@call
0;JMP
(Memory.alloc.call.4)
// {line: 12512}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 12521}
// push local 4
@4
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12527}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12532}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 12542}
// pop local 4
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
A=A+1
A=A+1
M=D
// {line: 12544}
// goto Memory.alloc.while.0
@Memory.alloc.while.0
0;JMP
// {line: 12545}
(Memory.alloc.while.1)
// {line: 12558}
// call Memory.defrag nArgs: 0
@0
D=A
@R14
M=D
@Memory.defrag
D=A
@R15
M=D
@Memory.alloc.call.5
D=A
@call
0;JMP
(Memory.alloc.call.5)
// {line: 12563}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 12565}
// return
@return
0;JMP
// {line: 12566}
// function Memory.defrag nLocals: 0
(Memory.defrag)
// {line: 12572}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12585}
// call Sys.error nArgs: 1
@1
D=A
@R14
M=D
@Sys.error
D=A
@R15
M=D
@Memory.defrag.call.0
D=A
@call
0;JMP
(Memory.defrag.call.0)
// {line: 12590}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 12592}
// return
@return
0;JMP
// {line: 12597}
// function Memory.deAlloc nLocals: 1
(Memory.deAlloc)
@SP
AM=M+1
A=A-1
M=0
// {line: 12606}
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
// {line: 12612}
// push static 3
@Memory.static.3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12619}
// eq
@Memory.deAlloc.eq.0
D=A
@R14
M=D
@eq
0;JMP
(Memory.deAlloc.eq.0)
// {line: 12624}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 12630}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12636}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12639}
// not
@SP
A=M-1
M=!M
// {line: 12644}
// if-goto Memory.deAlloc.if.0
@SP
AM=M-1
D=M
@Memory.deAlloc.if.0
D;JNE
// {line: 12650}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12652}
// return
@return
0;JMP
// {line: 12653}
(Memory.deAlloc.if.0)
// {line: 12658}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 12667}
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
// {line: 12673}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 12682}
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
// {line: 12688}
// push static 2
@Memory.static.2
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12694}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12699}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 12712}
// call Memory.peek nArgs: 1
@1
D=A
@R14
M=D
@Memory.peek
D=A
@R15
M=D
@Memory.deAlloc.call.0
D=A
@call
0;JMP
(Memory.deAlloc.call.0)
// {line: 12725}
// call Memory.poke nArgs: 2
@2
D=A
@R14
M=D
@Memory.poke
D=A
@R15
M=D
@Memory.deAlloc.call.1
D=A
@call
0;JMP
(Memory.deAlloc.call.1)
// {line: 12730}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 12736}
// push static 2
@Memory.static.2
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12742}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12747}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 12756}
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
// {line: 12769}
// call Memory.poke nArgs: 2
@2
D=A
@R14
M=D
@Memory.poke
D=A
@R15
M=D
@Memory.deAlloc.call.2
D=A
@call
0;JMP
(Memory.deAlloc.call.2)
// {line: 12774}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 12776}
// return
@return
0;JMP
// {line: 12777}
// function Memory.isValid nLocals: 0
(Memory.isValid)
// {line: 12786}
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
// {line: 12792}
// push static 0
@Memory.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12799}
// gt
@Memory.isValid.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Memory.isValid.gt.0)
// {line: 12808}
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
// {line: 12814}
// push static 0
@Memory.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12821}
// eq
@Memory.isValid.eq.0
D=A
@R14
M=D
@eq
0;JMP
(Memory.isValid.eq.0)
// {line: 12826}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 12835}
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
// {line: 12841}
// push static 1
@Memory.static.1
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12848}
// lt
@Memory.isValid.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Memory.isValid.lt.0)
// {line: 12857}
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
// {line: 12863}
// push static 1
@Memory.static.1
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12870}
// eq
@Memory.isValid.eq.1
D=A
@R14
M=D
@eq
0;JMP
(Memory.isValid.eq.1)
// {line: 12875}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 12880}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 12885}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 12891}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12897}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12900}
// not
@SP
A=M-1
M=!M
// {line: 12905}
// if-goto Memory.isValid.if.0
@SP
AM=M-1
D=M
@Memory.isValid.if.0
D;JNE
// {line: 12911}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12914}
// not
@SP
A=M-1
M=!M
// {line: 12916}
// return
@return
0;JMP
// {line: 12917}
(Memory.isValid.if.0)
// {line: 12922}
// if-goto Memory.isValid.goto.0
@SP
AM=M-1
D=M
@Memory.isValid.goto.0
D;JNE
// {line: 12928}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12930}
// return
@return
0;JMP
// {line: 12931}
(Memory.isValid.goto.0)
// {line: 12933}
// return
@return
0;JMP
// {line: 12938}
// function String.new nLocals: 1
(String.new)
@SP
AM=M+1
A=A-1
M=0
// {line: 12944}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12957}
// call Memory.alloc nArgs: 1
@1
D=A
@R14
M=D
@Memory.alloc
D=A
@R15
M=D
@String.new.call.0
D=A
@call
0;JMP
(String.new.call.0)
// {line: 12962}
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// {line: 12971}
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
// {line: 12977}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12984}
// lt
@String.new.lt.0
D=A
@R14
M=D
@lt
0;JMP
(String.new.lt.0)
// {line: 12989}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 12995}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13001}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13004}
// not
@SP
A=M-1
M=!M
// {line: 13009}
// if-goto String.new.if.0
@SP
AM=M-1
D=M
@String.new.if.0
D;JNE
// {line: 13015}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13021}
// pop argument 0
@SP
AM=M-1
D=M
@ARG
A=M
M=D
// {line: 13022}
(String.new.if.0)
// {line: 13027}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 13033}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13041}
// pop this 2
@SP
AM=M-1
D=M
@THIS
A=M
A=A+1
A=A+1
M=D
// {line: 13050}
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
// {line: 13057}
// pop this 1
@SP
AM=M-1
D=M
@THIS
A=M
A=A+1
M=D
// {line: 13066}
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
// {line: 13079}
// call Array.new nArgs: 1
@1
D=A
@R14
M=D
@Array.new
D=A
@R15
M=D
@String.new.call.1
D=A
@call
0;JMP
(String.new.call.1)
// {line: 13085}
// pop this 0
@SP
AM=M-1
D=M
@THIS
A=M
M=D
// {line: 13091}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13097}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 13098}
(String.new.while.0)
// {line: 13107}
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
// {line: 13116}
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
// {line: 13123}
// lt
@String.new.lt.1
D=A
@R14
M=D
@lt
0;JMP
(String.new.lt.1)
// {line: 13126}
// not
@SP
A=M-1
M=!M
// {line: 13131}
// if-goto String.new.while.1
@SP
AM=M-1
D=M
@String.new.while.1
D;JNE
// {line: 13140}
// push this 0
@0
D=A
@THIS
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13149}
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
// {line: 13154}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 13159}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 13165}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13171}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 13180}
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
// {line: 13186}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13191}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 13197}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 13199}
// goto String.new.while.0
@String.new.while.0
0;JMP
// {line: 13200}
(String.new.while.1)
// {line: 13206}
// push pointer 0
@3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13208}
// return
@return
0;JMP
// {line: 13213}
// function String.dispose nLocals: 1
(String.dispose)
@SP
AM=M+1
A=A-1
M=0
// {line: 13222}
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
// {line: 13227}
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// {line: 13233}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13240}
// pop this 1
@SP
AM=M-1
D=M
@THIS
A=M
A=A+1
M=D
// {line: 13246}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13254}
// pop this 2
@SP
AM=M-1
D=M
@THIS
A=M
A=A+1
A=A+1
M=D
// {line: 13263}
// push this 0
@0
D=A
@THIS
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13276}
// call Array.dispose nArgs: 1
@1
D=A
@R14
M=D
@Array.dispose
D=A
@R15
M=D
@String.dispose.call.0
D=A
@call
0;JMP
(String.dispose.call.0)
// {line: 13281}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 13283}
// return
@return
0;JMP
// {line: 13288}
// function String.length nLocals: 1
(String.length)
@SP
AM=M+1
A=A-1
M=0
// {line: 13297}
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
// {line: 13302}
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// {line: 13311}
// push this 1
@1
D=A
@THIS
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13313}
// return
@return
0;JMP
// {line: 13318}
// function String.charAt nLocals: 1
(String.charAt)
@SP
AM=M+1
A=A-1
M=0
// {line: 13327}
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
// {line: 13332}
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// {line: 13341}
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
// {line: 13347}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13354}
// lt
@String.charAt.lt.0
D=A
@R14
M=D
@lt
0;JMP
(String.charAt.lt.0)
// {line: 13359}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 13365}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13371}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13374}
// not
@SP
A=M-1
M=!M
// {line: 13379}
// if-goto String.charAt.if.0
@SP
AM=M-1
D=M
@String.charAt.if.0
D;JNE
// {line: 13388}
// push this 1
@1
D=A
@THIS
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13397}
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
// {line: 13402}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 13415}
// call Math.abs nArgs: 1
@1
D=A
@R14
M=D
@Math.abs
D=A
@R15
M=D
@String.charAt.call.0
D=A
@call
0;JMP
(String.charAt.call.0)
// {line: 13422}
// pop argument 1
@SP
AM=M-1
D=M
@ARG
A=M
A=A+1
M=D
// {line: 13423}
(String.charAt.if.0)
// {line: 13428}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 13437}
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
// {line: 13446}
// push this 1
@1
D=A
@THIS
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13453}
// gt
@String.charAt.gt.0
D=A
@R14
M=D
@gt
0;JMP
(String.charAt.gt.0)
// {line: 13462}
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
// {line: 13471}
// push this 1
@1
D=A
@THIS
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13478}
// eq
@String.charAt.eq.0
D=A
@R14
M=D
@eq
0;JMP
(String.charAt.eq.0)
// {line: 13483}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 13488}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 13494}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13500}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13503}
// not
@SP
A=M-1
M=!M
// {line: 13508}
// if-goto String.charAt.if.1
@SP
AM=M-1
D=M
@String.charAt.if.1
D;JNE
// {line: 13517}
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
// {line: 13526}
// push this 1
@1
D=A
@THIS
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13539}
// call Math.mod nArgs: 2
@2
D=A
@R14
M=D
@Math.mod
D=A
@R15
M=D
@String.charAt.call.1
D=A
@call
0;JMP
(String.charAt.call.1)
// {line: 13546}
// pop argument 1
@SP
AM=M-1
D=M
@ARG
A=M
A=A+1
M=D
// {line: 13547}
(String.charAt.if.1)
// {line: 13552}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 13558}
// push pointer 1
@4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13567}
// push this 0
@0
D=A
@THIS
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13576}
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
// {line: 13581}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 13586}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 13595}
// push that 0
@0
D=A
@THAT
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13600}
// pop temp 2
@SP
AM=M-1
D=M
@R7
M=D
// {line: 13605}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 13611}
// push temp 2
@7
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13613}
// return
@return
0;JMP
// {line: 13618}
// function String.setCharAt nLocals: 1
(String.setCharAt)
@SP
AM=M+1
A=A-1
M=0
// {line: 13627}
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
// {line: 13632}
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// {line: 13641}
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
// {line: 13647}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13654}
// lt
@String.setCharAt.lt.0
D=A
@R14
M=D
@lt
0;JMP
(String.setCharAt.lt.0)
// {line: 13659}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 13665}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13671}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13674}
// not
@SP
A=M-1
M=!M
// {line: 13679}
// if-goto String.setCharAt.if.0
@SP
AM=M-1
D=M
@String.setCharAt.if.0
D;JNE
// {line: 13688}
// push this 1
@1
D=A
@THIS
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13697}
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
// {line: 13702}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 13715}
// call Math.abs nArgs: 1
@1
D=A
@R14
M=D
@Math.abs
D=A
@R15
M=D
@String.setCharAt.call.0
D=A
@call
0;JMP
(String.setCharAt.call.0)
// {line: 13722}
// pop argument 1
@SP
AM=M-1
D=M
@ARG
A=M
A=A+1
M=D
// {line: 13723}
(String.setCharAt.if.0)
// {line: 13728}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 13737}
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
// {line: 13746}
// push this 1
@1
D=A
@THIS
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13753}
// gt
@String.setCharAt.gt.0
D=A
@R14
M=D
@gt
0;JMP
(String.setCharAt.gt.0)
// {line: 13762}
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
// {line: 13771}
// push this 1
@1
D=A
@THIS
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13778}
// eq
@String.setCharAt.eq.0
D=A
@R14
M=D
@eq
0;JMP
(String.setCharAt.eq.0)
// {line: 13783}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 13788}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 13794}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13800}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13803}
// not
@SP
A=M-1
M=!M
// {line: 13808}
// if-goto String.setCharAt.if.1
@SP
AM=M-1
D=M
@String.setCharAt.if.1
D;JNE
// {line: 13817}
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
// {line: 13826}
// push this 1
@1
D=A
@THIS
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13839}
// call Math.mod nArgs: 2
@2
D=A
@R14
M=D
@Math.mod
D=A
@R15
M=D
@String.setCharAt.call.1
D=A
@call
0;JMP
(String.setCharAt.call.1)
// {line: 13846}
// pop argument 1
@SP
AM=M-1
D=M
@ARG
A=M
A=A+1
M=D
// {line: 13847}
(String.setCharAt.if.1)
// {line: 13852}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 13861}
// push this 0
@0
D=A
@THIS
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13870}
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
// {line: 13875}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 13880}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 13889}
// push argument 2
@2
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13895}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 13897}
// return
@return
0;JMP
// {line: 13902}
// function String.appendChar nLocals: 1
(String.appendChar)
@SP
AM=M+1
A=A-1
M=0
// {line: 13911}
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
// {line: 13916}
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// {line: 13925}
// push this 2
@2
D=A
@THIS
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13934}
// push this 1
@1
D=A
@THIS
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13941}
// eq
@String.appendChar.eq.0
D=A
@R14
M=D
@eq
0;JMP
(String.appendChar.eq.0)
// {line: 13946}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 13952}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13958}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13961}
// not
@SP
A=M-1
M=!M
// {line: 13966}
// if-goto String.appendChar.if.0
@SP
AM=M-1
D=M
@String.appendChar.if.0
D;JNE
// {line: 13972}
// push pointer 0
@3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13978}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13991}
// call String.grow nArgs: 2
@2
D=A
@R14
M=D
@String.grow
D=A
@R15
M=D
@String.appendChar.call.0
D=A
@call
0;JMP
(String.appendChar.call.0)
// {line: 13996}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 13997}
(String.appendChar.if.0)
// {line: 14002}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 14011}
// push this 0
@0
D=A
@THIS
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14020}
// push this 2
@2
D=A
@THIS
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14025}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14030}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 14039}
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
// {line: 14045}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 14054}
// push this 2
@2
D=A
@THIS
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14060}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14065}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14073}
// pop this 2
@SP
AM=M-1
D=M
@THIS
A=M
A=A+1
A=A+1
M=D
// {line: 14079}
// push pointer 0
@3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14081}
// return
@return
0;JMP
// {line: 14090}
// function String.slice nLocals: 2
(String.slice)
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
// {line: 14099}
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
// {line: 14104}
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// {line: 14113}
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
// {line: 14122}
// push argument 2
@2
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14129}
// eq
@String.slice.eq.0
D=A
@R14
M=D
@eq
0;JMP
(String.slice.eq.0)
// {line: 14134}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 14140}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14146}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14149}
// not
@SP
A=M-1
M=!M
// {line: 14154}
// if-goto String.slice.if.0
@SP
AM=M-1
D=M
@String.slice.if.0
D;JNE
// {line: 14160}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14173}
// call String.new nArgs: 1
@1
D=A
@R14
M=D
@String.new
D=A
@R15
M=D
@String.slice.call.0
D=A
@call
0;JMP
(String.slice.call.0)
// {line: 14179}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 14188}
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
// {line: 14194}
// push pointer 0
@3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14203}
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
// {line: 14216}
// call String.charAt nArgs: 2
@2
D=A
@R14
M=D
@String.charAt
D=A
@R15
M=D
@String.slice.call.1
D=A
@call
0;JMP
(String.slice.call.1)
// {line: 14229}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@String.slice.call.2
D=A
@call
0;JMP
(String.slice.call.2)
// {line: 14234}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 14235}
(String.slice.if.0)
// {line: 14240}
// if-goto String.slice.goto.0
@SP
AM=M-1
D=M
@String.slice.goto.0
D;JNE
// {line: 14249}
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
// {line: 14258}
// push argument 2
@2
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14265}
// lt
@String.slice.lt.0
D=A
@R14
M=D
@lt
0;JMP
(String.slice.lt.0)
// {line: 14270}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 14276}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14282}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14285}
// not
@SP
A=M-1
M=!M
// {line: 14290}
// if-goto String.slice.if.1
@SP
AM=M-1
D=M
@String.slice.if.1
D;JNE
// {line: 14299}
// push argument 2
@2
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14308}
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
// {line: 14313}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 14319}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14324}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14337}
// call String.new nArgs: 1
@1
D=A
@R14
M=D
@String.new
D=A
@R15
M=D
@String.slice.call.3
D=A
@call
0;JMP
(String.slice.call.3)
// {line: 14343}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 14344}
(String.slice.while.0)
// {line: 14353}
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
// {line: 14362}
// push argument 2
@2
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14369}
// lt
@String.slice.lt.1
D=A
@R14
M=D
@lt
0;JMP
(String.slice.lt.1)
// {line: 14378}
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
// {line: 14387}
// push argument 2
@2
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14394}
// eq
@String.slice.eq.1
D=A
@R14
M=D
@eq
0;JMP
(String.slice.eq.1)
// {line: 14399}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 14402}
// not
@SP
A=M-1
M=!M
// {line: 14407}
// if-goto String.slice.while.1
@SP
AM=M-1
D=M
@String.slice.while.1
D;JNE
// {line: 14416}
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
// {line: 14422}
// push pointer 0
@3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14431}
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
// {line: 14444}
// call String.charAt nArgs: 2
@2
D=A
@R14
M=D
@String.charAt
D=A
@R15
M=D
@String.slice.call.4
D=A
@call
0;JMP
(String.slice.call.4)
// {line: 14457}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@String.slice.call.5
D=A
@call
0;JMP
(String.slice.call.5)
// {line: 14462}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 14471}
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
// {line: 14477}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14482}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14489}
// pop argument 1
@SP
AM=M-1
D=M
@ARG
A=M
A=A+1
M=D
// {line: 14491}
// goto String.slice.while.0
@String.slice.while.0
0;JMP
// {line: 14492}
(String.slice.while.1)
// {line: 14493}
(String.slice.if.1)
// {line: 14498}
// if-goto String.slice.goto.1
@SP
AM=M-1
D=M
@String.slice.goto.1
D;JNE
// {line: 14507}
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
// {line: 14516}
// push argument 2
@2
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14521}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 14527}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14532}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14545}
// call String.new nArgs: 1
@1
D=A
@R14
M=D
@String.new
D=A
@R15
M=D
@String.slice.call.6
D=A
@call
0;JMP
(String.slice.call.6)
// {line: 14551}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 14552}
(String.slice.while.2)
// {line: 14561}
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
// {line: 14570}
// push argument 2
@2
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14577}
// gt
@String.slice.gt.0
D=A
@R14
M=D
@gt
0;JMP
(String.slice.gt.0)
// {line: 14586}
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
// {line: 14595}
// push argument 2
@2
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14602}
// eq
@String.slice.eq.2
D=A
@R14
M=D
@eq
0;JMP
(String.slice.eq.2)
// {line: 14607}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 14610}
// not
@SP
A=M-1
M=!M
// {line: 14615}
// if-goto String.slice.while.3
@SP
AM=M-1
D=M
@String.slice.while.3
D;JNE
// {line: 14624}
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
// {line: 14630}
// push pointer 0
@3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14639}
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
// {line: 14652}
// call String.charAt nArgs: 2
@2
D=A
@R14
M=D
@String.charAt
D=A
@R15
M=D
@String.slice.call.7
D=A
@call
0;JMP
(String.slice.call.7)
// {line: 14665}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@String.slice.call.8
D=A
@call
0;JMP
(String.slice.call.8)
// {line: 14670}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 14679}
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
// {line: 14685}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14690}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 14697}
// pop argument 1
@SP
AM=M-1
D=M
@ARG
A=M
A=A+1
M=D
// {line: 14699}
// goto String.slice.while.2
@String.slice.while.2
0;JMP
// {line: 14700}
(String.slice.while.3)
// {line: 14701}
(String.slice.goto.1)
// {line: 14702}
(String.slice.goto.0)
// {line: 14711}
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
// {line: 14713}
// return
@return
0;JMP
// {line: 14726}
// function String.grow nLocals: 3
(String.grow)
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
// {line: 14735}
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
// {line: 14740}
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// {line: 14749}
// push this 1
@1
D=A
@THIS
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14755}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14760}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14773}
// call Array.new nArgs: 1
@1
D=A
@R14
M=D
@Array.new
D=A
@R15
M=D
@String.grow.call.0
D=A
@call
0;JMP
(String.grow.call.0)
// {line: 14780}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 14786}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14792}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 14793}
(String.grow.while.0)
// {line: 14802}
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
// {line: 14811}
// push this 1
@1
D=A
@THIS
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14818}
// lt
@String.grow.lt.0
D=A
@R14
M=D
@lt
0;JMP
(String.grow.lt.0)
// {line: 14821}
// not
@SP
A=M-1
M=!M
// {line: 14826}
// if-goto String.grow.while.1
@SP
AM=M-1
D=M
@String.grow.while.1
D;JNE
// {line: 14835}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14844}
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
// {line: 14849}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14854}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 14860}
// push pointer 0
@3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14869}
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
// {line: 14882}
// call String.charAt nArgs: 2
@2
D=A
@R14
M=D
@String.charAt
D=A
@R15
M=D
@String.grow.call.1
D=A
@call
0;JMP
(String.grow.call.1)
// {line: 14888}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 14897}
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
// {line: 14903}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14908}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14914}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 14916}
// goto String.grow.while.0
@String.grow.while.0
0;JMP
// {line: 14917}
(String.grow.while.1)
// {line: 14926}
// push this 0
@0
D=A
@THIS
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14939}
// call Array.dispose nArgs: 1
@1
D=A
@R14
M=D
@Array.dispose
D=A
@R15
M=D
@String.grow.call.2
D=A
@call
0;JMP
(String.grow.call.2)
// {line: 14944}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 14953}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14959}
// pop this 0
@SP
AM=M-1
D=M
@THIS
A=M
M=D
// {line: 14968}
// push this 1
@1
D=A
@THIS
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14974}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14979}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14986}
// pop this 1
@SP
AM=M-1
D=M
@THIS
A=M
A=A+1
M=D
// {line: 14988}
// return
@return
0;JMP
// {line: 14993}
// function String.eraseLastChar nLocals: 1
(String.eraseLastChar)
@SP
AM=M+1
A=A-1
M=0
// {line: 15002}
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
// {line: 15007}
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// {line: 15016}
// push this 2
@2
D=A
@THIS
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15022}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15029}
// gt
@String.eraseLastChar.gt.0
D=A
@R14
M=D
@gt
0;JMP
(String.eraseLastChar.gt.0)
// {line: 15034}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 15040}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15046}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15049}
// not
@SP
A=M-1
M=!M
// {line: 15054}
// if-goto String.eraseLastChar.if.0
@SP
AM=M-1
D=M
@String.eraseLastChar.if.0
D;JNE
// {line: 15063}
// push this 2
@2
D=A
@THIS
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15069}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15074}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 15082}
// pop this 2
@SP
AM=M-1
D=M
@THIS
A=M
A=A+1
A=A+1
M=D
// {line: 15091}
// push this 1
@1
D=A
@THIS
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15097}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15102}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 15109}
// pop this 1
@SP
AM=M-1
D=M
@THIS
A=M
A=A+1
M=D
// {line: 15110}
(String.eraseLastChar.if.0)
// {line: 15115}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 15117}
// return
@return
0;JMP
// {line: 15134}
// function String.intValue nLocals: 4
(String.intValue)
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
// {line: 15143}
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
// {line: 15148}
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// {line: 15154}
// push pointer 0
@3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15160}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15173}
// call String.charAt nArgs: 2
@2
D=A
@R14
M=D
@String.charAt
D=A
@R15
M=D
@String.intValue.call.0
D=A
@call
0;JMP
(String.intValue.call.0)
// {line: 15179}
// push constant 45
@45
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15186}
// eq
@String.intValue.eq.0
D=A
@R14
M=D
@eq
0;JMP
(String.intValue.eq.0)
// {line: 15191}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 15197}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15203}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15206}
// not
@SP
A=M-1
M=!M
// {line: 15211}
// if-goto String.intValue.if.0
@SP
AM=M-1
D=M
@String.intValue.if.0
D;JNE
// {line: 15217}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15223}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 15224}
(String.intValue.if.0)
// {line: 15229}
// if-goto String.intValue.goto.0
@SP
AM=M-1
D=M
@String.intValue.goto.0
D;JNE
// {line: 15235}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15241}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 15242}
(String.intValue.goto.0)
// {line: 15248}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15255}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 15256}
(String.intValue.while.0)
// {line: 15265}
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
// {line: 15274}
// push this 1
@1
D=A
@THIS
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15281}
// lt
@String.intValue.lt.0
D=A
@R14
M=D
@lt
0;JMP
(String.intValue.lt.0)
// {line: 15284}
// not
@SP
A=M-1
M=!M
// {line: 15289}
// if-goto String.intValue.while.1
@SP
AM=M-1
D=M
@String.intValue.while.1
D;JNE
// {line: 15298}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15304}
// push constant 10
@10
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15317}
// call Math.multiply nArgs: 2
@2
D=A
@R14
M=D
@Math.multiply
D=A
@R15
M=D
@String.intValue.call.1
D=A
@call
0;JMP
(String.intValue.call.1)
// {line: 15323}
// push pointer 1
@4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15332}
// push this 0
@0
D=A
@THIS
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15341}
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
// {line: 15346}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 15351}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 15360}
// push that 0
@0
D=A
@THAT
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15365}
// pop temp 2
@SP
AM=M-1
D=M
@R7
M=D
// {line: 15370}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 15376}
// push temp 2
@7
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15382}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15387}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 15392}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 15399}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 15408}
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
// {line: 15414}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15419}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 15425}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 15427}
// goto String.intValue.while.0
@String.intValue.while.0
0;JMP
// {line: 15428}
(String.intValue.while.1)
// {line: 15434}
// push pointer 0
@3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15440}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15453}
// call String.charAt nArgs: 2
@2
D=A
@R14
M=D
@String.charAt
D=A
@R15
M=D
@String.intValue.call.2
D=A
@call
0;JMP
(String.intValue.call.2)
// {line: 15459}
// push constant 45
@45
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15466}
// eq
@String.intValue.eq.1
D=A
@R14
M=D
@eq
0;JMP
(String.intValue.eq.1)
// {line: 15471}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 15477}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15483}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15486}
// not
@SP
A=M-1
M=!M
// {line: 15491}
// if-goto String.intValue.if.1
@SP
AM=M-1
D=M
@String.intValue.if.1
D;JNE
// {line: 15500}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15503}
// neg
@SP
A=M-1
M=-M
// {line: 15505}
// return
@return
0;JMP
// {line: 15506}
(String.intValue.if.1)
// {line: 15511}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 15520}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15522}
// return
@return
0;JMP
// {line: 15539}
// function String.setInt nLocals: 4
(String.setInt)
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
// {line: 15548}
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
// {line: 15553}
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// {line: 15562}
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
// {line: 15575}
// call Math.abs nArgs: 1
@1
D=A
@R14
M=D
@Math.abs
D=A
@R15
M=D
@String.setInt.call.0
D=A
@call
0;JMP
(String.setInt.call.0)
// {line: 15582}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 15591}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15597}
// push constant 10
@10
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15610}
// call Math.mod nArgs: 2
@2
D=A
@R14
M=D
@Math.mod
D=A
@R15
M=D
@String.setInt.call.1
D=A
@call
0;JMP
(String.setInt.call.1)
// {line: 15616}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 15625}
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
// {line: 15631}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15636}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 15644}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 15653}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15659}
// push constant 10
@10
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15666}
// lt
@String.setInt.lt.0
D=A
@R14
M=D
@lt
0;JMP
(String.setInt.lt.0)
// {line: 15671}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 15677}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15683}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15686}
// not
@SP
A=M-1
M=!M
// {line: 15691}
// if-goto String.setInt.if.0
@SP
AM=M-1
D=M
@String.setInt.if.0
D;JNE
// {line: 15697}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15704}
// pop this 1
@SP
AM=M-1
D=M
@THIS
A=M
A=A+1
M=D
// {line: 15710}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15718}
// pop this 2
@SP
AM=M-1
D=M
@THIS
A=M
A=A+1
A=A+1
M=D
// {line: 15727}
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
// {line: 15733}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15740}
// lt
@String.setInt.lt.1
D=A
@R14
M=D
@lt
0;JMP
(String.setInt.lt.1)
// {line: 15745}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 15751}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15757}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15760}
// not
@SP
A=M-1
M=!M
// {line: 15765}
// if-goto String.setInt.if.1
@SP
AM=M-1
D=M
@String.setInt.if.1
D;JNE
// {line: 15771}
// push pointer 0
@3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15777}
// push constant 45
@45
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15790}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@String.setInt.call.2
D=A
@call
0;JMP
(String.setInt.call.2)
// {line: 15795}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 15796}
(String.setInt.if.1)
// {line: 15801}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 15807}
// push pointer 0
@3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15816}
// push local 2
@2
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15829}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@String.setInt.call.3
D=A
@call
0;JMP
(String.setInt.call.3)
// {line: 15834}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 15835}
(String.setInt.if.0)
// {line: 15840}
// if-goto String.setInt.goto.0
@SP
AM=M-1
D=M
@String.setInt.goto.0
D;JNE
// {line: 15846}
// push pointer 0
@3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15855}
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
// {line: 15861}
// push constant 10
@10
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15874}
// call Math.divide nArgs: 2
@2
D=A
@R14
M=D
@Math.divide
D=A
@R15
M=D
@String.setInt.call.4
D=A
@call
0;JMP
(String.setInt.call.4)
// {line: 15887}
// call String.setInt nArgs: 2
@2
D=A
@R14
M=D
@String.setInt
D=A
@R15
M=D
@String.setInt.call.5
D=A
@call
0;JMP
(String.setInt.call.5)
// {line: 15892}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 15898}
// push pointer 0
@3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15907}
// push local 2
@2
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15920}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@String.setInt.call.6
D=A
@call
0;JMP
(String.setInt.call.6)
// {line: 15925}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 15926}
(String.setInt.goto.0)
// {line: 15928}
// return
@return
0;JMP
// {line: 15929}
// function String.newLine nLocals: 0
(String.newLine)
// {line: 15935}
// push constant 128
@128
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15937}
// return
@return
0;JMP
// {line: 15938}
// function String.backSpace nLocals: 0
(String.backSpace)
// {line: 15944}
// push constant 129
@129
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15946}
// return
@return
0;JMP
// {line: 15947}
// function String.doubleQuote nLocals: 0
(String.doubleQuote)
// {line: 15953}
// push constant 34
@34
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15955}
// return
@return
0;JMP
// {line: 15960}
// function Math.init nLocals: 1
(Math.init)
@SP
AM=M+1
A=A-1
M=0
// {line: 15966}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15971}
// pop static 5
@SP
AM=M-1
D=M
@Math.static.5
M=D
// {line: 15977}
// push static 5
@Math.static.5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15983}
// push constant 2
@2
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15996}
// call Math.divide nArgs: 2
@2
D=A
@R14
M=D
@Math.divide
D=A
@R15
M=D
@Math.init.call.0
D=A
@call
0;JMP
(Math.init.call.0)
// {line: 16002}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16007}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 16012}
// pop static 6
@SP
AM=M-1
D=M
@Math.static.6
M=D
// {line: 16018}
// push static 5
@Math.static.5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16031}
// call Array.new nArgs: 1
@1
D=A
@R14
M=D
@Array.new
D=A
@R15
M=D
@Math.init.call.1
D=A
@call
0;JMP
(Math.init.call.1)
// {line: 16036}
// pop static 4
@SP
AM=M-1
D=M
@Math.static.4
M=D
// {line: 16042}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16048}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 16054}
// push static 4
@Math.static.4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16060}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16065}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 16070}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 16076}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16082}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 16083}
(Math.init.while.0)
// {line: 16092}
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
// {line: 16098}
// push static 5
@Math.static.5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16104}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16109}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 16116}
// lt
@Math.init.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Math.init.lt.0)
// {line: 16119}
// not
@SP
A=M-1
M=!M
// {line: 16124}
// if-goto Math.init.while.1
@SP
AM=M-1
D=M
@Math.init.while.1
D;JNE
// {line: 16130}
// push static 4
@Math.static.4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16139}
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
// {line: 16144}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 16149}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 16155}
// push pointer 1
@4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16161}
// push static 4
@Math.static.4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16170}
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
// {line: 16176}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16181}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 16186}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 16191}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 16200}
// push that 0
@0
D=A
@THAT
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16205}
// pop temp 2
@SP
AM=M-1
D=M
@R7
M=D
// {line: 16210}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 16216}
// push temp 2
@7
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16222}
// push pointer 1
@4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16228}
// push static 4
@Math.static.4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16237}
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
// {line: 16243}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16248}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 16253}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 16258}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 16267}
// push that 0
@0
D=A
@THAT
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16272}
// pop temp 2
@SP
AM=M-1
D=M
@R7
M=D
// {line: 16277}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 16283}
// push temp 2
@7
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16288}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 16294}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 16303}
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
// {line: 16309}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16314}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 16320}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 16322}
// goto Math.init.while.0
@Math.init.while.0
0;JMP
// {line: 16323}
(Math.init.while.1)
// {line: 16325}
// return
@return
0;JMP
// {line: 16326}
// function Math.twoToThe nLocals: 0
(Math.twoToThe)
// {line: 16332}
// push pointer 1
@4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16338}
// push static 4
@Math.static.4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16347}
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
// {line: 16352}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 16357}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 16366}
// push that 0
@0
D=A
@THAT
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16371}
// pop temp 2
@SP
AM=M-1
D=M
@R7
M=D
// {line: 16376}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 16382}
// push temp 2
@7
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16384}
// return
@return
0;JMP
// {line: 16385}
// function Math.abs nLocals: 0
(Math.abs)
// {line: 16394}
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
// {line: 16400}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16407}
// lt
@Math.abs.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Math.abs.lt.0)
// {line: 16412}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 16418}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16424}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16427}
// not
@SP
A=M-1
M=!M
// {line: 16432}
// if-goto Math.abs.if.0
@SP
AM=M-1
D=M
@Math.abs.if.0
D;JNE
// {line: 16441}
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
// {line: 16444}
// neg
@SP
A=M-1
M=-M
// {line: 16446}
// return
@return
0;JMP
// {line: 16447}
(Math.abs.if.0)
// {line: 16452}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 16461}
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
// {line: 16463}
// return
@return
0;JMP
// {line: 16476}
// function Math.multiply nLocals: 3
(Math.multiply)
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
// {line: 16482}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16490}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 16496}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16502}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 16511}
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
// {line: 16518}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 16519}
(Math.multiply.while.0)
// {line: 16528}
// push local 2
@2
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16534}
// push static 5
@Math.static.5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16541}
// lt
@Math.multiply.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Math.multiply.lt.0)
// {line: 16544}
// not
@SP
A=M-1
M=!M
// {line: 16549}
// if-goto Math.multiply.while.1
@SP
AM=M-1
D=M
@Math.multiply.while.1
D;JNE
// {line: 16558}
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
// {line: 16567}
// push local 2
@2
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16580}
// call Math.bit nArgs: 2
@2
D=A
@R14
M=D
@Math.bit
D=A
@R15
M=D
@Math.multiply.call.0
D=A
@call
0;JMP
(Math.multiply.call.0)
// {line: 16585}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 16591}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16597}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16600}
// not
@SP
A=M-1
M=!M
// {line: 16605}
// if-goto Math.multiply.if.0
@SP
AM=M-1
D=M
@Math.multiply.if.0
D;JNE
// {line: 16614}
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
// {line: 16623}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16628}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 16634}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 16635}
(Math.multiply.if.0)
// {line: 16640}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 16649}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16658}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16663}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 16670}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 16679}
// push local 2
@2
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16685}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16690}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 16698}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 16700}
// goto Math.multiply.while.0
@Math.multiply.while.0
0;JMP
// {line: 16701}
(Math.multiply.while.1)
// {line: 16710}
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
// {line: 16712}
// return
@return
0;JMP
// {line: 16713}
// function Math.bit nLocals: 0
(Math.bit)
// {line: 16722}
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
// {line: 16728}
// push pointer 1
@4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16734}
// push static 4
@Math.static.4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16743}
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
// {line: 16748}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 16753}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 16762}
// push that 0
@0
D=A
@THAT
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16767}
// pop temp 2
@SP
AM=M-1
D=M
@R7
M=D
// {line: 16772}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 16778}
// push temp 2
@7
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16783}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 16789}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16796}
// eq
@Math.bit.eq.0
D=A
@R14
M=D
@eq
0;JMP
(Math.bit.eq.0)
// {line: 16799}
// not
@SP
A=M-1
M=!M
// {line: 16804}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 16810}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16816}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16819}
// not
@SP
A=M-1
M=!M
// {line: 16824}
// if-goto Math.bit.if.0
@SP
AM=M-1
D=M
@Math.bit.if.0
D;JNE
// {line: 16830}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16833}
// not
@SP
A=M-1
M=!M
// {line: 16835}
// return
@return
0;JMP
// {line: 16836}
(Math.bit.if.0)
// {line: 16841}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 16847}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16849}
// return
@return
0;JMP
// {line: 16854}
// function Math.divide nLocals: 1
(Math.divide)
@SP
AM=M+1
A=A-1
M=0
// {line: 16863}
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
// {line: 16869}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16876}
// eq
@Math.divide.eq.0
D=A
@R14
M=D
@eq
0;JMP
(Math.divide.eq.0)
// {line: 16881}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 16887}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16893}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16896}
// not
@SP
A=M-1
M=!M
// {line: 16901}
// if-goto Math.divide.if.0
@SP
AM=M-1
D=M
@Math.divide.if.0
D;JNE
// {line: 16907}
// push constant 5
@5
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16920}
// call Sys.error nArgs: 1
@1
D=A
@R14
M=D
@Sys.error
D=A
@R15
M=D
@Math.divide.call.0
D=A
@call
0;JMP
(Math.divide.call.0)
// {line: 16925}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 16926}
(Math.divide.if.0)
// {line: 16931}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 16940}
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
// {line: 16949}
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
// {line: 16962}
// call Math.xor nArgs: 2
@2
D=A
@R14
M=D
@Math.xor
D=A
@R15
M=D
@Math.divide.call.1
D=A
@call
0;JMP
(Math.divide.call.1)
// {line: 16968}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16975}
// lt
@Math.divide.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Math.divide.lt.0)
// {line: 16981}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 16990}
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
// {line: 17003}
// call Math.abs nArgs: 1
@1
D=A
@R14
M=D
@Math.abs
D=A
@R15
M=D
@Math.divide.call.2
D=A
@call
0;JMP
(Math.divide.call.2)
// {line: 17009}
// pop argument 0
@SP
AM=M-1
D=M
@ARG
A=M
M=D
// {line: 17018}
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
// {line: 17031}
// call Math.abs nArgs: 1
@1
D=A
@R14
M=D
@Math.abs
D=A
@R15
M=D
@Math.divide.call.3
D=A
@call
0;JMP
(Math.divide.call.3)
// {line: 17038}
// pop argument 1
@SP
AM=M-1
D=M
@ARG
A=M
A=A+1
M=D
// {line: 17047}
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
// {line: 17052}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 17058}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17064}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17067}
// not
@SP
A=M-1
M=!M
// {line: 17072}
// if-goto Math.divide.if.1
@SP
AM=M-1
D=M
@Math.divide.if.1
D;JNE
// {line: 17081}
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
// {line: 17090}
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
// {line: 17103}
// call Math._subdivide nArgs: 2
@2
D=A
@R14
M=D
@Math._subdivide
D=A
@R15
M=D
@Math.divide.call.4
D=A
@call
0;JMP
(Math.divide.call.4)
// {line: 17106}
// neg
@SP
A=M-1
M=-M
// {line: 17108}
// return
@return
0;JMP
// {line: 17109}
(Math.divide.if.1)
// {line: 17114}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 17123}
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
// {line: 17132}
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
// {line: 17145}
// call Math._subdivide nArgs: 2
@2
D=A
@R14
M=D
@Math._subdivide
D=A
@R15
M=D
@Math.divide.call.5
D=A
@call
0;JMP
(Math.divide.call.5)
// {line: 17147}
// return
@return
0;JMP
// {line: 17148}
// function Math.div nLocals: 0
(Math.div)
// {line: 17157}
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
// {line: 17166}
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
// {line: 17179}
// call Math.divide nArgs: 2
@2
D=A
@R14
M=D
@Math.divide
D=A
@R15
M=D
@Math.div.call.0
D=A
@call
0;JMP
(Math.div.call.0)
// {line: 17181}
// return
@return
0;JMP
// {line: 17186}
// function Math._subdivide nLocals: 1
(Math._subdivide)
@SP
AM=M+1
A=A-1
M=0
// {line: 17195}
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
// {line: 17204}
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
// {line: 17211}
// gt
@Math._subdivide.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Math._subdivide.gt.0)
// {line: 17220}
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
// {line: 17226}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17233}
// lt
@Math._subdivide.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Math._subdivide.lt.0)
// {line: 17238}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 17243}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 17249}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17255}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17258}
// not
@SP
A=M-1
M=!M
// {line: 17263}
// if-goto Math._subdivide.if.0
@SP
AM=M-1
D=M
@Math._subdivide.if.0
D;JNE
// {line: 17269}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17274}
// pop static 7
@SP
AM=M-1
D=M
@Math.static.7
M=D
// {line: 17280}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17282}
// return
@return
0;JMP
// {line: 17283}
(Math._subdivide.if.0)
// {line: 17288}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 17297}
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
// {line: 17306}
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
// {line: 17315}
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
// {line: 17320}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 17333}
// call Math._subdivide nArgs: 2
@2
D=A
@R14
M=D
@Math._subdivide
D=A
@R15
M=D
@Math._subdivide.call.0
D=A
@call
0;JMP
(Math._subdivide.call.0)
// {line: 17339}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 17348}
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
// {line: 17354}
// push static 7
@Math.static.7
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17359}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 17368}
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
// {line: 17375}
// lt
@Math._subdivide.lt.1
D=A
@R14
M=D
@lt
0;JMP
(Math._subdivide.lt.1)
// {line: 17380}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 17386}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17392}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17395}
// not
@SP
A=M-1
M=!M
// {line: 17400}
// if-goto Math._subdivide.if.1
@SP
AM=M-1
D=M
@Math._subdivide.if.1
D;JNE
// {line: 17409}
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
// {line: 17418}
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
// {line: 17423}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 17425}
// return
@return
0;JMP
// {line: 17426}
(Math._subdivide.if.1)
// {line: 17431}
// if-goto Math._subdivide.goto.0
@SP
AM=M-1
D=M
@Math._subdivide.goto.0
D;JNE
// {line: 17437}
// push static 7
@Math.static.7
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17446}
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
// {line: 17451}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 17456}
// pop static 7
@SP
AM=M-1
D=M
@Math.static.7
M=D
// {line: 17465}
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
// {line: 17474}
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
// {line: 17479}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 17485}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17490}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 17492}
// return
@return
0;JMP
// {line: 17493}
(Math._subdivide.goto.0)
// {line: 17495}
// return
@return
0;JMP
// {line: 17496}
// function Math.xor nLocals: 0
(Math.xor)
// {line: 17505}
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
// {line: 17514}
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
// {line: 17517}
// not
@SP
A=M-1
M=!M
// {line: 17522}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 17531}
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
// {line: 17534}
// not
@SP
A=M-1
M=!M
// {line: 17543}
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
// {line: 17548}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 17553}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 17555}
// return
@return
0;JMP
// {line: 17572}
// function Math.sqrt nLocals: 4
(Math.sqrt)
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
// {line: 17578}
// push static 6
@Math.static.6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17584}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 17590}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17597}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 17598}
(Math.sqrt.while.0)
// {line: 17607}
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
// {line: 17613}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17620}
// gt
@Math.sqrt.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Math.sqrt.gt.0)
// {line: 17629}
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
// {line: 17635}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17642}
// eq
@Math.sqrt.eq.0
D=A
@R14
M=D
@eq
0;JMP
(Math.sqrt.eq.0)
// {line: 17647}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 17650}
// not
@SP
A=M-1
M=!M
// {line: 17655}
// if-goto Math.sqrt.while.1
@SP
AM=M-1
D=M
@Math.sqrt.while.1
D;JNE
// {line: 17664}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17670}
// push pointer 1
@4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17676}
// push static 4
@Math.static.4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17685}
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
// {line: 17690}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 17695}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 17704}
// push that 0
@0
D=A
@THAT
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17709}
// pop temp 2
@SP
AM=M-1
D=M
@R7
M=D
// {line: 17714}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 17720}
// push temp 2
@7
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17725}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 17733}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 17742}
// push local 2
@2
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17751}
// push local 2
@2
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17764}
// call Math.multiply nArgs: 2
@2
D=A
@R14
M=D
@Math.multiply
D=A
@R15
M=D
@Math.sqrt.call.0
D=A
@call
0;JMP
(Math.sqrt.call.0)
// {line: 17773}
// pop local 3
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
A=A+1
M=D
// {line: 17782}
// push local 3
@3
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17791}
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
// {line: 17798}
// lt
@Math.sqrt.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Math.sqrt.lt.0)
// {line: 17807}
// push local 3
@3
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17816}
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
// {line: 17823}
// eq
@Math.sqrt.eq.1
D=A
@R14
M=D
@eq
0;JMP
(Math.sqrt.eq.1)
// {line: 17828}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 17837}
// push local 3
@3
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17843}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17850}
// gt
@Math.sqrt.gt.1
D=A
@R14
M=D
@gt
0;JMP
(Math.sqrt.gt.1)
// {line: 17855}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 17860}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 17866}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17872}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17875}
// not
@SP
A=M-1
M=!M
// {line: 17880}
// if-goto Math.sqrt.if.0
@SP
AM=M-1
D=M
@Math.sqrt.if.0
D;JNE
// {line: 17889}
// push local 2
@2
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17896}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 17897}
(Math.sqrt.if.0)
// {line: 17902}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 17911}
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
// {line: 17917}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17922}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 17928}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 17930}
// goto Math.sqrt.while.0
@Math.sqrt.while.0
0;JMP
// {line: 17931}
(Math.sqrt.while.1)
// {line: 17940}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17942}
// return
@return
0;JMP
// {line: 17943}
// function Math.max nLocals: 0
(Math.max)
// {line: 17952}
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
// {line: 17961}
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
// {line: 17968}
// gt
@Math.max.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Math.max.gt.0)
// {line: 17973}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 17979}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17985}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17988}
// not
@SP
A=M-1
M=!M
// {line: 17993}
// if-goto Math.max.if.0
@SP
AM=M-1
D=M
@Math.max.if.0
D;JNE
// {line: 18002}
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
// {line: 18004}
// return
@return
0;JMP
// {line: 18005}
(Math.max.if.0)
// {line: 18010}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 18019}
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
// {line: 18021}
// return
@return
0;JMP
// {line: 18022}
// function Math.min nLocals: 0
(Math.min)
// {line: 18031}
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
// {line: 18040}
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
// {line: 18047}
// lt
@Math.min.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Math.min.lt.0)
// {line: 18052}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 18058}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18064}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18067}
// not
@SP
A=M-1
M=!M
// {line: 18072}
// if-goto Math.min.if.0
@SP
AM=M-1
D=M
@Math.min.if.0
D;JNE
// {line: 18081}
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
// {line: 18083}
// return
@return
0;JMP
// {line: 18084}
(Math.min.if.0)
// {line: 18089}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 18098}
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
// {line: 18100}
// return
@return
0;JMP
// {line: 18101}
// function Math.mod nLocals: 0
(Math.mod)
// {line: 18110}
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
// {line: 18119}
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
// {line: 18128}
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
// {line: 18141}
// call Math.divide nArgs: 2
@2
D=A
@R14
M=D
@Math.divide
D=A
@R15
M=D
@Math.mod.call.0
D=A
@call
0;JMP
(Math.mod.call.0)
// {line: 18150}
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
// {line: 18163}
// call Math.multiply nArgs: 2
@2
D=A
@R14
M=D
@Math.multiply
D=A
@R15
M=D
@Math.mod.call.1
D=A
@call
0;JMP
(Math.mod.call.1)
// {line: 18168}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 18170}
// return
@return
0;JMP
// {line: 18171}
// function Screen.init nLocals: 0
(Screen.init)
// {line: 18177}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18180}
// not
@SP
A=M-1
M=!M
// {line: 18185}
// pop static 13
@SP
AM=M-1
D=M
@Screen.static.13
M=D
// {line: 18191}
// push constant 512
@512
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18196}
// pop static 14
@SP
AM=M-1
D=M
@Screen.static.14
M=D
// {line: 18202}
// push constant 256
@256
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18207}
// pop static 15
@SP
AM=M-1
D=M
@Screen.static.15
M=D
// {line: 18213}
// push constant 16384
@16384
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18218}
// pop static 16
@SP
AM=M-1
D=M
@Screen.static.16
M=D
// {line: 18220}
// return
@return
0;JMP
// {line: 18221}
// function Screen.clearScreen nLocals: 0
(Screen.clearScreen)
// {line: 18223}
// return
@return
0;JMP
// {line: 18224}
// function Screen.setColor nLocals: 0
(Screen.setColor)
// {line: 18233}
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
// {line: 18238}
// pop static 13
@SP
AM=M-1
D=M
@Screen.static.13
M=D
// {line: 18240}
// return
@return
0;JMP
// {line: 18241}
// function Screen.getColor nLocals: 0
(Screen.getColor)
// {line: 18247}
// push static 13
@Screen.static.13
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18249}
// return
@return
0;JMP
// {line: 18258}
// function Screen.drawPixel nLocals: 2
(Screen.drawPixel)
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
// {line: 18267}
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
// {line: 18273}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18286}
// call Math.divide nArgs: 2
@2
D=A
@R14
M=D
@Math.divide
D=A
@R15
M=D
@Screen.drawPixel.call.0
D=A
@call
0;JMP
(Screen.drawPixel.call.0)
// {line: 18295}
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
// {line: 18301}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18314}
// call Math.multiply nArgs: 2
@2
D=A
@R14
M=D
@Math.multiply
D=A
@R15
M=D
@Screen.drawPixel.call.1
D=A
@call
0;JMP
(Screen.drawPixel.call.1)
// {line: 18319}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 18325}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 18334}
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
// {line: 18340}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18353}
// call Math.mod nArgs: 2
@2
D=A
@R14
M=D
@Math.mod
D=A
@R15
M=D
@Screen.drawPixel.call.2
D=A
@call
0;JMP
(Screen.drawPixel.call.2)
// {line: 18366}
// call Math.twoToThe nArgs: 1
@1
D=A
@R14
M=D
@Math.twoToThe
D=A
@R15
M=D
@Screen.drawPixel.call.3
D=A
@call
0;JMP
(Screen.drawPixel.call.3)
// {line: 18373}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 18379}
// push static 13
@Screen.static.13
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18384}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 18390}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18396}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18399}
// not
@SP
A=M-1
M=!M
// {line: 18404}
// if-goto Screen.drawPixel.if.0
@SP
AM=M-1
D=M
@Screen.drawPixel.if.0
D;JNE
// {line: 18410}
// push static 16
@Screen.static.16
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18419}
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
// {line: 18424}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 18429}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 18435}
// push pointer 1
@4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18441}
// push static 16
@Screen.static.16
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18450}
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
// {line: 18455}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 18460}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 18469}
// push that 0
@0
D=A
@THAT
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18474}
// pop temp 2
@SP
AM=M-1
D=M
@R7
M=D
// {line: 18479}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 18485}
// push temp 2
@7
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18494}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18499}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 18505}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 18506}
(Screen.drawPixel.if.0)
// {line: 18511}
// if-goto Screen.drawPixel.goto.0
@SP
AM=M-1
D=M
@Screen.drawPixel.goto.0
D;JNE
// {line: 18517}
// push static 16
@Screen.static.16
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18526}
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
// {line: 18531}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 18536}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 18542}
// push pointer 1
@4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18548}
// push static 16
@Screen.static.16
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18557}
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
// {line: 18562}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 18567}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 18576}
// push that 0
@0
D=A
@THAT
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18581}
// pop temp 2
@SP
AM=M-1
D=M
@R7
M=D
// {line: 18586}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 18592}
// push temp 2
@7
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18601}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18604}
// not
@SP
A=M-1
M=!M
// {line: 18609}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 18615}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 18616}
(Screen.drawPixel.goto.0)
// {line: 18618}
// return
@return
0;JMP
// {line: 18623}
// function Screen._drawChunk nLocals: 1
(Screen._drawChunk)
@SP
AM=M+1
A=A-1
M=0
// {line: 18632}
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
// {line: 18638}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18651}
// call Math.divide nArgs: 2
@2
D=A
@R14
M=D
@Math.divide
D=A
@R15
M=D
@Screen._drawChunk.call.0
D=A
@call
0;JMP
(Screen._drawChunk.call.0)
// {line: 18660}
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
// {line: 18666}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18679}
// call Math.multiply nArgs: 2
@2
D=A
@R14
M=D
@Math.multiply
D=A
@R15
M=D
@Screen._drawChunk.call.1
D=A
@call
0;JMP
(Screen._drawChunk.call.1)
// {line: 18684}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 18690}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 18696}
// push static 16
@Screen.static.16
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18705}
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
// {line: 18710}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 18715}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 18721}
// push static 13
@Screen.static.13
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18727}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 18729}
// return
@return
0;JMP
// {line: 18742}
// function Screen.drawHoriz nLocals: 3
(Screen.drawHoriz)
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
// {line: 18751}
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
// {line: 18760}
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
// {line: 18765}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 18771}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 18780}
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
// {line: 18786}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18793}
// gt
@Screen.drawHoriz.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Screen.drawHoriz.gt.0)
// {line: 18798}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 18804}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18810}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18813}
// not
@SP
A=M-1
M=!M
// {line: 18818}
// if-goto Screen.drawHoriz.if.0
@SP
AM=M-1
D=M
@Screen.drawHoriz.if.0
D;JNE
// {line: 18827}
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
// {line: 18833}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18840}
// gt
@Screen.drawHoriz.gt.1
D=A
@R14
M=D
@gt
0;JMP
(Screen.drawHoriz.gt.1)
// {line: 18845}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 18851}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18857}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18860}
// not
@SP
A=M-1
M=!M
// {line: 18865}
// if-goto Screen.drawHoriz.if.1
@SP
AM=M-1
D=M
@Screen.drawHoriz.if.1
D;JNE
// {line: 18874}
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
// {line: 18880}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18893}
// call Math.mod nArgs: 2
@2
D=A
@R14
M=D
@Math.mod
D=A
@R15
M=D
@Screen.drawHoriz.call.0
D=A
@call
0;JMP
(Screen.drawHoriz.call.0)
// {line: 18900}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 18906}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18915}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18920}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 18927}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 18928}
(Screen.drawHoriz.while.0)
// {line: 18937}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18943}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18950}
// gt
@Screen.drawHoriz.gt.2
D=A
@R14
M=D
@gt
0;JMP
(Screen.drawHoriz.gt.2)
// {line: 18953}
// not
@SP
A=M-1
M=!M
// {line: 18958}
// if-goto Screen.drawHoriz.while.1
@SP
AM=M-1
D=M
@Screen.drawHoriz.while.1
D;JNE
// {line: 18967}
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
// {line: 18976}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18981}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 18990}
// push argument 2
@2
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 19003}
// call Screen.drawPixel nArgs: 2
@2
D=A
@R14
M=D
@Screen.drawPixel
D=A
@R15
M=D
@Screen.drawHoriz.call.1
D=A
@call
0;JMP
(Screen.drawHoriz.call.1)
// {line: 19008}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 19017}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 19023}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19028}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 19035}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 19037}
// goto Screen.drawHoriz.while.0
@Screen.drawHoriz.while.0
0;JMP
// {line: 19038}
(Screen.drawHoriz.while.1)
// {line: 19047}
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
// {line: 19053}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19062}
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
// {line: 19068}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19081}
// call Math.mod nArgs: 2
@2
D=A
@R14
M=D
@Math.mod
D=A
@R15
M=D
@Screen.drawHoriz.call.2
D=A
@call
0;JMP
(Screen.drawHoriz.call.2)
// {line: 19086}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 19091}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 19097}
// pop argument 0
@SP
AM=M-1
D=M
@ARG
A=M
M=D
// {line: 19106}
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
// {line: 19112}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19125}
// call Math.mod nArgs: 2
@2
D=A
@R14
M=D
@Math.mod
D=A
@R15
M=D
@Screen.drawHoriz.call.3
D=A
@call
0;JMP
(Screen.drawHoriz.call.3)
// {line: 19132}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 19133}
(Screen.drawHoriz.while.2)
// {line: 19142}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 19148}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19155}
// gt
@Screen.drawHoriz.gt.3
D=A
@R14
M=D
@gt
0;JMP
(Screen.drawHoriz.gt.3)
// {line: 19158}
// not
@SP
A=M-1
M=!M
// {line: 19163}
// if-goto Screen.drawHoriz.while.3
@SP
AM=M-1
D=M
@Screen.drawHoriz.while.3
D;JNE
// {line: 19172}
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
// {line: 19181}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 19186}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 19195}
// push argument 2
@2
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 19208}
// call Screen.drawPixel nArgs: 2
@2
D=A
@R14
M=D
@Screen.drawPixel
D=A
@R15
M=D
@Screen.drawHoriz.call.4
D=A
@call
0;JMP
(Screen.drawHoriz.call.4)
// {line: 19213}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 19222}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 19228}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19233}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 19240}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 19242}
// goto Screen.drawHoriz.while.2
@Screen.drawHoriz.while.2
0;JMP
// {line: 19243}
(Screen.drawHoriz.while.3)
// {line: 19252}
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
// {line: 19261}
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
// {line: 19267}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19280}
// call Math.mod nArgs: 2
@2
D=A
@R14
M=D
@Math.mod
D=A
@R15
M=D
@Screen.drawHoriz.call.5
D=A
@call
0;JMP
(Screen.drawHoriz.call.5)
// {line: 19285}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 19292}
// pop argument 1
@SP
AM=M-1
D=M
@ARG
A=M
A=A+1
M=D
// {line: 19301}
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
// {line: 19310}
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
// {line: 19315}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 19321}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 19322}
(Screen.drawHoriz.while.4)
// {line: 19331}
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
// {line: 19337}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19344}
// gt
@Screen.drawHoriz.gt.4
D=A
@R14
M=D
@gt
0;JMP
(Screen.drawHoriz.gt.4)
// {line: 19347}
// not
@SP
A=M-1
M=!M
// {line: 19352}
// if-goto Screen.drawHoriz.while.5
@SP
AM=M-1
D=M
@Screen.drawHoriz.while.5
D;JNE
// {line: 19361}
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
// {line: 19370}
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
// {line: 19375}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 19384}
// push argument 2
@2
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 19397}
// call Screen._drawChunk nArgs: 2
@2
D=A
@R14
M=D
@Screen._drawChunk
D=A
@R15
M=D
@Screen.drawHoriz.call.6
D=A
@call
0;JMP
(Screen.drawHoriz.call.6)
// {line: 19402}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 19411}
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
// {line: 19417}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19422}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 19428}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 19430}
// goto Screen.drawHoriz.while.4
@Screen.drawHoriz.while.4
0;JMP
// {line: 19431}
(Screen.drawHoriz.while.5)
// {line: 19432}
(Screen.drawHoriz.if.1)
// {line: 19437}
// if-goto Screen.drawHoriz.goto.0
@SP
AM=M-1
D=M
@Screen.drawHoriz.goto.0
D;JNE
// {line: 19438}
(Screen.drawHoriz.while.6)
// {line: 19447}
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
// {line: 19453}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19460}
// gt
@Screen.drawHoriz.gt.5
D=A
@R14
M=D
@gt
0;JMP
(Screen.drawHoriz.gt.5)
// {line: 19463}
// not
@SP
A=M-1
M=!M
// {line: 19468}
// if-goto Screen.drawHoriz.while.7
@SP
AM=M-1
D=M
@Screen.drawHoriz.while.7
D;JNE
// {line: 19477}
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
// {line: 19486}
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
// {line: 19491}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 19500}
// push argument 2
@2
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 19513}
// call Screen.drawPixel nArgs: 2
@2
D=A
@R14
M=D
@Screen.drawPixel
D=A
@R15
M=D
@Screen.drawHoriz.call.7
D=A
@call
0;JMP
(Screen.drawHoriz.call.7)
// {line: 19518}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 19527}
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
// {line: 19533}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19538}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 19544}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 19546}
// goto Screen.drawHoriz.while.6
@Screen.drawHoriz.while.6
0;JMP
// {line: 19547}
(Screen.drawHoriz.while.7)
// {line: 19548}
(Screen.drawHoriz.goto.0)
// {line: 19549}
(Screen.drawHoriz.if.0)
// {line: 19554}
// if-goto Screen.drawHoriz.goto.1
@SP
AM=M-1
D=M
@Screen.drawHoriz.goto.1
D;JNE
// {line: 19563}
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
// {line: 19572}
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
// {line: 19581}
// push argument 2
@2
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 19594}
// call Screen.drawHoriz nArgs: 3
@3
D=A
@R14
M=D
@Screen.drawHoriz
D=A
@R15
M=D
@Screen.drawHoriz.call.8
D=A
@call
0;JMP
(Screen.drawHoriz.call.8)
// {line: 19599}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 19600}
(Screen.drawHoriz.goto.1)
// {line: 19602}
// return
@return
0;JMP
// {line: 19615}
// function Screen.drawVert nLocals: 3
(Screen.drawVert)
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
// {line: 19624}
// push argument 2
@2
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 19633}
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
// {line: 19638}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 19644}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19651}
// lt
@Screen.drawVert.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawVert.lt.0)
// {line: 19656}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 19662}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 19668}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 19671}
// not
@SP
A=M-1
M=!M
// {line: 19676}
// if-goto Screen.drawVert.if.0
@SP
AM=M-1
D=M
@Screen.drawVert.if.0
D;JNE
// {line: 19685}
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
// {line: 19694}
// push argument 2
@2
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 19703}
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
// {line: 19716}
// call Screen.drawVert nArgs: 3
@3
D=A
@R14
M=D
@Screen.drawVert
D=A
@R15
M=D
@Screen.drawVert.call.0
D=A
@call
0;JMP
(Screen.drawVert.call.0)
// {line: 19721}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 19722}
(Screen.drawVert.if.0)
// {line: 19727}
// if-goto Screen.drawVert.goto.0
@SP
AM=M-1
D=M
@Screen.drawVert.goto.0
D;JNE
// {line: 19736}
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
// {line: 19742}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19755}
// call Math.divide nArgs: 2
@2
D=A
@R14
M=D
@Math.divide
D=A
@R15
M=D
@Screen.drawVert.call.1
D=A
@call
0;JMP
(Screen.drawVert.call.1)
// {line: 19764}
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
// {line: 19770}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19783}
// call Math.multiply nArgs: 2
@2
D=A
@R14
M=D
@Math.multiply
D=A
@R15
M=D
@Screen.drawVert.call.2
D=A
@call
0;JMP
(Screen.drawVert.call.2)
// {line: 19788}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 19794}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 19803}
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
// {line: 19809}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19822}
// call Math.mod nArgs: 2
@2
D=A
@R14
M=D
@Math.mod
D=A
@R15
M=D
@Screen.drawVert.call.3
D=A
@call
0;JMP
(Screen.drawVert.call.3)
// {line: 19835}
// call Math.twoToThe nArgs: 1
@1
D=A
@R14
M=D
@Math.twoToThe
D=A
@R15
M=D
@Screen.drawVert.call.4
D=A
@call
0;JMP
(Screen.drawVert.call.4)
// {line: 19842}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 19843}
(Screen.drawVert.while.0)
// {line: 19852}
// push argument 2
@2
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 19861}
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
// {line: 19868}
// gt
@Screen.drawVert.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Screen.drawVert.gt.0)
// {line: 19871}
// not
@SP
A=M-1
M=!M
// {line: 19876}
// if-goto Screen.drawVert.while.1
@SP
AM=M-1
D=M
@Screen.drawVert.while.1
D;JNE
// {line: 19882}
// push static 13
@Screen.static.13
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 19887}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 19893}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 19899}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 19902}
// not
@SP
A=M-1
M=!M
// {line: 19907}
// if-goto Screen.drawVert.if.1
@SP
AM=M-1
D=M
@Screen.drawVert.if.1
D;JNE
// {line: 19913}
// push static 16
@Screen.static.16
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 19922}
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
// {line: 19927}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 19932}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 19938}
// push pointer 1
@4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 19944}
// push static 16
@Screen.static.16
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 19953}
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
// {line: 19958}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 19963}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 19972}
// push that 0
@0
D=A
@THAT
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 19977}
// pop temp 2
@SP
AM=M-1
D=M
@R7
M=D
// {line: 19982}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 19988}
// push temp 2
@7
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 19997}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20002}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 20008}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 20009}
(Screen.drawVert.if.1)
// {line: 20014}
// if-goto Screen.drawVert.goto.1
@SP
AM=M-1
D=M
@Screen.drawVert.goto.1
D;JNE
// {line: 20020}
// push static 16
@Screen.static.16
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20029}
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
// {line: 20034}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 20039}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 20045}
// push pointer 1
@4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20051}
// push static 16
@Screen.static.16
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20060}
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
// {line: 20065}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 20070}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 20079}
// push that 0
@0
D=A
@THAT
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20084}
// pop temp 2
@SP
AM=M-1
D=M
@R7
M=D
// {line: 20089}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 20095}
// push temp 2
@7
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20104}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20107}
// not
@SP
A=M-1
M=!M
// {line: 20112}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 20118}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 20119}
(Screen.drawVert.goto.1)
// {line: 20128}
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
// {line: 20137}
// push argument 2
@2
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20150}
// call Screen.drawPixel nArgs: 2
@2
D=A
@R14
M=D
@Screen.drawPixel
D=A
@R15
M=D
@Screen.drawVert.call.5
D=A
@call
0;JMP
(Screen.drawVert.call.5)
// {line: 20155}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 20164}
// push argument 2
@2
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20170}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20175}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 20183}
// pop argument 2
@SP
AM=M-1
D=M
@ARG
A=M
A=A+1
A=A+1
M=D
// {line: 20192}
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
// {line: 20198}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20203}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 20209}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 20211}
// goto Screen.drawVert.while.0
@Screen.drawVert.while.0
0;JMP
// {line: 20212}
(Screen.drawVert.while.1)
// {line: 20213}
(Screen.drawVert.goto.0)
// {line: 20215}
// return
@return
0;JMP
// {line: 20236}
// function Screen.drawLine nLocals: 5
(Screen.drawLine)
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
// {line: 20242}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20252}
// pop local 4
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
A=A+1
A=A+1
M=D
// {line: 20261}
// push argument 2
@2
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20270}
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
// {line: 20275}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 20281}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 20290}
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
// {line: 20296}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20303}
// eq
@Screen.drawLine.eq.0
D=A
@R14
M=D
@eq
0;JMP
(Screen.drawLine.eq.0)
// {line: 20308}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 20314}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20320}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20323}
// not
@SP
A=M-1
M=!M
// {line: 20328}
// if-goto Screen.drawLine.if.0
@SP
AM=M-1
D=M
@Screen.drawLine.if.0
D;JNE
// {line: 20337}
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
// {line: 20346}
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
// {line: 20355}
// push argument 3
@3
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20368}
// call Screen.drawVert nArgs: 3
@3
D=A
@R14
M=D
@Screen.drawVert
D=A
@R15
M=D
@Screen.drawLine.call.0
D=A
@call
0;JMP
(Screen.drawLine.call.0)
// {line: 20373}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 20379}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20381}
// return
@return
0;JMP
// {line: 20382}
(Screen.drawLine.if.0)
// {line: 20387}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 20396}
// push argument 3
@3
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20405}
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
// {line: 20410}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 20417}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 20426}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20432}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20439}
// eq
@Screen.drawLine.eq.1
D=A
@R14
M=D
@eq
0;JMP
(Screen.drawLine.eq.1)
// {line: 20444}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 20450}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20456}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20459}
// not
@SP
A=M-1
M=!M
// {line: 20464}
// if-goto Screen.drawLine.if.1
@SP
AM=M-1
D=M
@Screen.drawLine.if.1
D;JNE
// {line: 20473}
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
// {line: 20482}
// push argument 2
@2
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20491}
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
// {line: 20504}
// call Screen.drawHoriz nArgs: 3
@3
D=A
@R14
M=D
@Screen.drawHoriz
D=A
@R15
M=D
@Screen.drawLine.call.1
D=A
@call
0;JMP
(Screen.drawLine.call.1)
// {line: 20509}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 20515}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20517}
// return
@return
0;JMP
// {line: 20518}
(Screen.drawLine.if.1)
// {line: 20523}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 20529}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20537}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 20543}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20552}
// pop local 3
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
A=A+1
M=D
// {line: 20558}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20568}
// pop local 4
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
A=A+1
A=A+1
M=D
// {line: 20577}
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
// {line: 20583}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20590}
// lt
@Screen.drawLine.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawLine.lt.0)
// {line: 20595}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 20601}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20607}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20610}
// not
@SP
A=M-1
M=!M
// {line: 20615}
// if-goto Screen.drawLine.if.2
@SP
AM=M-1
D=M
@Screen.drawLine.if.2
D;JNE
// {line: 20624}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20630}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20637}
// lt
@Screen.drawLine.lt.1
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawLine.lt.1)
// {line: 20642}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 20648}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20654}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20657}
// not
@SP
A=M-1
M=!M
// {line: 20662}
// if-goto Screen.drawLine.if.3
@SP
AM=M-1
D=M
@Screen.drawLine.if.3
D;JNE
// {line: 20671}
// push argument 2
@2
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20680}
// push argument 3
@3
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20689}
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
// {line: 20698}
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
// {line: 20711}
// call Screen.drawLine nArgs: 4
@4
D=A
@R14
M=D
@Screen.drawLine
D=A
@R15
M=D
@Screen.drawLine.call.2
D=A
@call
0;JMP
(Screen.drawLine.call.2)
// {line: 20716}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 20722}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20724}
// return
@return
0;JMP
// {line: 20725}
(Screen.drawLine.if.3)
// {line: 20730}
// if-goto Screen.drawLine.goto.0
@SP
AM=M-1
D=M
@Screen.drawLine.goto.0
D;JNE
// {line: 20739}
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
// {line: 20742}
// neg
@SP
A=M-1
M=-M
// {line: 20748}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 20749}
(Screen.drawLine.while.0)
// {line: 20758}
// push local 2
@2
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20767}
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
// {line: 20774}
// lt
@Screen.drawLine.lt.2
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawLine.lt.2)
// {line: 20783}
// push local 2
@2
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20792}
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
// {line: 20799}
// eq
@Screen.drawLine.eq.2
D=A
@R14
M=D
@eq
0;JMP
(Screen.drawLine.eq.2)
// {line: 20804}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 20813}
// push local 3
@3
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20822}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20829}
// lt
@Screen.drawLine.lt.3
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawLine.lt.3)
// {line: 20838}
// push local 3
@3
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20847}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20854}
// eq
@Screen.drawLine.eq.3
D=A
@R14
M=D
@eq
0;JMP
(Screen.drawLine.eq.3)
// {line: 20859}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 20864}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 20867}
// not
@SP
A=M-1
M=!M
// {line: 20872}
// if-goto Screen.drawLine.while.1
@SP
AM=M-1
D=M
@Screen.drawLine.while.1
D;JNE
// {line: 20881}
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
// {line: 20890}
// push local 2
@2
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20895}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 20904}
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
// {line: 20913}
// push local 3
@3
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20918}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 20931}
// call Screen.drawPixel nArgs: 2
@2
D=A
@R14
M=D
@Screen.drawPixel
D=A
@R15
M=D
@Screen.drawLine.call.3
D=A
@call
0;JMP
(Screen.drawLine.call.3)
// {line: 20936}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 20945}
// push local 4
@4
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20951}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20958}
// lt
@Screen.drawLine.lt.4
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawLine.lt.4)
// {line: 20963}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 20969}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20975}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20978}
// not
@SP
A=M-1
M=!M
// {line: 20983}
// if-goto Screen.drawLine.if.4
@SP
AM=M-1
D=M
@Screen.drawLine.if.4
D;JNE
// {line: 20992}
// push local 2
@2
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20998}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 21003}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 21011}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 21020}
// push local 4
@4
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21029}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21034}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 21044}
// pop local 4
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
A=A+1
A=A+1
M=D
// {line: 21045}
(Screen.drawLine.if.4)
// {line: 21050}
// if-goto Screen.drawLine.goto.1
@SP
AM=M-1
D=M
@Screen.drawLine.goto.1
D;JNE
// {line: 21059}
// push local 3
@3
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21065}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 21070}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 21079}
// pop local 3
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
A=A+1
M=D
// {line: 21088}
// push local 4
@4
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21097}
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
// {line: 21102}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 21112}
// pop local 4
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
A=A+1
A=A+1
M=D
// {line: 21113}
(Screen.drawLine.goto.1)
// {line: 21115}
// goto Screen.drawLine.while.0
@Screen.drawLine.while.0
0;JMP
// {line: 21116}
(Screen.drawLine.while.1)
// {line: 21122}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 21124}
// return
@return
0;JMP
// {line: 21125}
(Screen.drawLine.goto.0)
// {line: 21126}
(Screen.drawLine.if.2)
// {line: 21131}
// if-goto Screen.drawLine.goto.2
@SP
AM=M-1
D=M
@Screen.drawLine.goto.2
D;JNE
// {line: 21140}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21146}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 21153}
// lt
@Screen.drawLine.lt.5
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawLine.lt.5)
// {line: 21158}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 21164}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21170}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21173}
// not
@SP
A=M-1
M=!M
// {line: 21178}
// if-goto Screen.drawLine.if.5
@SP
AM=M-1
D=M
@Screen.drawLine.if.5
D;JNE
// {line: 21187}
// push argument 2
@2
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21196}
// push argument 3
@3
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21205}
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
// {line: 21214}
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
// {line: 21227}
// call Screen.drawLine nArgs: 4
@4
D=A
@R14
M=D
@Screen.drawLine
D=A
@R15
M=D
@Screen.drawLine.call.4
D=A
@call
0;JMP
(Screen.drawLine.call.4)
// {line: 21232}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 21238}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 21240}
// return
@return
0;JMP
// {line: 21241}
(Screen.drawLine.if.5)
// {line: 21246}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 21247}
(Screen.drawLine.goto.2)
// {line: 21248}
(Screen.drawLine.while.2)
// {line: 21257}
// push local 2
@2
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21266}
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
// {line: 21273}
// lt
@Screen.drawLine.lt.6
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawLine.lt.6)
// {line: 21282}
// push local 2
@2
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21291}
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
// {line: 21298}
// eq
@Screen.drawLine.eq.4
D=A
@R14
M=D
@eq
0;JMP
(Screen.drawLine.eq.4)
// {line: 21303}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 21312}
// push local 3
@3
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21321}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21328}
// lt
@Screen.drawLine.lt.7
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawLine.lt.7)
// {line: 21337}
// push local 3
@3
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21346}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21353}
// eq
@Screen.drawLine.eq.5
D=A
@R14
M=D
@eq
0;JMP
(Screen.drawLine.eq.5)
// {line: 21358}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 21363}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 21366}
// not
@SP
A=M-1
M=!M
// {line: 21371}
// if-goto Screen.drawLine.while.3
@SP
AM=M-1
D=M
@Screen.drawLine.while.3
D;JNE
// {line: 21380}
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
// {line: 21389}
// push local 2
@2
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21394}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 21403}
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
// {line: 21412}
// push local 3
@3
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21417}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 21430}
// call Screen.drawPixel nArgs: 2
@2
D=A
@R14
M=D
@Screen.drawPixel
D=A
@R15
M=D
@Screen.drawLine.call.5
D=A
@call
0;JMP
(Screen.drawLine.call.5)
// {line: 21435}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 21444}
// push local 4
@4
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21450}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 21457}
// lt
@Screen.drawLine.lt.8
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawLine.lt.8)
// {line: 21462}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 21468}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21474}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21477}
// not
@SP
A=M-1
M=!M
// {line: 21482}
// if-goto Screen.drawLine.if.6
@SP
AM=M-1
D=M
@Screen.drawLine.if.6
D;JNE
// {line: 21491}
// push local 2
@2
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21497}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 21502}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 21510}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 21519}
// push local 4
@4
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21528}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21533}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 21543}
// pop local 4
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
A=A+1
A=A+1
M=D
// {line: 21544}
(Screen.drawLine.if.6)
// {line: 21549}
// if-goto Screen.drawLine.goto.3
@SP
AM=M-1
D=M
@Screen.drawLine.goto.3
D;JNE
// {line: 21558}
// push local 3
@3
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21564}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 21569}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 21578}
// pop local 3
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
A=A+1
M=D
// {line: 21587}
// push local 4
@4
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21596}
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
// {line: 21601}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 21611}
// pop local 4
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
A=A+1
A=A+1
M=D
// {line: 21612}
(Screen.drawLine.goto.3)
// {line: 21614}
// goto Screen.drawLine.while.2
@Screen.drawLine.while.2
0;JMP
// {line: 21615}
(Screen.drawLine.while.3)
// {line: 21617}
// return
@return
0;JMP
// {line: 21618}
// function Screen.drawRectangle nLocals: 0
(Screen.drawRectangle)
// {line: 21619}
(Screen.drawRectangle.while.0)
// {line: 21628}
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
// {line: 21634}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 21639}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 21648}
// push argument 3
@3
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21655}
// lt
@Screen.drawRectangle.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawRectangle.lt.0)
// {line: 21658}
// not
@SP
A=M-1
M=!M
// {line: 21663}
// if-goto Screen.drawRectangle.while.1
@SP
AM=M-1
D=M
@Screen.drawRectangle.while.1
D;JNE
// {line: 21672}
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
// {line: 21681}
// push argument 2
@2
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21690}
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
// {line: 21703}
// call Screen.drawHoriz nArgs: 3
@3
D=A
@R14
M=D
@Screen.drawHoriz
D=A
@R15
M=D
@Screen.drawRectangle.call.0
D=A
@call
0;JMP
(Screen.drawRectangle.call.0)
// {line: 21708}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 21717}
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
// {line: 21723}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 21728}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 21735}
// pop argument 1
@SP
AM=M-1
D=M
@ARG
A=M
A=A+1
M=D
// {line: 21737}
// goto Screen.drawRectangle.while.0
@Screen.drawRectangle.while.0
0;JMP
// {line: 21738}
(Screen.drawRectangle.while.1)
// {line: 21740}
// return
@return
0;JMP
// {line: 21749}
// function Screen.drawCircle nLocals: 2
(Screen.drawCircle)
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
// {line: 21758}
// push argument 2
@2
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21771}
// call Math.abs nArgs: 1
@1
D=A
@R14
M=D
@Math.abs
D=A
@R15
M=D
@Screen.drawCircle.call.0
D=A
@call
0;JMP
(Screen.drawCircle.call.0)
// {line: 21779}
// pop argument 2
@SP
AM=M-1
D=M
@ARG
A=M
A=A+1
A=A+1
M=D
// {line: 21788}
// push argument 2
@2
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21791}
// neg
@SP
A=M-1
M=-M
// {line: 21797}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 21798}
(Screen.drawCircle.while.0)
// {line: 21807}
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
// {line: 21813}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 21818}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 21827}
// push argument 2
@2
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21834}
// lt
@Screen.drawCircle.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawCircle.lt.0)
// {line: 21837}
// not
@SP
A=M-1
M=!M
// {line: 21842}
// if-goto Screen.drawCircle.while.1
@SP
AM=M-1
D=M
@Screen.drawCircle.while.1
D;JNE
// {line: 21851}
// push argument 2
@2
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21860}
// push argument 2
@2
D=A
@ARG
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21873}
// call Math.multiply nArgs: 2
@2
D=A
@R14
M=D
@Math.multiply
D=A
@R15
M=D
@Screen.drawCircle.call.1
D=A
@call
0;JMP
(Screen.drawCircle.call.1)
// {line: 21882}
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
// {line: 21891}
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
// {line: 21904}
// call Math.multiply nArgs: 2
@2
D=A
@R14
M=D
@Math.multiply
D=A
@R15
M=D
@Screen.drawCircle.call.2
D=A
@call
0;JMP
(Screen.drawCircle.call.2)
// {line: 21909}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 21922}
// call Math.sqrt nArgs: 1
@1
D=A
@R14
M=D
@Math.sqrt
D=A
@R15
M=D
@Screen.drawCircle.call.3
D=A
@call
0;JMP
(Screen.drawCircle.call.3)
// {line: 21929}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 21938}
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
// {line: 21947}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21952}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 21961}
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
// {line: 21970}
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
// {line: 21975}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 21984}
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
// {line: 21993}
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21998}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 22007}
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
// {line: 22016}
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
// {line: 22021}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 22034}
// call Screen.drawLine nArgs: 4
@4
D=A
@R14
M=D
@Screen.drawLine
D=A
@R15
M=D
@Screen.drawCircle.call.4
D=A
@call
0;JMP
(Screen.drawCircle.call.4)
// {line: 22039}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 22048}
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
// {line: 22054}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22059}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 22065}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 22067}
// goto Screen.drawCircle.while.0
@Screen.drawCircle.while.0
0;JMP
// {line: 22068}
(Screen.drawCircle.while.1)
// {line: 22070}
// return
@return
0;JMP
// {line: 22071}
// function Sys.init nLocals: 0
(Sys.init)
// {line: 22077}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22090}
// call Sys.setSplash nArgs: 1
@1
D=A
@R14
M=D
@Sys.setSplash
D=A
@R15
M=D
@Sys.init.call.0
D=A
@call
0;JMP
(Sys.init.call.0)
// {line: 22095}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 22108}
// call Memory.init nArgs: 0
@0
D=A
@R14
M=D
@Memory.init
D=A
@R15
M=D
@Sys.init.call.1
D=A
@call
0;JMP
(Sys.init.call.1)
// {line: 22113}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 22126}
// call Screen.init nArgs: 0
@0
D=A
@R14
M=D
@Screen.init
D=A
@R15
M=D
@Sys.init.call.2
D=A
@call
0;JMP
(Sys.init.call.2)
// {line: 22131}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 22144}
// call Output.init nArgs: 0
@0
D=A
@R14
M=D
@Output.init
D=A
@R15
M=D
@Sys.init.call.3
D=A
@call
0;JMP
(Sys.init.call.3)
// {line: 22149}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 22162}
// call Math.init nArgs: 0
@0
D=A
@R14
M=D
@Math.init
D=A
@R15
M=D
@Sys.init.call.4
D=A
@call
0;JMP
(Sys.init.call.4)
// {line: 22167}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 22180}
// call Keyboard.init nArgs: 0
@0
D=A
@R14
M=D
@Keyboard.init
D=A
@R15
M=D
@Sys.init.call.5
D=A
@call
0;JMP
(Sys.init.call.5)
// {line: 22185}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 22191}
// push constant 60
@60
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22204}
// call Sys.setWaitRate nArgs: 1
@1
D=A
@R14
M=D
@Sys.setWaitRate
D=A
@R15
M=D
@Sys.init.call.6
D=A
@call
0;JMP
(Sys.init.call.6)
// {line: 22209}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 22215}
// push static 12
@Sys.static.12
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 22220}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 22226}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 22232}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 22235}
// not
@SP
A=M-1
M=!M
// {line: 22240}
// if-goto Sys.init.if.0
@SP
AM=M-1
D=M
@Sys.init.if.0
D;JNE
// {line: 22253}
// call Sys.splash nArgs: 0
@0
D=A
@R14
M=D
@Sys.splash
D=A
@R15
M=D
@Sys.init.call.7
D=A
@call
0;JMP
(Sys.init.call.7)
// {line: 22258}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 22259}
(Sys.init.if.0)
// {line: 22264}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 22277}
// call Main.main nArgs: 0
@0
D=A
@R14
M=D
@Main.main
D=A
@R15
M=D
@Sys.init.call.8
D=A
@call
0;JMP
(Sys.init.call.8)
// {line: 22282}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 22295}
// call Sys.halt nArgs: 0
@0
D=A
@R14
M=D
@Sys.halt
D=A
@R15
M=D
@Sys.init.call.9
D=A
@call
0;JMP
(Sys.init.call.9)
// {line: 22300}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 22306}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22308}
// return
@return
0;JMP
// {line: 22309}
// function Sys.setSplash nLocals: 0
(Sys.setSplash)
// {line: 22318}
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
// {line: 22323}
// pop static 12
@SP
AM=M-1
D=M
@Sys.static.12
M=D
// {line: 22325}
// return
@return
0;JMP
// {line: 22326}
// function Sys.setWaitRate nLocals: 0
(Sys.setWaitRate)
// {line: 22335}
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
// {line: 22340}
// pop static 11
@SP
AM=M-1
D=M
@Sys.static.11
M=D
// {line: 22342}
// return
@return
0;JMP
// {line: 22347}
// function Sys.splash nLocals: 1
(Sys.splash)
@SP
AM=M+1
A=A-1
M=0
// {line: 22353}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22359}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 22365}
// push constant 10
@10
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22378}
// call String.new nArgs: 1
@1
D=A
@R14
M=D
@String.new
D=A
@R15
M=D
@Sys.splash.call.0
D=A
@call
0;JMP
(Sys.splash.call.0)
// {line: 22384}
// push constant 74
@74
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22397}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Sys.splash.call.1
D=A
@call
0;JMP
(Sys.splash.call.1)
// {line: 22403}
// push constant 97
@97
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22416}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Sys.splash.call.2
D=A
@call
0;JMP
(Sys.splash.call.2)
// {line: 22422}
// push constant 114
@114
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22435}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Sys.splash.call.3
D=A
@call
0;JMP
(Sys.splash.call.3)
// {line: 22441}
// push constant 118
@118
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22454}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Sys.splash.call.4
D=A
@call
0;JMP
(Sys.splash.call.4)
// {line: 22460}
// push constant 105
@105
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22473}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Sys.splash.call.5
D=A
@call
0;JMP
(Sys.splash.call.5)
// {line: 22479}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22492}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Sys.splash.call.6
D=A
@call
0;JMP
(Sys.splash.call.6)
// {line: 22498}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22511}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Sys.splash.call.7
D=A
@call
0;JMP
(Sys.splash.call.7)
// {line: 22517}
// push constant 49
@49
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22530}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Sys.splash.call.8
D=A
@call
0;JMP
(Sys.splash.call.8)
// {line: 22536}
// push constant 46
@46
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22549}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Sys.splash.call.9
D=A
@call
0;JMP
(Sys.splash.call.9)
// {line: 22555}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22568}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Sys.splash.call.10
D=A
@call
0;JMP
(Sys.splash.call.10)
// {line: 22581}
// call Output.printString nArgs: 1
@1
D=A
@R14
M=D
@Output.printString
D=A
@R15
M=D
@Sys.splash.call.11
D=A
@call
0;JMP
(Sys.splash.call.11)
// {line: 22586}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 22599}
// call Output.println nArgs: 0
@0
D=A
@R14
M=D
@Output.println
D=A
@R15
M=D
@Sys.splash.call.12
D=A
@call
0;JMP
(Sys.splash.call.12)
// {line: 22604}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 22610}
// push constant 700
@700
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22623}
// call Sys.wait nArgs: 1
@1
D=A
@R14
M=D
@Sys.wait
D=A
@R15
M=D
@Sys.splash.call.13
D=A
@call
0;JMP
(Sys.splash.call.13)
// {line: 22628}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 22634}
// push constant 7
@7
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22647}
// call String.new nArgs: 1
@1
D=A
@R14
M=D
@String.new
D=A
@R15
M=D
@Sys.splash.call.14
D=A
@call
0;JMP
(Sys.splash.call.14)
// {line: 22653}
// push constant 98
@98
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22666}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Sys.splash.call.15
D=A
@call
0;JMP
(Sys.splash.call.15)
// {line: 22672}
// push constant 111
@111
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22685}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Sys.splash.call.16
D=A
@call
0;JMP
(Sys.splash.call.16)
// {line: 22691}
// push constant 111
@111
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22704}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Sys.splash.call.17
D=A
@call
0;JMP
(Sys.splash.call.17)
// {line: 22710}
// push constant 116
@116
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22723}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Sys.splash.call.18
D=A
@call
0;JMP
(Sys.splash.call.18)
// {line: 22729}
// push constant 105
@105
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22742}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Sys.splash.call.19
D=A
@call
0;JMP
(Sys.splash.call.19)
// {line: 22748}
// push constant 110
@110
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22761}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Sys.splash.call.20
D=A
@call
0;JMP
(Sys.splash.call.20)
// {line: 22767}
// push constant 103
@103
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22780}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Sys.splash.call.21
D=A
@call
0;JMP
(Sys.splash.call.21)
// {line: 22793}
// call Output.printString nArgs: 1
@1
D=A
@R14
M=D
@Output.printString
D=A
@R15
M=D
@Sys.splash.call.22
D=A
@call
0;JMP
(Sys.splash.call.22)
// {line: 22798}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 22799}
(Sys.splash.while.0)
// {line: 22808}
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
// {line: 22814}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22821}
// gt
@Sys.splash.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Sys.splash.gt.0)
// {line: 22824}
// not
@SP
A=M-1
M=!M
// {line: 22829}
// if-goto Sys.splash.while.1
@SP
AM=M-1
D=M
@Sys.splash.while.1
D;JNE
// {line: 22835}
// push constant 600
@600
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22848}
// call Sys.wait nArgs: 1
@1
D=A
@R14
M=D
@Sys.wait
D=A
@R15
M=D
@Sys.splash.call.23
D=A
@call
0;JMP
(Sys.splash.call.23)
// {line: 22853}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 22859}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22872}
// call String.new nArgs: 1
@1
D=A
@R14
M=D
@String.new
D=A
@R15
M=D
@Sys.splash.call.24
D=A
@call
0;JMP
(Sys.splash.call.24)
// {line: 22878}
// push constant 46
@46
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22891}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Sys.splash.call.25
D=A
@call
0;JMP
(Sys.splash.call.25)
// {line: 22904}
// call Output.printString nArgs: 1
@1
D=A
@R14
M=D
@Output.printString
D=A
@R15
M=D
@Sys.splash.call.26
D=A
@call
0;JMP
(Sys.splash.call.26)
// {line: 22909}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 22918}
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
// {line: 22924}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22929}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 22935}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 22937}
// goto Sys.splash.while.0
@Sys.splash.while.0
0;JMP
// {line: 22938}
(Sys.splash.while.1)
// {line: 22944}
// push constant 1500
@1500
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22957}
// call Sys.wait nArgs: 1
@1
D=A
@R14
M=D
@Sys.wait
D=A
@R15
M=D
@Sys.splash.call.27
D=A
@call
0;JMP
(Sys.splash.call.27)
// {line: 22962}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 22975}
// call Screen.clearScreen nArgs: 0
@0
D=A
@R14
M=D
@Screen.clearScreen
D=A
@R15
M=D
@Sys.splash.call.28
D=A
@call
0;JMP
(Sys.splash.call.28)
// {line: 22980}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 22986}
// push constant 1000
@1000
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22999}
// call Sys.wait nArgs: 1
@1
D=A
@R14
M=D
@Sys.wait
D=A
@R15
M=D
@Sys.splash.call.29
D=A
@call
0;JMP
(Sys.splash.call.29)
// {line: 23004}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 23010}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23012}
// return
@return
0;JMP
// {line: 23013}
// function Sys.halt nLocals: 0
(Sys.halt)
// {line: 23014}
(Sys.halt.while.0)
// {line: 23020}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23023}
// not
@SP
A=M-1
M=!M
// {line: 23026}
// not
@SP
A=M-1
M=!M
// {line: 23031}
// if-goto Sys.halt.while.1
@SP
AM=M-1
D=M
@Sys.halt.while.1
D;JNE
// {line: 23033}
// goto Sys.halt.while.0
@Sys.halt.while.0
0;JMP
// {line: 23034}
(Sys.halt.while.1)
// {line: 23040}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23042}
// return
@return
0;JMP
// {line: 23047}
// function Sys.wait nLocals: 1
(Sys.wait)
@SP
AM=M+1
A=A-1
M=0
// {line: 23056}
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
// {line: 23062}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23069}
// lt
@Sys.wait.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Sys.wait.lt.0)
// {line: 23074}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 23080}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 23086}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 23089}
// not
@SP
A=M-1
M=!M
// {line: 23094}
// if-goto Sys.wait.if.0
@SP
AM=M-1
D=M
@Sys.wait.if.0
D;JNE
// {line: 23100}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23113}
// call Sys.error nArgs: 1
@1
D=A
@R14
M=D
@Sys.error
D=A
@R15
M=D
@Sys.wait.call.0
D=A
@call
0;JMP
(Sys.wait.call.0)
// {line: 23118}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 23119}
(Sys.wait.if.0)
// {line: 23124}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 23130}
// push static 11
@Sys.static.11
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 23136}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 23137}
(Sys.wait.while.0)
// {line: 23146}
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
// {line: 23152}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23159}
// gt
@Sys.wait.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Sys.wait.gt.0)
// {line: 23162}
// not
@SP
A=M-1
M=!M
// {line: 23167}
// if-goto Sys.wait.while.1
@SP
AM=M-1
D=M
@Sys.wait.while.1
D;JNE
// {line: 23168}
(Sys.wait.while.2)
// {line: 23177}
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
// {line: 23183}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23190}
// gt
@Sys.wait.gt.1
D=A
@R14
M=D
@gt
0;JMP
(Sys.wait.gt.1)
// {line: 23193}
// not
@SP
A=M-1
M=!M
// {line: 23198}
// if-goto Sys.wait.while.3
@SP
AM=M-1
D=M
@Sys.wait.while.3
D;JNE
// {line: 23207}
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
// {line: 23213}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23218}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 23224}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 23226}
// goto Sys.wait.while.2
@Sys.wait.while.2
0;JMP
// {line: 23227}
(Sys.wait.while.3)
// {line: 23233}
// push static 11
@Sys.static.11
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 23239}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 23248}
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
// {line: 23254}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23259}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 23265}
// pop argument 0
@SP
AM=M-1
D=M
@ARG
A=M
M=D
// {line: 23267}
// goto Sys.wait.while.0
@Sys.wait.while.0
0;JMP
// {line: 23268}
(Sys.wait.while.1)
// {line: 23274}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23276}
// return
@return
0;JMP
// {line: 23277}
// function Sys.error nLocals: 0
(Sys.error)
// {line: 23290}
// call Output.println nArgs: 0
@0
D=A
@R14
M=D
@Output.println
D=A
@R15
M=D
@Sys.error.call.0
D=A
@call
0;JMP
(Sys.error.call.0)
// {line: 23295}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 23301}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23314}
// call String.new nArgs: 1
@1
D=A
@R14
M=D
@String.new
D=A
@R15
M=D
@Sys.error.call.1
D=A
@call
0;JMP
(Sys.error.call.1)
// {line: 23320}
// push constant 69
@69
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23333}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Sys.error.call.2
D=A
@call
0;JMP
(Sys.error.call.2)
// {line: 23339}
// push constant 82
@82
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23352}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Sys.error.call.3
D=A
@call
0;JMP
(Sys.error.call.3)
// {line: 23358}
// push constant 82
@82
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23371}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Sys.error.call.4
D=A
@call
0;JMP
(Sys.error.call.4)
// {line: 23384}
// call Output.printString nArgs: 1
@1
D=A
@R14
M=D
@Output.printString
D=A
@R15
M=D
@Sys.error.call.5
D=A
@call
0;JMP
(Sys.error.call.5)
// {line: 23389}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 23398}
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
// {line: 23411}
// call Output.printInt nArgs: 1
@1
D=A
@R14
M=D
@Output.printInt
D=A
@R15
M=D
@Sys.error.call.6
D=A
@call
0;JMP
(Sys.error.call.6)
// {line: 23416}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 23429}
// call Sys.halt nArgs: 0
@0
D=A
@R14
M=D
@Sys.halt
D=A
@R15
M=D
@Sys.error.call.7
D=A
@call
0;JMP
(Sys.error.call.7)
// {line: 23434}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 23440}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23442}
// return
@return
0;JMP
// {line: 23443}
// function Keyboard.init nLocals: 0
(Keyboard.init)
// {line: 23445}
// return
@return
0;JMP
// {line: 23446}
// function Keyboard.keyPressed nLocals: 0
(Keyboard.keyPressed)
// {line: 23448}
// return
@return
0;JMP
// {line: 23449}
// function Keyboard.readChar nLocals: 0
(Keyboard.readChar)
// {line: 23451}
// return
@return
0;JMP
// {line: 23452}
// function Keyboard.readLine nLocals: 0
(Keyboard.readLine)
// {line: 23454}
// return
@return
0;JMP
// {line: 23455}
// function Keyboard.readInt nLocals: 0
(Keyboard.readInt)
// {line: 23457}
// return
@return
0;JMP
