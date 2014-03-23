// Bootstrap code
@256
D=A
@SP
M=D
@Sys.init
0;JMP
// ***
// OS
// compiled on Saturday March 22, 2014
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
// if-goto Output.printChar.goto.1
@SP
AM=M-1
D=M
@Output.printChar.goto.1
D;JNE
// {line: 9757}
// call Output.println nArgs: 0
@0
D=A
@R14
M=D
@Output.println
D=A
@R15
M=D
@Output.printChar.call.2
D=A
@call
0;JMP
(Output.printChar.call.2)
// {line: 9762}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 9763}
(Output.printChar.goto.1)
// {line: 9764}
(Output.printChar.goto.0)
// {line: 9766}
// return
@return
0;JMP
// {line: 9823}
// function Output._print nLocals: 14
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
// {line: 9829}
// push constant 16384
@16384
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9844}
// pop local 9
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
A=A+1
A=A+1
M=D
// {line: 9853}
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
// {line: 9866}
// call Output.getMap nArgs: 1
@1
D=A
@R14
M=D
@Output.getMap
D=A
@R15
M=D
@Output._print.call.0
D=A
@call
0;JMP
(Output._print.call.0)
// {line: 9872}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 9878}
// push static 10
@Output.static.10
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9884}
// push constant 8
@8
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9897}
// call Math.multiply nArgs: 2
@2
D=A
@R14
M=D
@Math.multiply
D=A
@R15
M=D
@Output._print.call.1
D=A
@call
0;JMP
(Output._print.call.1)
// {line: 9904}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 9910}
// push static 9
@Output.static.9
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9916}
// push constant 11
@11
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9929}
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
// {line: 9937}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 9946}
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
// {line: 9952}
// push constant 7
@7
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9957}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 9966}
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
// {line: 9975}
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
// {line: 9981}
// push constant 10
@10
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9986}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 9996}
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
// {line: 10002}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10014}
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
// {line: 10023}
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
// {line: 10029}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10042}
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
// {line: 10058}
// pop local 10
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
A=A+1
A=A+1
A=A+1
M=D
// {line: 10059}
(Output._print.while.0)
// {line: 10068}
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
// {line: 10077}
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
// {line: 10082}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 10091}
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
// {line: 10098}
// lt
@Output._print.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Output._print.lt.0)
// {line: 10101}
// not
@SP
A=M-1
M=!M
// {line: 10106}
// if-goto Output._print.while.1
@SP
AM=M-1
D=M
@Output._print.while.1
D;JNE
// {line: 10112}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10123}
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
// {line: 10129}
// push pointer 1
@4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10138}
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
// {line: 10147}
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
// {line: 10152}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 10157}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 10166}
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
// {line: 10171}
// pop temp 2
@SP
AM=M-1
D=M
@R7
M=D
// {line: 10176}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 10182}
// push temp 2
@7
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10199}
// pop local 11
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
A=A+1
A=A+1
A=A+1
A=A+1
M=D
// {line: 10208}
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
// {line: 10214}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10227}
// call Math.divide nArgs: 2
@2
D=A
@R14
M=D
@Math.divide
D=A
@R15
M=D
@Output._print.call.4
D=A
@call
0;JMP
(Output._print.call.4)
// {line: 10245}
// pop local 12
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
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
M=D
// {line: 10254}
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
// {line: 10260}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10273}
// call Math.mod nArgs: 2
@2
D=A
@R14
M=D
@Math.mod
D=A
@R15
M=D
@Output._print.call.5
D=A
@call
0;JMP
(Output._print.call.5)
// {line: 10286}
// call Math.twoToThe nArgs: 1
@1
D=A
@R14
M=D
@Math.twoToThe
D=A
@R15
M=D
@Output._print.call.6
D=A
@call
0;JMP
(Output._print.call.6)
// {line: 10299}
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
// {line: 10300}
(Output._print.while.2)
// {line: 10309}
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
// {line: 10318}
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
// {line: 10323}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 10332}
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
// {line: 10339}
// lt
@Output._print.lt.1
D=A
@R14
M=D
@lt
0;JMP
(Output._print.lt.1)
// {line: 10342}
// not
@SP
A=M-1
M=!M
// {line: 10347}
// if-goto Output._print.while.3
@SP
AM=M-1
D=M
@Output._print.while.3
D;JNE
// {line: 10356}
// push local 12
@12
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10365}
// push local 10
@10
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10370}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 10384}
// pop local 8
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
A=A+1
M=D
// {line: 10393}
// push local 11
@11
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10402}
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
// {line: 10415}
// call Math.bit nArgs: 2
@2
D=A
@R14
M=D
@Math.bit
D=A
@R15
M=D
@Output._print.call.7
D=A
@call
0;JMP
(Output._print.call.7)
// {line: 10434}
// pop local 13
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
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
M=D
// {line: 10443}
// push local 9
@9
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10452}
// push local 8
@8
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10457}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 10462}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 10468}
// push pointer 1
@4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10477}
// push local 9
@9
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10486}
// push local 8
@8
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10491}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 10496}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 10505}
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
// {line: 10510}
// pop temp 2
@SP
AM=M-1
D=M
@R7
M=D
// {line: 10515}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 10521}
// push temp 2
@7
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10530}
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
// {line: 10533}
// not
@SP
A=M-1
M=!M
// {line: 10538}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 10547}
// push local 13
@13
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10556}
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
// {line: 10561}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 10566}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 10572}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 10581}
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
// {line: 10590}
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
// {line: 10595}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 10608}
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
// {line: 10617}
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
// {line: 10623}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10630}
// lt
@Output._print.lt.2
D=A
@R14
M=D
@lt
0;JMP
(Output._print.lt.2)
// {line: 10635}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 10641}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10647}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10650}
// not
@SP
A=M-1
M=!M
// {line: 10655}
// if-goto Output._print.if.0
@SP
AM=M-1
D=M
@Output._print.if.0
D;JNE
// {line: 10661}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10674}
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
// {line: 10683}
// push local 12
@12
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10689}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10694}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 10712}
// pop local 12
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
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
M=D
// {line: 10713}
(Output._print.if.0)
// {line: 10718}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 10727}
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
// {line: 10733}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10738}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 10749}
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
// {line: 10751}
// goto Output._print.while.2
@Output._print.while.2
0;JMP
// {line: 10752}
(Output._print.while.3)
// {line: 10761}
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
// {line: 10767}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10772}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 10784}
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
// {line: 10793}
// push local 10
@10
D=A
@LCL
A=M+D
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10799}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10804}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 10820}
// pop local 10
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
A=A+1
A=A+1
A=A+1
M=D
// {line: 10822}
// goto Output._print.while.0
@Output._print.while.0
0;JMP
// {line: 10823}
(Output._print.while.1)
// {line: 10825}
// return
@return
0;JMP
// {line: 10834}
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
// {line: 10843}
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
// {line: 10856}
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
// {line: 10863}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 10869}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10875}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 10876}
(Output.printString.while.0)
// {line: 10885}
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
// {line: 10894}
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
// {line: 10901}
// lt
@Output.printString.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Output.printString.lt.0)
// {line: 10904}
// not
@SP
A=M-1
M=!M
// {line: 10909}
// if-goto Output.printString.while.1
@SP
AM=M-1
D=M
@Output.printString.while.1
D;JNE
// {line: 10918}
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
// {line: 10927}
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
// {line: 10940}
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
// {line: 10953}
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
// {line: 10958}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 10967}
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
// {line: 10973}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10978}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 10984}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 10986}
// goto Output.printString.while.0
@Output.printString.while.0
0;JMP
// {line: 10987}
(Output.printString.while.1)
// {line: 10989}
// return
@return
0;JMP
// {line: 10994}
// function Output.printInt nLocals: 1
(Output.printInt)
@SP
AM=M+1
A=A-1
M=0
// {line: 11000}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11013}
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
// {line: 11019}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 11028}
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
// {line: 11037}
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
// {line: 11050}
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
// {line: 11055}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 11064}
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
// {line: 11077}
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
// {line: 11082}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 11084}
// return
@return
0;JMP
// {line: 11085}
// function Output.println nLocals: 0
(Output.println)
// {line: 11091}
// push static 9
@Output.static.9
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 11097}
// push constant 23
@23
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11104}
// lt
@Output.println.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Output.println.lt.0)
// {line: 11109}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 11115}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 11121}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 11124}
// not
@SP
A=M-1
M=!M
// {line: 11129}
// if-goto Output.println.if.0
@SP
AM=M-1
D=M
@Output.println.if.0
D;JNE
// {line: 11135}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11140}
// pop static 10
@SP
AM=M-1
D=M
@Output.static.10
M=D
// {line: 11146}
// push static 9
@Output.static.9
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 11152}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11157}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 11162}
// pop static 9
@SP
AM=M-1
D=M
@Output.static.9
M=D
// {line: 11163}
(Output.println.if.0)
// {line: 11168}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 11170}
// return
@return
0;JMP
// {line: 11171}
// function Output.backSpace nLocals: 0
(Output.backSpace)
// {line: 11177}
// push static 10
@Output.static.10
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 11183}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11190}
// gt
@Output.backSpace.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Output.backSpace.gt.0)
// {line: 11195}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 11201}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 11207}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 11210}
// not
@SP
A=M-1
M=!M
// {line: 11215}
// if-goto Output.backSpace.if.0
@SP
AM=M-1
D=M
@Output.backSpace.if.0
D;JNE
// {line: 11221}
// push static 9
@Output.static.9
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 11227}
// push static 10
@Output.static.10
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 11233}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11238}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 11251}
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
// {line: 11256}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 11257}
(Output.backSpace.if.0)
// {line: 11262}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 11264}
// return
@return
0;JMP
// {line: 11285}
// function Main.main nLocals: 5
(Main.main)
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
// {line: 11291}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11301}
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
// {line: 11307}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11320}
// call String.new nArgs: 1
@1
D=A
@R14
M=D
@String.new
D=A
@R15
M=D
@Main.main.call.0
D=A
@call
0;JMP
(Main.main.call.0)
// {line: 11326}
// push constant 107
@107
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11339}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.1
D=A
@call
0;JMP
(Main.main.call.1)
// {line: 11345}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11358}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.2
D=A
@call
0;JMP
(Main.main.call.2)
// {line: 11364}
// push constant 121
@121
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11377}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.3
D=A
@call
0;JMP
(Main.main.call.3)
// {line: 11383}
// push constant 80
@80
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11396}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.4
D=A
@call
0;JMP
(Main.main.call.4)
// {line: 11402}
// push constant 114
@114
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11415}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.5
D=A
@call
0;JMP
(Main.main.call.5)
// {line: 11421}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11434}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.6
D=A
@call
0;JMP
(Main.main.call.6)
// {line: 11440}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11453}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.7
D=A
@call
0;JMP
(Main.main.call.7)
// {line: 11459}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11472}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.8
D=A
@call
0;JMP
(Main.main.call.8)
// {line: 11478}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11491}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.9
D=A
@call
0;JMP
(Main.main.call.9)
// {line: 11497}
// push constant 100
@100
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11510}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.10
D=A
@call
0;JMP
(Main.main.call.10)
// {line: 11516}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11529}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.11
D=A
@call
0;JMP
(Main.main.call.11)
// {line: 11535}
// push constant 116
@116
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11548}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.12
D=A
@call
0;JMP
(Main.main.call.12)
// {line: 11554}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11567}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.13
D=A
@call
0;JMP
(Main.main.call.13)
// {line: 11573}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11586}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.14
D=A
@call
0;JMP
(Main.main.call.14)
// {line: 11592}
// push constant 116
@116
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11605}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.15
D=A
@call
0;JMP
(Main.main.call.15)
// {line: 11611}
// push constant 58
@58
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11624}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.16
D=A
@call
0;JMP
(Main.main.call.16)
// {line: 11637}
// call Output.printString nArgs: 1
@1
D=A
@R14
M=D
@Output.printString
D=A
@R15
M=D
@Main.main.call.17
D=A
@call
0;JMP
(Main.main.call.17)
// {line: 11642}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 11655}
// call Output.println nArgs: 0
@0
D=A
@R14
M=D
@Output.println
D=A
@R15
M=D
@Main.main.call.18
D=A
@call
0;JMP
(Main.main.call.18)
// {line: 11660}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 11661}
(Main.main.while.0)
// {line: 11670}
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
// {line: 11673}
// not
@SP
A=M-1
M=!M
// {line: 11676}
// not
@SP
A=M-1
M=!M
// {line: 11681}
// if-goto Main.main.while.1
@SP
AM=M-1
D=M
@Main.main.while.1
D;JNE
// {line: 11687}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11700}
// call String.new nArgs: 1
@1
D=A
@R14
M=D
@String.new
D=A
@R15
M=D
@Main.main.call.19
D=A
@call
0;JMP
(Main.main.call.19)
// {line: 11706}
// push constant 80
@80
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11719}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.20
D=A
@call
0;JMP
(Main.main.call.20)
// {line: 11725}
// push constant 108
@108
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11738}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.21
D=A
@call
0;JMP
(Main.main.call.21)
// {line: 11744}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11757}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.22
D=A
@call
0;JMP
(Main.main.call.22)
// {line: 11763}
// push constant 97
@97
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11776}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.23
D=A
@call
0;JMP
(Main.main.call.23)
// {line: 11782}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11795}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.24
D=A
@call
0;JMP
(Main.main.call.24)
// {line: 11801}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11814}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.25
D=A
@call
0;JMP
(Main.main.call.25)
// {line: 11820}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11833}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.26
D=A
@call
0;JMP
(Main.main.call.26)
// {line: 11839}
// push constant 112
@112
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11852}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.27
D=A
@call
0;JMP
(Main.main.call.27)
// {line: 11858}
// push constant 114
@114
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11871}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.28
D=A
@call
0;JMP
(Main.main.call.28)
// {line: 11877}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11890}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.29
D=A
@call
0;JMP
(Main.main.call.29)
// {line: 11896}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11909}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.30
D=A
@call
0;JMP
(Main.main.call.30)
// {line: 11915}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11928}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.31
D=A
@call
0;JMP
(Main.main.call.31)
// {line: 11934}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11947}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.32
D=A
@call
0;JMP
(Main.main.call.32)
// {line: 11953}
// push constant 116
@116
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11966}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.33
D=A
@call
0;JMP
(Main.main.call.33)
// {line: 11972}
// push constant 104
@104
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11985}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.34
D=A
@call
0;JMP
(Main.main.call.34)
// {line: 11991}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12004}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.35
D=A
@call
0;JMP
(Main.main.call.35)
// {line: 12010}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12023}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.36
D=A
@call
0;JMP
(Main.main.call.36)
// {line: 12029}
// push constant 39
@39
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12042}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.37
D=A
@call
0;JMP
(Main.main.call.37)
// {line: 12048}
// push constant 80
@80
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12061}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.38
D=A
@call
0;JMP
(Main.main.call.38)
// {line: 12067}
// push constant 97
@97
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12080}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.39
D=A
@call
0;JMP
(Main.main.call.39)
// {line: 12086}
// push constant 103
@103
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12099}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.40
D=A
@call
0;JMP
(Main.main.call.40)
// {line: 12105}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12118}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.41
D=A
@call
0;JMP
(Main.main.call.41)
// {line: 12124}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12137}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.42
D=A
@call
0;JMP
(Main.main.call.42)
// {line: 12143}
// push constant 68
@68
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12156}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.43
D=A
@call
0;JMP
(Main.main.call.43)
// {line: 12162}
// push constant 111
@111
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12175}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.44
D=A
@call
0;JMP
(Main.main.call.44)
// {line: 12181}
// push constant 119
@119
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12194}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.45
D=A
@call
0;JMP
(Main.main.call.45)
// {line: 12200}
// push constant 110
@110
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12213}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.46
D=A
@call
0;JMP
(Main.main.call.46)
// {line: 12219}
// push constant 39
@39
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12232}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.47
D=A
@call
0;JMP
(Main.main.call.47)
// {line: 12238}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12251}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.48
D=A
@call
0;JMP
(Main.main.call.48)
// {line: 12257}
// push constant 107
@107
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12270}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.49
D=A
@call
0;JMP
(Main.main.call.49)
// {line: 12276}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12289}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.50
D=A
@call
0;JMP
(Main.main.call.50)
// {line: 12295}
// push constant 121
@121
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12308}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.51
D=A
@call
0;JMP
(Main.main.call.51)
// {line: 12321}
// call Output.printString nArgs: 1
@1
D=A
@R14
M=D
@Output.printString
D=A
@R15
M=D
@Main.main.call.52
D=A
@call
0;JMP
(Main.main.call.52)
// {line: 12326}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 12327}
(Main.main.while.2)
// {line: 12336}
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
// {line: 12342}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12349}
// eq
@Main.main.eq.0
D=A
@R14
M=D
@eq
0;JMP
(Main.main.eq.0)
// {line: 12352}
// not
@SP
A=M-1
M=!M
// {line: 12357}
// if-goto Main.main.while.3
@SP
AM=M-1
D=M
@Main.main.while.3
D;JNE
// {line: 12370}
// call Keyboard.keyPressed nArgs: 0
@0
D=A
@R14
M=D
@Keyboard.keyPressed
D=A
@R15
M=D
@Main.main.call.53
D=A
@call
0;JMP
(Main.main.call.53)
// {line: 12377}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 12379}
// goto Main.main.while.2
@Main.main.while.2
0;JMP
// {line: 12380}
(Main.main.while.3)
// {line: 12389}
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
// {line: 12395}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 12396}
(Main.main.while.4)
// {line: 12405}
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
// {line: 12411}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12418}
// eq
@Main.main.eq.1
D=A
@R14
M=D
@eq
0;JMP
(Main.main.eq.1)
// {line: 12421}
// not
@SP
A=M-1
M=!M
// {line: 12424}
// not
@SP
A=M-1
M=!M
// {line: 12429}
// if-goto Main.main.while.5
@SP
AM=M-1
D=M
@Main.main.while.5
D;JNE
// {line: 12442}
// call Keyboard.keyPressed nArgs: 0
@0
D=A
@R14
M=D
@Keyboard.keyPressed
D=A
@R15
M=D
@Main.main.call.54
D=A
@call
0;JMP
(Main.main.call.54)
// {line: 12449}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 12451}
// goto Main.main.while.4
@Main.main.while.4
0;JMP
// {line: 12452}
(Main.main.while.5)
// {line: 12465}
// call Output.println nArgs: 0
@0
D=A
@R14
M=D
@Output.println
D=A
@R15
M=D
@Main.main.call.55
D=A
@call
0;JMP
(Main.main.call.55)
// {line: 12470}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 12479}
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
// {line: 12485}
// push constant 137
@137
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12492}
// eq
@Main.main.eq.2
D=A
@R14
M=D
@eq
0;JMP
(Main.main.eq.2)
// {line: 12497}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 12503}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12509}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12512}
// not
@SP
A=M-1
M=!M
// {line: 12517}
// if-goto Main.main.if.0
@SP
AM=M-1
D=M
@Main.main.if.0
D;JNE
// {line: 12523}
// push constant 2
@2
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12536}
// call String.new nArgs: 1
@1
D=A
@R14
M=D
@String.new
D=A
@R15
M=D
@Main.main.call.56
D=A
@call
0;JMP
(Main.main.call.56)
// {line: 12542}
// push constant 111
@111
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12555}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.57
D=A
@call
0;JMP
(Main.main.call.57)
// {line: 12561}
// push constant 107
@107
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12574}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.58
D=A
@call
0;JMP
(Main.main.call.58)
// {line: 12587}
// call Output.printString nArgs: 1
@1
D=A
@R14
M=D
@Output.printString
D=A
@R15
M=D
@Main.main.call.59
D=A
@call
0;JMP
(Main.main.call.59)
// {line: 12592}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 12605}
// call Output.println nArgs: 0
@0
D=A
@R14
M=D
@Output.println
D=A
@R15
M=D
@Main.main.call.60
D=A
@call
0;JMP
(Main.main.call.60)
// {line: 12610}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 12616}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12619}
// not
@SP
A=M-1
M=!M
// {line: 12629}
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
// {line: 12630}
(Main.main.if.0)
// {line: 12635}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 12637}
// goto Main.main.while.0
@Main.main.while.0
0;JMP
// {line: 12638}
(Main.main.while.1)
// {line: 12644}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12654}
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
// {line: 12660}
// push constant 14
@14
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12673}
// call String.new nArgs: 1
@1
D=A
@R14
M=D
@String.new
D=A
@R15
M=D
@Main.main.call.61
D=A
@call
0;JMP
(Main.main.call.61)
// {line: 12679}
// push constant 114
@114
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12692}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.62
D=A
@call
0;JMP
(Main.main.call.62)
// {line: 12698}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12711}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.63
D=A
@call
0;JMP
(Main.main.call.63)
// {line: 12717}
// push constant 97
@97
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12730}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.64
D=A
@call
0;JMP
(Main.main.call.64)
// {line: 12736}
// push constant 100
@100
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12749}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.65
D=A
@call
0;JMP
(Main.main.call.65)
// {line: 12755}
// push constant 67
@67
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12768}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.66
D=A
@call
0;JMP
(Main.main.call.66)
// {line: 12774}
// push constant 104
@104
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12787}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.67
D=A
@call
0;JMP
(Main.main.call.67)
// {line: 12793}
// push constant 97
@97
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12806}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.68
D=A
@call
0;JMP
(Main.main.call.68)
// {line: 12812}
// push constant 114
@114
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12825}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.69
D=A
@call
0;JMP
(Main.main.call.69)
// {line: 12831}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12844}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.70
D=A
@call
0;JMP
(Main.main.call.70)
// {line: 12850}
// push constant 116
@116
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12863}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.71
D=A
@call
0;JMP
(Main.main.call.71)
// {line: 12869}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12882}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.72
D=A
@call
0;JMP
(Main.main.call.72)
// {line: 12888}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12901}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.73
D=A
@call
0;JMP
(Main.main.call.73)
// {line: 12907}
// push constant 116
@116
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12920}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.74
D=A
@call
0;JMP
(Main.main.call.74)
// {line: 12926}
// push constant 58
@58
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12939}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.75
D=A
@call
0;JMP
(Main.main.call.75)
// {line: 12952}
// call Output.printString nArgs: 1
@1
D=A
@R14
M=D
@Output.printString
D=A
@R15
M=D
@Main.main.call.76
D=A
@call
0;JMP
(Main.main.call.76)
// {line: 12957}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 12970}
// call Output.println nArgs: 0
@0
D=A
@R14
M=D
@Output.println
D=A
@R15
M=D
@Main.main.call.77
D=A
@call
0;JMP
(Main.main.call.77)
// {line: 12975}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 12981}
// push constant 59
@59
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12994}
// call String.new nArgs: 1
@1
D=A
@R14
M=D
@String.new
D=A
@R15
M=D
@Main.main.call.78
D=A
@call
0;JMP
(Main.main.call.78)
// {line: 13000}
// push constant 40
@40
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13013}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.79
D=A
@call
0;JMP
(Main.main.call.79)
// {line: 13019}
// push constant 86
@86
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13032}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.80
D=A
@call
0;JMP
(Main.main.call.80)
// {line: 13038}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13051}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.81
D=A
@call
0;JMP
(Main.main.call.81)
// {line: 13057}
// push constant 114
@114
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13070}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.82
D=A
@call
0;JMP
(Main.main.call.82)
// {line: 13076}
// push constant 105
@105
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13089}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.83
D=A
@call
0;JMP
(Main.main.call.83)
// {line: 13095}
// push constant 102
@102
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13108}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.84
D=A
@call
0;JMP
(Main.main.call.84)
// {line: 13114}
// push constant 121
@121
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13127}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.85
D=A
@call
0;JMP
(Main.main.call.85)
// {line: 13133}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13146}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.86
D=A
@call
0;JMP
(Main.main.call.86)
// {line: 13152}
// push constant 116
@116
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13165}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.87
D=A
@call
0;JMP
(Main.main.call.87)
// {line: 13171}
// push constant 104
@104
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13184}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.88
D=A
@call
0;JMP
(Main.main.call.88)
// {line: 13190}
// push constant 97
@97
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13203}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.89
D=A
@call
0;JMP
(Main.main.call.89)
// {line: 13209}
// push constant 116
@116
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13222}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.90
D=A
@call
0;JMP
(Main.main.call.90)
// {line: 13228}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13241}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.91
D=A
@call
0;JMP
(Main.main.call.91)
// {line: 13247}
// push constant 116
@116
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13260}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.92
D=A
@call
0;JMP
(Main.main.call.92)
// {line: 13266}
// push constant 104
@104
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13279}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.93
D=A
@call
0;JMP
(Main.main.call.93)
// {line: 13285}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13298}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.94
D=A
@call
0;JMP
(Main.main.call.94)
// {line: 13304}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13317}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.95
D=A
@call
0;JMP
(Main.main.call.95)
// {line: 13323}
// push constant 112
@112
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13336}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.96
D=A
@call
0;JMP
(Main.main.call.96)
// {line: 13342}
// push constant 114
@114
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13355}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.97
D=A
@call
0;JMP
(Main.main.call.97)
// {line: 13361}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13374}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.98
D=A
@call
0;JMP
(Main.main.call.98)
// {line: 13380}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13393}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.99
D=A
@call
0;JMP
(Main.main.call.99)
// {line: 13399}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13412}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.100
D=A
@call
0;JMP
(Main.main.call.100)
// {line: 13418}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13431}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.101
D=A
@call
0;JMP
(Main.main.call.101)
// {line: 13437}
// push constant 100
@100
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13450}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.102
D=A
@call
0;JMP
(Main.main.call.102)
// {line: 13456}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13469}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.103
D=A
@call
0;JMP
(Main.main.call.103)
// {line: 13475}
// push constant 99
@99
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13488}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.104
D=A
@call
0;JMP
(Main.main.call.104)
// {line: 13494}
// push constant 104
@104
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13507}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.105
D=A
@call
0;JMP
(Main.main.call.105)
// {line: 13513}
// push constant 97
@97
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13526}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.106
D=A
@call
0;JMP
(Main.main.call.106)
// {line: 13532}
// push constant 114
@114
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13545}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.107
D=A
@call
0;JMP
(Main.main.call.107)
// {line: 13551}
// push constant 97
@97
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13564}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.108
D=A
@call
0;JMP
(Main.main.call.108)
// {line: 13570}
// push constant 99
@99
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13583}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.109
D=A
@call
0;JMP
(Main.main.call.109)
// {line: 13589}
// push constant 116
@116
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13602}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.110
D=A
@call
0;JMP
(Main.main.call.110)
// {line: 13608}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13621}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.111
D=A
@call
0;JMP
(Main.main.call.111)
// {line: 13627}
// push constant 114
@114
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13640}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.112
D=A
@call
0;JMP
(Main.main.call.112)
// {line: 13646}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13659}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.113
D=A
@call
0;JMP
(Main.main.call.113)
// {line: 13665}
// push constant 105
@105
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13678}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.114
D=A
@call
0;JMP
(Main.main.call.114)
// {line: 13684}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13697}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.115
D=A
@call
0;JMP
(Main.main.call.115)
// {line: 13703}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13716}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.116
D=A
@call
0;JMP
(Main.main.call.116)
// {line: 13722}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13735}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.117
D=A
@call
0;JMP
(Main.main.call.117)
// {line: 13741}
// push constant 99
@99
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13754}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.118
D=A
@call
0;JMP
(Main.main.call.118)
// {line: 13760}
// push constant 104
@104
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13773}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.119
D=A
@call
0;JMP
(Main.main.call.119)
// {line: 13779}
// push constant 111
@111
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13792}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.120
D=A
@call
0;JMP
(Main.main.call.120)
// {line: 13798}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13811}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.121
D=A
@call
0;JMP
(Main.main.call.121)
// {line: 13817}
// push constant 100
@100
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13830}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.122
D=A
@call
0;JMP
(Main.main.call.122)
// {line: 13836}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13849}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.123
D=A
@call
0;JMP
(Main.main.call.123)
// {line: 13855}
// push constant 116
@116
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13868}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.124
D=A
@call
0;JMP
(Main.main.call.124)
// {line: 13874}
// push constant 111
@111
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13887}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.125
D=A
@call
0;JMP
(Main.main.call.125)
// {line: 13893}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13906}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.126
D=A
@call
0;JMP
(Main.main.call.126)
// {line: 13912}
// push constant 116
@116
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13925}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.127
D=A
@call
0;JMP
(Main.main.call.127)
// {line: 13931}
// push constant 104
@104
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13944}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.128
D=A
@call
0;JMP
(Main.main.call.128)
// {line: 13950}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13963}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.129
D=A
@call
0;JMP
(Main.main.call.129)
// {line: 13969}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13982}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.130
D=A
@call
0;JMP
(Main.main.call.130)
// {line: 13988}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14001}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.131
D=A
@call
0;JMP
(Main.main.call.131)
// {line: 14007}
// push constant 99
@99
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14020}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.132
D=A
@call
0;JMP
(Main.main.call.132)
// {line: 14026}
// push constant 114
@114
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14039}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.133
D=A
@call
0;JMP
(Main.main.call.133)
// {line: 14045}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14058}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.134
D=A
@call
0;JMP
(Main.main.call.134)
// {line: 14064}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14077}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.135
D=A
@call
0;JMP
(Main.main.call.135)
// {line: 14083}
// push constant 110
@110
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14096}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.136
D=A
@call
0;JMP
(Main.main.call.136)
// {line: 14102}
// push constant 41
@41
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14115}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.137
D=A
@call
0;JMP
(Main.main.call.137)
// {line: 14128}
// call Output.printString nArgs: 1
@1
D=A
@R14
M=D
@Output.printString
D=A
@R15
M=D
@Main.main.call.138
D=A
@call
0;JMP
(Main.main.call.138)
// {line: 14133}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 14146}
// call Output.println nArgs: 0
@0
D=A
@R14
M=D
@Output.println
D=A
@R15
M=D
@Main.main.call.139
D=A
@call
0;JMP
(Main.main.call.139)
// {line: 14151}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 14152}
(Main.main.while.6)
// {line: 14161}
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
// {line: 14164}
// not
@SP
A=M-1
M=!M
// {line: 14167}
// not
@SP
A=M-1
M=!M
// {line: 14172}
// if-goto Main.main.while.7
@SP
AM=M-1
D=M
@Main.main.while.7
D;JNE
// {line: 14178}
// push constant 29
@29
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14191}
// call String.new nArgs: 1
@1
D=A
@R14
M=D
@String.new
D=A
@R15
M=D
@Main.main.call.140
D=A
@call
0;JMP
(Main.main.call.140)
// {line: 14197}
// push constant 80
@80
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14210}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.141
D=A
@call
0;JMP
(Main.main.call.141)
// {line: 14216}
// push constant 108
@108
D=A
@SP
M=M+1
A=M-1
M=D
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
@Main.main.call.142
D=A
@call
0;JMP
(Main.main.call.142)
// {line: 14235}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14248}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.143
D=A
@call
0;JMP
(Main.main.call.143)
// {line: 14254}
// push constant 97
@97
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14267}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.144
D=A
@call
0;JMP
(Main.main.call.144)
// {line: 14273}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14286}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.145
D=A
@call
0;JMP
(Main.main.call.145)
// {line: 14292}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14305}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.146
D=A
@call
0;JMP
(Main.main.call.146)
// {line: 14311}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14324}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.147
D=A
@call
0;JMP
(Main.main.call.147)
// {line: 14330}
// push constant 112
@112
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14343}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.148
D=A
@call
0;JMP
(Main.main.call.148)
// {line: 14349}
// push constant 114
@114
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14362}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.149
D=A
@call
0;JMP
(Main.main.call.149)
// {line: 14368}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14381}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.150
D=A
@call
0;JMP
(Main.main.call.150)
// {line: 14387}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14400}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.151
D=A
@call
0;JMP
(Main.main.call.151)
// {line: 14406}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14419}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.152
D=A
@call
0;JMP
(Main.main.call.152)
// {line: 14425}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14438}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.153
D=A
@call
0;JMP
(Main.main.call.153)
// {line: 14444}
// push constant 116
@116
D=A
@SP
M=M+1
A=M-1
M=D
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
@Main.main.call.154
D=A
@call
0;JMP
(Main.main.call.154)
// {line: 14463}
// push constant 104
@104
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14476}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.155
D=A
@call
0;JMP
(Main.main.call.155)
// {line: 14482}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14495}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.156
D=A
@call
0;JMP
(Main.main.call.156)
// {line: 14501}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14514}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.157
D=A
@call
0;JMP
(Main.main.call.157)
// {line: 14520}
// push constant 110
@110
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14533}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.158
D=A
@call
0;JMP
(Main.main.call.158)
// {line: 14539}
// push constant 117
@117
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14552}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.159
D=A
@call
0;JMP
(Main.main.call.159)
// {line: 14558}
// push constant 109
@109
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14571}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.160
D=A
@call
0;JMP
(Main.main.call.160)
// {line: 14577}
// push constant 98
@98
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14590}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.161
D=A
@call
0;JMP
(Main.main.call.161)
// {line: 14596}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14609}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.162
D=A
@call
0;JMP
(Main.main.call.162)
// {line: 14615}
// push constant 114
@114
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14628}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.163
D=A
@call
0;JMP
(Main.main.call.163)
// {line: 14634}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14647}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.164
D=A
@call
0;JMP
(Main.main.call.164)
// {line: 14653}
// push constant 39
@39
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14666}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.165
D=A
@call
0;JMP
(Main.main.call.165)
// {line: 14672}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14685}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.166
D=A
@call
0;JMP
(Main.main.call.166)
// {line: 14691}
// push constant 39
@39
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14704}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.167
D=A
@call
0;JMP
(Main.main.call.167)
// {line: 14710}
// push constant 58
@58
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14723}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.168
D=A
@call
0;JMP
(Main.main.call.168)
// {line: 14729}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14742}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.169
D=A
@call
0;JMP
(Main.main.call.169)
// {line: 14755}
// call Output.printString nArgs: 1
@1
D=A
@R14
M=D
@Output.printString
D=A
@R15
M=D
@Main.main.call.170
D=A
@call
0;JMP
(Main.main.call.170)
// {line: 14760}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 14773}
// call Keyboard.readChar nArgs: 0
@0
D=A
@R14
M=D
@Keyboard.readChar
D=A
@R15
M=D
@Main.main.call.171
D=A
@call
0;JMP
(Main.main.call.171)
// {line: 14779}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 14792}
// call Output.println nArgs: 0
@0
D=A
@R14
M=D
@Output.println
D=A
@R15
M=D
@Main.main.call.172
D=A
@call
0;JMP
(Main.main.call.172)
// {line: 14797}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 14806}
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
// {line: 14812}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14819}
// eq
@Main.main.eq.3
D=A
@R14
M=D
@eq
0;JMP
(Main.main.eq.3)
// {line: 14824}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 14830}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14836}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14839}
// not
@SP
A=M-1
M=!M
// {line: 14844}
// if-goto Main.main.if.1
@SP
AM=M-1
D=M
@Main.main.if.1
D;JNE
// {line: 14850}
// push constant 2
@2
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14863}
// call String.new nArgs: 1
@1
D=A
@R14
M=D
@String.new
D=A
@R15
M=D
@Main.main.call.173
D=A
@call
0;JMP
(Main.main.call.173)
// {line: 14869}
// push constant 111
@111
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14882}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.174
D=A
@call
0;JMP
(Main.main.call.174)
// {line: 14888}
// push constant 107
@107
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14901}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.175
D=A
@call
0;JMP
(Main.main.call.175)
// {line: 14914}
// call Output.printString nArgs: 1
@1
D=A
@R14
M=D
@Output.printString
D=A
@R15
M=D
@Main.main.call.176
D=A
@call
0;JMP
(Main.main.call.176)
// {line: 14919}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 14932}
// call Output.println nArgs: 0
@0
D=A
@R14
M=D
@Output.println
D=A
@R15
M=D
@Main.main.call.177
D=A
@call
0;JMP
(Main.main.call.177)
// {line: 14937}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 14943}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14946}
// not
@SP
A=M-1
M=!M
// {line: 14956}
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
// {line: 14957}
(Main.main.if.1)
// {line: 14962}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 14964}
// goto Main.main.while.6
@Main.main.while.6
0;JMP
// {line: 14965}
(Main.main.while.7)
// {line: 14971}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14981}
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
// {line: 14987}
// push constant 14
@14
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15000}
// call String.new nArgs: 1
@1
D=A
@R14
M=D
@String.new
D=A
@R15
M=D
@Main.main.call.178
D=A
@call
0;JMP
(Main.main.call.178)
// {line: 15006}
// push constant 114
@114
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15019}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.179
D=A
@call
0;JMP
(Main.main.call.179)
// {line: 15025}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15038}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.180
D=A
@call
0;JMP
(Main.main.call.180)
// {line: 15044}
// push constant 97
@97
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15057}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.181
D=A
@call
0;JMP
(Main.main.call.181)
// {line: 15063}
// push constant 100
@100
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15076}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.182
D=A
@call
0;JMP
(Main.main.call.182)
// {line: 15082}
// push constant 76
@76
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15095}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.183
D=A
@call
0;JMP
(Main.main.call.183)
// {line: 15101}
// push constant 105
@105
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15114}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.184
D=A
@call
0;JMP
(Main.main.call.184)
// {line: 15120}
// push constant 110
@110
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15133}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.185
D=A
@call
0;JMP
(Main.main.call.185)
// {line: 15139}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15152}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.186
D=A
@call
0;JMP
(Main.main.call.186)
// {line: 15158}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15171}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.187
D=A
@call
0;JMP
(Main.main.call.187)
// {line: 15177}
// push constant 116
@116
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15190}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.188
D=A
@call
0;JMP
(Main.main.call.188)
// {line: 15196}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15209}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.189
D=A
@call
0;JMP
(Main.main.call.189)
// {line: 15215}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15228}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.190
D=A
@call
0;JMP
(Main.main.call.190)
// {line: 15234}
// push constant 116
@116
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15247}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.191
D=A
@call
0;JMP
(Main.main.call.191)
// {line: 15253}
// push constant 58
@58
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15266}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.192
D=A
@call
0;JMP
(Main.main.call.192)
// {line: 15279}
// call Output.printString nArgs: 1
@1
D=A
@R14
M=D
@Output.printString
D=A
@R15
M=D
@Main.main.call.193
D=A
@call
0;JMP
(Main.main.call.193)
// {line: 15284}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 15297}
// call Output.println nArgs: 0
@0
D=A
@R14
M=D
@Output.println
D=A
@R15
M=D
@Main.main.call.194
D=A
@call
0;JMP
(Main.main.call.194)
// {line: 15302}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 15308}
// push constant 38
@38
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15321}
// call String.new nArgs: 1
@1
D=A
@R14
M=D
@String.new
D=A
@R15
M=D
@Main.main.call.195
D=A
@call
0;JMP
(Main.main.call.195)
// {line: 15327}
// push constant 40
@40
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15340}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.196
D=A
@call
0;JMP
(Main.main.call.196)
// {line: 15346}
// push constant 86
@86
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15359}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.197
D=A
@call
0;JMP
(Main.main.call.197)
// {line: 15365}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15378}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.198
D=A
@call
0;JMP
(Main.main.call.198)
// {line: 15384}
// push constant 114
@114
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15397}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.199
D=A
@call
0;JMP
(Main.main.call.199)
// {line: 15403}
// push constant 105
@105
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15416}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.200
D=A
@call
0;JMP
(Main.main.call.200)
// {line: 15422}
// push constant 102
@102
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15435}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.201
D=A
@call
0;JMP
(Main.main.call.201)
// {line: 15441}
// push constant 121
@121
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15454}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.202
D=A
@call
0;JMP
(Main.main.call.202)
// {line: 15460}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15473}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.203
D=A
@call
0;JMP
(Main.main.call.203)
// {line: 15479}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15492}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.204
D=A
@call
0;JMP
(Main.main.call.204)
// {line: 15498}
// push constant 99
@99
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15511}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.205
D=A
@call
0;JMP
(Main.main.call.205)
// {line: 15517}
// push constant 104
@104
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15530}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.206
D=A
@call
0;JMP
(Main.main.call.206)
// {line: 15536}
// push constant 111
@111
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15549}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.207
D=A
@call
0;JMP
(Main.main.call.207)
// {line: 15555}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15568}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.208
D=A
@call
0;JMP
(Main.main.call.208)
// {line: 15574}
// push constant 97
@97
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15587}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.209
D=A
@call
0;JMP
(Main.main.call.209)
// {line: 15593}
// push constant 110
@110
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15606}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.210
D=A
@call
0;JMP
(Main.main.call.210)
// {line: 15612}
// push constant 100
@100
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15625}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.211
D=A
@call
0;JMP
(Main.main.call.211)
// {line: 15631}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15644}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.212
D=A
@call
0;JMP
(Main.main.call.212)
// {line: 15650}
// push constant 117
@117
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15663}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.213
D=A
@call
0;JMP
(Main.main.call.213)
// {line: 15669}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15682}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.214
D=A
@call
0;JMP
(Main.main.call.214)
// {line: 15688}
// push constant 97
@97
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15701}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.215
D=A
@call
0;JMP
(Main.main.call.215)
// {line: 15707}
// push constant 103
@103
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15720}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.216
D=A
@call
0;JMP
(Main.main.call.216)
// {line: 15726}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15739}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.217
D=A
@call
0;JMP
(Main.main.call.217)
// {line: 15745}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15758}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.218
D=A
@call
0;JMP
(Main.main.call.218)
// {line: 15764}
// push constant 111
@111
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15777}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.219
D=A
@call
0;JMP
(Main.main.call.219)
// {line: 15783}
// push constant 102
@102
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15796}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.220
D=A
@call
0;JMP
(Main.main.call.220)
// {line: 15802}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15815}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.221
D=A
@call
0;JMP
(Main.main.call.221)
// {line: 15821}
// push constant 39
@39
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15834}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.222
D=A
@call
0;JMP
(Main.main.call.222)
// {line: 15840}
// push constant 98
@98
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15853}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.223
D=A
@call
0;JMP
(Main.main.call.223)
// {line: 15859}
// push constant 97
@97
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15872}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.224
D=A
@call
0;JMP
(Main.main.call.224)
// {line: 15878}
// push constant 99
@99
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15891}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.225
D=A
@call
0;JMP
(Main.main.call.225)
// {line: 15897}
// push constant 107
@107
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15910}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.226
D=A
@call
0;JMP
(Main.main.call.226)
// {line: 15916}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15929}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.227
D=A
@call
0;JMP
(Main.main.call.227)
// {line: 15935}
// push constant 112
@112
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15948}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.228
D=A
@call
0;JMP
(Main.main.call.228)
// {line: 15954}
// push constant 97
@97
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15967}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.229
D=A
@call
0;JMP
(Main.main.call.229)
// {line: 15973}
// push constant 99
@99
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15986}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.230
D=A
@call
0;JMP
(Main.main.call.230)
// {line: 15992}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16005}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.231
D=A
@call
0;JMP
(Main.main.call.231)
// {line: 16011}
// push constant 39
@39
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16024}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.232
D=A
@call
0;JMP
(Main.main.call.232)
// {line: 16030}
// push constant 41
@41
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16043}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.233
D=A
@call
0;JMP
(Main.main.call.233)
// {line: 16056}
// call Output.printString nArgs: 1
@1
D=A
@R14
M=D
@Output.printString
D=A
@R15
M=D
@Main.main.call.234
D=A
@call
0;JMP
(Main.main.call.234)
// {line: 16061}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 16074}
// call Output.println nArgs: 0
@0
D=A
@R14
M=D
@Output.println
D=A
@R15
M=D
@Main.main.call.235
D=A
@call
0;JMP
(Main.main.call.235)
// {line: 16079}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 16080}
(Main.main.while.8)
// {line: 16089}
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
// {line: 16092}
// not
@SP
A=M-1
M=!M
// {line: 16095}
// not
@SP
A=M-1
M=!M
// {line: 16100}
// if-goto Main.main.while.9
@SP
AM=M-1
D=M
@Main.main.while.9
D;JNE
// {line: 16106}
// push constant 36
@36
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16119}
// call String.new nArgs: 1
@1
D=A
@R14
M=D
@String.new
D=A
@R15
M=D
@Main.main.call.236
D=A
@call
0;JMP
(Main.main.call.236)
// {line: 16125}
// push constant 80
@80
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16138}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.237
D=A
@call
0;JMP
(Main.main.call.237)
// {line: 16144}
// push constant 108
@108
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16157}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.238
D=A
@call
0;JMP
(Main.main.call.238)
// {line: 16163}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16176}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.239
D=A
@call
0;JMP
(Main.main.call.239)
// {line: 16182}
// push constant 97
@97
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16195}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.240
D=A
@call
0;JMP
(Main.main.call.240)
// {line: 16201}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16214}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.241
D=A
@call
0;JMP
(Main.main.call.241)
// {line: 16220}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16233}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.242
D=A
@call
0;JMP
(Main.main.call.242)
// {line: 16239}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16252}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.243
D=A
@call
0;JMP
(Main.main.call.243)
// {line: 16258}
// push constant 116
@116
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16271}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.244
D=A
@call
0;JMP
(Main.main.call.244)
// {line: 16277}
// push constant 121
@121
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16290}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.245
D=A
@call
0;JMP
(Main.main.call.245)
// {line: 16296}
// push constant 112
@112
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16309}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.246
D=A
@call
0;JMP
(Main.main.call.246)
// {line: 16315}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16328}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.247
D=A
@call
0;JMP
(Main.main.call.247)
// {line: 16334}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16347}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.248
D=A
@call
0;JMP
(Main.main.call.248)
// {line: 16353}
// push constant 39
@39
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16366}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.249
D=A
@call
0;JMP
(Main.main.call.249)
// {line: 16372}
// push constant 74
@74
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16385}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.250
D=A
@call
0;JMP
(Main.main.call.250)
// {line: 16391}
// push constant 65
@65
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16404}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.251
D=A
@call
0;JMP
(Main.main.call.251)
// {line: 16410}
// push constant 67
@67
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16423}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.252
D=A
@call
0;JMP
(Main.main.call.252)
// {line: 16429}
// push constant 75
@75
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16442}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.253
D=A
@call
0;JMP
(Main.main.call.253)
// {line: 16448}
// push constant 39
@39
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16461}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.254
D=A
@call
0;JMP
(Main.main.call.254)
// {line: 16467}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16480}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.255
D=A
@call
0;JMP
(Main.main.call.255)
// {line: 16486}
// push constant 97
@97
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16499}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.256
D=A
@call
0;JMP
(Main.main.call.256)
// {line: 16505}
// push constant 110
@110
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16518}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.257
D=A
@call
0;JMP
(Main.main.call.257)
// {line: 16524}
// push constant 100
@100
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16537}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.258
D=A
@call
0;JMP
(Main.main.call.258)
// {line: 16543}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16556}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.259
D=A
@call
0;JMP
(Main.main.call.259)
// {line: 16562}
// push constant 112
@112
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16575}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.260
D=A
@call
0;JMP
(Main.main.call.260)
// {line: 16581}
// push constant 114
@114
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16594}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.261
D=A
@call
0;JMP
(Main.main.call.261)
// {line: 16600}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16613}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.262
D=A
@call
0;JMP
(Main.main.call.262)
// {line: 16619}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16632}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.263
D=A
@call
0;JMP
(Main.main.call.263)
// {line: 16638}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16651}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.264
D=A
@call
0;JMP
(Main.main.call.264)
// {line: 16657}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16670}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.265
D=A
@call
0;JMP
(Main.main.call.265)
// {line: 16676}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16689}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.266
D=A
@call
0;JMP
(Main.main.call.266)
// {line: 16695}
// push constant 110
@110
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16708}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.267
D=A
@call
0;JMP
(Main.main.call.267)
// {line: 16714}
// push constant 116
@116
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16727}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.268
D=A
@call
0;JMP
(Main.main.call.268)
// {line: 16733}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16746}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.269
D=A
@call
0;JMP
(Main.main.call.269)
// {line: 16752}
// push constant 114
@114
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16765}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.270
D=A
@call
0;JMP
(Main.main.call.270)
// {line: 16771}
// push constant 58
@58
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16784}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.271
D=A
@call
0;JMP
(Main.main.call.271)
// {line: 16790}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16803}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.272
D=A
@call
0;JMP
(Main.main.call.272)
// {line: 16816}
// call Keyboard.readLine nArgs: 1
@1
D=A
@R14
M=D
@Keyboard.readLine
D=A
@R15
M=D
@Main.main.call.273
D=A
@call
0;JMP
(Main.main.call.273)
// {line: 16824}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 16837}
// call Output.println nArgs: 0
@0
D=A
@R14
M=D
@Output.println
D=A
@R15
M=D
@Main.main.call.274
D=A
@call
0;JMP
(Main.main.call.274)
// {line: 16842}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 16851}
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
// {line: 16864}
// call String.length nArgs: 1
@1
D=A
@R14
M=D
@String.length
D=A
@R15
M=D
@Main.main.call.275
D=A
@call
0;JMP
(Main.main.call.275)
// {line: 16870}
// push constant 4
@4
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16877}
// eq
@Main.main.eq.4
D=A
@R14
M=D
@eq
0;JMP
(Main.main.eq.4)
// {line: 16882}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 16888}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16894}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16897}
// not
@SP
A=M-1
M=!M
// {line: 16902}
// if-goto Main.main.if.2
@SP
AM=M-1
D=M
@Main.main.if.2
D;JNE
// {line: 16911}
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
// {line: 16917}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16930}
// call String.charAt nArgs: 2
@2
D=A
@R14
M=D
@String.charAt
D=A
@R15
M=D
@Main.main.call.276
D=A
@call
0;JMP
(Main.main.call.276)
// {line: 16936}
// push constant 74
@74
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16943}
// eq
@Main.main.eq.5
D=A
@R14
M=D
@eq
0;JMP
(Main.main.eq.5)
// {line: 16952}
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
// {line: 16958}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16971}
// call String.charAt nArgs: 2
@2
D=A
@R14
M=D
@String.charAt
D=A
@R15
M=D
@Main.main.call.277
D=A
@call
0;JMP
(Main.main.call.277)
// {line: 16977}
// push constant 65
@65
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16984}
// eq
@Main.main.eq.6
D=A
@R14
M=D
@eq
0;JMP
(Main.main.eq.6)
// {line: 16989}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 16998}
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
// {line: 17004}
// push constant 2
@2
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17017}
// call String.charAt nArgs: 2
@2
D=A
@R14
M=D
@String.charAt
D=A
@R15
M=D
@Main.main.call.278
D=A
@call
0;JMP
(Main.main.call.278)
// {line: 17023}
// push constant 67
@67
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17030}
// eq
@Main.main.eq.7
D=A
@R14
M=D
@eq
0;JMP
(Main.main.eq.7)
// {line: 17035}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 17044}
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
// {line: 17050}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17063}
// call String.charAt nArgs: 2
@2
D=A
@R14
M=D
@String.charAt
D=A
@R15
M=D
@Main.main.call.279
D=A
@call
0;JMP
(Main.main.call.279)
// {line: 17069}
// push constant 75
@75
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17076}
// eq
@Main.main.eq.8
D=A
@R14
M=D
@eq
0;JMP
(Main.main.eq.8)
// {line: 17081}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 17086}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 17092}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17098}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17101}
// not
@SP
A=M-1
M=!M
// {line: 17106}
// if-goto Main.main.if.3
@SP
AM=M-1
D=M
@Main.main.if.3
D;JNE
// {line: 17112}
// push constant 2
@2
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17125}
// call String.new nArgs: 1
@1
D=A
@R14
M=D
@String.new
D=A
@R15
M=D
@Main.main.call.280
D=A
@call
0;JMP
(Main.main.call.280)
// {line: 17131}
// push constant 111
@111
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17144}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.281
D=A
@call
0;JMP
(Main.main.call.281)
// {line: 17150}
// push constant 107
@107
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17163}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.282
D=A
@call
0;JMP
(Main.main.call.282)
// {line: 17176}
// call Output.printString nArgs: 1
@1
D=A
@R14
M=D
@Output.printString
D=A
@R15
M=D
@Main.main.call.283
D=A
@call
0;JMP
(Main.main.call.283)
// {line: 17181}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 17194}
// call Output.println nArgs: 0
@0
D=A
@R14
M=D
@Output.println
D=A
@R15
M=D
@Main.main.call.284
D=A
@call
0;JMP
(Main.main.call.284)
// {line: 17199}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 17205}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17208}
// not
@SP
A=M-1
M=!M
// {line: 17218}
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
// {line: 17219}
(Main.main.if.3)
// {line: 17224}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 17225}
(Main.main.if.2)
// {line: 17230}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 17232}
// goto Main.main.while.8
@Main.main.while.8
0;JMP
// {line: 17233}
(Main.main.while.9)
// {line: 17239}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17249}
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
// {line: 17255}
// push constant 13
@13
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17268}
// call String.new nArgs: 1
@1
D=A
@R14
M=D
@String.new
D=A
@R15
M=D
@Main.main.call.285
D=A
@call
0;JMP
(Main.main.call.285)
// {line: 17274}
// push constant 114
@114
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17287}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.286
D=A
@call
0;JMP
(Main.main.call.286)
// {line: 17293}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17306}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.287
D=A
@call
0;JMP
(Main.main.call.287)
// {line: 17312}
// push constant 97
@97
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17325}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.288
D=A
@call
0;JMP
(Main.main.call.288)
// {line: 17331}
// push constant 100
@100
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17344}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.289
D=A
@call
0;JMP
(Main.main.call.289)
// {line: 17350}
// push constant 73
@73
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17363}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.290
D=A
@call
0;JMP
(Main.main.call.290)
// {line: 17369}
// push constant 110
@110
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17382}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.291
D=A
@call
0;JMP
(Main.main.call.291)
// {line: 17388}
// push constant 116
@116
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17401}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.292
D=A
@call
0;JMP
(Main.main.call.292)
// {line: 17407}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17420}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.293
D=A
@call
0;JMP
(Main.main.call.293)
// {line: 17426}
// push constant 116
@116
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17439}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.294
D=A
@call
0;JMP
(Main.main.call.294)
// {line: 17445}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17458}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.295
D=A
@call
0;JMP
(Main.main.call.295)
// {line: 17464}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17477}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.296
D=A
@call
0;JMP
(Main.main.call.296)
// {line: 17483}
// push constant 116
@116
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17496}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.297
D=A
@call
0;JMP
(Main.main.call.297)
// {line: 17502}
// push constant 58
@58
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17515}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.298
D=A
@call
0;JMP
(Main.main.call.298)
// {line: 17528}
// call Output.printString nArgs: 1
@1
D=A
@R14
M=D
@Output.printString
D=A
@R15
M=D
@Main.main.call.299
D=A
@call
0;JMP
(Main.main.call.299)
// {line: 17533}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 17546}
// call Output.println nArgs: 0
@0
D=A
@R14
M=D
@Output.println
D=A
@R15
M=D
@Main.main.call.300
D=A
@call
0;JMP
(Main.main.call.300)
// {line: 17551}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 17557}
// push constant 38
@38
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17570}
// call String.new nArgs: 1
@1
D=A
@R14
M=D
@String.new
D=A
@R15
M=D
@Main.main.call.301
D=A
@call
0;JMP
(Main.main.call.301)
// {line: 17576}
// push constant 40
@40
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17589}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.302
D=A
@call
0;JMP
(Main.main.call.302)
// {line: 17595}
// push constant 86
@86
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17608}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.303
D=A
@call
0;JMP
(Main.main.call.303)
// {line: 17614}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17627}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.304
D=A
@call
0;JMP
(Main.main.call.304)
// {line: 17633}
// push constant 114
@114
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17646}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.305
D=A
@call
0;JMP
(Main.main.call.305)
// {line: 17652}
// push constant 105
@105
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17665}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.306
D=A
@call
0;JMP
(Main.main.call.306)
// {line: 17671}
// push constant 102
@102
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17684}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.307
D=A
@call
0;JMP
(Main.main.call.307)
// {line: 17690}
// push constant 121
@121
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17703}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.308
D=A
@call
0;JMP
(Main.main.call.308)
// {line: 17709}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17722}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.309
D=A
@call
0;JMP
(Main.main.call.309)
// {line: 17728}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17741}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.310
D=A
@call
0;JMP
(Main.main.call.310)
// {line: 17747}
// push constant 99
@99
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17760}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.311
D=A
@call
0;JMP
(Main.main.call.311)
// {line: 17766}
// push constant 104
@104
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17779}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.312
D=A
@call
0;JMP
(Main.main.call.312)
// {line: 17785}
// push constant 111
@111
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17798}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.313
D=A
@call
0;JMP
(Main.main.call.313)
// {line: 17804}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17817}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.314
D=A
@call
0;JMP
(Main.main.call.314)
// {line: 17823}
// push constant 97
@97
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17836}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.315
D=A
@call
0;JMP
(Main.main.call.315)
// {line: 17842}
// push constant 110
@110
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17855}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.316
D=A
@call
0;JMP
(Main.main.call.316)
// {line: 17861}
// push constant 100
@100
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17874}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.317
D=A
@call
0;JMP
(Main.main.call.317)
// {line: 17880}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17893}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.318
D=A
@call
0;JMP
(Main.main.call.318)
// {line: 17899}
// push constant 117
@117
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17912}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.319
D=A
@call
0;JMP
(Main.main.call.319)
// {line: 17918}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17931}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.320
D=A
@call
0;JMP
(Main.main.call.320)
// {line: 17937}
// push constant 97
@97
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17950}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.321
D=A
@call
0;JMP
(Main.main.call.321)
// {line: 17956}
// push constant 103
@103
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17969}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.322
D=A
@call
0;JMP
(Main.main.call.322)
// {line: 17975}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17988}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.323
D=A
@call
0;JMP
(Main.main.call.323)
// {line: 17994}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18007}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.324
D=A
@call
0;JMP
(Main.main.call.324)
// {line: 18013}
// push constant 111
@111
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18026}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.325
D=A
@call
0;JMP
(Main.main.call.325)
// {line: 18032}
// push constant 102
@102
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18045}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.326
D=A
@call
0;JMP
(Main.main.call.326)
// {line: 18051}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18064}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.327
D=A
@call
0;JMP
(Main.main.call.327)
// {line: 18070}
// push constant 39
@39
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18083}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.328
D=A
@call
0;JMP
(Main.main.call.328)
// {line: 18089}
// push constant 98
@98
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18102}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.329
D=A
@call
0;JMP
(Main.main.call.329)
// {line: 18108}
// push constant 97
@97
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18121}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.330
D=A
@call
0;JMP
(Main.main.call.330)
// {line: 18127}
// push constant 99
@99
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18140}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.331
D=A
@call
0;JMP
(Main.main.call.331)
// {line: 18146}
// push constant 107
@107
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18159}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.332
D=A
@call
0;JMP
(Main.main.call.332)
// {line: 18165}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18178}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.333
D=A
@call
0;JMP
(Main.main.call.333)
// {line: 18184}
// push constant 112
@112
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18197}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.334
D=A
@call
0;JMP
(Main.main.call.334)
// {line: 18203}
// push constant 97
@97
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18216}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.335
D=A
@call
0;JMP
(Main.main.call.335)
// {line: 18222}
// push constant 99
@99
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18235}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.336
D=A
@call
0;JMP
(Main.main.call.336)
// {line: 18241}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18254}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.337
D=A
@call
0;JMP
(Main.main.call.337)
// {line: 18260}
// push constant 39
@39
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18273}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.338
D=A
@call
0;JMP
(Main.main.call.338)
// {line: 18279}
// push constant 41
@41
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18292}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.339
D=A
@call
0;JMP
(Main.main.call.339)
// {line: 18305}
// call Output.printString nArgs: 1
@1
D=A
@R14
M=D
@Output.printString
D=A
@R15
M=D
@Main.main.call.340
D=A
@call
0;JMP
(Main.main.call.340)
// {line: 18310}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 18323}
// call Output.println nArgs: 0
@0
D=A
@R14
M=D
@Output.println
D=A
@R15
M=D
@Main.main.call.341
D=A
@call
0;JMP
(Main.main.call.341)
// {line: 18328}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 18329}
(Main.main.while.10)
// {line: 18338}
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
// {line: 18341}
// not
@SP
A=M-1
M=!M
// {line: 18344}
// not
@SP
A=M-1
M=!M
// {line: 18349}
// if-goto Main.main.while.11
@SP
AM=M-1
D=M
@Main.main.while.11
D;JNE
// {line: 18355}
// push constant 38
@38
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18368}
// call String.new nArgs: 1
@1
D=A
@R14
M=D
@String.new
D=A
@R15
M=D
@Main.main.call.342
D=A
@call
0;JMP
(Main.main.call.342)
// {line: 18374}
// push constant 80
@80
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18387}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.343
D=A
@call
0;JMP
(Main.main.call.343)
// {line: 18393}
// push constant 108
@108
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18406}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.344
D=A
@call
0;JMP
(Main.main.call.344)
// {line: 18412}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18425}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.345
D=A
@call
0;JMP
(Main.main.call.345)
// {line: 18431}
// push constant 97
@97
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18444}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.346
D=A
@call
0;JMP
(Main.main.call.346)
// {line: 18450}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18463}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.347
D=A
@call
0;JMP
(Main.main.call.347)
// {line: 18469}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18482}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.348
D=A
@call
0;JMP
(Main.main.call.348)
// {line: 18488}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18501}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.349
D=A
@call
0;JMP
(Main.main.call.349)
// {line: 18507}
// push constant 116
@116
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18520}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.350
D=A
@call
0;JMP
(Main.main.call.350)
// {line: 18526}
// push constant 121
@121
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18539}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.351
D=A
@call
0;JMP
(Main.main.call.351)
// {line: 18545}
// push constant 112
@112
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18558}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.352
D=A
@call
0;JMP
(Main.main.call.352)
// {line: 18564}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18577}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.353
D=A
@call
0;JMP
(Main.main.call.353)
// {line: 18583}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18596}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.354
D=A
@call
0;JMP
(Main.main.call.354)
// {line: 18602}
// push constant 39
@39
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18615}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.355
D=A
@call
0;JMP
(Main.main.call.355)
// {line: 18621}
// push constant 45
@45
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18634}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.356
D=A
@call
0;JMP
(Main.main.call.356)
// {line: 18640}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18653}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.357
D=A
@call
0;JMP
(Main.main.call.357)
// {line: 18659}
// push constant 50
@50
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18672}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.358
D=A
@call
0;JMP
(Main.main.call.358)
// {line: 18678}
// push constant 49
@49
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18691}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.359
D=A
@call
0;JMP
(Main.main.call.359)
// {line: 18697}
// push constant 50
@50
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18710}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.360
D=A
@call
0;JMP
(Main.main.call.360)
// {line: 18716}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18729}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.361
D=A
@call
0;JMP
(Main.main.call.361)
// {line: 18735}
// push constant 39
@39
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18748}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.362
D=A
@call
0;JMP
(Main.main.call.362)
// {line: 18754}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18767}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.363
D=A
@call
0;JMP
(Main.main.call.363)
// {line: 18773}
// push constant 97
@97
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18786}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.364
D=A
@call
0;JMP
(Main.main.call.364)
// {line: 18792}
// push constant 110
@110
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18805}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.365
D=A
@call
0;JMP
(Main.main.call.365)
// {line: 18811}
// push constant 100
@100
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18824}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.366
D=A
@call
0;JMP
(Main.main.call.366)
// {line: 18830}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18843}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.367
D=A
@call
0;JMP
(Main.main.call.367)
// {line: 18849}
// push constant 112
@112
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18862}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.368
D=A
@call
0;JMP
(Main.main.call.368)
// {line: 18868}
// push constant 114
@114
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18881}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.369
D=A
@call
0;JMP
(Main.main.call.369)
// {line: 18887}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18900}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.370
D=A
@call
0;JMP
(Main.main.call.370)
// {line: 18906}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18919}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.371
D=A
@call
0;JMP
(Main.main.call.371)
// {line: 18925}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18938}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.372
D=A
@call
0;JMP
(Main.main.call.372)
// {line: 18944}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18957}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.373
D=A
@call
0;JMP
(Main.main.call.373)
// {line: 18963}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18976}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.374
D=A
@call
0;JMP
(Main.main.call.374)
// {line: 18982}
// push constant 110
@110
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18995}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.375
D=A
@call
0;JMP
(Main.main.call.375)
// {line: 19001}
// push constant 116
@116
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19014}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.376
D=A
@call
0;JMP
(Main.main.call.376)
// {line: 19020}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19033}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.377
D=A
@call
0;JMP
(Main.main.call.377)
// {line: 19039}
// push constant 114
@114
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19052}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.378
D=A
@call
0;JMP
(Main.main.call.378)
// {line: 19058}
// push constant 58
@58
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19071}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.379
D=A
@call
0;JMP
(Main.main.call.379)
// {line: 19077}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19090}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.380
D=A
@call
0;JMP
(Main.main.call.380)
// {line: 19103}
// call Keyboard.readInt nArgs: 1
@1
D=A
@R14
M=D
@Keyboard.readInt
D=A
@R15
M=D
@Main.main.call.381
D=A
@call
0;JMP
(Main.main.call.381)
// {line: 19112}
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
// {line: 19125}
// call Output.println nArgs: 0
@0
D=A
@R14
M=D
@Output.println
D=A
@R15
M=D
@Main.main.call.382
D=A
@call
0;JMP
(Main.main.call.382)
// {line: 19130}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 19139}
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
// {line: 19145}
// push constant 32123
@32123
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19148}
// neg
@SP
A=M-1
M=-M
// {line: 19155}
// eq
@Main.main.eq.9
D=A
@R14
M=D
@eq
0;JMP
(Main.main.eq.9)
// {line: 19160}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 19166}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 19172}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 19175}
// not
@SP
A=M-1
M=!M
// {line: 19180}
// if-goto Main.main.if.4
@SP
AM=M-1
D=M
@Main.main.if.4
D;JNE
// {line: 19186}
// push constant 2
@2
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19199}
// call String.new nArgs: 1
@1
D=A
@R14
M=D
@String.new
D=A
@R15
M=D
@Main.main.call.383
D=A
@call
0;JMP
(Main.main.call.383)
// {line: 19205}
// push constant 111
@111
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19218}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.384
D=A
@call
0;JMP
(Main.main.call.384)
// {line: 19224}
// push constant 107
@107
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19237}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.385
D=A
@call
0;JMP
(Main.main.call.385)
// {line: 19250}
// call Output.printString nArgs: 1
@1
D=A
@R14
M=D
@Output.printString
D=A
@R15
M=D
@Main.main.call.386
D=A
@call
0;JMP
(Main.main.call.386)
// {line: 19255}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 19268}
// call Output.println nArgs: 0
@0
D=A
@R14
M=D
@Output.println
D=A
@R15
M=D
@Main.main.call.387
D=A
@call
0;JMP
(Main.main.call.387)
// {line: 19273}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 19279}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19282}
// not
@SP
A=M-1
M=!M
// {line: 19292}
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
// {line: 19293}
(Main.main.if.4)
// {line: 19298}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 19300}
// goto Main.main.while.10
@Main.main.while.10
0;JMP
// {line: 19301}
(Main.main.while.11)
// {line: 19314}
// call Output.println nArgs: 0
@0
D=A
@R14
M=D
@Output.println
D=A
@R15
M=D
@Main.main.call.388
D=A
@call
0;JMP
(Main.main.call.388)
// {line: 19319}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 19325}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19338}
// call String.new nArgs: 1
@1
D=A
@R14
M=D
@String.new
D=A
@R15
M=D
@Main.main.call.389
D=A
@call
0;JMP
(Main.main.call.389)
// {line: 19344}
// push constant 84
@84
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19357}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.390
D=A
@call
0;JMP
(Main.main.call.390)
// {line: 19363}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19376}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.391
D=A
@call
0;JMP
(Main.main.call.391)
// {line: 19382}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19395}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.392
D=A
@call
0;JMP
(Main.main.call.392)
// {line: 19401}
// push constant 116
@116
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19414}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.393
D=A
@call
0;JMP
(Main.main.call.393)
// {line: 19420}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19433}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.394
D=A
@call
0;JMP
(Main.main.call.394)
// {line: 19439}
// push constant 99
@99
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19452}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.395
D=A
@call
0;JMP
(Main.main.call.395)
// {line: 19458}
// push constant 111
@111
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19471}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.396
D=A
@call
0;JMP
(Main.main.call.396)
// {line: 19477}
// push constant 109
@109
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19490}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.397
D=A
@call
0;JMP
(Main.main.call.397)
// {line: 19496}
// push constant 112
@112
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19509}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.398
D=A
@call
0;JMP
(Main.main.call.398)
// {line: 19515}
// push constant 108
@108
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19528}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.399
D=A
@call
0;JMP
(Main.main.call.399)
// {line: 19534}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19547}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.400
D=A
@call
0;JMP
(Main.main.call.400)
// {line: 19553}
// push constant 116
@116
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19566}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.401
D=A
@call
0;JMP
(Main.main.call.401)
// {line: 19572}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19585}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.402
D=A
@call
0;JMP
(Main.main.call.402)
// {line: 19591}
// push constant 100
@100
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19604}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.403
D=A
@call
0;JMP
(Main.main.call.403)
// {line: 19610}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19623}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.404
D=A
@call
0;JMP
(Main.main.call.404)
// {line: 19629}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19642}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.405
D=A
@call
0;JMP
(Main.main.call.405)
// {line: 19648}
// push constant 117
@117
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19661}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.406
D=A
@call
0;JMP
(Main.main.call.406)
// {line: 19667}
// push constant 99
@99
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19680}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.407
D=A
@call
0;JMP
(Main.main.call.407)
// {line: 19686}
// push constant 99
@99
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19699}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.408
D=A
@call
0;JMP
(Main.main.call.408)
// {line: 19705}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19718}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.409
D=A
@call
0;JMP
(Main.main.call.409)
// {line: 19724}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19737}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.410
D=A
@call
0;JMP
(Main.main.call.410)
// {line: 19743}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19756}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.411
D=A
@call
0;JMP
(Main.main.call.411)
// {line: 19762}
// push constant 102
@102
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19775}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.412
D=A
@call
0;JMP
(Main.main.call.412)
// {line: 19781}
// push constant 117
@117
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19794}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.413
D=A
@call
0;JMP
(Main.main.call.413)
// {line: 19800}
// push constant 108
@108
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19813}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.414
D=A
@call
0;JMP
(Main.main.call.414)
// {line: 19819}
// push constant 108
@108
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19832}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.415
D=A
@call
0;JMP
(Main.main.call.415)
// {line: 19838}
// push constant 121
@121
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19851}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.416
D=A
@call
0;JMP
(Main.main.call.416)
// {line: 19864}
// call Output.printString nArgs: 1
@1
D=A
@R14
M=D
@Output.printString
D=A
@R15
M=D
@Main.main.call.417
D=A
@call
0;JMP
(Main.main.call.417)
// {line: 19869}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 19875}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19877}
// return
@return
0;JMP
// {line: 19882}
// function Array.new nLocals: 1
(Array.new)
@SP
AM=M+1
A=A-1
M=0
// {line: 19891}
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
// {line: 19904}
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
// {line: 19910}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 19919}
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
// {line: 19921}
// return
@return
0;JMP
// {line: 19926}
// function Array.dispose nLocals: 1
(Array.dispose)
@SP
AM=M+1
A=A-1
M=0
// {line: 19935}
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
// {line: 19940}
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// {line: 19946}
// push pointer 0
@3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 19959}
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
// {line: 19964}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 19966}
// return
@return
0;JMP
// {line: 19971}
// function Memory.init nLocals: 1
(Memory.init)
@SP
AM=M+1
A=A-1
M=0
// {line: 19977}
// push constant 2048
@2048
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19982}
// pop static 0
@SP
AM=M-1
D=M
@Memory.static.0
M=D
// {line: 19988}
// push constant 16382
@16382
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19993}
// pop static 1
@SP
AM=M-1
D=M
@Memory.static.1
M=D
// {line: 19999}
// push constant 16383
@16383
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20004}
// pop static 3
@SP
AM=M-1
D=M
@Memory.static.3
M=D
// {line: 20010}
// push static 0
@Memory.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20015}
// pop static 2
@SP
AM=M-1
D=M
@Memory.static.2
M=D
// {line: 20021}
// push static 0
@Memory.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20027}
// push static 1
@Memory.static.1
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20033}
// push static 0
@Memory.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20038}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 20044}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20049}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 20062}
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
// {line: 20067}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 20073}
// push static 0
@Memory.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20079}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20084}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 20090}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20103}
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
// {line: 20108}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 20110}
// return
@return
0;JMP
// {line: 20115}
// function Memory.peek nLocals: 1
(Memory.peek)
@SP
AM=M+1
A=A-1
M=0
// {line: 20121}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20127}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 20133}
// push pointer 1
@4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20142}
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
// {line: 20151}
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
// {line: 20156}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 20161}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 20170}
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
// {line: 20175}
// pop temp 2
@SP
AM=M-1
D=M
@R7
M=D
// {line: 20180}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 20186}
// push temp 2
@7
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20188}
// return
@return
0;JMP
// {line: 20193}
// function Memory.poke nLocals: 1
(Memory.poke)
@SP
AM=M+1
A=A-1
M=0
// {line: 20199}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20205}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 20214}
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
// {line: 20223}
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
// {line: 20228}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 20233}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 20242}
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
// {line: 20248}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 20250}
// return
@return
0;JMP
// {line: 20271}
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
// {line: 20280}
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
// {line: 20286}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20293}
// lt
@Memory.alloc.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Memory.alloc.lt.0)
// {line: 20302}
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
// {line: 20308}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20315}
// eq
@Memory.alloc.eq.0
D=A
@R14
M=D
@eq
0;JMP
(Memory.alloc.eq.0)
// {line: 20320}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 20325}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 20331}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20337}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20340}
// not
@SP
A=M-1
M=!M
// {line: 20345}
// if-goto Memory.alloc.if.0
@SP
AM=M-1
D=M
@Memory.alloc.if.0
D;JNE
// {line: 20351}
// push static 3
@Memory.static.3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20353}
// return
@return
0;JMP
// {line: 20354}
(Memory.alloc.if.0)
// {line: 20359}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 20365}
// push static 2
@Memory.static.2
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20372}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 20381}
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
// {line: 20387}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 20393}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20403}
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
// {line: 20404}
(Memory.alloc.while.0)
// {line: 20413}
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
// {line: 20419}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20426}
// eq
@Memory.alloc.eq.1
D=A
@R14
M=D
@eq
0;JMP
(Memory.alloc.eq.1)
// {line: 20429}
// not
@SP
A=M-1
M=!M
// {line: 20432}
// not
@SP
A=M-1
M=!M
// {line: 20437}
// if-goto Memory.alloc.while.1
@SP
AM=M-1
D=M
@Memory.alloc.while.1
D;JNE
// {line: 20446}
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
// {line: 20459}
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
// {line: 20467}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 20476}
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
// {line: 20485}
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
// {line: 20492}
// eq
@Memory.alloc.eq.2
D=A
@R14
M=D
@eq
0;JMP
(Memory.alloc.eq.2)
// {line: 20497}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 20503}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20509}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20512}
// not
@SP
A=M-1
M=!M
// {line: 20517}
// if-goto Memory.alloc.if.1
@SP
AM=M-1
D=M
@Memory.alloc.if.1
D;JNE
// {line: 20526}
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
// {line: 20532}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20537}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 20546}
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
// {line: 20552}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20557}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 20570}
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
// {line: 20575}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 20584}
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
// {line: 20586}
// return
@return
0;JMP
// {line: 20587}
(Memory.alloc.if.1)
// {line: 20592}
// if-goto Memory.alloc.goto.0
@SP
AM=M-1
D=M
@Memory.alloc.goto.0
D;JNE
// {line: 20601}
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
// {line: 20610}
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
// {line: 20617}
// gt
@Memory.alloc.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Memory.alloc.gt.0)
// {line: 20622}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 20628}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20634}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20637}
// not
@SP
A=M-1
M=!M
// {line: 20642}
// if-goto Memory.alloc.if.2
@SP
AM=M-1
D=M
@Memory.alloc.if.2
D;JNE
// {line: 20651}
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
// {line: 20660}
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
// {line: 20665}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 20671}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20676}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 20685}
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
// {line: 20690}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 20699}
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
// {line: 20708}
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
// {line: 20717}
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
// {line: 20730}
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
// {line: 20735}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 20744}
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
// {line: 20753}
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
// {line: 20762}
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
// {line: 20767}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 20773}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20778}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 20791}
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
// {line: 20796}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 20805}
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
// {line: 20811}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20816}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 20818}
// return
@return
0;JMP
// {line: 20819}
(Memory.alloc.if.2)
// {line: 20824}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 20825}
(Memory.alloc.goto.0)
// {line: 20834}
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
// {line: 20840}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 20849}
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
// {line: 20855}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20860}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 20873}
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
// {line: 20880}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 20889}
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
// {line: 20895}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20900}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 20910}
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
// {line: 20912}
// goto Memory.alloc.while.0
@Memory.alloc.while.0
0;JMP
// {line: 20913}
(Memory.alloc.while.1)
// {line: 20926}
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
// {line: 20931}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 20933}
// return
@return
0;JMP
// {line: 20934}
// function Memory.defrag nLocals: 0
(Memory.defrag)
// {line: 20940}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20953}
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
// {line: 20958}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 20960}
// return
@return
0;JMP
// {line: 20965}
// function Memory.deAlloc nLocals: 1
(Memory.deAlloc)
@SP
AM=M+1
A=A-1
M=0
// {line: 20974}
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
// {line: 20980}
// push static 3
@Memory.static.3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20987}
// eq
@Memory.deAlloc.eq.0
D=A
@R14
M=D
@eq
0;JMP
(Memory.deAlloc.eq.0)
// {line: 20992}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 20998}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21004}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21007}
// not
@SP
A=M-1
M=!M
// {line: 21012}
// if-goto Memory.deAlloc.if.0
@SP
AM=M-1
D=M
@Memory.deAlloc.if.0
D;JNE
// {line: 21018}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 21020}
// return
@return
0;JMP
// {line: 21021}
(Memory.deAlloc.if.0)
// {line: 21026}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 21035}
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
// {line: 21041}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 21050}
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
// {line: 21056}
// push static 2
@Memory.static.2
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21062}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 21067}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 21080}
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
// {line: 21093}
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
// {line: 21098}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 21104}
// push static 2
@Memory.static.2
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21110}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 21115}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 21124}
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
// {line: 21137}
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
// {line: 21142}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 21144}
// return
@return
0;JMP
// {line: 21145}
// function Memory.isValid nLocals: 0
(Memory.isValid)
// {line: 21154}
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
// {line: 21160}
// push static 0
@Memory.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21167}
// gt
@Memory.isValid.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Memory.isValid.gt.0)
// {line: 21176}
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
// {line: 21182}
// push static 0
@Memory.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21189}
// eq
@Memory.isValid.eq.0
D=A
@R14
M=D
@eq
0;JMP
(Memory.isValid.eq.0)
// {line: 21194}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 21203}
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
// {line: 21209}
// push static 1
@Memory.static.1
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21216}
// lt
@Memory.isValid.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Memory.isValid.lt.0)
// {line: 21225}
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
// {line: 21231}
// push static 1
@Memory.static.1
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21238}
// eq
@Memory.isValid.eq.1
D=A
@R14
M=D
@eq
0;JMP
(Memory.isValid.eq.1)
// {line: 21243}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 21248}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 21253}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 21259}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21265}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21268}
// not
@SP
A=M-1
M=!M
// {line: 21273}
// if-goto Memory.isValid.if.0
@SP
AM=M-1
D=M
@Memory.isValid.if.0
D;JNE
// {line: 21279}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 21282}
// not
@SP
A=M-1
M=!M
// {line: 21284}
// return
@return
0;JMP
// {line: 21285}
(Memory.isValid.if.0)
// {line: 21290}
// if-goto Memory.isValid.goto.0
@SP
AM=M-1
D=M
@Memory.isValid.goto.0
D;JNE
// {line: 21296}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 21298}
// return
@return
0;JMP
// {line: 21299}
(Memory.isValid.goto.0)
// {line: 21301}
// return
@return
0;JMP
// {line: 21306}
// function String.new nLocals: 1
(String.new)
@SP
AM=M+1
A=A-1
M=0
// {line: 21312}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 21325}
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
// {line: 21330}
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// {line: 21339}
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
// {line: 21345}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 21352}
// lt
@String.new.lt.0
D=A
@R14
M=D
@lt
0;JMP
(String.new.lt.0)
// {line: 21357}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 21363}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21369}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21372}
// not
@SP
A=M-1
M=!M
// {line: 21377}
// if-goto String.new.if.0
@SP
AM=M-1
D=M
@String.new.if.0
D;JNE
// {line: 21383}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 21389}
// pop argument 0
@SP
AM=M-1
D=M
@ARG
A=M
M=D
// {line: 21390}
(String.new.if.0)
// {line: 21395}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 21401}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 21409}
// pop this 2
@SP
AM=M-1
D=M
@THIS
A=M
A=A+1
A=A+1
M=D
// {line: 21418}
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
// {line: 21425}
// pop this 1
@SP
AM=M-1
D=M
@THIS
A=M
A=A+1
M=D
// {line: 21434}
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
// {line: 21447}
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
// {line: 21453}
// pop this 0
@SP
AM=M-1
D=M
@THIS
A=M
M=D
// {line: 21459}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 21465}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 21466}
(String.new.while.0)
// {line: 21475}
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
// {line: 21484}
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
// {line: 21491}
// lt
@String.new.lt.1
D=A
@R14
M=D
@lt
0;JMP
(String.new.lt.1)
// {line: 21494}
// not
@SP
A=M-1
M=!M
// {line: 21499}
// if-goto String.new.while.1
@SP
AM=M-1
D=M
@String.new.while.1
D;JNE
// {line: 21508}
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
// {line: 21517}
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
// {line: 21522}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 21527}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 21533}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 21539}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 21548}
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
// {line: 21554}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 21559}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 21565}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 21567}
// goto String.new.while.0
@String.new.while.0
0;JMP
// {line: 21568}
(String.new.while.1)
// {line: 21574}
// push pointer 0
@3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21576}
// return
@return
0;JMP
// {line: 21581}
// function String.dispose nLocals: 1
(String.dispose)
@SP
AM=M+1
A=A-1
M=0
// {line: 21590}
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
// {line: 21595}
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// {line: 21601}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 21608}
// pop this 1
@SP
AM=M-1
D=M
@THIS
A=M
A=A+1
M=D
// {line: 21614}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 21622}
// pop this 2
@SP
AM=M-1
D=M
@THIS
A=M
A=A+1
A=A+1
M=D
// {line: 21631}
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
// {line: 21644}
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
// {line: 21649}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 21651}
// return
@return
0;JMP
// {line: 21656}
// function String.length nLocals: 1
(String.length)
@SP
AM=M+1
A=A-1
M=0
// {line: 21665}
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
// {line: 21670}
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// {line: 21679}
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
// {line: 21681}
// return
@return
0;JMP
// {line: 21686}
// function String.charAt nLocals: 1
(String.charAt)
@SP
AM=M+1
A=A-1
M=0
// {line: 21695}
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
// {line: 21700}
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// {line: 21709}
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
// {line: 21715}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 21722}
// lt
@String.charAt.lt.0
D=A
@R14
M=D
@lt
0;JMP
(String.charAt.lt.0)
// {line: 21727}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 21733}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21739}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21742}
// not
@SP
A=M-1
M=!M
// {line: 21747}
// if-goto String.charAt.if.0
@SP
AM=M-1
D=M
@String.charAt.if.0
D;JNE
// {line: 21756}
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
// {line: 21765}
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
// {line: 21770}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 21783}
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
// {line: 21790}
// pop argument 1
@SP
AM=M-1
D=M
@ARG
A=M
A=A+1
M=D
// {line: 21791}
(String.charAt.if.0)
// {line: 21796}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 21805}
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
// {line: 21814}
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
// {line: 21821}
// gt
@String.charAt.gt.0
D=A
@R14
M=D
@gt
0;JMP
(String.charAt.gt.0)
// {line: 21830}
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
// {line: 21839}
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
// {line: 21846}
// eq
@String.charAt.eq.0
D=A
@R14
M=D
@eq
0;JMP
(String.charAt.eq.0)
// {line: 21851}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 21856}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 21862}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21868}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21871}
// not
@SP
A=M-1
M=!M
// {line: 21876}
// if-goto String.charAt.if.1
@SP
AM=M-1
D=M
@String.charAt.if.1
D;JNE
// {line: 21885}
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
// {line: 21894}
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
// {line: 21907}
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
// {line: 21914}
// pop argument 1
@SP
AM=M-1
D=M
@ARG
A=M
A=A+1
M=D
// {line: 21915}
(String.charAt.if.1)
// {line: 21920}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 21926}
// push pointer 1
@4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21935}
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
// {line: 21944}
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
// {line: 21949}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 21954}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 21963}
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
// {line: 21968}
// pop temp 2
@SP
AM=M-1
D=M
@R7
M=D
// {line: 21973}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 21979}
// push temp 2
@7
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 21981}
// return
@return
0;JMP
// {line: 21986}
// function String.setCharAt nLocals: 1
(String.setCharAt)
@SP
AM=M+1
A=A-1
M=0
// {line: 21995}
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
// {line: 22000}
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// {line: 22009}
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
// {line: 22015}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22022}
// lt
@String.setCharAt.lt.0
D=A
@R14
M=D
@lt
0;JMP
(String.setCharAt.lt.0)
// {line: 22027}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 22033}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 22039}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 22042}
// not
@SP
A=M-1
M=!M
// {line: 22047}
// if-goto String.setCharAt.if.0
@SP
AM=M-1
D=M
@String.setCharAt.if.0
D;JNE
// {line: 22056}
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
// {line: 22065}
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
// {line: 22070}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 22083}
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
// {line: 22090}
// pop argument 1
@SP
AM=M-1
D=M
@ARG
A=M
A=A+1
M=D
// {line: 22091}
(String.setCharAt.if.0)
// {line: 22096}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 22105}
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
// {line: 22114}
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
// {line: 22121}
// gt
@String.setCharAt.gt.0
D=A
@R14
M=D
@gt
0;JMP
(String.setCharAt.gt.0)
// {line: 22130}
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
// {line: 22139}
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
// {line: 22146}
// eq
@String.setCharAt.eq.0
D=A
@R14
M=D
@eq
0;JMP
(String.setCharAt.eq.0)
// {line: 22151}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 22156}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 22162}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 22168}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 22171}
// not
@SP
A=M-1
M=!M
// {line: 22176}
// if-goto String.setCharAt.if.1
@SP
AM=M-1
D=M
@String.setCharAt.if.1
D;JNE
// {line: 22185}
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
// {line: 22194}
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
// {line: 22207}
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
// {line: 22214}
// pop argument 1
@SP
AM=M-1
D=M
@ARG
A=M
A=A+1
M=D
// {line: 22215}
(String.setCharAt.if.1)
// {line: 22220}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 22229}
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
// {line: 22238}
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
// {line: 22243}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 22248}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 22257}
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
// {line: 22263}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 22265}
// return
@return
0;JMP
// {line: 22270}
// function String.appendChar nLocals: 1
(String.appendChar)
@SP
AM=M+1
A=A-1
M=0
// {line: 22279}
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
// {line: 22284}
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// {line: 22293}
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
// {line: 22302}
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
// {line: 22309}
// eq
@String.appendChar.eq.0
D=A
@R14
M=D
@eq
0;JMP
(String.appendChar.eq.0)
// {line: 22314}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 22320}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 22326}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 22329}
// not
@SP
A=M-1
M=!M
// {line: 22334}
// if-goto String.appendChar.if.0
@SP
AM=M-1
D=M
@String.appendChar.if.0
D;JNE
// {line: 22340}
// push pointer 0
@3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 22346}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22359}
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
// {line: 22364}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 22365}
(String.appendChar.if.0)
// {line: 22370}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 22379}
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
// {line: 22388}
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
// {line: 22393}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 22398}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 22407}
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
// {line: 22413}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 22422}
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
// {line: 22428}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22433}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 22441}
// pop this 2
@SP
AM=M-1
D=M
@THIS
A=M
A=A+1
A=A+1
M=D
// {line: 22447}
// push pointer 0
@3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 22449}
// return
@return
0;JMP
// {line: 22458}
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
// {line: 22467}
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
// {line: 22472}
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// {line: 22481}
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
// {line: 22490}
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
// {line: 22497}
// eq
@String.slice.eq.0
D=A
@R14
M=D
@eq
0;JMP
(String.slice.eq.0)
// {line: 22502}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 22508}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 22514}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 22517}
// not
@SP
A=M-1
M=!M
// {line: 22522}
// if-goto String.slice.if.0
@SP
AM=M-1
D=M
@String.slice.if.0
D;JNE
// {line: 22528}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22541}
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
// {line: 22547}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 22556}
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
// {line: 22562}
// push pointer 0
@3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 22571}
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
// {line: 22584}
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
// {line: 22597}
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
// {line: 22602}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 22603}
(String.slice.if.0)
// {line: 22608}
// if-goto String.slice.goto.0
@SP
AM=M-1
D=M
@String.slice.goto.0
D;JNE
// {line: 22617}
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
// {line: 22626}
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
// {line: 22633}
// lt
@String.slice.lt.0
D=A
@R14
M=D
@lt
0;JMP
(String.slice.lt.0)
// {line: 22638}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 22644}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 22650}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 22653}
// not
@SP
A=M-1
M=!M
// {line: 22658}
// if-goto String.slice.if.1
@SP
AM=M-1
D=M
@String.slice.if.1
D;JNE
// {line: 22667}
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
// {line: 22676}
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
// {line: 22681}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 22687}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22692}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 22705}
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
// {line: 22711}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 22712}
(String.slice.while.0)
// {line: 22721}
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
// {line: 22730}
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
// {line: 22737}
// lt
@String.slice.lt.1
D=A
@R14
M=D
@lt
0;JMP
(String.slice.lt.1)
// {line: 22746}
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
// {line: 22755}
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
// {line: 22762}
// eq
@String.slice.eq.1
D=A
@R14
M=D
@eq
0;JMP
(String.slice.eq.1)
// {line: 22767}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 22770}
// not
@SP
A=M-1
M=!M
// {line: 22775}
// if-goto String.slice.while.1
@SP
AM=M-1
D=M
@String.slice.while.1
D;JNE
// {line: 22784}
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
// {line: 22790}
// push pointer 0
@3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 22799}
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
// {line: 22812}
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
// {line: 22825}
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
// {line: 22830}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 22839}
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
// {line: 22845}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22850}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 22857}
// pop argument 1
@SP
AM=M-1
D=M
@ARG
A=M
A=A+1
M=D
// {line: 22859}
// goto String.slice.while.0
@String.slice.while.0
0;JMP
// {line: 22860}
(String.slice.while.1)
// {line: 22861}
(String.slice.if.1)
// {line: 22866}
// if-goto String.slice.goto.1
@SP
AM=M-1
D=M
@String.slice.goto.1
D;JNE
// {line: 22875}
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
// {line: 22884}
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
// {line: 22889}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 22895}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22900}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 22913}
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
// {line: 22919}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 22920}
(String.slice.while.2)
// {line: 22929}
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
// {line: 22938}
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
// {line: 22945}
// gt
@String.slice.gt.0
D=A
@R14
M=D
@gt
0;JMP
(String.slice.gt.0)
// {line: 22954}
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
// {line: 22963}
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
// {line: 22970}
// eq
@String.slice.eq.2
D=A
@R14
M=D
@eq
0;JMP
(String.slice.eq.2)
// {line: 22975}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 22978}
// not
@SP
A=M-1
M=!M
// {line: 22983}
// if-goto String.slice.while.3
@SP
AM=M-1
D=M
@String.slice.while.3
D;JNE
// {line: 22992}
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
// {line: 22998}
// push pointer 0
@3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 23007}
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
// {line: 23020}
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
// {line: 23033}
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
// {line: 23038}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 23047}
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
// {line: 23053}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23058}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 23065}
// pop argument 1
@SP
AM=M-1
D=M
@ARG
A=M
A=A+1
M=D
// {line: 23067}
// goto String.slice.while.2
@String.slice.while.2
0;JMP
// {line: 23068}
(String.slice.while.3)
// {line: 23069}
(String.slice.goto.1)
// {line: 23070}
(String.slice.goto.0)
// {line: 23079}
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
// {line: 23081}
// return
@return
0;JMP
// {line: 23094}
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
// {line: 23103}
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
// {line: 23108}
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// {line: 23117}
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
// {line: 23123}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23128}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 23141}
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
// {line: 23148}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 23154}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23160}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 23161}
(String.grow.while.0)
// {line: 23170}
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
// {line: 23179}
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
// {line: 23186}
// lt
@String.grow.lt.0
D=A
@R14
M=D
@lt
0;JMP
(String.grow.lt.0)
// {line: 23189}
// not
@SP
A=M-1
M=!M
// {line: 23194}
// if-goto String.grow.while.1
@SP
AM=M-1
D=M
@String.grow.while.1
D;JNE
// {line: 23203}
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
// {line: 23212}
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
// {line: 23217}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 23222}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 23228}
// push pointer 0
@3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 23237}
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
// {line: 23250}
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
// {line: 23256}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 23265}
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
// {line: 23271}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23276}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 23282}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 23284}
// goto String.grow.while.0
@String.grow.while.0
0;JMP
// {line: 23285}
(String.grow.while.1)
// {line: 23294}
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
// {line: 23307}
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
// {line: 23312}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 23321}
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
// {line: 23327}
// pop this 0
@SP
AM=M-1
D=M
@THIS
A=M
M=D
// {line: 23336}
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
// {line: 23342}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23347}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 23354}
// pop this 1
@SP
AM=M-1
D=M
@THIS
A=M
A=A+1
M=D
// {line: 23356}
// return
@return
0;JMP
// {line: 23361}
// function String.eraseLastChar nLocals: 1
(String.eraseLastChar)
@SP
AM=M+1
A=A-1
M=0
// {line: 23370}
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
// {line: 23375}
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// {line: 23384}
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
// {line: 23390}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23397}
// gt
@String.eraseLastChar.gt.0
D=A
@R14
M=D
@gt
0;JMP
(String.eraseLastChar.gt.0)
// {line: 23402}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 23408}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 23414}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 23417}
// not
@SP
A=M-1
M=!M
// {line: 23422}
// if-goto String.eraseLastChar.if.0
@SP
AM=M-1
D=M
@String.eraseLastChar.if.0
D;JNE
// {line: 23431}
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
// {line: 23437}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23442}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 23450}
// pop this 2
@SP
AM=M-1
D=M
@THIS
A=M
A=A+1
A=A+1
M=D
// {line: 23459}
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
// {line: 23465}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23470}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 23477}
// pop this 1
@SP
AM=M-1
D=M
@THIS
A=M
A=A+1
M=D
// {line: 23478}
(String.eraseLastChar.if.0)
// {line: 23483}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 23485}
// return
@return
0;JMP
// {line: 23506}
// function String.intValue nLocals: 5
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
@SP
AM=M+1
A=A-1
M=0
// {line: 23515}
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
// {line: 23520}
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// {line: 23526}
// push pointer 0
@3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 23532}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23545}
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
// {line: 23551}
// push constant 45
@45
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23558}
// eq
@String.intValue.eq.0
D=A
@R14
M=D
@eq
0;JMP
(String.intValue.eq.0)
// {line: 23563}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 23569}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 23575}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 23578}
// not
@SP
A=M-1
M=!M
// {line: 23583}
// if-goto String.intValue.if.0
@SP
AM=M-1
D=M
@String.intValue.if.0
D;JNE
// {line: 23589}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23595}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 23596}
(String.intValue.if.0)
// {line: 23601}
// if-goto String.intValue.goto.0
@SP
AM=M-1
D=M
@String.intValue.goto.0
D;JNE
// {line: 23607}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23613}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 23614}
(String.intValue.goto.0)
// {line: 23620}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23627}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 23633}
// push pointer 1
@4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 23642}
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
// {line: 23651}
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
// {line: 23656}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 23661}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 23670}
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
// {line: 23675}
// pop temp 2
@SP
AM=M-1
D=M
@R7
M=D
// {line: 23680}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 23686}
// push temp 2
@7
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 23695}
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
// {line: 23696}
(String.intValue.while.0)
// {line: 23705}
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
// {line: 23714}
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
// {line: 23721}
// lt
@String.intValue.lt.0
D=A
@R14
M=D
@lt
0;JMP
(String.intValue.lt.0)
// {line: 23730}
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
// {line: 23736}
// push constant 47
@47
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23743}
// gt
@String.intValue.gt.0
D=A
@R14
M=D
@gt
0;JMP
(String.intValue.gt.0)
// {line: 23752}
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
// {line: 23758}
// push constant 58
@58
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23765}
// lt
@String.intValue.lt.1
D=A
@R14
M=D
@lt
0;JMP
(String.intValue.lt.1)
// {line: 23770}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 23775}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 23778}
// not
@SP
A=M-1
M=!M
// {line: 23783}
// if-goto String.intValue.while.1
@SP
AM=M-1
D=M
@String.intValue.while.1
D;JNE
// {line: 23792}
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
// {line: 23798}
// push constant 10
@10
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23811}
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
// {line: 23820}
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
// {line: 23826}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23831}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 23836}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 23843}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 23852}
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
// {line: 23858}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23863}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 23869}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 23875}
// push pointer 1
@4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 23884}
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
// {line: 23893}
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
// {line: 23898}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 23903}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 23912}
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
// {line: 23917}
// pop temp 2
@SP
AM=M-1
D=M
@R7
M=D
// {line: 23922}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 23928}
// push temp 2
@7
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 23937}
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
// {line: 23939}
// goto String.intValue.while.0
@String.intValue.while.0
0;JMP
// {line: 23940}
(String.intValue.while.1)
// {line: 23946}
// push pointer 0
@3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 23952}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23965}
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
// {line: 23971}
// push constant 45
@45
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23978}
// eq
@String.intValue.eq.1
D=A
@R14
M=D
@eq
0;JMP
(String.intValue.eq.1)
// {line: 23983}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 23989}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 23995}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 23998}
// not
@SP
A=M-1
M=!M
// {line: 24003}
// if-goto String.intValue.if.1
@SP
AM=M-1
D=M
@String.intValue.if.1
D;JNE
// {line: 24012}
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
// {line: 24015}
// neg
@SP
A=M-1
M=-M
// {line: 24017}
// return
@return
0;JMP
// {line: 24018}
(String.intValue.if.1)
// {line: 24023}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 24032}
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
// {line: 24034}
// return
@return
0;JMP
// {line: 24051}
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
// {line: 24060}
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
// {line: 24065}
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// {line: 24074}
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
// {line: 24087}
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
// {line: 24094}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 24103}
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
// {line: 24109}
// push constant 10
@10
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24122}
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
// {line: 24128}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 24137}
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
// {line: 24143}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24148}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 24156}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 24165}
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
// {line: 24171}
// push constant 10
@10
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24178}
// lt
@String.setInt.lt.0
D=A
@R14
M=D
@lt
0;JMP
(String.setInt.lt.0)
// {line: 24183}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 24189}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 24195}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 24198}
// not
@SP
A=M-1
M=!M
// {line: 24203}
// if-goto String.setInt.if.0
@SP
AM=M-1
D=M
@String.setInt.if.0
D;JNE
// {line: 24209}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24216}
// pop this 1
@SP
AM=M-1
D=M
@THIS
A=M
A=A+1
M=D
// {line: 24222}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24230}
// pop this 2
@SP
AM=M-1
D=M
@THIS
A=M
A=A+1
A=A+1
M=D
// {line: 24239}
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
// {line: 24245}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24252}
// lt
@String.setInt.lt.1
D=A
@R14
M=D
@lt
0;JMP
(String.setInt.lt.1)
// {line: 24257}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 24263}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 24269}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 24272}
// not
@SP
A=M-1
M=!M
// {line: 24277}
// if-goto String.setInt.if.1
@SP
AM=M-1
D=M
@String.setInt.if.1
D;JNE
// {line: 24283}
// push pointer 0
@3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 24289}
// push constant 45
@45
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24302}
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
// {line: 24307}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 24308}
(String.setInt.if.1)
// {line: 24313}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 24319}
// push pointer 0
@3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 24328}
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
// {line: 24341}
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
// {line: 24346}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 24347}
(String.setInt.if.0)
// {line: 24352}
// if-goto String.setInt.goto.0
@SP
AM=M-1
D=M
@String.setInt.goto.0
D;JNE
// {line: 24358}
// push pointer 0
@3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 24367}
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
// {line: 24373}
// push constant 10
@10
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24386}
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
// {line: 24399}
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
// {line: 24404}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 24410}
// push pointer 0
@3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 24419}
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
// {line: 24432}
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
// {line: 24437}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 24438}
(String.setInt.goto.0)
// {line: 24440}
// return
@return
0;JMP
// {line: 24441}
// function String.newLine nLocals: 0
(String.newLine)
// {line: 24447}
// push constant 128
@128
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24449}
// return
@return
0;JMP
// {line: 24450}
// function String.backSpace nLocals: 0
(String.backSpace)
// {line: 24456}
// push constant 129
@129
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24458}
// return
@return
0;JMP
// {line: 24459}
// function String.doubleQuote nLocals: 0
(String.doubleQuote)
// {line: 24465}
// push constant 34
@34
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24467}
// return
@return
0;JMP
// {line: 24472}
// function Math.init nLocals: 1
(Math.init)
@SP
AM=M+1
A=A-1
M=0
// {line: 24478}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24483}
// pop static 5
@SP
AM=M-1
D=M
@Math.static.5
M=D
// {line: 24489}
// push static 5
@Math.static.5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 24495}
// push constant 2
@2
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24508}
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
// {line: 24514}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24519}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 24524}
// pop static 6
@SP
AM=M-1
D=M
@Math.static.6
M=D
// {line: 24530}
// push static 5
@Math.static.5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 24543}
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
// {line: 24548}
// pop static 4
@SP
AM=M-1
D=M
@Math.static.4
M=D
// {line: 24554}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24560}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 24566}
// push static 4
@Math.static.4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 24572}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24577}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 24582}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 24588}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24594}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 24595}
(Math.init.while.0)
// {line: 24604}
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
// {line: 24610}
// push static 5
@Math.static.5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 24616}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24621}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 24628}
// lt
@Math.init.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Math.init.lt.0)
// {line: 24631}
// not
@SP
A=M-1
M=!M
// {line: 24636}
// if-goto Math.init.while.1
@SP
AM=M-1
D=M
@Math.init.while.1
D;JNE
// {line: 24642}
// push static 4
@Math.static.4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 24651}
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
// {line: 24656}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 24661}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 24667}
// push pointer 1
@4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 24673}
// push static 4
@Math.static.4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 24682}
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
// {line: 24688}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24693}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 24698}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 24703}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 24712}
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
// {line: 24717}
// pop temp 2
@SP
AM=M-1
D=M
@R7
M=D
// {line: 24722}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 24728}
// push temp 2
@7
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 24734}
// push pointer 1
@4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 24740}
// push static 4
@Math.static.4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 24749}
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
// {line: 24755}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24760}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 24765}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 24770}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 24779}
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
// {line: 24784}
// pop temp 2
@SP
AM=M-1
D=M
@R7
M=D
// {line: 24789}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 24795}
// push temp 2
@7
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 24800}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 24806}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 24815}
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
// {line: 24821}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24826}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 24832}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 24834}
// goto Math.init.while.0
@Math.init.while.0
0;JMP
// {line: 24835}
(Math.init.while.1)
// {line: 24837}
// return
@return
0;JMP
// {line: 24838}
// function Math.twoToThe nLocals: 0
(Math.twoToThe)
// {line: 24844}
// push pointer 1
@4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 24850}
// push static 4
@Math.static.4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 24859}
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
// {line: 24864}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 24869}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 24878}
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
// {line: 24883}
// pop temp 2
@SP
AM=M-1
D=M
@R7
M=D
// {line: 24888}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 24894}
// push temp 2
@7
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 24896}
// return
@return
0;JMP
// {line: 24897}
// function Math.abs nLocals: 0
(Math.abs)
// {line: 24906}
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
// {line: 24912}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24919}
// lt
@Math.abs.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Math.abs.lt.0)
// {line: 24924}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 24930}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 24936}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 24939}
// not
@SP
A=M-1
M=!M
// {line: 24944}
// if-goto Math.abs.if.0
@SP
AM=M-1
D=M
@Math.abs.if.0
D;JNE
// {line: 24953}
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
// {line: 24956}
// neg
@SP
A=M-1
M=-M
// {line: 24958}
// return
@return
0;JMP
// {line: 24959}
(Math.abs.if.0)
// {line: 24964}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 24973}
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
// {line: 24975}
// return
@return
0;JMP
// {line: 24988}
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
// {line: 24994}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25002}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 25008}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25014}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 25023}
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
// {line: 25030}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 25031}
(Math.multiply.while.0)
// {line: 25040}
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
// {line: 25046}
// push static 5
@Math.static.5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 25053}
// lt
@Math.multiply.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Math.multiply.lt.0)
// {line: 25056}
// not
@SP
A=M-1
M=!M
// {line: 25061}
// if-goto Math.multiply.while.1
@SP
AM=M-1
D=M
@Math.multiply.while.1
D;JNE
// {line: 25070}
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
// {line: 25079}
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
// {line: 25092}
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
// {line: 25097}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 25103}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 25109}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 25112}
// not
@SP
A=M-1
M=!M
// {line: 25117}
// if-goto Math.multiply.if.0
@SP
AM=M-1
D=M
@Math.multiply.if.0
D;JNE
// {line: 25126}
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
// {line: 25135}
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
// {line: 25140}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 25146}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 25147}
(Math.multiply.if.0)
// {line: 25152}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 25161}
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
// {line: 25170}
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
// {line: 25175}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 25182}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 25191}
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
// {line: 25197}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25202}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 25210}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 25212}
// goto Math.multiply.while.0
@Math.multiply.while.0
0;JMP
// {line: 25213}
(Math.multiply.while.1)
// {line: 25222}
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
// {line: 25224}
// return
@return
0;JMP
// {line: 25225}
// function Math.bit nLocals: 0
(Math.bit)
// {line: 25234}
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
// {line: 25240}
// push pointer 1
@4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 25246}
// push static 4
@Math.static.4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 25255}
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
// {line: 25260}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 25265}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 25274}
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
// {line: 25279}
// pop temp 2
@SP
AM=M-1
D=M
@R7
M=D
// {line: 25284}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 25290}
// push temp 2
@7
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 25295}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 25301}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25308}
// eq
@Math.bit.eq.0
D=A
@R14
M=D
@eq
0;JMP
(Math.bit.eq.0)
// {line: 25311}
// not
@SP
A=M-1
M=!M
// {line: 25316}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 25322}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 25328}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 25331}
// not
@SP
A=M-1
M=!M
// {line: 25336}
// if-goto Math.bit.if.0
@SP
AM=M-1
D=M
@Math.bit.if.0
D;JNE
// {line: 25342}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25345}
// not
@SP
A=M-1
M=!M
// {line: 25347}
// return
@return
0;JMP
// {line: 25348}
(Math.bit.if.0)
// {line: 25353}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 25359}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25361}
// return
@return
0;JMP
// {line: 25366}
// function Math.divide nLocals: 1
(Math.divide)
@SP
AM=M+1
A=A-1
M=0
// {line: 25375}
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
// {line: 25381}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25388}
// eq
@Math.divide.eq.0
D=A
@R14
M=D
@eq
0;JMP
(Math.divide.eq.0)
// {line: 25393}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 25399}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 25405}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 25408}
// not
@SP
A=M-1
M=!M
// {line: 25413}
// if-goto Math.divide.if.0
@SP
AM=M-1
D=M
@Math.divide.if.0
D;JNE
// {line: 25419}
// push constant 5
@5
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25432}
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
// {line: 25437}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 25438}
(Math.divide.if.0)
// {line: 25443}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 25452}
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
// {line: 25461}
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
// {line: 25474}
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
// {line: 25480}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25487}
// lt
@Math.divide.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Math.divide.lt.0)
// {line: 25493}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 25502}
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
// {line: 25515}
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
// {line: 25521}
// pop argument 0
@SP
AM=M-1
D=M
@ARG
A=M
M=D
// {line: 25530}
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
// {line: 25543}
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
// {line: 25550}
// pop argument 1
@SP
AM=M-1
D=M
@ARG
A=M
A=A+1
M=D
// {line: 25559}
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
// {line: 25564}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 25570}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 25576}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 25579}
// not
@SP
A=M-1
M=!M
// {line: 25584}
// if-goto Math.divide.if.1
@SP
AM=M-1
D=M
@Math.divide.if.1
D;JNE
// {line: 25593}
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
// {line: 25602}
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
// {line: 25615}
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
// {line: 25618}
// neg
@SP
A=M-1
M=-M
// {line: 25620}
// return
@return
0;JMP
// {line: 25621}
(Math.divide.if.1)
// {line: 25626}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 25635}
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
// {line: 25644}
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
// {line: 25657}
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
// {line: 25659}
// return
@return
0;JMP
// {line: 25660}
// function Math.div nLocals: 0
(Math.div)
// {line: 25669}
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
// {line: 25678}
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
// {line: 25691}
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
// {line: 25693}
// return
@return
0;JMP
// {line: 25698}
// function Math._subdivide nLocals: 1
(Math._subdivide)
@SP
AM=M+1
A=A-1
M=0
// {line: 25707}
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
// {line: 25716}
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
// {line: 25723}
// gt
@Math._subdivide.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Math._subdivide.gt.0)
// {line: 25732}
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
// {line: 25738}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25745}
// lt
@Math._subdivide.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Math._subdivide.lt.0)
// {line: 25750}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 25755}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 25761}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 25767}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 25770}
// not
@SP
A=M-1
M=!M
// {line: 25775}
// if-goto Math._subdivide.if.0
@SP
AM=M-1
D=M
@Math._subdivide.if.0
D;JNE
// {line: 25781}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25786}
// pop static 7
@SP
AM=M-1
D=M
@Math.static.7
M=D
// {line: 25792}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25794}
// return
@return
0;JMP
// {line: 25795}
(Math._subdivide.if.0)
// {line: 25800}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 25809}
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
// {line: 25818}
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
// {line: 25827}
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
// {line: 25832}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 25845}
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
// {line: 25851}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 25860}
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
// {line: 25866}
// push static 7
@Math.static.7
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 25871}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 25880}
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
// {line: 25887}
// lt
@Math._subdivide.lt.1
D=A
@R14
M=D
@lt
0;JMP
(Math._subdivide.lt.1)
// {line: 25892}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 25898}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 25904}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 25907}
// not
@SP
A=M-1
M=!M
// {line: 25912}
// if-goto Math._subdivide.if.1
@SP
AM=M-1
D=M
@Math._subdivide.if.1
D;JNE
// {line: 25921}
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
// {line: 25930}
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
// {line: 25935}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 25937}
// return
@return
0;JMP
// {line: 25938}
(Math._subdivide.if.1)
// {line: 25943}
// if-goto Math._subdivide.goto.0
@SP
AM=M-1
D=M
@Math._subdivide.goto.0
D;JNE
// {line: 25949}
// push static 7
@Math.static.7
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 25958}
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
// {line: 25963}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 25968}
// pop static 7
@SP
AM=M-1
D=M
@Math.static.7
M=D
// {line: 25977}
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
// {line: 25986}
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
// {line: 25991}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 25997}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 26002}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 26004}
// return
@return
0;JMP
// {line: 26005}
(Math._subdivide.goto.0)
// {line: 26007}
// return
@return
0;JMP
// {line: 26008}
// function Math.xor nLocals: 0
(Math.xor)
// {line: 26017}
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
// {line: 26026}
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
// {line: 26029}
// not
@SP
A=M-1
M=!M
// {line: 26034}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 26043}
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
// {line: 26046}
// not
@SP
A=M-1
M=!M
// {line: 26055}
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
// {line: 26060}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 26065}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 26067}
// return
@return
0;JMP
// {line: 26084}
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
// {line: 26090}
// push static 6
@Math.static.6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 26096}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 26102}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 26109}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 26110}
(Math.sqrt.while.0)
// {line: 26119}
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
// {line: 26125}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 26132}
// gt
@Math.sqrt.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Math.sqrt.gt.0)
// {line: 26141}
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
// {line: 26147}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 26154}
// eq
@Math.sqrt.eq.0
D=A
@R14
M=D
@eq
0;JMP
(Math.sqrt.eq.0)
// {line: 26159}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 26162}
// not
@SP
A=M-1
M=!M
// {line: 26167}
// if-goto Math.sqrt.while.1
@SP
AM=M-1
D=M
@Math.sqrt.while.1
D;JNE
// {line: 26176}
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
// {line: 26182}
// push pointer 1
@4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 26188}
// push static 4
@Math.static.4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 26197}
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
// {line: 26202}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 26207}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 26216}
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
// {line: 26221}
// pop temp 2
@SP
AM=M-1
D=M
@R7
M=D
// {line: 26226}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 26232}
// push temp 2
@7
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 26237}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 26245}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 26254}
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
// {line: 26263}
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
// {line: 26276}
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
// {line: 26285}
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
// {line: 26294}
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
// {line: 26303}
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
// {line: 26310}
// lt
@Math.sqrt.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Math.sqrt.lt.0)
// {line: 26319}
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
// {line: 26328}
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
// {line: 26335}
// eq
@Math.sqrt.eq.1
D=A
@R14
M=D
@eq
0;JMP
(Math.sqrt.eq.1)
// {line: 26340}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 26349}
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
// {line: 26355}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 26362}
// gt
@Math.sqrt.gt.1
D=A
@R14
M=D
@gt
0;JMP
(Math.sqrt.gt.1)
// {line: 26367}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 26372}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 26378}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 26384}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 26387}
// not
@SP
A=M-1
M=!M
// {line: 26392}
// if-goto Math.sqrt.if.0
@SP
AM=M-1
D=M
@Math.sqrt.if.0
D;JNE
// {line: 26401}
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
// {line: 26408}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 26409}
(Math.sqrt.if.0)
// {line: 26414}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 26423}
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
// {line: 26429}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 26434}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 26440}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 26442}
// goto Math.sqrt.while.0
@Math.sqrt.while.0
0;JMP
// {line: 26443}
(Math.sqrt.while.1)
// {line: 26452}
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
// {line: 26454}
// return
@return
0;JMP
// {line: 26455}
// function Math.max nLocals: 0
(Math.max)
// {line: 26464}
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
// {line: 26473}
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
// {line: 26480}
// gt
@Math.max.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Math.max.gt.0)
// {line: 26485}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 26491}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 26497}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 26500}
// not
@SP
A=M-1
M=!M
// {line: 26505}
// if-goto Math.max.if.0
@SP
AM=M-1
D=M
@Math.max.if.0
D;JNE
// {line: 26514}
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
// {line: 26516}
// return
@return
0;JMP
// {line: 26517}
(Math.max.if.0)
// {line: 26522}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 26531}
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
// {line: 26533}
// return
@return
0;JMP
// {line: 26534}
// function Math.min nLocals: 0
(Math.min)
// {line: 26543}
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
// {line: 26552}
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
// {line: 26559}
// lt
@Math.min.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Math.min.lt.0)
// {line: 26564}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 26570}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 26576}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 26579}
// not
@SP
A=M-1
M=!M
// {line: 26584}
// if-goto Math.min.if.0
@SP
AM=M-1
D=M
@Math.min.if.0
D;JNE
// {line: 26593}
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
// {line: 26595}
// return
@return
0;JMP
// {line: 26596}
(Math.min.if.0)
// {line: 26601}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 26610}
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
// {line: 26612}
// return
@return
0;JMP
// {line: 26613}
// function Math.mod nLocals: 0
(Math.mod)
// {line: 26622}
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
// {line: 26631}
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
// {line: 26640}
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
// {line: 26653}
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
// {line: 26662}
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
// {line: 26675}
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
// {line: 26680}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 26682}
// return
@return
0;JMP
// {line: 26683}
// function Screen.init nLocals: 0
(Screen.init)
// {line: 26689}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 26692}
// not
@SP
A=M-1
M=!M
// {line: 26697}
// pop static 14
@SP
AM=M-1
D=M
@Screen.static.14
M=D
// {line: 26703}
// push constant 512
@512
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 26708}
// pop static 15
@SP
AM=M-1
D=M
@Screen.static.15
M=D
// {line: 26714}
// push constant 256
@256
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 26719}
// pop static 16
@SP
AM=M-1
D=M
@Screen.static.16
M=D
// {line: 26725}
// push constant 16384
@16384
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 26730}
// pop static 17
@SP
AM=M-1
D=M
@Screen.static.17
M=D
// {line: 26732}
// return
@return
0;JMP
// {line: 26737}
// function Screen.clearScreen nLocals: 1
(Screen.clearScreen)
@SP
AM=M+1
A=A-1
M=0
// {line: 26743}
// push constant 8191
@8191
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 26749}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 26750}
(Screen.clearScreen.while.0)
// {line: 26759}
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
// {line: 26765}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 26768}
// neg
@SP
A=M-1
M=-M
// {line: 26775}
// gt
@Screen.clearScreen.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Screen.clearScreen.gt.0)
// {line: 26778}
// not
@SP
A=M-1
M=!M
// {line: 26783}
// if-goto Screen.clearScreen.while.1
@SP
AM=M-1
D=M
@Screen.clearScreen.while.1
D;JNE
// {line: 26789}
// push static 17
@Screen.static.17
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 26798}
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
// {line: 26803}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 26808}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 26814}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 26820}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 26829}
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
// {line: 26835}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 26840}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 26846}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 26848}
// goto Screen.clearScreen.while.0
@Screen.clearScreen.while.0
0;JMP
// {line: 26849}
(Screen.clearScreen.while.1)
// {line: 26851}
// return
@return
0;JMP
// {line: 26852}
// function Screen.setColor nLocals: 0
(Screen.setColor)
// {line: 26861}
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
// {line: 26866}
// pop static 14
@SP
AM=M-1
D=M
@Screen.static.14
M=D
// {line: 26868}
// return
@return
0;JMP
// {line: 26869}
// function Screen.getColor nLocals: 0
(Screen.getColor)
// {line: 26875}
// push static 14
@Screen.static.14
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 26877}
// return
@return
0;JMP
// {line: 26894}
// function Screen.drawPixel nLocals: 4
(Screen.drawPixel)
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
// {line: 26903}
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
// {line: 26909}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 26922}
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
// {line: 26931}
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
// {line: 26937}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 26950}
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
// {line: 26955}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 26961}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 26970}
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
// {line: 26976}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 26989}
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
// {line: 27002}
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
// {line: 27009}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 27015}
// push static 17
@Screen.static.17
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 27024}
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
// {line: 27029}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 27034}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 27040}
// push pointer 1
@4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 27046}
// push static 17
@Screen.static.17
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 27055}
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
// {line: 27060}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 27065}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 27074}
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
// {line: 27079}
// pop temp 2
@SP
AM=M-1
D=M
@R7
M=D
// {line: 27084}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 27090}
// push temp 2
@7
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 27099}
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
// {line: 27102}
// not
@SP
A=M-1
M=!M
// {line: 27107}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 27113}
// push static 14
@Screen.static.14
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 27122}
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
// {line: 27127}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 27132}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 27138}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 27140}
// return
@return
0;JMP
// {line: 27169}
// function Screen.drawHoriz nLocals: 7
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
// {line: 27178}
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
// {line: 27187}
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
// {line: 27192}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 27198}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 27207}
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
// {line: 27213}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 27220}
// gt
@Screen.drawHoriz.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Screen.drawHoriz.gt.0)
// {line: 27225}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 27231}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 27237}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 27240}
// not
@SP
A=M-1
M=!M
// {line: 27245}
// if-goto Screen.drawHoriz.if.0
@SP
AM=M-1
D=M
@Screen.drawHoriz.if.0
D;JNE
// {line: 27254}
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
// {line: 27260}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 27267}
// gt
@Screen.drawHoriz.gt.1
D=A
@R14
M=D
@gt
0;JMP
(Screen.drawHoriz.gt.1)
// {line: 27272}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 27278}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 27284}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 27287}
// not
@SP
A=M-1
M=!M
// {line: 27292}
// if-goto Screen.drawHoriz.if.1
@SP
AM=M-1
D=M
@Screen.drawHoriz.if.1
D;JNE
// {line: 27298}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 27307}
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
// {line: 27313}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 27326}
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
// {line: 27331}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 27338}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 27347}
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
// {line: 27353}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 27366}
// call Math.multiply nArgs: 2
@2
D=A
@R14
M=D
@Math.multiply
D=A
@R15
M=D
@Screen.drawHoriz.call.1
D=A
@call
0;JMP
(Screen.drawHoriz.call.1)
// {line: 27378}
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
// {line: 27379}
(Screen.drawHoriz.while.0)
// {line: 27388}
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
// {line: 27394}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 27401}
// gt
@Screen.drawHoriz.gt.2
D=A
@R14
M=D
@gt
0;JMP
(Screen.drawHoriz.gt.2)
// {line: 27404}
// not
@SP
A=M-1
M=!M
// {line: 27409}
// if-goto Screen.drawHoriz.while.1
@SP
AM=M-1
D=M
@Screen.drawHoriz.while.1
D;JNE
// {line: 27418}
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
// {line: 27427}
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
// {line: 27432}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 27438}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 27451}
// call Math.divide nArgs: 2
@2
D=A
@R14
M=D
@Math.divide
D=A
@R15
M=D
@Screen.drawHoriz.call.2
D=A
@call
0;JMP
(Screen.drawHoriz.call.2)
// {line: 27460}
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
// {line: 27465}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 27476}
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
// {line: 27485}
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
// {line: 27494}
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
// {line: 27499}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 27505}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 27518}
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
// {line: 27531}
// call Math.twoToThe nArgs: 1
@1
D=A
@R14
M=D
@Math.twoToThe
D=A
@R15
M=D
@Screen.drawHoriz.call.4
D=A
@call
0;JMP
(Screen.drawHoriz.call.4)
// {line: 27540}
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
// {line: 27546}
// push static 17
@Screen.static.17
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 27555}
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
// {line: 27560}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 27565}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 27571}
// push pointer 1
@4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 27577}
// push static 17
@Screen.static.17
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 27586}
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
// {line: 27591}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 27596}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 27605}
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
// {line: 27610}
// pop temp 2
@SP
AM=M-1
D=M
@R7
M=D
// {line: 27615}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 27621}
// push temp 2
@7
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 27630}
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
// {line: 27633}
// not
@SP
A=M-1
M=!M
// {line: 27638}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 27644}
// push static 14
@Screen.static.14
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 27653}
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
// {line: 27658}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 27663}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 27669}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 27678}
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
// {line: 27684}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 27689}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 27696}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 27698}
// goto Screen.drawHoriz.while.0
@Screen.drawHoriz.while.0
0;JMP
// {line: 27699}
(Screen.drawHoriz.while.1)
// {line: 27708}
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
// {line: 27714}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 27723}
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
// {line: 27729}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 27742}
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
// {line: 27747}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 27752}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 27758}
// pop argument 0
@SP
AM=M-1
D=M
@ARG
A=M
M=D
// {line: 27767}
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
// {line: 27773}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 27786}
// call Math.mod nArgs: 2
@2
D=A
@R14
M=D
@Math.mod
D=A
@R15
M=D
@Screen.drawHoriz.call.6
D=A
@call
0;JMP
(Screen.drawHoriz.call.6)
// {line: 27793}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 27794}
(Screen.drawHoriz.while.2)
// {line: 27803}
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
// {line: 27809}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 27816}
// gt
@Screen.drawHoriz.gt.3
D=A
@R14
M=D
@gt
0;JMP
(Screen.drawHoriz.gt.3)
// {line: 27819}
// not
@SP
A=M-1
M=!M
// {line: 27824}
// if-goto Screen.drawHoriz.while.3
@SP
AM=M-1
D=M
@Screen.drawHoriz.while.3
D;JNE
// {line: 27833}
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
// {line: 27842}
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
// {line: 27847}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 27853}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 27866}
// call Math.divide nArgs: 2
@2
D=A
@R14
M=D
@Math.divide
D=A
@R15
M=D
@Screen.drawHoriz.call.7
D=A
@call
0;JMP
(Screen.drawHoriz.call.7)
// {line: 27875}
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
// {line: 27880}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 27891}
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
// {line: 27900}
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
// {line: 27909}
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
// {line: 27914}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 27920}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 27933}
// call Math.mod nArgs: 2
@2
D=A
@R14
M=D
@Math.mod
D=A
@R15
M=D
@Screen.drawHoriz.call.8
D=A
@call
0;JMP
(Screen.drawHoriz.call.8)
// {line: 27946}
// call Math.twoToThe nArgs: 1
@1
D=A
@R14
M=D
@Math.twoToThe
D=A
@R15
M=D
@Screen.drawHoriz.call.9
D=A
@call
0;JMP
(Screen.drawHoriz.call.9)
// {line: 27955}
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
// {line: 27961}
// push static 17
@Screen.static.17
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 27970}
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
// {line: 27975}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 27980}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 27986}
// push pointer 1
@4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 27992}
// push static 17
@Screen.static.17
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 28001}
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
// {line: 28006}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 28011}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 28020}
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
// {line: 28025}
// pop temp 2
@SP
AM=M-1
D=M
@R7
M=D
// {line: 28030}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 28036}
// push temp 2
@7
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 28045}
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
// {line: 28048}
// not
@SP
A=M-1
M=!M
// {line: 28053}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 28059}
// push static 14
@Screen.static.14
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 28068}
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
// {line: 28073}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 28078}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 28084}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 28093}
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
// {line: 28099}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 28104}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 28111}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 28113}
// goto Screen.drawHoriz.while.2
@Screen.drawHoriz.while.2
0;JMP
// {line: 28114}
(Screen.drawHoriz.while.3)
// {line: 28123}
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
// {line: 28132}
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
// {line: 28138}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 28151}
// call Math.mod nArgs: 2
@2
D=A
@R14
M=D
@Math.mod
D=A
@R15
M=D
@Screen.drawHoriz.call.10
D=A
@call
0;JMP
(Screen.drawHoriz.call.10)
// {line: 28156}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 28163}
// pop argument 1
@SP
AM=M-1
D=M
@ARG
A=M
A=A+1
M=D
// {line: 28172}
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
// {line: 28181}
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
// {line: 28186}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 28192}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 28193}
(Screen.drawHoriz.while.4)
// {line: 28202}
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
// {line: 28208}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 28215}
// gt
@Screen.drawHoriz.gt.4
D=A
@R14
M=D
@gt
0;JMP
(Screen.drawHoriz.gt.4)
// {line: 28218}
// not
@SP
A=M-1
M=!M
// {line: 28223}
// if-goto Screen.drawHoriz.while.5
@SP
AM=M-1
D=M
@Screen.drawHoriz.while.5
D;JNE
// {line: 28232}
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
// {line: 28241}
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
// {line: 28246}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 28252}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 28265}
// call Math.divide nArgs: 2
@2
D=A
@R14
M=D
@Math.divide
D=A
@R15
M=D
@Screen.drawHoriz.call.11
D=A
@call
0;JMP
(Screen.drawHoriz.call.11)
// {line: 28274}
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
// {line: 28279}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 28290}
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
// {line: 28296}
// push static 17
@Screen.static.17
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 28305}
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
// {line: 28310}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 28315}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 28321}
// push static 14
@Screen.static.14
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 28327}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 28336}
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
// {line: 28342}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 28347}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 28353}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 28355}
// goto Screen.drawHoriz.while.4
@Screen.drawHoriz.while.4
0;JMP
// {line: 28356}
(Screen.drawHoriz.while.5)
// {line: 28357}
(Screen.drawHoriz.if.1)
// {line: 28362}
// if-goto Screen.drawHoriz.goto.0
@SP
AM=M-1
D=M
@Screen.drawHoriz.goto.0
D;JNE
// {line: 28363}
(Screen.drawHoriz.while.6)
// {line: 28372}
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
// {line: 28378}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 28385}
// gt
@Screen.drawHoriz.gt.5
D=A
@R14
M=D
@gt
0;JMP
(Screen.drawHoriz.gt.5)
// {line: 28388}
// not
@SP
A=M-1
M=!M
// {line: 28393}
// if-goto Screen.drawHoriz.while.7
@SP
AM=M-1
D=M
@Screen.drawHoriz.while.7
D;JNE
// {line: 28402}
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
// {line: 28411}
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
// {line: 28416}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 28425}
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
// {line: 28438}
// call Screen.drawPixel nArgs: 2
@2
D=A
@R14
M=D
@Screen.drawPixel
D=A
@R15
M=D
@Screen.drawHoriz.call.12
D=A
@call
0;JMP
(Screen.drawHoriz.call.12)
// {line: 28443}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 28452}
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
// {line: 28458}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 28463}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 28469}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 28471}
// goto Screen.drawHoriz.while.6
@Screen.drawHoriz.while.6
0;JMP
// {line: 28472}
(Screen.drawHoriz.while.7)
// {line: 28473}
(Screen.drawHoriz.goto.0)
// {line: 28474}
(Screen.drawHoriz.if.0)
// {line: 28479}
// if-goto Screen.drawHoriz.goto.1
@SP
AM=M-1
D=M
@Screen.drawHoriz.goto.1
D;JNE
// {line: 28488}
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
// {line: 28497}
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
// {line: 28506}
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
// {line: 28519}
// call Screen.drawHoriz nArgs: 3
@3
D=A
@R14
M=D
@Screen.drawHoriz
D=A
@R15
M=D
@Screen.drawHoriz.call.13
D=A
@call
0;JMP
(Screen.drawHoriz.call.13)
// {line: 28524}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 28525}
(Screen.drawHoriz.goto.1)
// {line: 28527}
// return
@return
0;JMP
// {line: 28540}
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
// {line: 28549}
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
// {line: 28558}
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
// {line: 28563}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 28569}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 28576}
// lt
@Screen.drawVert.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawVert.lt.0)
// {line: 28581}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 28587}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 28593}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 28596}
// not
@SP
A=M-1
M=!M
// {line: 28601}
// if-goto Screen.drawVert.if.0
@SP
AM=M-1
D=M
@Screen.drawVert.if.0
D;JNE
// {line: 28610}
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
// {line: 28619}
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
// {line: 28628}
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
// {line: 28641}
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
// {line: 28646}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 28647}
(Screen.drawVert.if.0)
// {line: 28652}
// if-goto Screen.drawVert.goto.0
@SP
AM=M-1
D=M
@Screen.drawVert.goto.0
D;JNE
// {line: 28661}
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
// {line: 28667}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 28680}
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
// {line: 28689}
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
// {line: 28695}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 28708}
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
// {line: 28713}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 28719}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 28728}
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
// {line: 28734}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 28747}
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
// {line: 28760}
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
// {line: 28767}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 28768}
(Screen.drawVert.while.0)
// {line: 28777}
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
// {line: 28786}
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
// {line: 28793}
// gt
@Screen.drawVert.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Screen.drawVert.gt.0)
// {line: 28796}
// not
@SP
A=M-1
M=!M
// {line: 28801}
// if-goto Screen.drawVert.while.1
@SP
AM=M-1
D=M
@Screen.drawVert.while.1
D;JNE
// {line: 28807}
// push static 17
@Screen.static.17
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 28816}
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
// {line: 28821}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 28826}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 28832}
// push pointer 1
@4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 28838}
// push static 17
@Screen.static.17
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 28847}
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
// {line: 28852}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 28857}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 28866}
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
// {line: 28871}
// pop temp 2
@SP
AM=M-1
D=M
@R7
M=D
// {line: 28876}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 28882}
// push temp 2
@7
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 28891}
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
// {line: 28894}
// not
@SP
A=M-1
M=!M
// {line: 28899}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 28905}
// push static 14
@Screen.static.14
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 28914}
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
// {line: 28919}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 28924}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 28930}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 28939}
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
// {line: 28945}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 28950}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 28958}
// pop argument 2
@SP
AM=M-1
D=M
@ARG
A=M
A=A+1
A=A+1
M=D
// {line: 28967}
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
// {line: 28973}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 28978}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 28984}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 28986}
// goto Screen.drawVert.while.0
@Screen.drawVert.while.0
0;JMP
// {line: 28987}
(Screen.drawVert.while.1)
// {line: 28988}
(Screen.drawVert.goto.0)
// {line: 28990}
// return
@return
0;JMP
// {line: 29011}
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
// {line: 29017}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 29027}
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
// {line: 29036}
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
// {line: 29045}
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
// {line: 29050}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 29056}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 29065}
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
// {line: 29071}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 29078}
// eq
@Screen.drawLine.eq.0
D=A
@R14
M=D
@eq
0;JMP
(Screen.drawLine.eq.0)
// {line: 29083}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 29089}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 29095}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 29098}
// not
@SP
A=M-1
M=!M
// {line: 29103}
// if-goto Screen.drawLine.if.0
@SP
AM=M-1
D=M
@Screen.drawLine.if.0
D;JNE
// {line: 29112}
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
// {line: 29121}
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
// {line: 29130}
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
// {line: 29143}
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
// {line: 29148}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 29154}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 29156}
// return
@return
0;JMP
// {line: 29157}
(Screen.drawLine.if.0)
// {line: 29162}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 29171}
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
// {line: 29180}
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
// {line: 29185}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 29192}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 29201}
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
// {line: 29207}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 29214}
// eq
@Screen.drawLine.eq.1
D=A
@R14
M=D
@eq
0;JMP
(Screen.drawLine.eq.1)
// {line: 29219}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 29225}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 29231}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 29234}
// not
@SP
A=M-1
M=!M
// {line: 29239}
// if-goto Screen.drawLine.if.1
@SP
AM=M-1
D=M
@Screen.drawLine.if.1
D;JNE
// {line: 29248}
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
// {line: 29257}
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
// {line: 29266}
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
// {line: 29279}
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
// {line: 29284}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 29290}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 29292}
// return
@return
0;JMP
// {line: 29293}
(Screen.drawLine.if.1)
// {line: 29298}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 29304}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 29312}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 29318}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 29327}
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
// {line: 29333}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 29343}
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
// {line: 29352}
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
// {line: 29358}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 29365}
// lt
@Screen.drawLine.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawLine.lt.0)
// {line: 29370}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 29376}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 29382}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 29385}
// not
@SP
A=M-1
M=!M
// {line: 29390}
// if-goto Screen.drawLine.if.2
@SP
AM=M-1
D=M
@Screen.drawLine.if.2
D;JNE
// {line: 29399}
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
// {line: 29405}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 29412}
// lt
@Screen.drawLine.lt.1
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawLine.lt.1)
// {line: 29417}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 29423}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 29429}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 29432}
// not
@SP
A=M-1
M=!M
// {line: 29437}
// if-goto Screen.drawLine.if.3
@SP
AM=M-1
D=M
@Screen.drawLine.if.3
D;JNE
// {line: 29446}
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
// {line: 29455}
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
// {line: 29464}
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
// {line: 29473}
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
// {line: 29486}
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
// {line: 29491}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 29497}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 29499}
// return
@return
0;JMP
// {line: 29500}
(Screen.drawLine.if.3)
// {line: 29505}
// if-goto Screen.drawLine.goto.0
@SP
AM=M-1
D=M
@Screen.drawLine.goto.0
D;JNE
// {line: 29514}
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
// {line: 29517}
// neg
@SP
A=M-1
M=-M
// {line: 29523}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 29524}
(Screen.drawLine.while.0)
// {line: 29533}
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
// {line: 29542}
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
// {line: 29549}
// lt
@Screen.drawLine.lt.2
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawLine.lt.2)
// {line: 29558}
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
// {line: 29567}
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
// {line: 29574}
// eq
@Screen.drawLine.eq.2
D=A
@R14
M=D
@eq
0;JMP
(Screen.drawLine.eq.2)
// {line: 29579}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 29588}
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
// {line: 29597}
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
// {line: 29604}
// lt
@Screen.drawLine.lt.3
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawLine.lt.3)
// {line: 29613}
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
// {line: 29622}
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
// {line: 29629}
// eq
@Screen.drawLine.eq.3
D=A
@R14
M=D
@eq
0;JMP
(Screen.drawLine.eq.3)
// {line: 29634}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 29639}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 29642}
// not
@SP
A=M-1
M=!M
// {line: 29647}
// if-goto Screen.drawLine.while.1
@SP
AM=M-1
D=M
@Screen.drawLine.while.1
D;JNE
// {line: 29656}
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
// {line: 29665}
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
// {line: 29670}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 29679}
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
// {line: 29688}
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
// {line: 29693}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 29706}
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
// {line: 29711}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 29720}
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
// {line: 29726}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 29733}
// lt
@Screen.drawLine.lt.4
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawLine.lt.4)
// {line: 29738}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 29744}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 29750}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 29753}
// not
@SP
A=M-1
M=!M
// {line: 29758}
// if-goto Screen.drawLine.if.4
@SP
AM=M-1
D=M
@Screen.drawLine.if.4
D;JNE
// {line: 29767}
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
// {line: 29773}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 29778}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 29786}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 29795}
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
// {line: 29804}
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
// {line: 29809}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 29819}
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
// {line: 29820}
(Screen.drawLine.if.4)
// {line: 29825}
// if-goto Screen.drawLine.goto.1
@SP
AM=M-1
D=M
@Screen.drawLine.goto.1
D;JNE
// {line: 29834}
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
// {line: 29840}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 29845}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 29854}
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
// {line: 29863}
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
// {line: 29872}
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
// {line: 29877}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 29887}
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
// {line: 29888}
(Screen.drawLine.goto.1)
// {line: 29890}
// goto Screen.drawLine.while.0
@Screen.drawLine.while.0
0;JMP
// {line: 29891}
(Screen.drawLine.while.1)
// {line: 29897}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 29899}
// return
@return
0;JMP
// {line: 29900}
(Screen.drawLine.goto.0)
// {line: 29901}
(Screen.drawLine.if.2)
// {line: 29906}
// if-goto Screen.drawLine.goto.2
@SP
AM=M-1
D=M
@Screen.drawLine.goto.2
D;JNE
// {line: 29915}
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
// {line: 29921}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 29928}
// lt
@Screen.drawLine.lt.5
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawLine.lt.5)
// {line: 29933}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 29939}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 29945}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 29948}
// not
@SP
A=M-1
M=!M
// {line: 29953}
// if-goto Screen.drawLine.if.5
@SP
AM=M-1
D=M
@Screen.drawLine.if.5
D;JNE
// {line: 29962}
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
// {line: 29971}
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
// {line: 29980}
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
// {line: 29989}
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
// {line: 30002}
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
// {line: 30007}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 30013}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 30015}
// return
@return
0;JMP
// {line: 30016}
(Screen.drawLine.if.5)
// {line: 30021}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 30022}
(Screen.drawLine.goto.2)
// {line: 30023}
(Screen.drawLine.while.2)
// {line: 30032}
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
// {line: 30041}
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
// {line: 30048}
// lt
@Screen.drawLine.lt.6
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawLine.lt.6)
// {line: 30057}
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
// {line: 30066}
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
// {line: 30073}
// eq
@Screen.drawLine.eq.4
D=A
@R14
M=D
@eq
0;JMP
(Screen.drawLine.eq.4)
// {line: 30078}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 30087}
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
// {line: 30096}
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
// {line: 30103}
// lt
@Screen.drawLine.lt.7
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawLine.lt.7)
// {line: 30112}
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
// {line: 30121}
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
// {line: 30128}
// eq
@Screen.drawLine.eq.5
D=A
@R14
M=D
@eq
0;JMP
(Screen.drawLine.eq.5)
// {line: 30133}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 30138}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 30141}
// not
@SP
A=M-1
M=!M
// {line: 30146}
// if-goto Screen.drawLine.while.3
@SP
AM=M-1
D=M
@Screen.drawLine.while.3
D;JNE
// {line: 30155}
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
// {line: 30164}
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
// {line: 30169}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 30178}
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
// {line: 30187}
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
// {line: 30192}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 30205}
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
// {line: 30210}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 30219}
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
// {line: 30225}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 30232}
// lt
@Screen.drawLine.lt.8
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawLine.lt.8)
// {line: 30237}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 30243}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 30249}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 30252}
// not
@SP
A=M-1
M=!M
// {line: 30257}
// if-goto Screen.drawLine.if.6
@SP
AM=M-1
D=M
@Screen.drawLine.if.6
D;JNE
// {line: 30266}
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
// {line: 30272}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 30277}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 30285}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 30294}
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
// {line: 30303}
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
// {line: 30308}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 30318}
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
// {line: 30319}
(Screen.drawLine.if.6)
// {line: 30324}
// if-goto Screen.drawLine.goto.3
@SP
AM=M-1
D=M
@Screen.drawLine.goto.3
D;JNE
// {line: 30333}
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
// {line: 30339}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 30344}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 30353}
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
// {line: 30362}
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
// {line: 30371}
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
// {line: 30376}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 30386}
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
// {line: 30387}
(Screen.drawLine.goto.3)
// {line: 30389}
// goto Screen.drawLine.while.2
@Screen.drawLine.while.2
0;JMP
// {line: 30390}
(Screen.drawLine.while.3)
// {line: 30392}
// return
@return
0;JMP
// {line: 30393}
// function Screen.drawRectangle nLocals: 0
(Screen.drawRectangle)
// {line: 30394}
(Screen.drawRectangle.while.0)
// {line: 30403}
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
// {line: 30409}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 30414}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 30423}
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
// {line: 30430}
// lt
@Screen.drawRectangle.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawRectangle.lt.0)
// {line: 30433}
// not
@SP
A=M-1
M=!M
// {line: 30438}
// if-goto Screen.drawRectangle.while.1
@SP
AM=M-1
D=M
@Screen.drawRectangle.while.1
D;JNE
// {line: 30447}
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
// {line: 30456}
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
// {line: 30465}
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
// {line: 30478}
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
// {line: 30483}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 30492}
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
// {line: 30498}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 30503}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 30510}
// pop argument 1
@SP
AM=M-1
D=M
@ARG
A=M
A=A+1
M=D
// {line: 30512}
// goto Screen.drawRectangle.while.0
@Screen.drawRectangle.while.0
0;JMP
// {line: 30513}
(Screen.drawRectangle.while.1)
// {line: 30515}
// return
@return
0;JMP
// {line: 30524}
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
// {line: 30533}
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
// {line: 30546}
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
// {line: 30554}
// pop argument 2
@SP
AM=M-1
D=M
@ARG
A=M
A=A+1
A=A+1
M=D
// {line: 30563}
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
// {line: 30566}
// neg
@SP
A=M-1
M=-M
// {line: 30572}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 30573}
(Screen.drawCircle.while.0)
// {line: 30582}
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
// {line: 30588}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 30593}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 30602}
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
// {line: 30609}
// lt
@Screen.drawCircle.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawCircle.lt.0)
// {line: 30612}
// not
@SP
A=M-1
M=!M
// {line: 30617}
// if-goto Screen.drawCircle.while.1
@SP
AM=M-1
D=M
@Screen.drawCircle.while.1
D;JNE
// {line: 30626}
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
// {line: 30635}
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
// {line: 30648}
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
// {line: 30657}
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
// {line: 30666}
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
// {line: 30679}
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
// {line: 30684}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 30697}
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
// {line: 30704}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 30713}
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
// {line: 30722}
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
// {line: 30727}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 30736}
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
// {line: 30745}
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
// {line: 30750}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 30759}
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
// {line: 30768}
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
// {line: 30773}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 30782}
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
// {line: 30791}
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
// {line: 30796}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 30809}
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
// {line: 30814}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 30823}
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
// {line: 30829}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 30834}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 30840}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 30842}
// goto Screen.drawCircle.while.0
@Screen.drawCircle.while.0
0;JMP
// {line: 30843}
(Screen.drawCircle.while.1)
// {line: 30845}
// return
@return
0;JMP
// {line: 30846}
// function Sys.init nLocals: 0
(Sys.init)
// {line: 30852}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 30865}
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
// {line: 30870}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 30883}
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
// {line: 30888}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 30901}
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
// {line: 30906}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 30919}
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
// {line: 30924}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 30937}
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
// {line: 30942}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 30955}
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
// {line: 30960}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 30966}
// push constant 60
@60
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 30979}
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
// {line: 30984}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 30990}
// push static 12
@Sys.static.12
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 30995}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 31001}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 31007}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 31010}
// not
@SP
A=M-1
M=!M
// {line: 31015}
// if-goto Sys.init.if.0
@SP
AM=M-1
D=M
@Sys.init.if.0
D;JNE
// {line: 31028}
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
// {line: 31033}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 31034}
(Sys.init.if.0)
// {line: 31039}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 31052}
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
// {line: 31057}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 31070}
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
// {line: 31075}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 31081}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31083}
// return
@return
0;JMP
// {line: 31084}
// function Sys.setSplash nLocals: 0
(Sys.setSplash)
// {line: 31093}
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
// {line: 31098}
// pop static 12
@SP
AM=M-1
D=M
@Sys.static.12
M=D
// {line: 31100}
// return
@return
0;JMP
// {line: 31101}
// function Sys.setWaitRate nLocals: 0
(Sys.setWaitRate)
// {line: 31110}
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
// {line: 31115}
// pop static 11
@SP
AM=M-1
D=M
@Sys.static.11
M=D
// {line: 31117}
// return
@return
0;JMP
// {line: 31122}
// function Sys.splash nLocals: 1
(Sys.splash)
@SP
AM=M+1
A=A-1
M=0
// {line: 31128}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31134}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 31140}
// push constant 10
@10
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31153}
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
// {line: 31159}
// push constant 74
@74
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31172}
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
// {line: 31178}
// push constant 97
@97
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31191}
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
// {line: 31197}
// push constant 114
@114
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31210}
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
// {line: 31216}
// push constant 118
@118
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31229}
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
// {line: 31235}
// push constant 105
@105
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31248}
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
// {line: 31254}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31267}
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
// {line: 31273}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31286}
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
// {line: 31292}
// push constant 49
@49
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31305}
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
// {line: 31311}
// push constant 46
@46
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31324}
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
// {line: 31330}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31343}
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
// {line: 31356}
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
// {line: 31361}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 31374}
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
// {line: 31379}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 31385}
// push constant 700
@700
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31398}
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
// {line: 31403}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 31409}
// push constant 7
@7
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31422}
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
// {line: 31428}
// push constant 98
@98
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31441}
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
// {line: 31447}
// push constant 111
@111
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31460}
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
// {line: 31466}
// push constant 111
@111
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31479}
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
// {line: 31485}
// push constant 116
@116
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31498}
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
// {line: 31504}
// push constant 105
@105
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31517}
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
// {line: 31523}
// push constant 110
@110
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31536}
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
// {line: 31542}
// push constant 103
@103
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31555}
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
// {line: 31568}
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
// {line: 31573}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 31574}
(Sys.splash.while.0)
// {line: 31583}
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
// {line: 31589}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31596}
// gt
@Sys.splash.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Sys.splash.gt.0)
// {line: 31599}
// not
@SP
A=M-1
M=!M
// {line: 31604}
// if-goto Sys.splash.while.1
@SP
AM=M-1
D=M
@Sys.splash.while.1
D;JNE
// {line: 31610}
// push constant 600
@600
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31623}
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
// {line: 31628}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 31634}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31647}
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
// {line: 31653}
// push constant 46
@46
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31666}
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
// {line: 31679}
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
// {line: 31684}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 31693}
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
// {line: 31699}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31704}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 31710}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 31712}
// goto Sys.splash.while.0
@Sys.splash.while.0
0;JMP
// {line: 31713}
(Sys.splash.while.1)
// {line: 31719}
// push constant 1500
@1500
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31732}
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
// {line: 31737}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 31750}
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
// {line: 31755}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 31761}
// push constant 1000
@1000
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31774}
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
// {line: 31779}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 31785}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31787}
// return
@return
0;JMP
// {line: 31788}
// function Sys.halt nLocals: 0
(Sys.halt)
// {line: 31789}
(Sys.halt.while.0)
// {line: 31795}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31798}
// not
@SP
A=M-1
M=!M
// {line: 31801}
// not
@SP
A=M-1
M=!M
// {line: 31806}
// if-goto Sys.halt.while.1
@SP
AM=M-1
D=M
@Sys.halt.while.1
D;JNE
// {line: 31808}
// goto Sys.halt.while.0
@Sys.halt.while.0
0;JMP
// {line: 31809}
(Sys.halt.while.1)
// {line: 31815}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31817}
// return
@return
0;JMP
// {line: 31822}
// function Sys.wait nLocals: 1
(Sys.wait)
@SP
AM=M+1
A=A-1
M=0
// {line: 31831}
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
// {line: 31837}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31844}
// lt
@Sys.wait.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Sys.wait.lt.0)
// {line: 31849}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 31855}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 31861}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 31864}
// not
@SP
A=M-1
M=!M
// {line: 31869}
// if-goto Sys.wait.if.0
@SP
AM=M-1
D=M
@Sys.wait.if.0
D;JNE
// {line: 31875}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31888}
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
// {line: 31893}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 31894}
(Sys.wait.if.0)
// {line: 31899}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 31905}
// push static 11
@Sys.static.11
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 31911}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 31912}
(Sys.wait.while.0)
// {line: 31921}
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
// {line: 31927}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31934}
// gt
@Sys.wait.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Sys.wait.gt.0)
// {line: 31937}
// not
@SP
A=M-1
M=!M
// {line: 31942}
// if-goto Sys.wait.while.1
@SP
AM=M-1
D=M
@Sys.wait.while.1
D;JNE
// {line: 31943}
(Sys.wait.while.2)
// {line: 31952}
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
// {line: 31958}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31965}
// gt
@Sys.wait.gt.1
D=A
@R14
M=D
@gt
0;JMP
(Sys.wait.gt.1)
// {line: 31968}
// not
@SP
A=M-1
M=!M
// {line: 31973}
// if-goto Sys.wait.while.3
@SP
AM=M-1
D=M
@Sys.wait.while.3
D;JNE
// {line: 31982}
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
// {line: 31988}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 31993}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 31999}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 32001}
// goto Sys.wait.while.2
@Sys.wait.while.2
0;JMP
// {line: 32002}
(Sys.wait.while.3)
// {line: 32008}
// push static 11
@Sys.static.11
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 32014}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 32023}
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
// {line: 32029}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 32034}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 32040}
// pop argument 0
@SP
AM=M-1
D=M
@ARG
A=M
M=D
// {line: 32042}
// goto Sys.wait.while.0
@Sys.wait.while.0
0;JMP
// {line: 32043}
(Sys.wait.while.1)
// {line: 32049}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 32051}
// return
@return
0;JMP
// {line: 32052}
// function Sys.error nLocals: 0
(Sys.error)
// {line: 32065}
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
// {line: 32070}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 32076}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 32089}
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
// {line: 32095}
// push constant 69
@69
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 32108}
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
// {line: 32114}
// push constant 82
@82
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 32127}
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
// {line: 32133}
// push constant 82
@82
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 32146}
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
// {line: 32159}
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
// {line: 32164}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 32173}
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
// {line: 32186}
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
// {line: 32191}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 32204}
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
// {line: 32209}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 32215}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 32217}
// return
@return
0;JMP
// {line: 32218}
// function Keyboard.init nLocals: 0
(Keyboard.init)
// {line: 32224}
// push constant 24576
@24576
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 32229}
// pop static 13
@SP
AM=M-1
D=M
@Keyboard.static.13
M=D
// {line: 32231}
// return
@return
0;JMP
// {line: 32232}
// function Keyboard.keyPressed nLocals: 0
(Keyboard.keyPressed)
// {line: 32238}
// push pointer 1
@4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 32244}
// push static 13
@Keyboard.static.13
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 32250}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 32255}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 32260}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 32269}
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
// {line: 32274}
// pop temp 2
@SP
AM=M-1
D=M
@R7
M=D
// {line: 32279}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 32285}
// push temp 2
@7
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 32287}
// return
@return
0;JMP
// {line: 32292}
// function Keyboard.readChar nLocals: 1
(Keyboard.readChar)
@SP
AM=M+1
A=A-1
M=0
// {line: 32298}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 32304}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 32305}
(Keyboard.readChar.while.0)
// {line: 32314}
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
// {line: 32320}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 32327}
// eq
@Keyboard.readChar.eq.0
D=A
@R14
M=D
@eq
0;JMP
(Keyboard.readChar.eq.0)
// {line: 32330}
// not
@SP
A=M-1
M=!M
// {line: 32335}
// if-goto Keyboard.readChar.while.1
@SP
AM=M-1
D=M
@Keyboard.readChar.while.1
D;JNE
// {line: 32348}
// call Keyboard.keyPressed nArgs: 0
@0
D=A
@R14
M=D
@Keyboard.keyPressed
D=A
@R15
M=D
@Keyboard.readChar.call.0
D=A
@call
0;JMP
(Keyboard.readChar.call.0)
// {line: 32354}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 32356}
// goto Keyboard.readChar.while.0
@Keyboard.readChar.while.0
0;JMP
// {line: 32357}
(Keyboard.readChar.while.1)
// {line: 32366}
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
// {line: 32379}
// call String.backSpace nArgs: 0
@0
D=A
@R14
M=D
@String.backSpace
D=A
@R15
M=D
@Keyboard.readChar.call.1
D=A
@call
0;JMP
(Keyboard.readChar.call.1)
// {line: 32386}
// eq
@Keyboard.readChar.eq.1
D=A
@R14
M=D
@eq
0;JMP
(Keyboard.readChar.eq.1)
// {line: 32395}
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
// {line: 32408}
// call String.newLine nArgs: 0
@0
D=A
@R14
M=D
@String.newLine
D=A
@R15
M=D
@Keyboard.readChar.call.2
D=A
@call
0;JMP
(Keyboard.readChar.call.2)
// {line: 32415}
// eq
@Keyboard.readChar.eq.2
D=A
@R14
M=D
@eq
0;JMP
(Keyboard.readChar.eq.2)
// {line: 32420}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 32423}
// not
@SP
A=M-1
M=!M
// {line: 32428}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 32434}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 32440}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 32443}
// not
@SP
A=M-1
M=!M
// {line: 32448}
// if-goto Keyboard.readChar.if.0
@SP
AM=M-1
D=M
@Keyboard.readChar.if.0
D;JNE
// {line: 32457}
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
// {line: 32470}
// call Output.printChar nArgs: 1
@1
D=A
@R14
M=D
@Output.printChar
D=A
@R15
M=D
@Keyboard.readChar.call.3
D=A
@call
0;JMP
(Keyboard.readChar.call.3)
// {line: 32475}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 32476}
(Keyboard.readChar.if.0)
// {line: 32481}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 32487}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 32500}
// call Sys.wait nArgs: 1
@1
D=A
@R14
M=D
@Sys.wait
D=A
@R15
M=D
@Keyboard.readChar.call.4
D=A
@call
0;JMP
(Keyboard.readChar.call.4)
// {line: 32505}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 32514}
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
// {line: 32516}
// return
@return
0;JMP
// {line: 32525}
// function Keyboard.readLine nLocals: 2
(Keyboard.readLine)
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
// {line: 32531}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 32538}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 32544}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 32557}
// call String.new nArgs: 1
@1
D=A
@R14
M=D
@String.new
D=A
@R15
M=D
@Keyboard.readLine.call.0
D=A
@call
0;JMP
(Keyboard.readLine.call.0)
// {line: 32563}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 32572}
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
// {line: 32585}
// call Output.printString nArgs: 1
@1
D=A
@R14
M=D
@Output.printString
D=A
@R15
M=D
@Keyboard.readLine.call.1
D=A
@call
0;JMP
(Keyboard.readLine.call.1)
// {line: 32590}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 32591}
(Keyboard.readLine.while.0)
// {line: 32600}
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
// {line: 32613}
// call String.newLine nArgs: 0
@0
D=A
@R14
M=D
@String.newLine
D=A
@R15
M=D
@Keyboard.readLine.call.2
D=A
@call
0;JMP
(Keyboard.readLine.call.2)
// {line: 32620}
// eq
@Keyboard.readLine.eq.0
D=A
@R14
M=D
@eq
0;JMP
(Keyboard.readLine.eq.0)
// {line: 32623}
// not
@SP
A=M-1
M=!M
// {line: 32626}
// not
@SP
A=M-1
M=!M
// {line: 32631}
// if-goto Keyboard.readLine.while.1
@SP
AM=M-1
D=M
@Keyboard.readLine.while.1
D;JNE
// {line: 32644}
// call Keyboard.readChar nArgs: 0
@0
D=A
@R14
M=D
@Keyboard.readChar
D=A
@R15
M=D
@Keyboard.readLine.call.3
D=A
@call
0;JMP
(Keyboard.readLine.call.3)
// {line: 32651}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 32660}
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
// {line: 32673}
// call String.backSpace nArgs: 0
@0
D=A
@R14
M=D
@String.backSpace
D=A
@R15
M=D
@Keyboard.readLine.call.4
D=A
@call
0;JMP
(Keyboard.readLine.call.4)
// {line: 32680}
// eq
@Keyboard.readLine.eq.1
D=A
@R14
M=D
@eq
0;JMP
(Keyboard.readLine.eq.1)
// {line: 32685}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 32691}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 32697}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 32700}
// not
@SP
A=M-1
M=!M
// {line: 32705}
// if-goto Keyboard.readLine.if.0
@SP
AM=M-1
D=M
@Keyboard.readLine.if.0
D;JNE
// {line: 32714}
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
// {line: 32727}
// call String.length nArgs: 1
@1
D=A
@R14
M=D
@String.length
D=A
@R15
M=D
@Keyboard.readLine.call.5
D=A
@call
0;JMP
(Keyboard.readLine.call.5)
// {line: 32733}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 32740}
// gt
@Keyboard.readLine.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Keyboard.readLine.gt.0)
// {line: 32745}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 32751}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 32757}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 32760}
// not
@SP
A=M-1
M=!M
// {line: 32765}
// if-goto Keyboard.readLine.if.1
@SP
AM=M-1
D=M
@Keyboard.readLine.if.1
D;JNE
// {line: 32778}
// call Output.backSpace nArgs: 0
@0
D=A
@R14
M=D
@Output.backSpace
D=A
@R15
M=D
@Keyboard.readLine.call.6
D=A
@call
0;JMP
(Keyboard.readLine.call.6)
// {line: 32783}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 32792}
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
// {line: 32805}
// call String.eraseLastChar nArgs: 1
@1
D=A
@R14
M=D
@String.eraseLastChar
D=A
@R15
M=D
@Keyboard.readLine.call.7
D=A
@call
0;JMP
(Keyboard.readLine.call.7)
// {line: 32810}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 32811}
(Keyboard.readLine.if.1)
// {line: 32816}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 32817}
(Keyboard.readLine.if.0)
// {line: 32822}
// if-goto Keyboard.readLine.goto.0
@SP
AM=M-1
D=M
@Keyboard.readLine.goto.0
D;JNE
// {line: 32831}
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
// {line: 32844}
// call String.newLine nArgs: 0
@0
D=A
@R14
M=D
@String.newLine
D=A
@R15
M=D
@Keyboard.readLine.call.8
D=A
@call
0;JMP
(Keyboard.readLine.call.8)
// {line: 32851}
// eq
@Keyboard.readLine.eq.2
D=A
@R14
M=D
@eq
0;JMP
(Keyboard.readLine.eq.2)
// {line: 32854}
// not
@SP
A=M-1
M=!M
// {line: 32859}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 32865}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 32871}
// push temp 1
@6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 32874}
// not
@SP
A=M-1
M=!M
// {line: 32879}
// if-goto Keyboard.readLine.if.2
@SP
AM=M-1
D=M
@Keyboard.readLine.if.2
D;JNE
// {line: 32888}
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
// {line: 32897}
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
// {line: 32910}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Keyboard.readLine.call.9
D=A
@call
0;JMP
(Keyboard.readLine.call.9)
// {line: 32915}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 32916}
(Keyboard.readLine.if.2)
// {line: 32921}
// pop temp 1
@SP
AM=M-1
D=M
@R6
M=D
// {line: 32922}
(Keyboard.readLine.goto.0)
// {line: 32924}
// goto Keyboard.readLine.while.0
@Keyboard.readLine.while.0
0;JMP
// {line: 32925}
(Keyboard.readLine.while.1)
// {line: 32934}
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
// {line: 32936}
// return
@return
0;JMP
// {line: 32941}
// function Keyboard.readInt nLocals: 1
(Keyboard.readInt)
@SP
AM=M+1
A=A-1
M=0
// {line: 32950}
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
// {line: 32963}
// call Keyboard.readLine nArgs: 1
@1
D=A
@R14
M=D
@Keyboard.readLine
D=A
@R15
M=D
@Keyboard.readInt.call.0
D=A
@call
0;JMP
(Keyboard.readInt.call.0)
// {line: 32969}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 32978}
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
// {line: 32991}
// call String.intValue nArgs: 1
@1
D=A
@R14
M=D
@String.intValue
D=A
@R15
M=D
@Keyboard.readInt.call.1
D=A
@call
0;JMP
(Keyboard.readInt.call.1)
// {line: 32993}
// return
@return
0;JMP
