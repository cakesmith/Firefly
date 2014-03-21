// Bootstrap code
@256
D=A
@SP
M=D
@Sys.init
0;JMP
// ***
// Average
// compiled on Saturday March 15, 2014
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
// {line: 1}
// function Output.init nLocals: 0
(Output.init)
// {line: 7}
// push constant 16384
@16384
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12}
// pop static 4
@SP
AM=M-1
D=M
@Output.static.4
M=D
// {line: 18}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 21}
// not
@SP
A=M-1
M=!M
// {line: 26}
// pop static 2
@SP
AM=M-1
D=M
@Output.static.2
M=D
// {line: 32}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 37}
// pop static 1
@SP
AM=M-1
D=M
@Output.static.1
M=D
// {line: 43}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 48}
// pop static 0
@SP
AM=M-1
D=M
@Output.static.0
M=D
// {line: 54}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 67}
// call String.new nArgs: 1
@1
D=A
@R14
M=D
@String.new
D=A
@R15
M=D
@Output.init.call.0
D=A
@call
0;JMP
(Output.init.call.0)
// {line: 72}
// pop static 3
@SP
AM=M-1
D=M
@Output.static.3
M=D
// {line: 85}
// call Output.initMap nArgs: 0
@0
D=A
@R14
M=D
@Output.initMap
D=A
@R15
M=D
@Output.init.call.1
D=A
@call
0;JMP
(Output.init.call.1)
// {line: 90}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 103}
// call Output.createShiftedMap nArgs: 0
@0
D=A
@R14
M=D
@Output.createShiftedMap
D=A
@R15
M=D
@Output.init.call.2
D=A
@call
0;JMP
(Output.init.call.2)
// {line: 108}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 114}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 116}
// return
@return
0;JMP
// {line: 117}
// function Output.initMap nLocals: 0
(Output.initMap)
// {line: 123}
// push constant 127
@127
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 136}
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
// {line: 141}
// pop static 5
@SP
AM=M-1
D=M
@Output.static.5
M=D
// {line: 147}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 153}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 159}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 165}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 171}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 177}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 183}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 189}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 195}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 201}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 207}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 213}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 226}
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
// {line: 231}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 237}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 243}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 249}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 255}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 261}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 267}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 273}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 279}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 285}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 291}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 297}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 303}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 316}
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
// {line: 321}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 327}
// push constant 33
@33
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 333}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 339}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 345}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 351}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 357}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 363}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 369}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 375}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 381}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 387}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 393}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 406}
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
// {line: 411}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 417}
// push constant 34
@34
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 423}
// push constant 54
@54
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 429}
// push constant 54
@54
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 435}
// push constant 20
@20
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 441}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 447}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 453}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 459}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 465}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 471}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 477}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 483}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 496}
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
// {line: 501}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 507}
// push constant 35
@35
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 513}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 519}
// push constant 18
@18
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 525}
// push constant 18
@18
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 531}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 537}
// push constant 18
@18
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 543}
// push constant 18
@18
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 549}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 555}
// push constant 18
@18
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 561}
// push constant 18
@18
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 567}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 573}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 586}
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
// {line: 591}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 597}
// push constant 36
@36
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 603}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 609}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 615}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 621}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 627}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 633}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 639}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 645}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 651}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 657}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 663}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 676}
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
// {line: 681}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 687}
// push constant 37
@37
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 693}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 699}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 705}
// push constant 35
@35
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 711}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 717}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 723}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 729}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 735}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 741}
// push constant 49
@49
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 747}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 753}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 766}
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
// {line: 771}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 777}
// push constant 38
@38
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 783}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 789}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 795}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 801}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 807}
// push constant 54
@54
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 813}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 819}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 825}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 831}
// push constant 54
@54
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 837}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 843}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 856}
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
// {line: 861}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 867}
// push constant 39
@39
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 873}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 879}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 885}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 891}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 897}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 903}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 909}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 915}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 921}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 927}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 933}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 946}
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
// {line: 951}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 957}
// push constant 40
@40
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 963}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 969}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 975}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 981}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 987}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 993}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 999}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1005}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1011}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1017}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1023}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1036}
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
// {line: 1041}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 1047}
// push constant 41
@41
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1053}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1059}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1065}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1071}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1077}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1083}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1089}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1095}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1101}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1107}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1113}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1126}
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
// {line: 1131}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 1137}
// push constant 42
@42
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1143}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1149}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1155}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1161}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1167}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1173}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1179}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1185}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1191}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1197}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1203}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1216}
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
// {line: 1221}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 1227}
// push constant 43
@43
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1233}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1239}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1245}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1251}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1257}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1263}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1269}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1275}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1281}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1287}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1293}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1306}
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
// {line: 1311}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 1317}
// push constant 44
@44
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1323}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1329}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1335}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1341}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1347}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1353}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1359}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1365}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1371}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1377}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1383}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1396}
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
// {line: 1401}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 1407}
// push constant 45
@45
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1413}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1419}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1425}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1431}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1437}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1443}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1449}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1455}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1461}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1467}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1473}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1486}
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
// {line: 1491}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 1497}
// push constant 46
@46
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1503}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1509}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1515}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1521}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1527}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1533}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1539}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1545}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1551}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1557}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1563}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1576}
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
// {line: 1581}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 1587}
// push constant 47
@47
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1593}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1599}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1605}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1611}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1617}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1623}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1629}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1635}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1641}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1647}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1653}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1666}
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
// {line: 1671}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 1677}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1683}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1689}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1695}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1701}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1707}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1713}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1719}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1725}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1731}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1737}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1743}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1756}
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
// {line: 1761}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 1767}
// push constant 49
@49
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1773}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1779}
// push constant 14
@14
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1785}
// push constant 15
@15
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1791}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1797}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1803}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1809}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1815}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1821}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1827}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1833}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1846}
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
// {line: 1851}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 1857}
// push constant 50
@50
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1863}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1869}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1875}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1881}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1887}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1893}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1899}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1905}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1911}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1917}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1923}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1936}
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
// {line: 1941}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 1947}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1953}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1959}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1965}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1971}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1977}
// push constant 28
@28
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1983}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1989}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 1995}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2001}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2007}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2013}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2026}
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
// {line: 2031}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 2037}
// push constant 52
@52
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2043}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2049}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2055}
// push constant 28
@28
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2061}
// push constant 26
@26
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2067}
// push constant 25
@25
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2073}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2079}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2085}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2091}
// push constant 60
@60
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2097}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2103}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2116}
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
// {line: 2121}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 2127}
// push constant 53
@53
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2133}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2139}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2145}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2151}
// push constant 31
@31
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2157}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2163}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2169}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2175}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2181}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2187}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2193}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2206}
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
// {line: 2211}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 2217}
// push constant 54
@54
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2223}
// push constant 28
@28
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2229}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2235}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2241}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2247}
// push constant 31
@31
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2253}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2259}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2265}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2271}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2277}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2283}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2296}
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
// {line: 2301}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 2307}
// push constant 55
@55
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2313}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2319}
// push constant 49
@49
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2325}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2331}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2337}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2343}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2349}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2355}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2361}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2367}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2373}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2386}
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
// {line: 2391}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 2397}
// push constant 56
@56
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2403}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2409}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2415}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2421}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2427}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2433}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2439}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2445}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2451}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2457}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2463}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2476}
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
// {line: 2481}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 2487}
// push constant 57
@57
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2493}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2499}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2505}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2511}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2517}
// push constant 62
@62
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2523}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2529}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2535}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2541}
// push constant 14
@14
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2547}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2553}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2566}
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
// {line: 2571}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 2577}
// push constant 58
@58
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2583}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2589}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2595}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2601}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2607}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2613}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2619}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2625}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2631}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2637}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2643}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2656}
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
// {line: 2661}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 2667}
// push constant 59
@59
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2673}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2679}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2685}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2691}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2697}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2703}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2709}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2715}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2721}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2727}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2733}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2746}
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
// {line: 2751}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 2757}
// push constant 60
@60
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2763}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2769}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2775}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2781}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2787}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2793}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2799}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2805}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2811}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2817}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2823}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2836}
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
// {line: 2841}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 2847}
// push constant 61
@61
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2853}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2859}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2865}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2871}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2877}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2883}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2889}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2895}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2901}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2907}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2913}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2926}
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
// {line: 2931}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 2937}
// push constant 62
@62
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2943}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2949}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2955}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2961}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2967}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2973}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2979}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2985}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2991}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 2997}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3003}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3016}
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
// {line: 3021}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 3027}
// push constant 64
@64
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3033}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3039}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3045}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3051}
// push constant 59
@59
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3057}
// push constant 59
@59
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3063}
// push constant 59
@59
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3069}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3075}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3081}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3087}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3093}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3106}
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
// {line: 3111}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 3117}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3123}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3129}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3135}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3141}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3147}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3153}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3159}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3165}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3171}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3177}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3183}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3196}
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
// {line: 3201}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 3207}
// push constant 65
@65
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3213}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3219}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3225}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3231}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3237}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3243}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3249}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3255}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3261}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3267}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3273}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3286}
// call Output.create nArgs: 12
@12
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
// {line: 3291}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 3297}
// push constant 66
@66
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3303}
// push constant 31
@31
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3309}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3315}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3321}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3327}
// push constant 31
@31
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3333}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3339}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3345}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3351}
// push constant 31
@31
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3357}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3363}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3376}
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
// {line: 3381}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 3387}
// push constant 67
@67
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3393}
// push constant 28
@28
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3399}
// push constant 54
@54
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3405}
// push constant 35
@35
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3411}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3417}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3423}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3429}
// push constant 35
@35
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3435}
// push constant 54
@54
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3441}
// push constant 28
@28
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3447}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3453}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3466}
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
// {line: 3471}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 3477}
// push constant 68
@68
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3483}
// push constant 15
@15
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3489}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3495}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3501}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3507}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3513}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3519}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3525}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3531}
// push constant 15
@15
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3537}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3543}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3556}
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
// {line: 3561}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 3567}
// push constant 69
@69
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3573}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3579}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3585}
// push constant 35
@35
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3591}
// push constant 11
@11
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3597}
// push constant 15
@15
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3603}
// push constant 11
@11
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3609}
// push constant 35
@35
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3615}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3621}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3627}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3633}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3646}
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
// {line: 3651}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 3657}
// push constant 70
@70
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3663}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3669}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3675}
// push constant 35
@35
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3681}
// push constant 11
@11
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3687}
// push constant 15
@15
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3693}
// push constant 11
@11
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3699}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3705}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3711}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3717}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3723}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3736}
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
// {line: 3741}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 3747}
// push constant 71
@71
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3753}
// push constant 28
@28
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3759}
// push constant 54
@54
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3765}
// push constant 35
@35
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3771}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3777}
// push constant 59
@59
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3783}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3789}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3795}
// push constant 54
@54
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3801}
// push constant 44
@44
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3807}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3813}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3826}
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
// {line: 3831}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 3837}
// push constant 72
@72
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3843}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3849}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3855}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3861}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3867}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3873}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3879}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3885}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3891}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3897}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3903}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3916}
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
// {line: 3921}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 3927}
// push constant 73
@73
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3933}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3939}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3945}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3951}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3957}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3963}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3969}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3975}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3981}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3987}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 3993}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4006}
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
// {line: 4011}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 4017}
// push constant 74
@74
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4023}
// push constant 60
@60
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4029}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4035}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4041}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4047}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4053}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4059}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4065}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4071}
// push constant 14
@14
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4077}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4083}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4096}
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
// {line: 4101}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 4107}
// push constant 75
@75
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4113}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4119}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4125}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4131}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4137}
// push constant 15
@15
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4143}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4149}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4155}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4161}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4167}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4173}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4186}
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
// {line: 4191}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 4197}
// push constant 76
@76
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4203}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4209}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4215}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4221}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4227}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4233}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4239}
// push constant 35
@35
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4245}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4251}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4257}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4263}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4276}
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
// {line: 4281}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 4287}
// push constant 77
@77
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4293}
// push constant 33
@33
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4299}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4305}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4311}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4317}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4323}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4329}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4335}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4341}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4347}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4353}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4366}
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
// {line: 4371}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 4377}
// push constant 78
@78
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4383}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4389}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4395}
// push constant 55
@55
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4401}
// push constant 55
@55
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4407}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4413}
// push constant 59
@59
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4419}
// push constant 59
@59
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4425}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4431}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4437}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4443}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4456}
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
// {line: 4461}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 4467}
// push constant 79
@79
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4473}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4479}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4485}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4491}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4497}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4503}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4509}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4515}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4521}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4527}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4533}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4546}
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
// {line: 4551}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 4557}
// push constant 80
@80
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4563}
// push constant 31
@31
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4569}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4575}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4581}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4587}
// push constant 31
@31
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4593}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4599}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4605}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4611}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4617}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4623}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4636}
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
// {line: 4641}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 4647}
// push constant 81
@81
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4653}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4659}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4665}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4671}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4677}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4683}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4689}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4695}
// push constant 59
@59
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4701}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4707}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4713}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4726}
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
// {line: 4731}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 4737}
// push constant 82
@82
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4743}
// push constant 31
@31
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4749}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4755}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4761}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4767}
// push constant 31
@31
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4773}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4779}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4785}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4791}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4797}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4803}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4816}
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
// {line: 4821}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 4827}
// push constant 83
@83
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4833}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4839}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4845}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4851}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4857}
// push constant 28
@28
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4863}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4869}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4875}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4881}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4887}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4893}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4906}
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
// {line: 4911}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 4917}
// push constant 84
@84
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4923}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4929}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4935}
// push constant 45
@45
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4941}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4947}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4953}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4959}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4965}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4971}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4977}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4983}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 4996}
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
// {line: 5001}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 5007}
// push constant 85
@85
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5013}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5019}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5025}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5031}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5037}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5043}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5049}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5055}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5061}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5067}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5073}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5086}
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
// {line: 5091}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 5097}
// push constant 86
@86
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5103}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5109}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5115}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5121}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5127}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5133}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5139}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5145}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5151}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5157}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5163}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5176}
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
// {line: 5181}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 5187}
// push constant 87
@87
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5193}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5199}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5205}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5211}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5217}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5223}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5229}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5235}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5241}
// push constant 18
@18
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5247}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5253}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5266}
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
// {line: 5271}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 5277}
// push constant 88
@88
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5283}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5289}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5295}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5301}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5307}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5313}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5319}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5325}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5331}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5337}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5343}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5356}
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
// {line: 5361}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 5367}
// push constant 89
@89
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5373}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5379}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5385}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5391}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5397}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5403}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5409}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5415}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5421}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5427}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5433}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5446}
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
// {line: 5451}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 5457}
// push constant 90
@90
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5463}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5469}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5475}
// push constant 49
@49
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5481}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5487}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5493}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5499}
// push constant 35
@35
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5505}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5511}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5517}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5523}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5536}
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
// {line: 5541}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 5547}
// push constant 91
@91
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5553}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5559}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5565}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5571}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5577}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5583}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5589}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5595}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5601}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5607}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5613}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5626}
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
// {line: 5631}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 5637}
// push constant 92
@92
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5643}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5649}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5655}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5661}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5667}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5673}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5679}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5685}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5691}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5697}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5703}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5716}
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
// {line: 5721}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 5727}
// push constant 93
@93
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5733}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5739}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5745}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5751}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5757}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5763}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5769}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5775}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5781}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5787}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5793}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5806}
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
// {line: 5811}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 5817}
// push constant 94
@94
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5823}
// push constant 8
@8
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5829}
// push constant 28
@28
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5835}
// push constant 54
@54
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5841}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5847}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5853}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5859}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5865}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5871}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5877}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5883}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5896}
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
// {line: 5901}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 5907}
// push constant 95
@95
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5913}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5919}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5925}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5931}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5937}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5943}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5949}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5955}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5961}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5967}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5973}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 5986}
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
// {line: 5991}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 5997}
// push constant 96
@96
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6003}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6009}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6015}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6021}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6027}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6033}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6039}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6045}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6051}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6057}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6063}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6076}
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
// {line: 6081}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 6087}
// push constant 97
@97
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6093}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6099}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6105}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6111}
// push constant 14
@14
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6117}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6123}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6129}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6135}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6141}
// push constant 54
@54
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6147}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6153}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6166}
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
// {line: 6171}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 6177}
// push constant 98
@98
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6183}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6189}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6195}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6201}
// push constant 15
@15
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6207}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6213}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6219}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6225}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6231}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6237}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6243}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6256}
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
// {line: 6261}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 6267}
// push constant 99
@99
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6273}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6279}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6285}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6291}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6297}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6303}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6309}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6315}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6321}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6327}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6333}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6346}
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
// {line: 6351}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 6357}
// push constant 100
@100
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6363}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6369}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6375}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6381}
// push constant 60
@60
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6387}
// push constant 54
@54
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6393}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6399}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6405}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6411}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6417}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6423}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6436}
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
// {line: 6441}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 6447}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6453}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6459}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6465}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6471}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6477}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6483}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6489}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6495}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6501}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6507}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6513}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6526}
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
// {line: 6531}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 6537}
// push constant 102
@102
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6543}
// push constant 28
@28
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6549}
// push constant 54
@54
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6555}
// push constant 38
@38
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6561}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6567}
// push constant 15
@15
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6573}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6579}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6585}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6591}
// push constant 15
@15
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6597}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6603}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6616}
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
// {line: 6621}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 6627}
// push constant 103
@103
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6633}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6639}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6645}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6651}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6657}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6663}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6669}
// push constant 62
@62
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6675}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6681}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6687}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6693}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6706}
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
// {line: 6711}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 6717}
// push constant 104
@104
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6723}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6729}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6735}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6741}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6747}
// push constant 55
@55
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6753}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6759}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6765}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6771}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6777}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6783}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6796}
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
// {line: 6801}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 6807}
// push constant 105
@105
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6813}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6819}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6825}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6831}
// push constant 14
@14
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6837}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6843}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6849}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6855}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6861}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6867}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6873}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6886}
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
// {line: 6891}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 6897}
// push constant 106
@106
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6903}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6909}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6915}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6921}
// push constant 56
@56
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6927}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6933}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6939}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6945}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6951}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6957}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6963}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6976}
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
// {line: 6981}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 6987}
// push constant 107
@107
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6993}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 6999}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7005}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7011}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7017}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7023}
// push constant 15
@15
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7029}
// push constant 15
@15
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7035}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7041}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7047}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7053}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7066}
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
// {line: 7071}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 7077}
// push constant 108
@108
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7083}
// push constant 14
@14
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7089}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7095}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7101}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7107}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7113}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7119}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7125}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7131}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7137}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7143}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7156}
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
// {line: 7161}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 7167}
// push constant 109
@109
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7173}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7179}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7185}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7191}
// push constant 29
@29
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7197}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7203}
// push constant 43
@43
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7209}
// push constant 43
@43
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7215}
// push constant 43
@43
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7221}
// push constant 43
@43
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7227}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7233}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7246}
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
// {line: 7251}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 7257}
// push constant 110
@110
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7263}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7269}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7275}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7281}
// push constant 29
@29
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7287}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7293}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7299}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7305}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7311}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7317}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7323}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7336}
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
// {line: 7341}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 7347}
// push constant 111
@111
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7353}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7359}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7365}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7371}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7377}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7383}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7389}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7395}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7401}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7407}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7413}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7426}
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
// {line: 7431}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 7437}
// push constant 112
@112
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7443}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7449}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7455}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7461}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7467}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7473}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7479}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7485}
// push constant 31
@31
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7491}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7497}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7503}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7516}
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
// {line: 7521}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 7527}
// push constant 113
@113
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7533}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7539}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7545}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7551}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7557}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7563}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7569}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7575}
// push constant 62
@62
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7581}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7587}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7593}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7606}
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
// {line: 7611}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 7617}
// push constant 114
@114
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7623}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7629}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7635}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7641}
// push constant 29
@29
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7647}
// push constant 55
@55
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7653}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7659}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7665}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7671}
// push constant 7
@7
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7677}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7683}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7696}
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
// {line: 7701}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 7707}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7713}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7719}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7725}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7731}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7737}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7743}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7749}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7755}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7761}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7767}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7773}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7786}
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
// {line: 7791}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 7797}
// push constant 116
@116
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7803}
// push constant 4
@4
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7809}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7815}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7821}
// push constant 15
@15
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7827}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7833}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7839}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7845}
// push constant 54
@54
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7851}
// push constant 28
@28
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7857}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7863}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7876}
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
// {line: 7881}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 7887}
// push constant 117
@117
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7893}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7899}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7905}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7911}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7917}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7923}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7929}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7935}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7941}
// push constant 54
@54
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7947}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7953}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7966}
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
// {line: 7971}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 7977}
// push constant 118
@118
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7983}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7989}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 7995}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8001}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8007}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8013}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8019}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8025}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8031}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8037}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8043}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8056}
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
// {line: 8061}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 8067}
// push constant 119
@119
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8073}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8079}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8085}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8091}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8097}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8103}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8109}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8115}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8121}
// push constant 18
@18
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8127}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8133}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8146}
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
// {line: 8151}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 8157}
// push constant 120
@120
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8163}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8169}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8175}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8181}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8187}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8193}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8199}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8205}
// push constant 30
@30
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8211}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8217}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8223}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8236}
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
// {line: 8241}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 8247}
// push constant 121
@121
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8253}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8259}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8265}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8271}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8277}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8283}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8289}
// push constant 62
@62
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8295}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8301}
// push constant 24
@24
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8307}
// push constant 15
@15
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8313}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8326}
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
// {line: 8331}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 8337}
// push constant 122
@122
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8343}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8349}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8355}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8361}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8367}
// push constant 27
@27
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8373}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8379}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8385}
// push constant 51
@51
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8391}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8397}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8403}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8416}
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
// {line: 8421}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 8427}
// push constant 123
@123
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8433}
// push constant 56
@56
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8439}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8445}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8451}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8457}
// push constant 7
@7
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8463}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8469}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8475}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8481}
// push constant 56
@56
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8487}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8493}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8506}
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
// {line: 8511}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 8517}
// push constant 124
@124
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8523}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8529}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8535}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8541}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8547}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8553}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8559}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8565}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8571}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8577}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8583}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8596}
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
// {line: 8601}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 8607}
// push constant 125
@125
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8613}
// push constant 7
@7
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8619}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8625}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8631}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8637}
// push constant 56
@56
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8643}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8649}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8655}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8661}
// push constant 7
@7
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8667}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8673}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8686}
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
// {line: 8691}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 8697}
// push constant 126
@126
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8703}
// push constant 38
@38
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8709}
// push constant 45
@45
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8715}
// push constant 25
@25
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8721}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8727}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8733}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8739}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8745}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8751}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8757}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8763}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8776}
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
// {line: 8781}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 8787}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8789}
// return
@return
0;JMP
// {line: 8794}
// function Output.create nLocals: 1
(Output.create)
@SP
AM=M+1
A=A-1
M=0
// {line: 8800}
// push constant 11
@11
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8813}
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
// {line: 8819}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 8828}
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
// {line: 8834}
// push static 5
@Output.static.5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 8839}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 8848}
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
// {line: 8853}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 8858}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 8864}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 8870}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 8876}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8885}
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
// {line: 8890}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 8899}
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
// {line: 8904}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 8909}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 8915}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 8921}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 8927}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8936}
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
// {line: 8941}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 8950}
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
// {line: 8955}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 8960}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 8966}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 8972}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 8978}
// push constant 2
@2
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 8987}
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
// {line: 8992}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 9001}
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
// {line: 9006}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 9011}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 9017}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9023}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 9029}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9038}
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
// {line: 9043}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 9052}
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
// {line: 9057}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 9062}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 9068}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9074}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 9080}
// push constant 4
@4
D=A
@SP
M=M+1
A=M-1
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
// {line: 9094}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 9103}
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
// {line: 9108}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 9113}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 9119}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9125}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 9131}
// push constant 5
@5
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9140}
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
// {line: 9145}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 9154}
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
// {line: 9159}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 9164}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 9170}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9176}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 9182}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9191}
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
// {line: 9196}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 9205}
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
// {line: 9210}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 9215}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 9221}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9227}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 9233}
// push constant 7
@7
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9242}
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
// {line: 9247}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 9256}
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
// {line: 9261}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 9266}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 9272}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9278}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 9284}
// push constant 8
@8
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9293}
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
// {line: 9298}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 9307}
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
// {line: 9312}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 9317}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 9323}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9329}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 9335}
// push constant 9
@9
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9344}
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
// {line: 9349}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 9358}
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
// {line: 9363}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 9368}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 9374}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9380}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 9386}
// push constant 10
@10
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9395}
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
// {line: 9400}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 9409}
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
// {line: 9414}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 9419}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 9425}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9431}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 9437}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9439}
// return
@return
0;JMP
// {line: 9456}
// function Output.createShiftedMap nLocals: 4
(Output.createShiftedMap)
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
// {line: 9462}
// push constant 127
@127
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9475}
// call Array.new nArgs: 1
@1
D=A
@R14
M=D
@Array.new
D=A
@R15
M=D
@Output.createShiftedMap.call.0
D=A
@call
0;JMP
(Output.createShiftedMap.call.0)
// {line: 9480}
// pop static 6
@SP
AM=M-1
D=M
@Output.static.6
M=D
// {line: 9486}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9494}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 9495}
(Output.createShiftedMap.WHILE_EXP0)
// {line: 9504}
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
// {line: 9510}
// push constant 127
@127
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9517}
// lt
@Output.createShiftedMap.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Output.createShiftedMap.lt.0)
// {line: 9520}
// not
@SP
A=M-1
M=!M
// {line: 9525}
// if-goto Output.createShiftedMap.WHILE_END0
@SP
AM=M-1
D=M
@Output.createShiftedMap.WHILE_END0
D;JNE
// {line: 9534}
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
// {line: 9540}
// push static 5
@Output.static.5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9545}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 9550}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 9559}
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
// {line: 9565}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 9571}
// push constant 11
@11
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9584}
// call Array.new nArgs: 1
@1
D=A
@R14
M=D
@Array.new
D=A
@R15
M=D
@Output.createShiftedMap.call.1
D=A
@call
0;JMP
(Output.createShiftedMap.call.1)
// {line: 9591}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 9600}
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
// {line: 9606}
// push static 6
@Output.static.6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9611}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 9620}
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
// {line: 9625}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 9630}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 9636}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9642}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 9648}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9657}
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
// {line: 9658}
(Output.createShiftedMap.WHILE_EXP1)
// {line: 9667}
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
// {line: 9673}
// push constant 11
@11
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9680}
// lt
@Output.createShiftedMap.lt.1
D=A
@R14
M=D
@lt
0;JMP
(Output.createShiftedMap.lt.1)
// {line: 9683}
// not
@SP
A=M-1
M=!M
// {line: 9688}
// if-goto Output.createShiftedMap.WHILE_END1
@SP
AM=M-1
D=M
@Output.createShiftedMap.WHILE_END1
D;JNE
// {line: 9697}
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
// {line: 9706}
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
// {line: 9711}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 9720}
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
// {line: 9729}
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
// {line: 9734}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 9739}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 9748}
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
// {line: 9754}
// push constant 256
@256
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9767}
// call Math.multiply nArgs: 2
@2
D=A
@R14
M=D
@Math.multiply
D=A
@R15
M=D
@Output.createShiftedMap.call.2
D=A
@call
0;JMP
(Output.createShiftedMap.call.2)
// {line: 9772}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 9777}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 9783}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9789}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 9798}
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
// {line: 9804}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9809}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 9818}
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
// {line: 9820}
// goto Output.createShiftedMap.WHILE_EXP1
@Output.createShiftedMap.WHILE_EXP1
0;JMP
// {line: 9821}
(Output.createShiftedMap.WHILE_END1)
// {line: 9830}
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
// {line: 9836}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9843}
// eq
@Output.createShiftedMap.eq.0
D=A
@R14
M=D
@eq
0;JMP
(Output.createShiftedMap.eq.0)
// {line: 9848}
// if-goto Output.createShiftedMap.IF_TRUE0
@SP
AM=M-1
D=M
@Output.createShiftedMap.IF_TRUE0
D;JNE
// {line: 9850}
// goto Output.createShiftedMap.IF_FALSE0
@Output.createShiftedMap.IF_FALSE0
0;JMP
// {line: 9851}
(Output.createShiftedMap.IF_TRUE0)
// {line: 9857}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9865}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 9867}
// goto Output.createShiftedMap.IF_END0
@Output.createShiftedMap.IF_END0
0;JMP
// {line: 9868}
(Output.createShiftedMap.IF_FALSE0)
// {line: 9877}
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
// {line: 9883}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9888}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 9896}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 9897}
(Output.createShiftedMap.IF_END0)
// {line: 9899}
// goto Output.createShiftedMap.WHILE_EXP0
@Output.createShiftedMap.WHILE_EXP0
0;JMP
// {line: 9900}
(Output.createShiftedMap.WHILE_END0)
// {line: 9906}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9908}
// return
@return
0;JMP
// {line: 9913}
// function Output.getMap nLocals: 1
(Output.getMap)
@SP
AM=M+1
A=A-1
M=0
// {line: 9922}
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
// {line: 9928}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9935}
// lt
@Output.getMap.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Output.getMap.lt.0)
// {line: 9944}
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
// {line: 9950}
// push constant 126
@126
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9957}
// gt
@Output.getMap.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Output.getMap.gt.0)
// {line: 9962}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 9967}
// if-goto Output.getMap.IF_TRUE0
@SP
AM=M-1
D=M
@Output.getMap.IF_TRUE0
D;JNE
// {line: 9969}
// goto Output.getMap.IF_FALSE0
@Output.getMap.IF_FALSE0
0;JMP
// {line: 9970}
(Output.getMap.IF_TRUE0)
// {line: 9976}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 9982}
// pop argument 0
@SP
AM=M-1
D=M
@ARG
A=M
M=D
// {line: 9983}
(Output.getMap.IF_FALSE0)
// {line: 9989}
// push static 2
@Output.static.2
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 9994}
// if-goto Output.getMap.IF_TRUE1
@SP
AM=M-1
D=M
@Output.getMap.IF_TRUE1
D;JNE
// {line: 9996}
// goto Output.getMap.IF_FALSE1
@Output.getMap.IF_FALSE1
0;JMP
// {line: 9997}
(Output.getMap.IF_TRUE1)
// {line: 10006}
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
// {line: 10012}
// push static 5
@Output.static.5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10017}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 10022}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 10031}
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
// {line: 10037}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 10039}
// goto Output.getMap.IF_END1
@Output.getMap.IF_END1
0;JMP
// {line: 10040}
(Output.getMap.IF_FALSE1)
// {line: 10049}
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
// {line: 10055}
// push static 6
@Output.static.6
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10060}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 10065}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 10074}
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
// {line: 10080}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 10081}
(Output.getMap.IF_END1)
// {line: 10090}
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
// {line: 10092}
// return
@return
0;JMP
// {line: 10109}
// function Output.drawChar nLocals: 4
(Output.drawChar)
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
// {line: 10118}
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
// {line: 10131}
// call Output.getMap nArgs: 1
@1
D=A
@R14
M=D
@Output.getMap
D=A
@R15
M=D
@Output.drawChar.call.0
D=A
@call
0;JMP
(Output.drawChar.call.0)
// {line: 10139}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 10145}
// push static 1
@Output.static.1
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10151}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 10152}
(Output.drawChar.WHILE_EXP0)
// {line: 10161}
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
// {line: 10167}
// push constant 11
@11
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10174}
// lt
@Output.drawChar.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Output.drawChar.lt.0)
// {line: 10177}
// not
@SP
A=M-1
M=!M
// {line: 10182}
// if-goto Output.drawChar.WHILE_END0
@SP
AM=M-1
D=M
@Output.drawChar.WHILE_END0
D;JNE
// {line: 10188}
// push static 2
@Output.static.2
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10193}
// if-goto Output.drawChar.IF_TRUE0
@SP
AM=M-1
D=M
@Output.drawChar.IF_TRUE0
D;JNE
// {line: 10195}
// goto Output.drawChar.IF_FALSE0
@Output.drawChar.IF_FALSE0
0;JMP
// {line: 10196}
(Output.drawChar.IF_TRUE0)
// {line: 10205}
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
// {line: 10211}
// push static 4
@Output.static.4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10216}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 10221}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 10230}
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
// {line: 10236}
// push constant 256
@256
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10239}
// neg
@SP
A=M-1
M=-M
// {line: 10244}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 10253}
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
// {line: 10255}
// goto Output.drawChar.IF_END0
@Output.drawChar.IF_END0
0;JMP
// {line: 10256}
(Output.drawChar.IF_FALSE0)
// {line: 10265}
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
// {line: 10271}
// push static 4
@Output.static.4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10276}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 10281}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 10290}
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
// {line: 10296}
// push constant 255
@255
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10301}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 10310}
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
// {line: 10311}
(Output.drawChar.IF_END0)
// {line: 10320}
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
// {line: 10326}
// push static 4
@Output.static.4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10331}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 10340}
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
// {line: 10349}
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
// {line: 10354}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 10359}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 10368}
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
// {line: 10377}
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
// {line: 10382}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 10387}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 10392}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 10398}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10404}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 10413}
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
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10424}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 10430}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 10439}
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
// {line: 10445}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10450}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 10457}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 10459}
// goto Output.drawChar.WHILE_EXP0
@Output.drawChar.WHILE_EXP0
0;JMP
// {line: 10460}
(Output.drawChar.WHILE_END0)
// {line: 10466}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10468}
// return
@return
0;JMP
// {line: 10469}
// function Output.moveCursor nLocals: 0
(Output.moveCursor)
// {line: 10478}
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
// {line: 10484}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10491}
// lt
@Output.moveCursor.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Output.moveCursor.lt.0)
// {line: 10500}
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
// {line: 10506}
// push constant 22
@22
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10513}
// gt
@Output.moveCursor.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Output.moveCursor.gt.0)
// {line: 10518}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 10527}
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
// {line: 10533}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10540}
// lt
@Output.moveCursor.lt.1
D=A
@R14
M=D
@lt
0;JMP
(Output.moveCursor.lt.1)
// {line: 10545}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 10554}
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
// {line: 10560}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10567}
// gt
@Output.moveCursor.gt.1
D=A
@R14
M=D
@gt
0;JMP
(Output.moveCursor.gt.1)
// {line: 10572}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 10577}
// if-goto Output.moveCursor.IF_TRUE0
@SP
AM=M-1
D=M
@Output.moveCursor.IF_TRUE0
D;JNE
// {line: 10579}
// goto Output.moveCursor.IF_FALSE0
@Output.moveCursor.IF_FALSE0
0;JMP
// {line: 10580}
(Output.moveCursor.IF_TRUE0)
// {line: 10586}
// push constant 20
@20
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10599}
// call Sys.error nArgs: 1
@1
D=A
@R14
M=D
@Sys.error
D=A
@R15
M=D
@Output.moveCursor.call.0
D=A
@call
0;JMP
(Output.moveCursor.call.0)
// {line: 10604}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 10605}
(Output.moveCursor.IF_FALSE0)
// {line: 10614}
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
// {line: 10620}
// push constant 2
@2
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10633}
// call Math.divide nArgs: 2
@2
D=A
@R14
M=D
@Math.divide
D=A
@R15
M=D
@Output.moveCursor.call.1
D=A
@call
0;JMP
(Output.moveCursor.call.1)
// {line: 10638}
// pop static 0
@SP
AM=M-1
D=M
@Output.static.0
M=D
// {line: 10644}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10653}
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
// {line: 10659}
// push constant 352
@352
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10672}
// call Math.multiply nArgs: 2
@2
D=A
@R14
M=D
@Math.multiply
D=A
@R15
M=D
@Output.moveCursor.call.2
D=A
@call
0;JMP
(Output.moveCursor.call.2)
// {line: 10677}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 10683}
// push static 0
@Output.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10688}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 10693}
// pop static 1
@SP
AM=M-1
D=M
@Output.static.1
M=D
// {line: 10702}
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
// {line: 10708}
// push static 0
@Output.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10714}
// push constant 2
@2
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10727}
// call Math.multiply nArgs: 2
@2
D=A
@R14
M=D
@Math.multiply
D=A
@R15
M=D
@Output.moveCursor.call.3
D=A
@call
0;JMP
(Output.moveCursor.call.3)
// {line: 10734}
// eq
@Output.moveCursor.eq.0
D=A
@R14
M=D
@eq
0;JMP
(Output.moveCursor.eq.0)
// {line: 10739}
// pop static 2
@SP
AM=M-1
D=M
@Output.static.2
M=D
// {line: 10745}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10758}
// call Output.drawChar nArgs: 1
@1
D=A
@R14
M=D
@Output.drawChar
D=A
@R15
M=D
@Output.moveCursor.call.4
D=A
@call
0;JMP
(Output.moveCursor.call.4)
// {line: 10763}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 10769}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10771}
// return
@return
0;JMP
// {line: 10772}
// function Output.printChar nLocals: 0
(Output.printChar)
// {line: 10781}
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
// {line: 10794}
// call String.newLine nArgs: 0
@0
D=A
@R14
M=D
@String.newLine
D=A
@R15
M=D
@Output.printChar.call.0
D=A
@call
0;JMP
(Output.printChar.call.0)
// {line: 10801}
// eq
@Output.printChar.eq.0
D=A
@R14
M=D
@eq
0;JMP
(Output.printChar.eq.0)
// {line: 10806}
// if-goto Output.printChar.IF_TRUE0
@SP
AM=M-1
D=M
@Output.printChar.IF_TRUE0
D;JNE
// {line: 10808}
// goto Output.printChar.IF_FALSE0
@Output.printChar.IF_FALSE0
0;JMP
// {line: 10809}
(Output.printChar.IF_TRUE0)
// {line: 10822}
// call Output.println nArgs: 0
@0
D=A
@R14
M=D
@Output.println
D=A
@R15
M=D
@Output.printChar.call.1
D=A
@call
0;JMP
(Output.printChar.call.1)
// {line: 10827}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 10829}
// goto Output.printChar.IF_END0
@Output.printChar.IF_END0
0;JMP
// {line: 10830}
(Output.printChar.IF_FALSE0)
// {line: 10839}
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
// {line: 10852}
// call String.backSpace nArgs: 0
@0
D=A
@R14
M=D
@String.backSpace
D=A
@R15
M=D
@Output.printChar.call.2
D=A
@call
0;JMP
(Output.printChar.call.2)
// {line: 10859}
// eq
@Output.printChar.eq.1
D=A
@R14
M=D
@eq
0;JMP
(Output.printChar.eq.1)
// {line: 10864}
// if-goto Output.printChar.IF_TRUE1
@SP
AM=M-1
D=M
@Output.printChar.IF_TRUE1
D;JNE
// {line: 10866}
// goto Output.printChar.IF_FALSE1
@Output.printChar.IF_FALSE1
0;JMP
// {line: 10867}
(Output.printChar.IF_TRUE1)
// {line: 10880}
// call Output.backSpace nArgs: 0
@0
D=A
@R14
M=D
@Output.backSpace
D=A
@R15
M=D
@Output.printChar.call.3
D=A
@call
0;JMP
(Output.printChar.call.3)
// {line: 10885}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 10887}
// goto Output.printChar.IF_END1
@Output.printChar.IF_END1
0;JMP
// {line: 10888}
(Output.printChar.IF_FALSE1)
// {line: 10897}
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
// {line: 10910}
// call Output.drawChar nArgs: 1
@1
D=A
@R14
M=D
@Output.drawChar
D=A
@R15
M=D
@Output.printChar.call.4
D=A
@call
0;JMP
(Output.printChar.call.4)
// {line: 10915}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 10921}
// push static 2
@Output.static.2
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10924}
// not
@SP
A=M-1
M=!M
// {line: 10929}
// if-goto Output.printChar.IF_TRUE2
@SP
AM=M-1
D=M
@Output.printChar.IF_TRUE2
D;JNE
// {line: 10931}
// goto Output.printChar.IF_FALSE2
@Output.printChar.IF_FALSE2
0;JMP
// {line: 10932}
(Output.printChar.IF_TRUE2)
// {line: 10938}
// push static 0
@Output.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10944}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10949}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 10954}
// pop static 0
@SP
AM=M-1
D=M
@Output.static.0
M=D
// {line: 10960}
// push static 1
@Output.static.1
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10966}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10971}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 10976}
// pop static 1
@SP
AM=M-1
D=M
@Output.static.1
M=D
// {line: 10977}
(Output.printChar.IF_FALSE2)
// {line: 10983}
// push static 0
@Output.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 10989}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 10996}
// eq
@Output.printChar.eq.2
D=A
@R14
M=D
@eq
0;JMP
(Output.printChar.eq.2)
// {line: 11001}
// if-goto Output.printChar.IF_TRUE3
@SP
AM=M-1
D=M
@Output.printChar.IF_TRUE3
D;JNE
// {line: 11003}
// goto Output.printChar.IF_FALSE3
@Output.printChar.IF_FALSE3
0;JMP
// {line: 11004}
(Output.printChar.IF_TRUE3)
// {line: 11017}
// call Output.println nArgs: 0
@0
D=A
@R14
M=D
@Output.println
D=A
@R15
M=D
@Output.printChar.call.5
D=A
@call
0;JMP
(Output.printChar.call.5)
// {line: 11022}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 11024}
// goto Output.printChar.IF_END3
@Output.printChar.IF_END3
0;JMP
// {line: 11025}
(Output.printChar.IF_FALSE3)
// {line: 11031}
// push static 2
@Output.static.2
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 11034}
// not
@SP
A=M-1
M=!M
// {line: 11039}
// pop static 2
@SP
AM=M-1
D=M
@Output.static.2
M=D
// {line: 11040}
(Output.printChar.IF_END3)
// {line: 11041}
(Output.printChar.IF_END1)
// {line: 11042}
(Output.printChar.IF_END0)
// {line: 11048}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11050}
// return
@return
0;JMP
// {line: 11059}
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
// {line: 11068}
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
// {line: 11081}
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
// {line: 11088}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 11089}
(Output.printString.WHILE_EXP0)
// {line: 11098}
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
// {line: 11107}
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
// {line: 11114}
// lt
@Output.printString.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Output.printString.lt.0)
// {line: 11117}
// not
@SP
A=M-1
M=!M
// {line: 11122}
// if-goto Output.printString.WHILE_END0
@SP
AM=M-1
D=M
@Output.printString.WHILE_END0
D;JNE
// {line: 11131}
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
// {line: 11140}
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
// {line: 11153}
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
// {line: 11166}
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
// {line: 11171}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 11180}
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
// {line: 11186}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11191}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 11197}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 11199}
// goto Output.printString.WHILE_EXP0
@Output.printString.WHILE_EXP0
0;JMP
// {line: 11200}
(Output.printString.WHILE_END0)
// {line: 11206}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11208}
// return
@return
0;JMP
// {line: 11209}
// function Output.printInt nLocals: 0
(Output.printInt)
// {line: 11215}
// push static 3
@Output.static.3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 11224}
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
// {line: 11237}
// call String.setInt nArgs: 2
@2
D=A
@R14
M=D
@String.setInt
D=A
@R15
M=D
@Output.printInt.call.0
D=A
@call
0;JMP
(Output.printInt.call.0)
// {line: 11242}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 11248}
// push static 3
@Output.static.3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 11261}
// call Output.printString nArgs: 1
@1
D=A
@R14
M=D
@Output.printString
D=A
@R15
M=D
@Output.printInt.call.1
D=A
@call
0;JMP
(Output.printInt.call.1)
// {line: 11266}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 11272}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11274}
// return
@return
0;JMP
// {line: 11275}
// function Output.println nLocals: 0
(Output.println)
// {line: 11281}
// push static 1
@Output.static.1
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 11287}
// push constant 352
@352
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11292}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 11298}
// push static 0
@Output.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 11303}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 11308}
// pop static 1
@SP
AM=M-1
D=M
@Output.static.1
M=D
// {line: 11314}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11319}
// pop static 0
@SP
AM=M-1
D=M
@Output.static.0
M=D
// {line: 11325}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11328}
// not
@SP
A=M-1
M=!M
// {line: 11333}
// pop static 2
@SP
AM=M-1
D=M
@Output.static.2
M=D
// {line: 11339}
// push static 1
@Output.static.1
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 11345}
// push constant 8128
@8128
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11352}
// eq
@Output.println.eq.0
D=A
@R14
M=D
@eq
0;JMP
(Output.println.eq.0)
// {line: 11357}
// if-goto Output.println.IF_TRUE0
@SP
AM=M-1
D=M
@Output.println.IF_TRUE0
D;JNE
// {line: 11359}
// goto Output.println.IF_FALSE0
@Output.println.IF_FALSE0
0;JMP
// {line: 11360}
(Output.println.IF_TRUE0)
// {line: 11366}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11371}
// pop static 1
@SP
AM=M-1
D=M
@Output.static.1
M=D
// {line: 11372}
(Output.println.IF_FALSE0)
// {line: 11378}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11380}
// return
@return
0;JMP
// {line: 11381}
// function Output.backSpace nLocals: 0
(Output.backSpace)
// {line: 11387}
// push static 2
@Output.static.2
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 11392}
// if-goto Output.backSpace.IF_TRUE0
@SP
AM=M-1
D=M
@Output.backSpace.IF_TRUE0
D;JNE
// {line: 11394}
// goto Output.backSpace.IF_FALSE0
@Output.backSpace.IF_FALSE0
0;JMP
// {line: 11395}
(Output.backSpace.IF_TRUE0)
// {line: 11401}
// push static 0
@Output.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 11407}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11414}
// gt
@Output.backSpace.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Output.backSpace.gt.0)
// {line: 11419}
// if-goto Output.backSpace.IF_TRUE1
@SP
AM=M-1
D=M
@Output.backSpace.IF_TRUE1
D;JNE
// {line: 11421}
// goto Output.backSpace.IF_FALSE1
@Output.backSpace.IF_FALSE1
0;JMP
// {line: 11422}
(Output.backSpace.IF_TRUE1)
// {line: 11428}
// push static 0
@Output.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 11434}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11439}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 11444}
// pop static 0
@SP
AM=M-1
D=M
@Output.static.0
M=D
// {line: 11450}
// push static 1
@Output.static.1
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 11456}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11461}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 11466}
// pop static 1
@SP
AM=M-1
D=M
@Output.static.1
M=D
// {line: 11468}
// goto Output.backSpace.IF_END1
@Output.backSpace.IF_END1
0;JMP
// {line: 11469}
(Output.backSpace.IF_FALSE1)
// {line: 11475}
// push constant 31
@31
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11480}
// pop static 0
@SP
AM=M-1
D=M
@Output.static.0
M=D
// {line: 11486}
// push static 1
@Output.static.1
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 11492}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11499}
// eq
@Output.backSpace.eq.0
D=A
@R14
M=D
@eq
0;JMP
(Output.backSpace.eq.0)
// {line: 11504}
// if-goto Output.backSpace.IF_TRUE2
@SP
AM=M-1
D=M
@Output.backSpace.IF_TRUE2
D;JNE
// {line: 11506}
// goto Output.backSpace.IF_FALSE2
@Output.backSpace.IF_FALSE2
0;JMP
// {line: 11507}
(Output.backSpace.IF_TRUE2)
// {line: 11513}
// push constant 8128
@8128
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11518}
// pop static 1
@SP
AM=M-1
D=M
@Output.static.1
M=D
// {line: 11519}
(Output.backSpace.IF_FALSE2)
// {line: 11525}
// push static 1
@Output.static.1
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 11531}
// push constant 321
@321
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11536}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 11541}
// pop static 1
@SP
AM=M-1
D=M
@Output.static.1
M=D
// {line: 11542}
(Output.backSpace.IF_END1)
// {line: 11548}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11553}
// pop static 2
@SP
AM=M-1
D=M
@Output.static.2
M=D
// {line: 11555}
// goto Output.backSpace.IF_END0
@Output.backSpace.IF_END0
0;JMP
// {line: 11556}
(Output.backSpace.IF_FALSE0)
// {line: 11562}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11565}
// not
@SP
A=M-1
M=!M
// {line: 11570}
// pop static 2
@SP
AM=M-1
D=M
@Output.static.2
M=D
// {line: 11571}
(Output.backSpace.IF_END0)
// {line: 11577}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11590}
// call Output.drawChar nArgs: 1
@1
D=A
@R14
M=D
@Output.drawChar
D=A
@R15
M=D
@Output.backSpace.call.0
D=A
@call
0;JMP
(Output.backSpace.call.0)
// {line: 11595}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 11601}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11603}
// return
@return
0;JMP
// {line: 11620}
// function Main.main nLocals: 4
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
// {line: 11626}
// push constant 20
@20
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11639}
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
// {line: 11645}
// push constant 72
@72
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11658}
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
// {line: 11664}
// push constant 111
@111
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11677}
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
// {line: 11683}
// push constant 119
@119
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11696}
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
// {line: 11702}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11715}
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
// {line: 11721}
// push constant 109
@109
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11734}
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
// {line: 11740}
// push constant 97
@97
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11753}
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
// {line: 11759}
// push constant 110
@110
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11772}
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
// {line: 11778}
// push constant 121
@121
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11791}
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
// {line: 11797}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11810}
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
// {line: 11816}
// push constant 110
@110
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11829}
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
// {line: 11835}
// push constant 117
@117
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11848}
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
// {line: 11854}
// push constant 109
@109
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11867}
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
// {line: 11873}
// push constant 98
@98
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11886}
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
// {line: 11892}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11905}
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
// {line: 11911}
// push constant 114
@114
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11924}
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
// {line: 11930}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11943}
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
// {line: 11949}
// push constant 63
@63
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11962}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.17
D=A
@call
0;JMP
(Main.main.call.17)
// {line: 11968}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 11981}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.18
D=A
@call
0;JMP
(Main.main.call.18)
// {line: 11994}
// call Keyboard.readInt nArgs: 1
@1
D=A
@R14
M=D
@Keyboard.readInt
D=A
@R15
M=D
@Main.main.call.19
D=A
@call
0;JMP
(Main.main.call.19)
// {line: 12001}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 12010}
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
// {line: 12023}
// call Array.new nArgs: 1
@1
D=A
@R14
M=D
@Array.new
D=A
@R15
M=D
@Main.main.call.20
D=A
@call
0;JMP
(Main.main.call.20)
// {line: 12029}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 12035}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12043}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 12044}
(Main.main.while.0)
// {line: 12053}
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
// {line: 12062}
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
// {line: 12069}
// lt
@Main.main.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Main.main.lt.0)
// {line: 12072}
// not
@SP
A=M-1
M=!M
// {line: 12077}
// if-goto Main.main.while.1
@SP
AM=M-1
D=M
@Main.main.while.1
D;JNE
// {line: 12086}
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
// {line: 12095}
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
// {line: 12100}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 12105}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 12111}
// push constant 25
@25
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12124}
// call String.new nArgs: 1
@1
D=A
@R14
M=D
@String.new
D=A
@R15
M=D
@Main.main.call.21
D=A
@call
0;JMP
(Main.main.call.21)
// {line: 12130}
// push constant 69
@69
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12143}
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
// {line: 12149}
// push constant 110
@110
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12162}
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
// {line: 12168}
// push constant 116
@116
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12181}
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
// {line: 12187}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12200}
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
// {line: 12206}
// push constant 114
@114
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12219}
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
// {line: 12225}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12238}
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
// {line: 12244}
// push constant 116
@116
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12257}
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
// {line: 12263}
// push constant 104
@104
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12276}
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
// {line: 12282}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12295}
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
// {line: 12301}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12314}
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
// {line: 12320}
// push constant 110
@110
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12333}
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
// {line: 12339}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12352}
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
// {line: 12358}
// push constant 120
@120
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12371}
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
// {line: 12377}
// push constant 116
@116
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12390}
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
// {line: 12396}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12409}
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
// {line: 12415}
// push constant 110
@110
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12428}
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
// {line: 12434}
// push constant 117
@117
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12447}
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
// {line: 12453}
// push constant 109
@109
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12466}
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
// {line: 12472}
// push constant 98
@98
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12485}
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
// {line: 12491}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12504}
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
// {line: 12510}
// push constant 114
@114
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12523}
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
// {line: 12529}
// push constant 58
@58
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12542}
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
// {line: 12548}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12561}
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
// {line: 12574}
// call Keyboard.readInt nArgs: 1
@1
D=A
@R14
M=D
@Keyboard.readInt
D=A
@R15
M=D
@Main.main.call.45
D=A
@call
0;JMP
(Main.main.call.45)
// {line: 12580}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 12589}
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
// {line: 12595}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12600}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 12608}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 12610}
// goto Main.main.while.0
@Main.main.while.0
0;JMP
// {line: 12611}
(Main.main.while.1)
// {line: 12617}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12625}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 12631}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12640}
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
// {line: 12641}
(Main.main.while.2)
// {line: 12650}
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
// {line: 12659}
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
// {line: 12666}
// lt
@Main.main.lt.1
D=A
@R14
M=D
@lt
0;JMP
(Main.main.lt.1)
// {line: 12669}
// not
@SP
A=M-1
M=!M
// {line: 12674}
// if-goto Main.main.while.3
@SP
AM=M-1
D=M
@Main.main.while.3
D;JNE
// {line: 12683}
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
// {line: 12689}
// push pointer 1
@4
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12694}
// pop temp 2
@SP
AM=M-1
D=M
@R7
M=D
// {line: 12703}
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
// {line: 12712}
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
// {line: 12717}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 12722}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 12731}
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
// {line: 12737}
// push temp 2
@7
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 12742}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 12747}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 12756}
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
// {line: 12765}
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
// {line: 12771}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12776}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 12784}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 12786}
// goto Main.main.while.2
@Main.main.while.2
0;JMP
// {line: 12787}
(Main.main.while.3)
// {line: 12793}
// push constant 18
@18
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12806}
// call String.new nArgs: 1
@1
D=A
@R14
M=D
@String.new
D=A
@R15
M=D
@Main.main.call.46
D=A
@call
0;JMP
(Main.main.call.46)
// {line: 12812}
// push constant 84
@84
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
@Main.main.call.47
D=A
@call
0;JMP
(Main.main.call.47)
// {line: 12831}
// push constant 104
@104
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
@Main.main.call.48
D=A
@call
0;JMP
(Main.main.call.48)
// {line: 12850}
// push constant 101
@101
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
@Main.main.call.49
D=A
@call
0;JMP
(Main.main.call.49)
// {line: 12869}
// push constant 32
@32
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
@Main.main.call.50
D=A
@call
0;JMP
(Main.main.call.50)
// {line: 12888}
// push constant 97
@97
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
@Main.main.call.51
D=A
@call
0;JMP
(Main.main.call.51)
// {line: 12907}
// push constant 118
@118
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
@Main.main.call.52
D=A
@call
0;JMP
(Main.main.call.52)
// {line: 12926}
// push constant 101
@101
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
@Main.main.call.53
D=A
@call
0;JMP
(Main.main.call.53)
// {line: 12945}
// push constant 114
@114
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12958}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.54
D=A
@call
0;JMP
(Main.main.call.54)
// {line: 12964}
// push constant 97
@97
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12977}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.55
D=A
@call
0;JMP
(Main.main.call.55)
// {line: 12983}
// push constant 103
@103
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 12996}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.56
D=A
@call
0;JMP
(Main.main.call.56)
// {line: 13002}
// push constant 101
@101
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13015}
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
// {line: 13021}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13034}
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
// {line: 13040}
// push constant 105
@105
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13053}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.59
D=A
@call
0;JMP
(Main.main.call.59)
// {line: 13059}
// push constant 115
@115
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13072}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.60
D=A
@call
0;JMP
(Main.main.call.60)
// {line: 13078}
// push constant 58
@58
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13091}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Main.main.call.61
D=A
@call
0;JMP
(Main.main.call.61)
// {line: 13097}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13110}
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
// {line: 13123}
// call Output.printString nArgs: 1
@1
D=A
@R14
M=D
@Output.printString
D=A
@R15
M=D
@Main.main.call.63
D=A
@call
0;JMP
(Main.main.call.63)
// {line: 13128}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 13137}
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
// {line: 13146}
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
// {line: 13159}
// call Math.divide nArgs: 2
@2
D=A
@R14
M=D
@Math.divide
D=A
@R15
M=D
@Main.main.call.64
D=A
@call
0;JMP
(Main.main.call.64)
// {line: 13172}
// call Output.printInt nArgs: 1
@1
D=A
@R14
M=D
@Output.printInt
D=A
@R15
M=D
@Main.main.call.65
D=A
@call
0;JMP
(Main.main.call.65)
// {line: 13177}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 13190}
// call Output.println nArgs: 0
@0
D=A
@R14
M=D
@Output.println
D=A
@R15
M=D
@Main.main.call.66
D=A
@call
0;JMP
(Main.main.call.66)
// {line: 13195}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 13201}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13203}
// return
@return
0;JMP
// {line: 13204}
// function Array.new nLocals: 0
(Array.new)
// {line: 13213}
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
// {line: 13219}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13226}
// gt
@Array.new.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Array.new.gt.0)
// {line: 13229}
// not
@SP
A=M-1
M=!M
// {line: 13234}
// if-goto Array.new.IF_TRUE0
@SP
AM=M-1
D=M
@Array.new.IF_TRUE0
D;JNE
// {line: 13236}
// goto Array.new.IF_FALSE0
@Array.new.IF_FALSE0
0;JMP
// {line: 13237}
(Array.new.IF_TRUE0)
// {line: 13243}
// push constant 2
@2
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13256}
// call Sys.error nArgs: 1
@1
D=A
@R14
M=D
@Sys.error
D=A
@R15
M=D
@Array.new.call.0
D=A
@call
0;JMP
(Array.new.call.0)
// {line: 13261}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 13262}
(Array.new.IF_FALSE0)
// {line: 13271}
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
// {line: 13284}
// call Memory.alloc nArgs: 1
@1
D=A
@R14
M=D
@Memory.alloc
D=A
@R15
M=D
@Array.new.call.1
D=A
@call
0;JMP
(Array.new.call.1)
// {line: 13286}
// return
@return
0;JMP
// {line: 13287}
// function Array.dispose nLocals: 0
(Array.dispose)
// {line: 13296}
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
// {line: 13301}
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// {line: 13307}
// push pointer 0
@3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13320}
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
// {line: 13325}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 13331}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13333}
// return
@return
0;JMP
// {line: 13334}
// function Memory.init nLocals: 0
(Memory.init)
// {line: 13340}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13345}
// pop static 0
@SP
AM=M-1
D=M
@Memory.static.0
M=D
// {line: 13351}
// push constant 2048
@2048
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13357}
// push static 0
@Memory.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13362}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 13368}
// push constant 14334
@14334
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13373}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 13378}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 13384}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13390}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 13396}
// push constant 2049
@2049
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13402}
// push static 0
@Memory.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13407}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 13413}
// push constant 2050
@2050
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13418}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 13423}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 13429}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13435}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 13441}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13443}
// return
@return
0;JMP
// {line: 13444}
// function Memory.peek nLocals: 0
(Memory.peek)
// {line: 13453}
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
// {line: 13459}
// push static 0
@Memory.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13464}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 13469}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 13478}
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
// {line: 13480}
// return
@return
0;JMP
// {line: 13481}
// function Memory.poke nLocals: 0
(Memory.poke)
// {line: 13490}
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
// {line: 13496}
// push static 0
@Memory.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13501}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 13510}
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
// {line: 13515}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 13520}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 13526}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13532}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 13538}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13540}
// return
@return
0;JMP
// {line: 13545}
// function Memory.alloc nLocals: 1
(Memory.alloc)
@SP
AM=M+1
A=A-1
M=0
// {line: 13554}
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
// {line: 13560}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13567}
// lt
@Memory.alloc.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Memory.alloc.lt.0)
// {line: 13572}
// if-goto Memory.alloc.IF_TRUE0
@SP
AM=M-1
D=M
@Memory.alloc.IF_TRUE0
D;JNE
// {line: 13574}
// goto Memory.alloc.IF_FALSE0
@Memory.alloc.IF_FALSE0
0;JMP
// {line: 13575}
(Memory.alloc.IF_TRUE0)
// {line: 13581}
// push constant 5
@5
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13594}
// call Sys.error nArgs: 1
@1
D=A
@R14
M=D
@Sys.error
D=A
@R15
M=D
@Memory.alloc.call.0
D=A
@call
0;JMP
(Memory.alloc.call.0)
// {line: 13599}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 13600}
(Memory.alloc.IF_FALSE0)
// {line: 13606}
// push constant 2048
@2048
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13612}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 13613}
(Memory.alloc.WHILE_EXP0)
// {line: 13619}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13628}
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
// {line: 13633}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 13638}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 13647}
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
// {line: 13656}
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
// {line: 13663}
// lt
@Memory.alloc.lt.1
D=A
@R14
M=D
@lt
0;JMP
(Memory.alloc.lt.1)
// {line: 13666}
// not
@SP
A=M-1
M=!M
// {line: 13671}
// if-goto Memory.alloc.WHILE_END0
@SP
AM=M-1
D=M
@Memory.alloc.WHILE_END0
D;JNE
// {line: 13677}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13686}
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
// {line: 13691}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 13696}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 13705}
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
// {line: 13711}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 13713}
// goto Memory.alloc.WHILE_EXP0
@Memory.alloc.WHILE_EXP0
0;JMP
// {line: 13714}
(Memory.alloc.WHILE_END0)
// {line: 13723}
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
// {line: 13732}
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
// {line: 13737}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 13743}
// push constant 16379
@16379
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13750}
// gt
@Memory.alloc.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Memory.alloc.gt.0)
// {line: 13755}
// if-goto Memory.alloc.IF_TRUE1
@SP
AM=M-1
D=M
@Memory.alloc.IF_TRUE1
D;JNE
// {line: 13757}
// goto Memory.alloc.IF_FALSE1
@Memory.alloc.IF_FALSE1
0;JMP
// {line: 13758}
(Memory.alloc.IF_TRUE1)
// {line: 13764}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13777}
// call Sys.error nArgs: 1
@1
D=A
@R14
M=D
@Sys.error
D=A
@R15
M=D
@Memory.alloc.call.1
D=A
@call
0;JMP
(Memory.alloc.call.1)
// {line: 13782}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 13783}
(Memory.alloc.IF_FALSE1)
// {line: 13789}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13798}
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
// {line: 13803}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 13808}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 13817}
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
// {line: 13826}
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
// {line: 13832}
// push constant 2
@2
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13837}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 13844}
// gt
@Memory.alloc.gt.1
D=A
@R14
M=D
@gt
0;JMP
(Memory.alloc.gt.1)
// {line: 13849}
// if-goto Memory.alloc.IF_TRUE2
@SP
AM=M-1
D=M
@Memory.alloc.IF_TRUE2
D;JNE
// {line: 13851}
// goto Memory.alloc.IF_FALSE2
@Memory.alloc.IF_FALSE2
0;JMP
// {line: 13852}
(Memory.alloc.IF_TRUE2)
// {line: 13861}
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
// {line: 13867}
// push constant 2
@2
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13872}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 13881}
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
// {line: 13886}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 13892}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13901}
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
// {line: 13906}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 13911}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 13920}
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
// {line: 13929}
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
// {line: 13934}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 13940}
// push constant 2
@2
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13945}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 13950}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 13955}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 13961}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 13967}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 13973}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 13982}
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
// {line: 13987}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 13992}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 14001}
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
// {line: 14010}
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
// {line: 14016}
// push constant 2
@2
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14021}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14028}
// eq
@Memory.alloc.eq.0
D=A
@R14
M=D
@eq
0;JMP
(Memory.alloc.eq.0)
// {line: 14033}
// if-goto Memory.alloc.IF_TRUE3
@SP
AM=M-1
D=M
@Memory.alloc.IF_TRUE3
D;JNE
// {line: 14035}
// goto Memory.alloc.IF_FALSE3
@Memory.alloc.IF_FALSE3
0;JMP
// {line: 14036}
(Memory.alloc.IF_TRUE3)
// {line: 14045}
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
// {line: 14051}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14056}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14065}
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
// {line: 14070}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14079}
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
// {line: 14088}
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
// {line: 14093}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14099}
// push constant 4
@4
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14104}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14109}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 14114}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 14120}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14126}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 14128}
// goto Memory.alloc.IF_END3
@Memory.alloc.IF_END3
0;JMP
// {line: 14129}
(Memory.alloc.IF_FALSE3)
// {line: 14138}
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
// {line: 14144}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14149}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14158}
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
// {line: 14163}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14169}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14178}
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
// {line: 14183}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14188}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 14197}
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
// {line: 14202}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 14207}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 14213}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14219}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 14220}
(Memory.alloc.IF_END3)
// {line: 14226}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14235}
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
// {line: 14240}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14249}
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
// {line: 14258}
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
// {line: 14263}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14269}
// push constant 2
@2
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14274}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14279}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 14284}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 14290}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14296}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 14297}
(Memory.alloc.IF_FALSE2)
// {line: 14303}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14312}
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
// {line: 14317}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14323}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14328}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 14333}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 14339}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14345}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 14354}
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
// {line: 14360}
// push constant 2
@2
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14365}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14367}
// return
@return
0;JMP
// {line: 14376}
// function Memory.deAlloc nLocals: 2
(Memory.deAlloc)
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
// {line: 14385}
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
// {line: 14391}
// push constant 2
@2
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14396}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 14402}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 14408}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14417}
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
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14427}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 14436}
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
// {line: 14443}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 14449}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14458}
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
// {line: 14463}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14468}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 14477}
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
// {line: 14483}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14490}
// eq
@Memory.deAlloc.eq.0
D=A
@R14
M=D
@eq
0;JMP
(Memory.deAlloc.eq.0)
// {line: 14495}
// if-goto Memory.deAlloc.IF_TRUE0
@SP
AM=M-1
D=M
@Memory.deAlloc.IF_TRUE0
D;JNE
// {line: 14497}
// goto Memory.deAlloc.IF_FALSE0
@Memory.deAlloc.IF_FALSE0
0;JMP
// {line: 14498}
(Memory.deAlloc.IF_TRUE0)
// {line: 14504}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14513}
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
// {line: 14518}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14524}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14533}
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
// {line: 14538}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14543}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 14552}
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
// {line: 14561}
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
// {line: 14566}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 14572}
// push constant 2
@2
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14577}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 14582}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 14587}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 14593}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14599}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 14601}
// goto Memory.deAlloc.IF_END0
@Memory.deAlloc.IF_END0
0;JMP
// {line: 14602}
(Memory.deAlloc.IF_FALSE0)
// {line: 14608}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14617}
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
// {line: 14622}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14628}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14637}
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
// {line: 14642}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14647}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 14656}
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
// {line: 14665}
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
// {line: 14670}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 14676}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14685}
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
// {line: 14690}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14695}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 14704}
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
// {line: 14709}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14714}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 14719}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 14725}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14731}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 14737}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14746}
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
// {line: 14751}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14756}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 14765}
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
// {line: 14774}
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
// {line: 14780}
// push constant 2
@2
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14785}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14792}
// eq
@Memory.deAlloc.eq.1
D=A
@R14
M=D
@eq
0;JMP
(Memory.deAlloc.eq.1)
// {line: 14797}
// if-goto Memory.deAlloc.IF_TRUE1
@SP
AM=M-1
D=M
@Memory.deAlloc.IF_TRUE1
D;JNE
// {line: 14799}
// goto Memory.deAlloc.IF_FALSE1
@Memory.deAlloc.IF_FALSE1
0;JMP
// {line: 14800}
(Memory.deAlloc.IF_TRUE1)
// {line: 14806}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14815}
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
// {line: 14820}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14829}
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
// {line: 14835}
// push constant 2
@2
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14840}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14845}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 14850}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 14856}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14862}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 14864}
// goto Memory.deAlloc.IF_END1
@Memory.deAlloc.IF_END1
0;JMP
// {line: 14865}
(Memory.deAlloc.IF_FALSE1)
// {line: 14871}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14880}
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
// {line: 14885}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14891}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14900}
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
// {line: 14905}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 14910}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 14919}
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
// {line: 14924}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 14929}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 14935}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 14941}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 14942}
(Memory.deAlloc.IF_END1)
// {line: 14943}
(Memory.deAlloc.IF_END0)
// {line: 14949}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14951}
// return
@return
0;JMP
// {line: 14952}
// function String.new nLocals: 0
(String.new)
// {line: 14958}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14971}
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
// {line: 14976}
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// {line: 14985}
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
// {line: 14991}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 14998}
// lt
@String.new.lt.0
D=A
@R14
M=D
@lt
0;JMP
(String.new.lt.0)
// {line: 15003}
// if-goto String.new.IF_TRUE0
@SP
AM=M-1
D=M
@String.new.IF_TRUE0
D;JNE
// {line: 15005}
// goto String.new.IF_FALSE0
@String.new.IF_FALSE0
0;JMP
// {line: 15006}
(String.new.IF_TRUE0)
// {line: 15012}
// push constant 14
@14
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15025}
// call Sys.error nArgs: 1
@1
D=A
@R14
M=D
@Sys.error
D=A
@R15
M=D
@String.new.call.1
D=A
@call
0;JMP
(String.new.call.1)
// {line: 15030}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 15031}
(String.new.IF_FALSE0)
// {line: 15040}
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
// {line: 15046}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15053}
// gt
@String.new.gt.0
D=A
@R14
M=D
@gt
0;JMP
(String.new.gt.0)
// {line: 15058}
// if-goto String.new.IF_TRUE1
@SP
AM=M-1
D=M
@String.new.IF_TRUE1
D;JNE
// {line: 15060}
// goto String.new.IF_FALSE1
@String.new.IF_FALSE1
0;JMP
// {line: 15061}
(String.new.IF_TRUE1)
// {line: 15070}
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
// {line: 15083}
// call Array.new nArgs: 1
@1
D=A
@R14
M=D
@Array.new
D=A
@R15
M=D
@String.new.call.2
D=A
@call
0;JMP
(String.new.call.2)
// {line: 15090}
// pop this 1
@SP
AM=M-1
D=M
@THIS
A=M
A=A+1
M=D
// {line: 15091}
(String.new.IF_FALSE1)
// {line: 15100}
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
// {line: 15106}
// pop this 0
@SP
AM=M-1
D=M
@THIS
A=M
M=D
// {line: 15112}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15120}
// pop this 2
@SP
AM=M-1
D=M
@THIS
A=M
A=A+1
A=A+1
M=D
// {line: 15126}
// push pointer 0
@3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15128}
// return
@return
0;JMP
// {line: 15129}
// function String.dispose nLocals: 0
(String.dispose)
// {line: 15138}
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
// {line: 15143}
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// {line: 15152}
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
// {line: 15158}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15165}
// gt
@String.dispose.gt.0
D=A
@R14
M=D
@gt
0;JMP
(String.dispose.gt.0)
// {line: 15170}
// if-goto String.dispose.IF_TRUE0
@SP
AM=M-1
D=M
@String.dispose.IF_TRUE0
D;JNE
// {line: 15172}
// goto String.dispose.IF_FALSE0
@String.dispose.IF_FALSE0
0;JMP
// {line: 15173}
(String.dispose.IF_TRUE0)
// {line: 15182}
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
// {line: 15195}
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
// {line: 15200}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 15201}
(String.dispose.IF_FALSE0)
// {line: 15207}
// push pointer 0
@3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15220}
// call Memory.deAlloc nArgs: 1
@1
D=A
@R14
M=D
@Memory.deAlloc
D=A
@R15
M=D
@String.dispose.call.1
D=A
@call
0;JMP
(String.dispose.call.1)
// {line: 15225}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 15231}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15233}
// return
@return
0;JMP
// {line: 15234}
// function String.length nLocals: 0
(String.length)
// {line: 15243}
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
// {line: 15248}
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// {line: 15257}
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
// {line: 15259}
// return
@return
0;JMP
// {line: 15260}
// function String.charAt nLocals: 0
(String.charAt)
// {line: 15269}
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
// {line: 15274}
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// {line: 15283}
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
// {line: 15289}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15296}
// lt
@String.charAt.lt.0
D=A
@R14
M=D
@lt
0;JMP
(String.charAt.lt.0)
// {line: 15305}
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
// {line: 15314}
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
// {line: 15321}
// gt
@String.charAt.gt.0
D=A
@R14
M=D
@gt
0;JMP
(String.charAt.gt.0)
// {line: 15326}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 15335}
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
// {line: 15344}
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
// {line: 15351}
// eq
@String.charAt.eq.0
D=A
@R14
M=D
@eq
0;JMP
(String.charAt.eq.0)
// {line: 15356}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 15361}
// if-goto String.charAt.IF_TRUE0
@SP
AM=M-1
D=M
@String.charAt.IF_TRUE0
D;JNE
// {line: 15363}
// goto String.charAt.IF_FALSE0
@String.charAt.IF_FALSE0
0;JMP
// {line: 15364}
(String.charAt.IF_TRUE0)
// {line: 15370}
// push constant 15
@15
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15383}
// call Sys.error nArgs: 1
@1
D=A
@R14
M=D
@Sys.error
D=A
@R15
M=D
@String.charAt.call.0
D=A
@call
0;JMP
(String.charAt.call.0)
// {line: 15388}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 15389}
(String.charAt.IF_FALSE0)
// {line: 15398}
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
// {line: 15407}
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
// {line: 15412}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 15417}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 15426}
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
// {line: 15428}
// return
@return
0;JMP
// {line: 15429}
// function String.setCharAt nLocals: 0
(String.setCharAt)
// {line: 15438}
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
// {line: 15443}
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// {line: 15452}
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
// {line: 15458}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15465}
// lt
@String.setCharAt.lt.0
D=A
@R14
M=D
@lt
0;JMP
(String.setCharAt.lt.0)
// {line: 15474}
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
// {line: 15483}
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
// {line: 15490}
// gt
@String.setCharAt.gt.0
D=A
@R14
M=D
@gt
0;JMP
(String.setCharAt.gt.0)
// {line: 15495}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 15504}
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
// {line: 15513}
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
// {line: 15520}
// eq
@String.setCharAt.eq.0
D=A
@R14
M=D
@eq
0;JMP
(String.setCharAt.eq.0)
// {line: 15525}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 15530}
// if-goto String.setCharAt.IF_TRUE0
@SP
AM=M-1
D=M
@String.setCharAt.IF_TRUE0
D;JNE
// {line: 15532}
// goto String.setCharAt.IF_FALSE0
@String.setCharAt.IF_FALSE0
0;JMP
// {line: 15533}
(String.setCharAt.IF_TRUE0)
// {line: 15539}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15552}
// call Sys.error nArgs: 1
@1
D=A
@R14
M=D
@Sys.error
D=A
@R15
M=D
@String.setCharAt.call.0
D=A
@call
0;JMP
(String.setCharAt.call.0)
// {line: 15557}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 15558}
(String.setCharAt.IF_FALSE0)
// {line: 15567}
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
// {line: 15576}
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
// {line: 15581}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 15590}
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
// {line: 15595}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 15600}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 15606}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15612}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 15618}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15620}
// return
@return
0;JMP
// {line: 15621}
// function String.appendChar nLocals: 0
(String.appendChar)
// {line: 15630}
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
// {line: 15635}
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// {line: 15644}
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
// {line: 15653}
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
// {line: 15660}
// eq
@String.appendChar.eq.0
D=A
@R14
M=D
@eq
0;JMP
(String.appendChar.eq.0)
// {line: 15665}
// if-goto String.appendChar.IF_TRUE0
@SP
AM=M-1
D=M
@String.appendChar.IF_TRUE0
D;JNE
// {line: 15667}
// goto String.appendChar.IF_FALSE0
@String.appendChar.IF_FALSE0
0;JMP
// {line: 15668}
(String.appendChar.IF_TRUE0)
// {line: 15674}
// push constant 17
@17
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15687}
// call Sys.error nArgs: 1
@1
D=A
@R14
M=D
@Sys.error
D=A
@R15
M=D
@String.appendChar.call.0
D=A
@call
0;JMP
(String.appendChar.call.0)
// {line: 15692}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 15693}
(String.appendChar.IF_FALSE0)
// {line: 15702}
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
// {line: 15711}
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
// {line: 15716}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 15725}
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
// {line: 15730}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 15735}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 15741}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15747}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 15756}
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
// {line: 15762}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15767}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 15775}
// pop this 2
@SP
AM=M-1
D=M
@THIS
A=M
A=A+1
A=A+1
M=D
// {line: 15781}
// push pointer 0
@3
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 15783}
// return
@return
0;JMP
// {line: 15784}
// function String.eraseLastChar nLocals: 0
(String.eraseLastChar)
// {line: 15793}
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
// {line: 15798}
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// {line: 15807}
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
// {line: 15813}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15820}
// eq
@String.eraseLastChar.eq.0
D=A
@R14
M=D
@eq
0;JMP
(String.eraseLastChar.eq.0)
// {line: 15825}
// if-goto String.eraseLastChar.IF_TRUE0
@SP
AM=M-1
D=M
@String.eraseLastChar.IF_TRUE0
D;JNE
// {line: 15827}
// goto String.eraseLastChar.IF_FALSE0
@String.eraseLastChar.IF_FALSE0
0;JMP
// {line: 15828}
(String.eraseLastChar.IF_TRUE0)
// {line: 15834}
// push constant 18
@18
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15847}
// call Sys.error nArgs: 1
@1
D=A
@R14
M=D
@Sys.error
D=A
@R15
M=D
@String.eraseLastChar.call.0
D=A
@call
0;JMP
(String.eraseLastChar.call.0)
// {line: 15852}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 15853}
(String.eraseLastChar.IF_FALSE0)
// {line: 15862}
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
// {line: 15868}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15873}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 15881}
// pop this 2
@SP
AM=M-1
D=M
@THIS
A=M
A=A+1
A=A+1
M=D
// {line: 15887}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15889}
// return
@return
0;JMP
// {line: 15910}
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
// {line: 15919}
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
// {line: 15924}
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// {line: 15933}
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
// {line: 15939}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15946}
// eq
@String.intValue.eq.0
D=A
@R14
M=D
@eq
0;JMP
(String.intValue.eq.0)
// {line: 15951}
// if-goto String.intValue.IF_TRUE0
@SP
AM=M-1
D=M
@String.intValue.IF_TRUE0
D;JNE
// {line: 15953}
// goto String.intValue.IF_FALSE0
@String.intValue.IF_FALSE0
0;JMP
// {line: 15954}
(String.intValue.IF_TRUE0)
// {line: 15960}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15962}
// return
@return
0;JMP
// {line: 15963}
(String.intValue.IF_FALSE0)
// {line: 15969}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15972}
// not
@SP
A=M-1
M=!M
// {line: 15981}
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
// {line: 15987}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 15996}
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
// {line: 16001}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 16006}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 16015}
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
// {line: 16021}
// push constant 45
@45
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16028}
// eq
@String.intValue.eq.1
D=A
@R14
M=D
@eq
0;JMP
(String.intValue.eq.1)
// {line: 16033}
// if-goto String.intValue.IF_TRUE1
@SP
AM=M-1
D=M
@String.intValue.IF_TRUE1
D;JNE
// {line: 16035}
// goto String.intValue.IF_FALSE1
@String.intValue.IF_FALSE1
0;JMP
// {line: 16036}
(String.intValue.IF_TRUE1)
// {line: 16042}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16045}
// not
@SP
A=M-1
M=!M
// {line: 16055}
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
// {line: 16061}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16067}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 16068}
(String.intValue.IF_FALSE1)
// {line: 16069}
(String.intValue.WHILE_EXP0)
// {line: 16078}
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
// {line: 16087}
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
// {line: 16094}
// lt
@String.intValue.lt.0
D=A
@R14
M=D
@lt
0;JMP
(String.intValue.lt.0)
// {line: 16103}
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
// {line: 16108}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 16111}
// not
@SP
A=M-1
M=!M
// {line: 16116}
// if-goto String.intValue.WHILE_END0
@SP
AM=M-1
D=M
@String.intValue.WHILE_END0
D;JNE
// {line: 16125}
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
// {line: 16134}
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
// {line: 16139}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 16144}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 16153}
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
// {line: 16159}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16164}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 16172}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 16181}
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
// {line: 16187}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16194}
// lt
@String.intValue.lt.1
D=A
@R14
M=D
@lt
0;JMP
(String.intValue.lt.1)
// {line: 16203}
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
// {line: 16209}
// push constant 9
@9
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16216}
// gt
@String.intValue.gt.0
D=A
@R14
M=D
@gt
0;JMP
(String.intValue.gt.0)
// {line: 16221}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 16224}
// not
@SP
A=M-1
M=!M
// {line: 16233}
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
// {line: 16242}
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
// {line: 16247}
// if-goto String.intValue.IF_TRUE2
@SP
AM=M-1
D=M
@String.intValue.IF_TRUE2
D;JNE
// {line: 16249}
// goto String.intValue.IF_FALSE2
@String.intValue.IF_FALSE2
0;JMP
// {line: 16250}
(String.intValue.IF_TRUE2)
// {line: 16259}
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
// {line: 16265}
// push constant 10
@10
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16278}
// call Math.multiply nArgs: 2
@2
D=A
@R14
M=D
@Math.multiply
D=A
@R15
M=D
@String.intValue.call.0
D=A
@call
0;JMP
(String.intValue.call.0)
// {line: 16287}
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
// {line: 16292}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 16299}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 16308}
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
// {line: 16314}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16319}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 16325}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 16326}
(String.intValue.IF_FALSE2)
// {line: 16328}
// goto String.intValue.WHILE_EXP0
@String.intValue.WHILE_EXP0
0;JMP
// {line: 16329}
(String.intValue.WHILE_END0)
// {line: 16338}
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
// {line: 16343}
// if-goto String.intValue.IF_TRUE3
@SP
AM=M-1
D=M
@String.intValue.IF_TRUE3
D;JNE
// {line: 16345}
// goto String.intValue.IF_FALSE3
@String.intValue.IF_FALSE3
0;JMP
// {line: 16346}
(String.intValue.IF_TRUE3)
// {line: 16355}
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
// {line: 16358}
// neg
@SP
A=M-1
M=-M
// {line: 16365}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 16366}
(String.intValue.IF_FALSE3)
// {line: 16375}
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
// {line: 16377}
// return
@return
0;JMP
// {line: 16394}
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
// {line: 16403}
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
// {line: 16408}
// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// {line: 16417}
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
// {line: 16423}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16430}
// eq
@String.setInt.eq.0
D=A
@R14
M=D
@eq
0;JMP
(String.setInt.eq.0)
// {line: 16435}
// if-goto String.setInt.IF_TRUE0
@SP
AM=M-1
D=M
@String.setInt.IF_TRUE0
D;JNE
// {line: 16437}
// goto String.setInt.IF_FALSE0
@String.setInt.IF_FALSE0
0;JMP
// {line: 16438}
(String.setInt.IF_TRUE0)
// {line: 16444}
// push constant 19
@19
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16457}
// call Sys.error nArgs: 1
@1
D=A
@R14
M=D
@Sys.error
D=A
@R15
M=D
@String.setInt.call.0
D=A
@call
0;JMP
(String.setInt.call.0)
// {line: 16462}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 16463}
(String.setInt.IF_FALSE0)
// {line: 16469}
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16482}
// call Array.new nArgs: 1
@1
D=A
@R14
M=D
@Array.new
D=A
@R15
M=D
@String.setInt.call.1
D=A
@call
0;JMP
(String.setInt.call.1)
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
// {line: 16499}
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
// {line: 16505}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16512}
// lt
@String.setInt.lt.0
D=A
@R14
M=D
@lt
0;JMP
(String.setInt.lt.0)
// {line: 16517}
// if-goto String.setInt.IF_TRUE1
@SP
AM=M-1
D=M
@String.setInt.IF_TRUE1
D;JNE
// {line: 16519}
// goto String.setInt.IF_FALSE1
@String.setInt.IF_FALSE1
0;JMP
// {line: 16520}
(String.setInt.IF_TRUE1)
// {line: 16526}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16529}
// not
@SP
A=M-1
M=!M
// {line: 16538}
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
// {line: 16547}
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
// {line: 16550}
// neg
@SP
A=M-1
M=-M
// {line: 16557}
// pop argument 1
@SP
AM=M-1
D=M
@ARG
A=M
A=A+1
M=D
// {line: 16558}
(String.setInt.IF_FALSE1)
// {line: 16567}
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
// {line: 16574}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 16575}
(String.setInt.WHILE_EXP0)
// {line: 16584}
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
// {line: 16590}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16597}
// gt
@String.setInt.gt.0
D=A
@R14
M=D
@gt
0;JMP
(String.setInt.gt.0)
// {line: 16600}
// not
@SP
A=M-1
M=!M
// {line: 16605}
// if-goto String.setInt.WHILE_END0
@SP
AM=M-1
D=M
@String.setInt.WHILE_END0
D;JNE
// {line: 16614}
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
// {line: 16620}
// push constant 10
@10
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16633}
// call Math.divide nArgs: 2
@2
D=A
@R14
M=D
@Math.divide
D=A
@R15
M=D
@String.setInt.call.2
D=A
@call
0;JMP
(String.setInt.call.2)
// {line: 16640}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 16649}
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
// {line: 16658}
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
// {line: 16663}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 16669}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16678}
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
// {line: 16687}
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
// {line: 16693}
// push constant 10
@10
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16706}
// call Math.multiply nArgs: 2
@2
D=A
@R14
M=D
@Math.multiply
D=A
@R15
M=D
@String.setInt.call.3
D=A
@call
0;JMP
(String.setInt.call.3)
// {line: 16711}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 16716}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 16721}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 16726}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 16732}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16738}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 16747}
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
// {line: 16753}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16758}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 16764}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 16773}
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
// {line: 16780}
// pop argument 1
@SP
AM=M-1
D=M
@ARG
A=M
A=A+1
M=D
// {line: 16782}
// goto String.setInt.WHILE_EXP0
@String.setInt.WHILE_EXP0
0;JMP
// {line: 16783}
(String.setInt.WHILE_END0)
// {line: 16792}
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
// {line: 16797}
// if-goto String.setInt.IF_TRUE2
@SP
AM=M-1
D=M
@String.setInt.IF_TRUE2
D;JNE
// {line: 16799}
// goto String.setInt.IF_FALSE2
@String.setInt.IF_FALSE2
0;JMP
// {line: 16800}
(String.setInt.IF_TRUE2)
// {line: 16809}
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
// {line: 16818}
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
// {line: 16823}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 16829}
// push constant 45
@45
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16834}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 16839}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 16845}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 16851}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 16860}
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
// {line: 16866}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16871}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 16877}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 16878}
(String.setInt.IF_FALSE2)
// {line: 16887}
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
// {line: 16896}
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
// {line: 16903}
// lt
@String.setInt.lt.1
D=A
@R14
M=D
@lt
0;JMP
(String.setInt.lt.1)
// {line: 16908}
// if-goto String.setInt.IF_TRUE3
@SP
AM=M-1
D=M
@String.setInt.IF_TRUE3
D;JNE
// {line: 16910}
// goto String.setInt.IF_FALSE3
@String.setInt.IF_FALSE3
0;JMP
// {line: 16911}
(String.setInt.IF_TRUE3)
// {line: 16917}
// push constant 19
@19
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16930}
// call Sys.error nArgs: 1
@1
D=A
@R14
M=D
@Sys.error
D=A
@R15
M=D
@String.setInt.call.4
D=A
@call
0;JMP
(String.setInt.call.4)
// {line: 16935}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 16936}
(String.setInt.IF_FALSE3)
// {line: 16945}
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
// {line: 16951}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16958}
// eq
@String.setInt.eq.1
D=A
@R14
M=D
@eq
0;JMP
(String.setInt.eq.1)
// {line: 16963}
// if-goto String.setInt.IF_TRUE4
@SP
AM=M-1
D=M
@String.setInt.IF_TRUE4
D;JNE
// {line: 16965}
// goto String.setInt.IF_FALSE4
@String.setInt.IF_FALSE4
0;JMP
// {line: 16966}
(String.setInt.IF_TRUE4)
// {line: 16972}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16981}
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
// {line: 16986}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 16992}
// push constant 48
@48
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 16997}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 17002}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 17008}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17014}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 17020}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17028}
// pop this 2
@SP
AM=M-1
D=M
@THIS
A=M
A=A+1
A=A+1
M=D
// {line: 17030}
// goto String.setInt.IF_END4
@String.setInt.IF_END4
0;JMP
// {line: 17031}
(String.setInt.IF_FALSE4)
// {line: 17037}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17045}
// pop this 2
@SP
AM=M-1
D=M
@THIS
A=M
A=A+1
A=A+1
M=D
// {line: 17046}
(String.setInt.WHILE_EXP1)
// {line: 17055}
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
// {line: 17064}
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
// {line: 17071}
// lt
@String.setInt.lt.2
D=A
@R14
M=D
@lt
0;JMP
(String.setInt.lt.2)
// {line: 17074}
// not
@SP
A=M-1
M=!M
// {line: 17079}
// if-goto String.setInt.WHILE_END1
@SP
AM=M-1
D=M
@String.setInt.WHILE_END1
D;JNE
// {line: 17088}
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
// {line: 17097}
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
// {line: 17102}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 17111}
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
// {line: 17120}
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
// {line: 17126}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17131}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 17136}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 17145}
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
// {line: 17150}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 17155}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 17164}
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
// {line: 17169}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 17174}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 17180}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17186}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 17195}
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
// {line: 17201}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17206}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 17214}
// pop this 2
@SP
AM=M-1
D=M
@THIS
A=M
A=A+1
A=A+1
M=D
// {line: 17216}
// goto String.setInt.WHILE_EXP1
@String.setInt.WHILE_EXP1
0;JMP
// {line: 17217}
(String.setInt.WHILE_END1)
// {line: 17218}
(String.setInt.IF_END4)
// {line: 17227}
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
// {line: 17240}
// call Array.dispose nArgs: 1
@1
D=A
@R14
M=D
@Array.dispose
D=A
@R15
M=D
@String.setInt.call.5
D=A
@call
0;JMP
(String.setInt.call.5)
// {line: 17245}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 17251}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17253}
// return
@return
0;JMP
// {line: 17254}
// function String.newLine nLocals: 0
(String.newLine)
// {line: 17260}
// push constant 128
@128
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17262}
// return
@return
0;JMP
// {line: 17263}
// function String.backSpace nLocals: 0
(String.backSpace)
// {line: 17269}
// push constant 129
@129
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17271}
// return
@return
0;JMP
// {line: 17272}
// function String.doubleQuote nLocals: 0
(String.doubleQuote)
// {line: 17278}
// push constant 34
@34
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17280}
// return
@return
0;JMP
// {line: 17285}
// function Math.init nLocals: 1
(Math.init)
@SP
AM=M+1
A=A-1
M=0
// {line: 17291}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17304}
// call Array.new nArgs: 1
@1
D=A
@R14
M=D
@Array.new
D=A
@R15
M=D
@Math.init.call.0
D=A
@call
0;JMP
(Math.init.call.0)
// {line: 17309}
// pop static 1
@SP
AM=M-1
D=M
@Math.static.1
M=D
// {line: 17315}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17328}
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
// {line: 17333}
// pop static 0
@SP
AM=M-1
D=M
@Math.static.0
M=D
// {line: 17339}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17345}
// push static 0
@Math.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17350}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 17356}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17361}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 17366}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 17372}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17378}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 17379}
(Math.init.WHILE_EXP0)
// {line: 17388}
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
// {line: 17394}
// push constant 15
@15
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17401}
// lt
@Math.init.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Math.init.lt.0)
// {line: 17404}
// not
@SP
A=M-1
M=!M
// {line: 17409}
// if-goto Math.init.WHILE_END0
@SP
AM=M-1
D=M
@Math.init.WHILE_END0
D;JNE
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
// {line: 17424}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17429}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 17435}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 17444}
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
// {line: 17450}
// push static 0
@Math.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17455}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 17464}
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
// {line: 17470}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17475}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 17481}
// push static 0
@Math.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17486}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 17491}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 17500}
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
// {line: 17509}
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
// {line: 17515}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17520}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 17526}
// push static 0
@Math.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17531}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 17536}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 17545}
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
// {line: 17550}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 17555}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 17560}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 17566}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17572}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 17574}
// goto Math.init.WHILE_EXP0
@Math.init.WHILE_EXP0
0;JMP
// {line: 17575}
(Math.init.WHILE_END0)
// {line: 17581}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17583}
// return
@return
0;JMP
// {line: 17584}
// function Math.abs nLocals: 0
(Math.abs)
// {line: 17593}
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
// {line: 17599}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17606}
// lt
@Math.abs.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Math.abs.lt.0)
// {line: 17611}
// if-goto Math.abs.IF_TRUE0
@SP
AM=M-1
D=M
@Math.abs.IF_TRUE0
D;JNE
// {line: 17613}
// goto Math.abs.IF_FALSE0
@Math.abs.IF_FALSE0
0;JMP
// {line: 17614}
(Math.abs.IF_TRUE0)
// {line: 17623}
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
// {line: 17626}
// neg
@SP
A=M-1
M=-M
// {line: 17632}
// pop argument 0
@SP
AM=M-1
D=M
@ARG
A=M
M=D
// {line: 17633}
(Math.abs.IF_FALSE0)
// {line: 17642}
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
// {line: 17644}
// return
@return
0;JMP
// {line: 17665}
// function Math.multiply nLocals: 5
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
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
// {line: 17674}
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
// {line: 17680}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17687}
// lt
@Math.multiply.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Math.multiply.lt.0)
// {line: 17696}
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
// {line: 17702}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17709}
// gt
@Math.multiply.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Math.multiply.gt.0)
// {line: 17714}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 17723}
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
// {line: 17729}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17736}
// gt
@Math.multiply.gt.1
D=A
@R14
M=D
@gt
0;JMP
(Math.multiply.gt.1)
// {line: 17745}
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
// {line: 17751}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 17758}
// lt
@Math.multiply.lt.1
D=A
@R14
M=D
@lt
0;JMP
(Math.multiply.lt.1)
// {line: 17763}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 17768}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 17778}
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
// {line: 17787}
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
// {line: 17800}
// call Math.abs nArgs: 1
@1
D=A
@R14
M=D
@Math.abs
D=A
@R15
M=D
@Math.multiply.call.0
D=A
@call
0;JMP
(Math.multiply.call.0)
// {line: 17806}
// pop argument 0
@SP
AM=M-1
D=M
@ARG
A=M
M=D
// {line: 17815}
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
// {line: 17828}
// call Math.abs nArgs: 1
@1
D=A
@R14
M=D
@Math.abs
D=A
@R15
M=D
@Math.multiply.call.1
D=A
@call
0;JMP
(Math.multiply.call.1)
// {line: 17835}
// pop argument 1
@SP
AM=M-1
D=M
@ARG
A=M
A=A+1
M=D
// {line: 17844}
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
// {line: 17853}
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
// {line: 17860}
// lt
@Math.multiply.lt.2
D=A
@R14
M=D
@lt
0;JMP
(Math.multiply.lt.2)
// {line: 17865}
// if-goto Math.multiply.IF_TRUE0
@SP
AM=M-1
D=M
@Math.multiply.IF_TRUE0
D;JNE
// {line: 17867}
// goto Math.multiply.IF_FALSE0
@Math.multiply.IF_FALSE0
0;JMP
// {line: 17868}
(Math.multiply.IF_TRUE0)
// {line: 17877}
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
// {line: 17884}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 17893}
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
// {line: 17899}
// pop argument 0
@SP
AM=M-1
D=M
@ARG
A=M
M=D
// {line: 17908}
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
// {line: 17915}
// pop argument 1
@SP
AM=M-1
D=M
@ARG
A=M
A=A+1
M=D
// {line: 17916}
(Math.multiply.IF_FALSE0)
// {line: 17917}
(Math.multiply.WHILE_EXP0)
// {line: 17926}
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
// {line: 17935}
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
// {line: 17942}
// lt
@Math.multiply.lt.3
D=A
@R14
M=D
@lt
0;JMP
(Math.multiply.lt.3)
// {line: 17945}
// not
@SP
A=M-1
M=!M
// {line: 17950}
// if-goto Math.multiply.WHILE_END0
@SP
AM=M-1
D=M
@Math.multiply.WHILE_END0
D;JNE
// {line: 17959}
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
// {line: 17965}
// push static 0
@Math.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 17970}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 17975}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 17984}
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
// {line: 17993}
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
// {line: 17998}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 18004}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18011}
// gt
@Math.multiply.gt.2
D=A
@R14
M=D
@gt
0;JMP
(Math.multiply.gt.2)
// {line: 18016}
// if-goto Math.multiply.IF_TRUE1
@SP
AM=M-1
D=M
@Math.multiply.IF_TRUE1
D;JNE
// {line: 18018}
// goto Math.multiply.IF_FALSE1
@Math.multiply.IF_FALSE1
0;JMP
// {line: 18019}
(Math.multiply.IF_TRUE1)
// {line: 18028}
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
// {line: 18037}
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
// {line: 18042}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 18048}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 18057}
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
// {line: 18066}
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
// {line: 18072}
// push static 0
@Math.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18077}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 18082}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 18091}
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
// {line: 18096}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 18104}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 18105}
(Math.multiply.IF_FALSE1)
// {line: 18114}
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
// {line: 18123}
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
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 18134}
// pop argument 0
@SP
AM=M-1
D=M
@ARG
A=M
M=D
// {line: 18143}
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
// {line: 18149}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18154}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 18163}
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
// {line: 18165}
// goto Math.multiply.WHILE_EXP0
@Math.multiply.WHILE_EXP0
0;JMP
// {line: 18166}
(Math.multiply.WHILE_END0)
// {line: 18175}
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
// {line: 18180}
// if-goto Math.multiply.IF_TRUE2
@SP
AM=M-1
D=M
@Math.multiply.IF_TRUE2
D;JNE
// {line: 18182}
// goto Math.multiply.IF_FALSE2
@Math.multiply.IF_FALSE2
0;JMP
// {line: 18183}
(Math.multiply.IF_TRUE2)
// {line: 18192}
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
// {line: 18195}
// neg
@SP
A=M-1
M=-M
// {line: 18201}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 18202}
(Math.multiply.IF_FALSE2)
// {line: 18211}
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
// {line: 18213}
// return
@return
0;JMP
// {line: 18230}
// function Math.divide nLocals: 4
(Math.divide)
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
// {line: 18239}
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
// {line: 18245}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18252}
// eq
@Math.divide.eq.0
D=A
@R14
M=D
@eq
0;JMP
(Math.divide.eq.0)
// {line: 18257}
// if-goto Math.divide.IF_TRUE0
@SP
AM=M-1
D=M
@Math.divide.IF_TRUE0
D;JNE
// {line: 18259}
// goto Math.divide.IF_FALSE0
@Math.divide.IF_FALSE0
0;JMP
// {line: 18260}
(Math.divide.IF_TRUE0)
// {line: 18266}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18279}
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
// {line: 18284}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 18285}
(Math.divide.IF_FALSE0)
// {line: 18294}
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
// {line: 18300}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18307}
// lt
@Math.divide.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Math.divide.lt.0)
// {line: 18316}
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
// {line: 18322}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18329}
// gt
@Math.divide.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Math.divide.gt.0)
// {line: 18334}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 18343}
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
// {line: 18349}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18356}
// gt
@Math.divide.gt.1
D=A
@R14
M=D
@gt
0;JMP
(Math.divide.gt.1)
// {line: 18365}
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
// {line: 18371}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18378}
// lt
@Math.divide.lt.1
D=A
@R14
M=D
@lt
0;JMP
(Math.divide.lt.1)
// {line: 18383}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 18388}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 18396}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 18402}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18408}
// push static 1
@Math.static.1
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18413}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 18422}
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
// {line: 18435}
// call Math.abs nArgs: 1
@1
D=A
@R14
M=D
@Math.abs
D=A
@R15
M=D
@Math.divide.call.1
D=A
@call
0;JMP
(Math.divide.call.1)
// {line: 18440}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 18445}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 18451}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18457}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 18466}
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
// {line: 18479}
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
// {line: 18485}
// pop argument 0
@SP
AM=M-1
D=M
@ARG
A=M
M=D
// {line: 18486}
(Math.divide.WHILE_EXP0)
// {line: 18495}
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
// {line: 18498}
// not
@SP
A=M-1
M=!M
// {line: 18501}
// not
@SP
A=M-1
M=!M
// {line: 18506}
// if-goto Math.divide.WHILE_END0
@SP
AM=M-1
D=M
@Math.divide.WHILE_END0
D;JNE
// {line: 18512}
// push constant 32767
@32767
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18521}
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
// {line: 18527}
// push static 1
@Math.static.1
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18532}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 18537}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 18546}
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
// {line: 18551}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 18560}
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
// {line: 18566}
// push static 1
@Math.static.1
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18571}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 18576}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 18585}
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
// {line: 18592}
// lt
@Math.divide.lt.2
D=A
@R14
M=D
@lt
0;JMP
(Math.divide.lt.2)
// {line: 18601}
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
// {line: 18610}
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
// {line: 18613}
// not
@SP
A=M-1
M=!M
// {line: 18618}
// if-goto Math.divide.IF_TRUE1
@SP
AM=M-1
D=M
@Math.divide.IF_TRUE1
D;JNE
// {line: 18620}
// goto Math.divide.IF_FALSE1
@Math.divide.IF_FALSE1
0;JMP
// {line: 18621}
(Math.divide.IF_TRUE1)
// {line: 18630}
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
// {line: 18636}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18641}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 18647}
// push static 1
@Math.static.1
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18652}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 18661}
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
// {line: 18667}
// push static 1
@Math.static.1
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18672}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 18677}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 18686}
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
// {line: 18695}
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
// {line: 18701}
// push static 1
@Math.static.1
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18706}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 18711}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 18720}
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
// {line: 18725}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 18730}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 18735}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 18741}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18747}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 18756}
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
// {line: 18762}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18767}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 18773}
// push static 1
@Math.static.1
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18778}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 18783}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 18792}
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
// {line: 18801}
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
// {line: 18808}
// gt
@Math.divide.gt.2
D=A
@R14
M=D
@gt
0;JMP
(Math.divide.gt.2)
// {line: 18817}
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
// {line: 18826}
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
// {line: 18829}
// not
@SP
A=M-1
M=!M
// {line: 18834}
// if-goto Math.divide.IF_TRUE2
@SP
AM=M-1
D=M
@Math.divide.IF_TRUE2
D;JNE
// {line: 18836}
// goto Math.divide.IF_FALSE2
@Math.divide.IF_FALSE2
0;JMP
// {line: 18837}
(Math.divide.IF_TRUE2)
// {line: 18846}
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
// {line: 18852}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18857}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 18863}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 18864}
(Math.divide.IF_FALSE2)
// {line: 18865}
(Math.divide.IF_FALSE1)
// {line: 18867}
// goto Math.divide.WHILE_EXP0
@Math.divide.WHILE_EXP0
0;JMP
// {line: 18868}
(Math.divide.WHILE_END0)
// {line: 18869}
(Math.divide.WHILE_EXP1)
// {line: 18878}
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
// {line: 18884}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 18887}
// neg
@SP
A=M-1
M=-M
// {line: 18894}
// gt
@Math.divide.gt.3
D=A
@R14
M=D
@gt
0;JMP
(Math.divide.gt.3)
// {line: 18897}
// not
@SP
A=M-1
M=!M
// {line: 18902}
// if-goto Math.divide.WHILE_END1
@SP
AM=M-1
D=M
@Math.divide.WHILE_END1
D;JNE
// {line: 18911}
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
// {line: 18917}
// push static 1
@Math.static.1
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18922}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 18927}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 18936}
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
// {line: 18945}
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
// {line: 18952}
// gt
@Math.divide.gt.4
D=A
@R14
M=D
@gt
0;JMP
(Math.divide.gt.4)
// {line: 18955}
// not
@SP
A=M-1
M=!M
// {line: 18960}
// if-goto Math.divide.IF_TRUE3
@SP
AM=M-1
D=M
@Math.divide.IF_TRUE3
D;JNE
// {line: 18962}
// goto Math.divide.IF_FALSE3
@Math.divide.IF_FALSE3
0;JMP
// {line: 18963}
(Math.divide.IF_TRUE3)
// {line: 18972}
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
// {line: 18987}
// push static 0
@Math.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 18992}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 18997}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 19006}
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
// {line: 19011}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 19018}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 19027}
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
// {line: 19036}
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
// {line: 19042}
// push static 1
@Math.static.1
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 19047}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 19052}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 19061}
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
// {line: 19066}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 19072}
// pop argument 0
@SP
AM=M-1
D=M
@ARG
A=M
M=D
// {line: 19073}
(Math.divide.IF_FALSE3)
// {line: 19082}
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
// {line: 19088}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19093}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 19099}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 19101}
// goto Math.divide.WHILE_EXP1
@Math.divide.WHILE_EXP1
0;JMP
// {line: 19102}
(Math.divide.WHILE_END1)
// {line: 19111}
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
// {line: 19116}
// if-goto Math.divide.IF_TRUE4
@SP
AM=M-1
D=M
@Math.divide.IF_TRUE4
D;JNE
// {line: 19118}
// goto Math.divide.IF_FALSE4
@Math.divide.IF_FALSE4
0;JMP
// {line: 19119}
(Math.divide.IF_TRUE4)
// {line: 19128}
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
// {line: 19131}
// neg
@SP
A=M-1
M=-M
// {line: 19138}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 19139}
(Math.divide.IF_FALSE4)
// {line: 19148}
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
// {line: 19150}
// return
@return
0;JMP
// {line: 19167}
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
// {line: 19176}
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
// {line: 19182}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19189}
// lt
@Math.sqrt.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Math.sqrt.lt.0)
// {line: 19194}
// if-goto Math.sqrt.IF_TRUE0
@SP
AM=M-1
D=M
@Math.sqrt.IF_TRUE0
D;JNE
// {line: 19196}
// goto Math.sqrt.IF_FALSE0
@Math.sqrt.IF_FALSE0
0;JMP
// {line: 19197}
(Math.sqrt.IF_TRUE0)
// {line: 19203}
// push constant 4
@4
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19216}
// call Sys.error nArgs: 1
@1
D=A
@R14
M=D
@Sys.error
D=A
@R15
M=D
@Math.sqrt.call.0
D=A
@call
0;JMP
(Math.sqrt.call.0)
// {line: 19221}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 19222}
(Math.sqrt.IF_FALSE0)
// {line: 19228}
// push constant 7
@7
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19234}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 19235}
(Math.sqrt.WHILE_EXP0)
// {line: 19244}
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
// {line: 19250}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19253}
// neg
@SP
A=M-1
M=-M
// {line: 19260}
// gt
@Math.sqrt.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Math.sqrt.gt.0)
// {line: 19263}
// not
@SP
A=M-1
M=!M
// {line: 19268}
// if-goto Math.sqrt.WHILE_END0
@SP
AM=M-1
D=M
@Math.sqrt.WHILE_END0
D;JNE
// {line: 19277}
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
// {line: 19286}
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
// {line: 19292}
// push static 0
@Math.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 19297}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 19302}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 19311}
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
// {line: 19316}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 19323}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 19332}
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
// {line: 19341}
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
// {line: 19354}
// call Math.multiply nArgs: 2
@2
D=A
@R14
M=D
@Math.multiply
D=A
@R15
M=D
@Math.sqrt.call.1
D=A
@call
0;JMP
(Math.sqrt.call.1)
// {line: 19362}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 19371}
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
// {line: 19380}
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
// {line: 19387}
// gt
@Math.sqrt.gt.1
D=A
@R14
M=D
@gt
0;JMP
(Math.sqrt.gt.1)
// {line: 19390}
// not
@SP
A=M-1
M=!M
// {line: 19399}
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
// {line: 19405}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19412}
// lt
@Math.sqrt.lt.1
D=A
@R14
M=D
@lt
0;JMP
(Math.sqrt.lt.1)
// {line: 19415}
// not
@SP
A=M-1
M=!M
// {line: 19420}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 19425}
// if-goto Math.sqrt.IF_TRUE1
@SP
AM=M-1
D=M
@Math.sqrt.IF_TRUE1
D;JNE
// {line: 19427}
// goto Math.sqrt.IF_FALSE1
@Math.sqrt.IF_FALSE1
0;JMP
// {line: 19428}
(Math.sqrt.IF_TRUE1)
// {line: 19437}
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
// {line: 19446}
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
// {line: 19447}
(Math.sqrt.IF_FALSE1)
// {line: 19456}
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
// {line: 19462}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19467}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 19473}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 19475}
// goto Math.sqrt.WHILE_EXP0
@Math.sqrt.WHILE_EXP0
0;JMP
// {line: 19476}
(Math.sqrt.WHILE_END0)
// {line: 19485}
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
// {line: 19487}
// return
@return
0;JMP
// {line: 19488}
// function Math.max nLocals: 0
(Math.max)
// {line: 19497}
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
// {line: 19506}
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
// {line: 19513}
// gt
@Math.max.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Math.max.gt.0)
// {line: 19518}
// if-goto Math.max.IF_TRUE0
@SP
AM=M-1
D=M
@Math.max.IF_TRUE0
D;JNE
// {line: 19520}
// goto Math.max.IF_FALSE0
@Math.max.IF_FALSE0
0;JMP
// {line: 19521}
(Math.max.IF_TRUE0)
// {line: 19530}
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
// {line: 19537}
// pop argument 1
@SP
AM=M-1
D=M
@ARG
A=M
A=A+1
M=D
// {line: 19538}
(Math.max.IF_FALSE0)
// {line: 19547}
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
// {line: 19549}
// return
@return
0;JMP
// {line: 19550}
// function Math.min nLocals: 0
(Math.min)
// {line: 19559}
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
// {line: 19568}
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
// {line: 19575}
// lt
@Math.min.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Math.min.lt.0)
// {line: 19580}
// if-goto Math.min.IF_TRUE0
@SP
AM=M-1
D=M
@Math.min.IF_TRUE0
D;JNE
// {line: 19582}
// goto Math.min.IF_FALSE0
@Math.min.IF_FALSE0
0;JMP
// {line: 19583}
(Math.min.IF_TRUE0)
// {line: 19592}
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
// {line: 19599}
// pop argument 1
@SP
AM=M-1
D=M
@ARG
A=M
A=A+1
M=D
// {line: 19600}
(Math.min.IF_FALSE0)
// {line: 19609}
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
// {line: 19611}
// return
@return
0;JMP
// {line: 19616}
// function Screen.init nLocals: 1
(Screen.init)
@SP
AM=M+1
A=A-1
M=0
// {line: 19622}
// push constant 16384
@16384
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19627}
// pop static 1
@SP
AM=M-1
D=M
@Screen.static.1
M=D
// {line: 19633}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19636}
// not
@SP
A=M-1
M=!M
// {line: 19641}
// pop static 2
@SP
AM=M-1
D=M
@Screen.static.2
M=D
// {line: 19647}
// push constant 17
@17
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19660}
// call Array.new nArgs: 1
@1
D=A
@R14
M=D
@Array.new
D=A
@R15
M=D
@Screen.init.call.0
D=A
@call
0;JMP
(Screen.init.call.0)
// {line: 19665}
// pop static 0
@SP
AM=M-1
D=M
@Screen.static.0
M=D
// {line: 19671}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19677}
// push static 0
@Screen.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 19682}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 19688}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19693}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 19698}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 19704}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 19710}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 19711}
(Screen.init.WHILE_EXP0)
// {line: 19720}
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
// {line: 19726}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19733}
// lt
@Screen.init.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Screen.init.lt.0)
// {line: 19736}
// not
@SP
A=M-1
M=!M
// {line: 19741}
// if-goto Screen.init.WHILE_END0
@SP
AM=M-1
D=M
@Screen.init.WHILE_END0
D;JNE
// {line: 19750}
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
// {line: 19756}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19761}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 19767}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 19776}
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
// {line: 19782}
// push static 0
@Screen.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 19787}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 19796}
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
// {line: 19802}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19807}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 19813}
// push static 0
@Screen.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 19818}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 19823}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 19832}
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
// {line: 19841}
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
// {line: 19847}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19852}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 19858}
// push static 0
@Screen.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 19863}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 19868}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 19877}
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
// {line: 19882}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 19887}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 19892}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 19898}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 19904}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 19906}
// goto Screen.init.WHILE_EXP0
@Screen.init.WHILE_EXP0
0;JMP
// {line: 19907}
(Screen.init.WHILE_END0)
// {line: 19913}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19915}
// return
@return
0;JMP
// {line: 19920}
// function Screen.clearScreen nLocals: 1
(Screen.clearScreen)
@SP
AM=M+1
A=A-1
M=0
// {line: 19921}
(Screen.clearScreen.WHILE_EXP0)
// {line: 19930}
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
// {line: 19936}
// push constant 8192
@8192
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19943}
// lt
@Screen.clearScreen.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Screen.clearScreen.lt.0)
// {line: 19946}
// not
@SP
A=M-1
M=!M
// {line: 19951}
// if-goto Screen.clearScreen.WHILE_END0
@SP
AM=M-1
D=M
@Screen.clearScreen.WHILE_END0
D;JNE
// {line: 19960}
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
// {line: 19966}
// push static 1
@Screen.static.1
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 19971}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 19977}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 19982}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 19987}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 19993}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 19999}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 20008}
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
// {line: 20014}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20019}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 20025}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 20027}
// goto Screen.clearScreen.WHILE_EXP0
@Screen.clearScreen.WHILE_EXP0
0;JMP
// {line: 20028}
(Screen.clearScreen.WHILE_END0)
// {line: 20034}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20036}
// return
@return
0;JMP
// {line: 20037}
// function Screen.updateLocation nLocals: 0
(Screen.updateLocation)
// {line: 20043}
// push static 2
@Screen.static.2
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20048}
// if-goto Screen.updateLocation.IF_TRUE0
@SP
AM=M-1
D=M
@Screen.updateLocation.IF_TRUE0
D;JNE
// {line: 20050}
// goto Screen.updateLocation.IF_FALSE0
@Screen.updateLocation.IF_FALSE0
0;JMP
// {line: 20051}
(Screen.updateLocation.IF_TRUE0)
// {line: 20060}
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
// {line: 20066}
// push static 1
@Screen.static.1
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20071}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 20080}
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
// {line: 20086}
// push static 1
@Screen.static.1
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20091}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 20096}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 20105}
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
// {line: 20114}
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
// {line: 20119}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 20124}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 20129}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 20135}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20141}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 20143}
// goto Screen.updateLocation.IF_END0
@Screen.updateLocation.IF_END0
0;JMP
// {line: 20144}
(Screen.updateLocation.IF_FALSE0)
// {line: 20153}
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
// {line: 20159}
// push static 1
@Screen.static.1
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20164}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 20173}
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
// {line: 20179}
// push static 1
@Screen.static.1
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20184}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 20189}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 20198}
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
// {line: 20207}
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
// {line: 20210}
// not
@SP
A=M-1
M=!M
// {line: 20215}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 20220}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 20225}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 20231}
// push temp 0
@5
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20237}
// pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// {line: 20238}
(Screen.updateLocation.IF_END0)
// {line: 20244}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20246}
// return
@return
0;JMP
// {line: 20247}
// function Screen.setColor nLocals: 0
(Screen.setColor)
// {line: 20256}
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
// {line: 20261}
// pop static 2
@SP
AM=M-1
D=M
@Screen.static.2
M=D
// {line: 20267}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20269}
// return
@return
0;JMP
// {line: 20282}
// function Screen.drawPixel nLocals: 3
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
// {line: 20291}
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
// {line: 20297}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20304}
// lt
@Screen.drawPixel.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawPixel.lt.0)
// {line: 20313}
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
// {line: 20319}
// push constant 511
@511
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20326}
// gt
@Screen.drawPixel.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Screen.drawPixel.gt.0)
// {line: 20331}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 20340}
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
// {line: 20346}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20353}
// lt
@Screen.drawPixel.lt.1
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawPixel.lt.1)
// {line: 20358}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 20367}
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
// {line: 20373}
// push constant 255
@255
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20380}
// gt
@Screen.drawPixel.gt.1
D=A
@R14
M=D
@gt
0;JMP
(Screen.drawPixel.gt.1)
// {line: 20385}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 20390}
// if-goto Screen.drawPixel.IF_TRUE0
@SP
AM=M-1
D=M
@Screen.drawPixel.IF_TRUE0
D;JNE
// {line: 20392}
// goto Screen.drawPixel.IF_FALSE0
@Screen.drawPixel.IF_FALSE0
0;JMP
// {line: 20393}
(Screen.drawPixel.IF_TRUE0)
// {line: 20399}
// push constant 7
@7
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20412}
// call Sys.error nArgs: 1
@1
D=A
@R14
M=D
@Sys.error
D=A
@R15
M=D
@Screen.drawPixel.call.0
D=A
@call
0;JMP
(Screen.drawPixel.call.0)
// {line: 20417}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 20418}
(Screen.drawPixel.IF_FALSE0)
// {line: 20427}
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
// {line: 20433}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20446}
// call Math.divide nArgs: 2
@2
D=A
@R14
M=D
@Math.divide
D=A
@R15
M=D
@Screen.drawPixel.call.1
D=A
@call
0;JMP
(Screen.drawPixel.call.1)
// {line: 20452}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 20461}
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
// {line: 20470}
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
// {line: 20476}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20489}
// call Math.multiply nArgs: 2
@2
D=A
@R14
M=D
@Math.multiply
D=A
@R15
M=D
@Screen.drawPixel.call.2
D=A
@call
0;JMP
(Screen.drawPixel.call.2)
// {line: 20494}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 20501}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 20510}
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
// {line: 20516}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20529}
// call Math.multiply nArgs: 2
@2
D=A
@R14
M=D
@Math.multiply
D=A
@R15
M=D
@Screen.drawPixel.call.3
D=A
@call
0;JMP
(Screen.drawPixel.call.3)
// {line: 20538}
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
// {line: 20543}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 20551}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 20560}
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
// {line: 20569}
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
// {line: 20575}
// push static 0
@Screen.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 20580}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 20585}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 20594}
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
// {line: 20607}
// call Screen.updateLocation nArgs: 2
@2
D=A
@R14
M=D
@Screen.updateLocation
D=A
@R15
M=D
@Screen.drawPixel.call.4
D=A
@call
0;JMP
(Screen.drawPixel.call.4)
// {line: 20612}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 20618}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20620}
// return
@return
0;JMP
// {line: 20621}
// function Screen.drawConditional nLocals: 0
(Screen.drawConditional)
// {line: 20630}
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
// {line: 20635}
// if-goto Screen.drawConditional.IF_TRUE0
@SP
AM=M-1
D=M
@Screen.drawConditional.IF_TRUE0
D;JNE
// {line: 20637}
// goto Screen.drawConditional.IF_FALSE0
@Screen.drawConditional.IF_FALSE0
0;JMP
// {line: 20638}
(Screen.drawConditional.IF_TRUE0)
// {line: 20647}
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
// {line: 20656}
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
// {line: 20669}
// call Screen.drawPixel nArgs: 2
@2
D=A
@R14
M=D
@Screen.drawPixel
D=A
@R15
M=D
@Screen.drawConditional.call.0
D=A
@call
0;JMP
(Screen.drawConditional.call.0)
// {line: 20674}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 20676}
// goto Screen.drawConditional.IF_END0
@Screen.drawConditional.IF_END0
0;JMP
// {line: 20677}
(Screen.drawConditional.IF_FALSE0)
// {line: 20686}
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
// {line: 20695}
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
// {line: 20708}
// call Screen.drawPixel nArgs: 2
@2
D=A
@R14
M=D
@Screen.drawPixel
D=A
@R15
M=D
@Screen.drawConditional.call.1
D=A
@call
0;JMP
(Screen.drawConditional.call.1)
// {line: 20713}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 20714}
(Screen.drawConditional.IF_END0)
// {line: 20720}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20722}
// return
@return
0;JMP
// {line: 20767}
// function Screen.drawLine nLocals: 11
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
// {line: 20776}
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
// {line: 20782}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20789}
// lt
@Screen.drawLine.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawLine.lt.0)
// {line: 20798}
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
// {line: 20804}
// push constant 511
@511
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20811}
// gt
@Screen.drawLine.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Screen.drawLine.gt.0)
// {line: 20816}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 20825}
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
// {line: 20831}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20838}
// lt
@Screen.drawLine.lt.1
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawLine.lt.1)
// {line: 20843}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 20852}
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
// {line: 20858}
// push constant 255
@255
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20865}
// gt
@Screen.drawLine.gt.1
D=A
@R14
M=D
@gt
0;JMP
(Screen.drawLine.gt.1)
// {line: 20870}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 20875}
// if-goto Screen.drawLine.IF_TRUE0
@SP
AM=M-1
D=M
@Screen.drawLine.IF_TRUE0
D;JNE
// {line: 20877}
// goto Screen.drawLine.IF_FALSE0
@Screen.drawLine.IF_FALSE0
0;JMP
// {line: 20878}
(Screen.drawLine.IF_TRUE0)
// {line: 20884}
// push constant 8
@8
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 20897}
// call Sys.error nArgs: 1
@1
D=A
@R14
M=D
@Sys.error
D=A
@R15
M=D
@Screen.drawLine.call.0
D=A
@call
0;JMP
(Screen.drawLine.call.0)
// {line: 20902}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 20903}
(Screen.drawLine.IF_FALSE0)
// {line: 20912}
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
// {line: 20921}
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
// {line: 20926}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 20939}
// call Math.abs nArgs: 1
@1
D=A
@R14
M=D
@Math.abs
D=A
@R15
M=D
@Screen.drawLine.call.1
D=A
@call
0;JMP
(Screen.drawLine.call.1)
// {line: 20948}
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
// {line: 20957}
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
// {line: 20966}
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
// {line: 20971}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 20984}
// call Math.abs nArgs: 1
@1
D=A
@R14
M=D
@Math.abs
D=A
@R15
M=D
@Screen.drawLine.call.2
D=A
@call
0;JMP
(Screen.drawLine.call.2)
// {line: 20992}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 21001}
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
// {line: 21010}
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
// {line: 21017}
// lt
@Screen.drawLine.lt.2
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawLine.lt.2)
// {line: 21029}
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
// {line: 21038}
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
// {line: 21047}
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
// {line: 21056}
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
// {line: 21063}
// lt
@Screen.drawLine.lt.3
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawLine.lt.3)
// {line: 21068}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 21077}
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
// {line: 21080}
// not
@SP
A=M-1
M=!M
// {line: 21089}
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
// {line: 21098}
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
// {line: 21105}
// lt
@Screen.drawLine.lt.4
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawLine.lt.4)
// {line: 21110}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 21115}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 21120}
// if-goto Screen.drawLine.IF_TRUE1
@SP
AM=M-1
D=M
@Screen.drawLine.IF_TRUE1
D;JNE
// {line: 21122}
// goto Screen.drawLine.IF_FALSE1
@Screen.drawLine.IF_FALSE1
0;JMP
// {line: 21123}
(Screen.drawLine.IF_TRUE1)
// {line: 21132}
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
// {line: 21142}
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
// {line: 21151}
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
// {line: 21157}
// pop argument 0
@SP
AM=M-1
D=M
@ARG
A=M
M=D
// {line: 21166}
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
// {line: 21174}
// pop argument 2
@SP
AM=M-1
D=M
@ARG
A=M
A=A+1
A=A+1
M=D
// {line: 21183}
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
// {line: 21193}
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
// {line: 21202}
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
// {line: 21209}
// pop argument 1
@SP
AM=M-1
D=M
@ARG
A=M
A=A+1
M=D
// {line: 21218}
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
// {line: 21227}
// pop argument 3
@SP
AM=M-1
D=M
@ARG
A=M
A=A+1
A=A+1
A=A+1
M=D
// {line: 21228}
(Screen.drawLine.IF_FALSE1)
// {line: 21237}
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
// {line: 21242}
// if-goto Screen.drawLine.IF_TRUE2
@SP
AM=M-1
D=M
@Screen.drawLine.IF_TRUE2
D;JNE
// {line: 21244}
// goto Screen.drawLine.IF_FALSE2
@Screen.drawLine.IF_FALSE2
0;JMP
// {line: 21245}
(Screen.drawLine.IF_TRUE2)
// {line: 21254}
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
// {line: 21264}
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
// {line: 21273}
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
// {line: 21282}
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
// {line: 21291}
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
// {line: 21299}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 21308}
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
// {line: 21315}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 21324}
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
// {line: 21330}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 21339}
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
// {line: 21353}
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
// {line: 21362}
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
// {line: 21371}
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
// {line: 21378}
// gt
@Screen.drawLine.gt.2
D=A
@R14
M=D
@gt
0;JMP
(Screen.drawLine.gt.2)
// {line: 21391}
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
// {line: 21393}
// goto Screen.drawLine.IF_END2
@Screen.drawLine.IF_END2
0;JMP
// {line: 21394}
(Screen.drawLine.IF_FALSE2)
// {line: 21403}
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
// {line: 21410}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 21419}
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
// {line: 21425}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 21434}
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
// {line: 21448}
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
// {line: 21457}
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
// {line: 21466}
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
// {line: 21473}
// gt
@Screen.drawLine.gt.3
D=A
@R14
M=D
@gt
0;JMP
(Screen.drawLine.gt.3)
// {line: 21486}
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
// {line: 21487}
(Screen.drawLine.IF_END2)
// {line: 21493}
// push constant 2
@2
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 21502}
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
// {line: 21515}
// call Math.multiply nArgs: 2
@2
D=A
@R14
M=D
@Math.multiply
D=A
@R15
M=D
@Screen.drawLine.call.3
D=A
@call
0;JMP
(Screen.drawLine.call.3)
// {line: 21524}
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
// {line: 21529}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 21540}
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
// {line: 21546}
// push constant 2
@2
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 21555}
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
// {line: 21568}
// call Math.multiply nArgs: 2
@2
D=A
@R14
M=D
@Math.multiply
D=A
@R15
M=D
@Screen.drawLine.call.4
D=A
@call
0;JMP
(Screen.drawLine.call.4)
// {line: 21583}
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
// {line: 21589}
// push constant 2
@2
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 21598}
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
// {line: 21607}
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
// {line: 21612}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 21625}
// call Math.multiply nArgs: 2
@2
D=A
@R14
M=D
@Math.multiply
D=A
@R15
M=D
@Screen.drawLine.call.5
D=A
@call
0;JMP
(Screen.drawLine.call.5)
// {line: 21641}
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
// {line: 21650}
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
// {line: 21659}
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
// {line: 21668}
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
// {line: 21681}
// call Screen.drawConditional nArgs: 3
@3
D=A
@R14
M=D
@Screen.drawConditional
D=A
@R15
M=D
@Screen.drawLine.call.6
D=A
@call
0;JMP
(Screen.drawLine.call.6)
// {line: 21686}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 21687}
(Screen.drawLine.WHILE_EXP0)
// {line: 21696}
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
// {line: 21705}
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
// {line: 21712}
// lt
@Screen.drawLine.lt.5
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawLine.lt.5)
// {line: 21715}
// not
@SP
A=M-1
M=!M
// {line: 21720}
// if-goto Screen.drawLine.WHILE_END0
@SP
AM=M-1
D=M
@Screen.drawLine.WHILE_END0
D;JNE
// {line: 21729}
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
// {line: 21735}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 21742}
// lt
@Screen.drawLine.lt.6
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawLine.lt.6)
// {line: 21747}
// if-goto Screen.drawLine.IF_TRUE3
@SP
AM=M-1
D=M
@Screen.drawLine.IF_TRUE3
D;JNE
// {line: 21749}
// goto Screen.drawLine.IF_FALSE3
@Screen.drawLine.IF_FALSE3
0;JMP
// {line: 21750}
(Screen.drawLine.IF_TRUE3)
// {line: 21759}
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
// {line: 21768}
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
// {line: 21773}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 21784}
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
// {line: 21786}
// goto Screen.drawLine.IF_END3
@Screen.drawLine.IF_END3
0;JMP
// {line: 21787}
(Screen.drawLine.IF_FALSE3)
// {line: 21796}
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
// {line: 21805}
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
// {line: 21810}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 21821}
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
// {line: 21830}
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
// {line: 21835}
// if-goto Screen.drawLine.IF_TRUE4
@SP
AM=M-1
D=M
@Screen.drawLine.IF_TRUE4
D;JNE
// {line: 21837}
// goto Screen.drawLine.IF_FALSE4
@Screen.drawLine.IF_FALSE4
0;JMP
// {line: 21838}
(Screen.drawLine.IF_TRUE4)
// {line: 21847}
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
// {line: 21853}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 21858}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 21864}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 21866}
// goto Screen.drawLine.IF_END4
@Screen.drawLine.IF_END4
0;JMP
// {line: 21867}
(Screen.drawLine.IF_FALSE4)
// {line: 21876}
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
// {line: 21882}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 21887}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 21893}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 21894}
(Screen.drawLine.IF_END4)
// {line: 21895}
(Screen.drawLine.IF_END3)
// {line: 21904}
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
// {line: 21910}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 21915}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 21922}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 21931}
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
// {line: 21940}
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
// {line: 21949}
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
// {line: 21962}
// call Screen.drawConditional nArgs: 3
@3
D=A
@R14
M=D
@Screen.drawConditional
D=A
@R15
M=D
@Screen.drawLine.call.7
D=A
@call
0;JMP
(Screen.drawLine.call.7)
// {line: 21967}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 21969}
// goto Screen.drawLine.WHILE_EXP0
@Screen.drawLine.WHILE_EXP0
0;JMP
// {line: 21970}
(Screen.drawLine.WHILE_END0)
// {line: 21976}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 21978}
// return
@return
0;JMP
// {line: 22015}
// function Screen.drawRectangle nLocals: 9
(Screen.drawRectangle)
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
// {line: 22024}
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
// {line: 22033}
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
// {line: 22040}
// gt
@Screen.drawRectangle.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Screen.drawRectangle.gt.0)
// {line: 22049}
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
// {line: 22058}
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
// {line: 22065}
// gt
@Screen.drawRectangle.gt.1
D=A
@R14
M=D
@gt
0;JMP
(Screen.drawRectangle.gt.1)
// {line: 22070}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 22079}
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
// {line: 22085}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22092}
// lt
@Screen.drawRectangle.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawRectangle.lt.0)
// {line: 22097}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 22106}
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
// {line: 22112}
// push constant 511
@511
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22119}
// gt
@Screen.drawRectangle.gt.2
D=A
@R14
M=D
@gt
0;JMP
(Screen.drawRectangle.gt.2)
// {line: 22124}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 22133}
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
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22146}
// lt
@Screen.drawRectangle.lt.1
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawRectangle.lt.1)
// {line: 22151}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 22160}
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
// {line: 22166}
// push constant 255
@255
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22173}
// gt
@Screen.drawRectangle.gt.3
D=A
@R14
M=D
@gt
0;JMP
(Screen.drawRectangle.gt.3)
// {line: 22178}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 22183}
// if-goto Screen.drawRectangle.IF_TRUE0
@SP
AM=M-1
D=M
@Screen.drawRectangle.IF_TRUE0
D;JNE
// {line: 22185}
// goto Screen.drawRectangle.IF_FALSE0
@Screen.drawRectangle.IF_FALSE0
0;JMP
// {line: 22186}
(Screen.drawRectangle.IF_TRUE0)
// {line: 22192}
// push constant 9
@9
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22205}
// call Sys.error nArgs: 1
@1
D=A
@R14
M=D
@Sys.error
D=A
@R15
M=D
@Screen.drawRectangle.call.0
D=A
@call
0;JMP
(Screen.drawRectangle.call.0)
// {line: 22210}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 22211}
(Screen.drawRectangle.IF_FALSE0)
// {line: 22220}
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
// {line: 22226}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22239}
// call Math.divide nArgs: 2
@2
D=A
@R14
M=D
@Math.divide
D=A
@R15
M=D
@Screen.drawRectangle.call.1
D=A
@call
0;JMP
(Screen.drawRectangle.call.1)
// {line: 22248}
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
// {line: 22257}
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
// {line: 22266}
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
// {line: 22272}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22285}
// call Math.multiply nArgs: 2
@2
D=A
@R14
M=D
@Math.multiply
D=A
@R15
M=D
@Screen.drawRectangle.call.2
D=A
@call
0;JMP
(Screen.drawRectangle.call.2)
// {line: 22290}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 22303}
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
// {line: 22312}
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
// {line: 22318}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22331}
// call Math.divide nArgs: 2
@2
D=A
@R14
M=D
@Math.divide
D=A
@R15
M=D
@Screen.drawRectangle.call.3
D=A
@call
0;JMP
(Screen.drawRectangle.call.3)
// {line: 22341}
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
// {line: 22350}
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
// {line: 22359}
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
// {line: 22365}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22378}
// call Math.multiply nArgs: 2
@2
D=A
@R14
M=D
@Math.multiply
D=A
@R15
M=D
@Screen.drawRectangle.call.4
D=A
@call
0;JMP
(Screen.drawRectangle.call.4)
// {line: 22383}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 22397}
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
// {line: 22406}
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
// {line: 22412}
// push static 0
@Screen.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 22417}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 22422}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 22431}
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
// {line: 22437}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22442}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 22445}
// not
@SP
A=M-1
M=!M
// {line: 22457}
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
// {line: 22466}
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
// {line: 22472}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22477}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 22483}
// push static 0
@Screen.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 22488}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 22493}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 22502}
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
// {line: 22508}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22513}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 22524}
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
// {line: 22533}
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
// {line: 22539}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22552}
// call Math.multiply nArgs: 2
@2
D=A
@R14
M=D
@Math.multiply
D=A
@R15
M=D
@Screen.drawRectangle.call.5
D=A
@call
0;JMP
(Screen.drawRectangle.call.5)
// {line: 22561}
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
// {line: 22566}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 22572}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 22581}
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
// {line: 22590}
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
// {line: 22595}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 22603}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 22604}
(Screen.drawRectangle.WHILE_EXP0)
// {line: 22613}
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
// {line: 22622}
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
// {line: 22629}
// gt
@Screen.drawRectangle.gt.4
D=A
@R14
M=D
@gt
0;JMP
(Screen.drawRectangle.gt.4)
// {line: 22632}
// not
@SP
A=M-1
M=!M
// {line: 22635}
// not
@SP
A=M-1
M=!M
// {line: 22640}
// if-goto Screen.drawRectangle.WHILE_END0
@SP
AM=M-1
D=M
@Screen.drawRectangle.WHILE_END0
D;JNE
// {line: 22649}
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
// {line: 22658}
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
// {line: 22663}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 22670}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 22679}
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
// {line: 22685}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22692}
// eq
@Screen.drawRectangle.eq.0
D=A
@R14
M=D
@eq
0;JMP
(Screen.drawRectangle.eq.0)
// {line: 22697}
// if-goto Screen.drawRectangle.IF_TRUE1
@SP
AM=M-1
D=M
@Screen.drawRectangle.IF_TRUE1
D;JNE
// {line: 22699}
// goto Screen.drawRectangle.IF_FALSE1
@Screen.drawRectangle.IF_FALSE1
0;JMP
// {line: 22700}
(Screen.drawRectangle.IF_TRUE1)
// {line: 22709}
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
// {line: 22718}
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
// {line: 22727}
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
// {line: 22732}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 22745}
// call Screen.updateLocation nArgs: 2
@2
D=A
@R14
M=D
@Screen.updateLocation
D=A
@R15
M=D
@Screen.drawRectangle.call.6
D=A
@call
0;JMP
(Screen.drawRectangle.call.6)
// {line: 22750}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 22752}
// goto Screen.drawRectangle.IF_END1
@Screen.drawRectangle.IF_END1
0;JMP
// {line: 22753}
(Screen.drawRectangle.IF_FALSE1)
// {line: 22762}
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
// {line: 22771}
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
// {line: 22784}
// call Screen.updateLocation nArgs: 2
@2
D=A
@R14
M=D
@Screen.updateLocation
D=A
@R15
M=D
@Screen.drawRectangle.call.7
D=A
@call
0;JMP
(Screen.drawRectangle.call.7)
// {line: 22789}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 22798}
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
// {line: 22804}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22809}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 22815}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 22816}
(Screen.drawRectangle.WHILE_EXP1)
// {line: 22825}
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
// {line: 22834}
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
// {line: 22841}
// lt
@Screen.drawRectangle.lt.2
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawRectangle.lt.2)
// {line: 22844}
// not
@SP
A=M-1
M=!M
// {line: 22849}
// if-goto Screen.drawRectangle.WHILE_END1
@SP
AM=M-1
D=M
@Screen.drawRectangle.WHILE_END1
D;JNE
// {line: 22858}
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
// {line: 22864}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22867}
// neg
@SP
A=M-1
M=-M
// {line: 22880}
// call Screen.updateLocation nArgs: 2
@2
D=A
@R14
M=D
@Screen.updateLocation
D=A
@R15
M=D
@Screen.drawRectangle.call.8
D=A
@call
0;JMP
(Screen.drawRectangle.call.8)
// {line: 22885}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 22894}
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
// {line: 22900}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22905}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 22911}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 22913}
// goto Screen.drawRectangle.WHILE_EXP1
@Screen.drawRectangle.WHILE_EXP1
0;JMP
// {line: 22914}
(Screen.drawRectangle.WHILE_END1)
// {line: 22923}
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
// {line: 22932}
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
// {line: 22945}
// call Screen.updateLocation nArgs: 2
@2
D=A
@R14
M=D
@Screen.updateLocation
D=A
@R15
M=D
@Screen.drawRectangle.call.9
D=A
@call
0;JMP
(Screen.drawRectangle.call.9)
// {line: 22950}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 22951}
(Screen.drawRectangle.IF_END1)
// {line: 22960}
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
// {line: 22966}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22971}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 22978}
// pop argument 1
@SP
AM=M-1
D=M
@ARG
A=M
A=A+1
M=D
// {line: 22987}
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
// {line: 22993}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 22998}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 23007}
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
// {line: 23012}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 23018}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 23020}
// goto Screen.drawRectangle.WHILE_EXP0
@Screen.drawRectangle.WHILE_EXP0
0;JMP
// {line: 23021}
(Screen.drawRectangle.WHILE_END0)
// {line: 23027}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23029}
// return
@return
0;JMP
// {line: 23074}
// function Screen.drawHorizontal nLocals: 11
(Screen.drawHorizontal)
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
// {line: 23083}
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
// {line: 23092}
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
// {line: 23105}
// call Math.min nArgs: 2
@2
D=A
@R14
M=D
@Math.min
D=A
@R15
M=D
@Screen.drawHorizontal.call.0
D=A
@call
0;JMP
(Screen.drawHorizontal.call.0)
// {line: 23118}
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
// {line: 23127}
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
// {line: 23136}
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
// {line: 23149}
// call Math.max nArgs: 2
@2
D=A
@R14
M=D
@Math.max
D=A
@R15
M=D
@Screen.drawHorizontal.call.1
D=A
@call
0;JMP
(Screen.drawHorizontal.call.1)
// {line: 23163}
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
// {line: 23172}
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
// {line: 23178}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23181}
// neg
@SP
A=M-1
M=-M
// {line: 23188}
// gt
@Screen.drawHorizontal.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Screen.drawHorizontal.gt.0)
// {line: 23197}
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
// {line: 23203}
// push constant 256
@256
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23210}
// lt
@Screen.drawHorizontal.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawHorizontal.lt.0)
// {line: 23215}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 23224}
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
// {line: 23230}
// push constant 512
@512
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23237}
// lt
@Screen.drawHorizontal.lt.1
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawHorizontal.lt.1)
// {line: 23242}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 23251}
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
// {line: 23257}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23260}
// neg
@SP
A=M-1
M=-M
// {line: 23267}
// gt
@Screen.drawHorizontal.gt.1
D=A
@R14
M=D
@gt
0;JMP
(Screen.drawHorizontal.gt.1)
// {line: 23272}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 23277}
// if-goto Screen.drawHorizontal.IF_TRUE0
@SP
AM=M-1
D=M
@Screen.drawHorizontal.IF_TRUE0
D;JNE
// {line: 23279}
// goto Screen.drawHorizontal.IF_FALSE0
@Screen.drawHorizontal.IF_FALSE0
0;JMP
// {line: 23280}
(Screen.drawHorizontal.IF_TRUE0)
// {line: 23289}
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
// {line: 23295}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23308}
// call Math.max nArgs: 2
@2
D=A
@R14
M=D
@Math.max
D=A
@R15
M=D
@Screen.drawHorizontal.call.2
D=A
@call
0;JMP
(Screen.drawHorizontal.call.2)
// {line: 23321}
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
// {line: 23330}
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
// {line: 23336}
// push constant 511
@511
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23349}
// call Math.min nArgs: 2
@2
D=A
@R14
M=D
@Math.min
D=A
@R15
M=D
@Screen.drawHorizontal.call.3
D=A
@call
0;JMP
(Screen.drawHorizontal.call.3)
// {line: 23363}
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
// {line: 23372}
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
// {line: 23378}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23391}
// call Math.divide nArgs: 2
@2
D=A
@R14
M=D
@Math.divide
D=A
@R15
M=D
@Screen.drawHorizontal.call.4
D=A
@call
0;JMP
(Screen.drawHorizontal.call.4)
// {line: 23398}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 23407}
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
// {line: 23416}
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
// {line: 23422}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23435}
// call Math.multiply nArgs: 2
@2
D=A
@R14
M=D
@Math.multiply
D=A
@R15
M=D
@Screen.drawHorizontal.call.5
D=A
@call
0;JMP
(Screen.drawHorizontal.call.5)
// {line: 23440}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 23455}
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
// {line: 23464}
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
// {line: 23470}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23483}
// call Math.divide nArgs: 2
@2
D=A
@R14
M=D
@Math.divide
D=A
@R15
M=D
@Screen.drawHorizontal.call.6
D=A
@call
0;JMP
(Screen.drawHorizontal.call.6)
// {line: 23491}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 23500}
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
// {line: 23509}
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
// {line: 23515}
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23528}
// call Math.multiply nArgs: 2
@2
D=A
@R14
M=D
@Math.multiply
D=A
@R15
M=D
@Screen.drawHorizontal.call.7
D=A
@call
0;JMP
(Screen.drawHorizontal.call.7)
// {line: 23533}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 23549}
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
// {line: 23558}
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
// {line: 23564}
// push static 0
@Screen.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 23569}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 23574}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 23583}
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
// {line: 23589}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23594}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 23597}
// not
@SP
A=M-1
M=!M
// {line: 23608}
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
// {line: 23617}
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
// {line: 23623}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23628}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 23634}
// push static 0
@Screen.static.0
D=M
@SP
M=M+1
A=M-1
M=D
// {line: 23639}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 23644}
// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// {line: 23653}
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
// {line: 23659}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23664}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 23674}
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
// {line: 23683}
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
// {line: 23689}
// push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23702}
// call Math.multiply nArgs: 2
@2
D=A
@R14
M=D
@Math.multiply
D=A
@R15
M=D
@Screen.drawHorizontal.call.8
D=A
@call
0;JMP
(Screen.drawHorizontal.call.8)
// {line: 23711}
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
// {line: 23716}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 23722}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 23731}
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
// {line: 23740}
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
// {line: 23745}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 23757}
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
// {line: 23766}
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
// {line: 23775}
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
// {line: 23780}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 23789}
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
// {line: 23798}
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
// {line: 23804}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23811}
// eq
@Screen.drawHorizontal.eq.0
D=A
@R14
M=D
@eq
0;JMP
(Screen.drawHorizontal.eq.0)
// {line: 23816}
// if-goto Screen.drawHorizontal.IF_TRUE1
@SP
AM=M-1
D=M
@Screen.drawHorizontal.IF_TRUE1
D;JNE
// {line: 23818}
// goto Screen.drawHorizontal.IF_FALSE1
@Screen.drawHorizontal.IF_FALSE1
0;JMP
// {line: 23819}
(Screen.drawHorizontal.IF_TRUE1)
// {line: 23828}
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
// {line: 23837}
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
// {line: 23846}
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
// {line: 23851}
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// {line: 23864}
// call Screen.updateLocation nArgs: 2
@2
D=A
@R14
M=D
@Screen.updateLocation
D=A
@R15
M=D
@Screen.drawHorizontal.call.9
D=A
@call
0;JMP
(Screen.drawHorizontal.call.9)
// {line: 23869}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 23871}
// goto Screen.drawHorizontal.IF_END1
@Screen.drawHorizontal.IF_END1
0;JMP
// {line: 23872}
(Screen.drawHorizontal.IF_FALSE1)
// {line: 23881}
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
// {line: 23890}
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
// {line: 23903}
// call Screen.updateLocation nArgs: 2
@2
D=A
@R14
M=D
@Screen.updateLocation
D=A
@R15
M=D
@Screen.drawHorizontal.call.10
D=A
@call
0;JMP
(Screen.drawHorizontal.call.10)
// {line: 23908}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 23917}
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
// {line: 23923}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23928}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 23934}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 23935}
(Screen.drawHorizontal.WHILE_EXP0)
// {line: 23944}
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
// {line: 23953}
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
// {line: 23960}
// lt
@Screen.drawHorizontal.lt.2
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawHorizontal.lt.2)
// {line: 23963}
// not
@SP
A=M-1
M=!M
// {line: 23968}
// if-goto Screen.drawHorizontal.WHILE_END0
@SP
AM=M-1
D=M
@Screen.drawHorizontal.WHILE_END0
D;JNE
// {line: 23977}
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
// {line: 23983}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 23986}
// neg
@SP
A=M-1
M=-M
// {line: 23999}
// call Screen.updateLocation nArgs: 2
@2
D=A
@R14
M=D
@Screen.updateLocation
D=A
@R15
M=D
@Screen.drawHorizontal.call.11
D=A
@call
0;JMP
(Screen.drawHorizontal.call.11)
// {line: 24004}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 24013}
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
// {line: 24019}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24024}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 24030}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 24032}
// goto Screen.drawHorizontal.WHILE_EXP0
@Screen.drawHorizontal.WHILE_EXP0
0;JMP
// {line: 24033}
(Screen.drawHorizontal.WHILE_END0)
// {line: 24042}
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
// {line: 24051}
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
// {line: 24064}
// call Screen.updateLocation nArgs: 2
@2
D=A
@R14
M=D
@Screen.updateLocation
D=A
@R15
M=D
@Screen.drawHorizontal.call.12
D=A
@call
0;JMP
(Screen.drawHorizontal.call.12)
// {line: 24069}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 24070}
(Screen.drawHorizontal.IF_END1)
// {line: 24071}
(Screen.drawHorizontal.IF_FALSE0)
// {line: 24077}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24079}
// return
@return
0;JMP
// {line: 24080}
// function Screen.drawSymetric nLocals: 0
(Screen.drawSymetric)
// {line: 24089}
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
// {line: 24098}
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
// {line: 24103}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 24112}
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
// {line: 24121}
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
// {line: 24126}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 24135}
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
// {line: 24144}
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
// {line: 24149}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 24162}
// call Screen.drawHorizontal nArgs: 3
@3
D=A
@R14
M=D
@Screen.drawHorizontal
D=A
@R15
M=D
@Screen.drawSymetric.call.0
D=A
@call
0;JMP
(Screen.drawSymetric.call.0)
// {line: 24167}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 24176}
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
// {line: 24185}
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
// {line: 24190}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 24199}
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
// {line: 24208}
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
// {line: 24213}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 24222}
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
// {line: 24231}
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
// {line: 24236}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 24249}
// call Screen.drawHorizontal nArgs: 3
@3
D=A
@R14
M=D
@Screen.drawHorizontal
D=A
@R15
M=D
@Screen.drawSymetric.call.1
D=A
@call
0;JMP
(Screen.drawSymetric.call.1)
// {line: 24254}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 24263}
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
// {line: 24272}
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
// {line: 24277}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 24286}
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
// {line: 24295}
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
// {line: 24300}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 24309}
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
// {line: 24318}
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
// {line: 24323}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 24336}
// call Screen.drawHorizontal nArgs: 3
@3
D=A
@R14
M=D
@Screen.drawHorizontal
D=A
@R15
M=D
@Screen.drawSymetric.call.2
D=A
@call
0;JMP
(Screen.drawSymetric.call.2)
// {line: 24341}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 24350}
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
// {line: 24359}
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
// {line: 24364}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 24373}
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
// {line: 24382}
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
// {line: 24387}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 24396}
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
// {line: 24405}
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
// {line: 24410}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 24423}
// call Screen.drawHorizontal nArgs: 3
@3
D=A
@R14
M=D
@Screen.drawHorizontal
D=A
@R15
M=D
@Screen.drawSymetric.call.3
D=A
@call
0;JMP
(Screen.drawSymetric.call.3)
// {line: 24428}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 24434}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24436}
// return
@return
0;JMP
// {line: 24449}
// function Screen.drawCircle nLocals: 3
(Screen.drawCircle)
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
// {line: 24458}
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
// {line: 24464}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24471}
// lt
@Screen.drawCircle.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawCircle.lt.0)
// {line: 24480}
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
// {line: 24486}
// push constant 511
@511
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24493}
// gt
@Screen.drawCircle.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Screen.drawCircle.gt.0)
// {line: 24498}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 24507}
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
// {line: 24513}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24520}
// lt
@Screen.drawCircle.lt.1
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawCircle.lt.1)
// {line: 24525}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 24534}
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
// {line: 24540}
// push constant 255
@255
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24547}
// gt
@Screen.drawCircle.gt.1
D=A
@R14
M=D
@gt
0;JMP
(Screen.drawCircle.gt.1)
// {line: 24552}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 24557}
// if-goto Screen.drawCircle.IF_TRUE0
@SP
AM=M-1
D=M
@Screen.drawCircle.IF_TRUE0
D;JNE
// {line: 24559}
// goto Screen.drawCircle.IF_FALSE0
@Screen.drawCircle.IF_FALSE0
0;JMP
// {line: 24560}
(Screen.drawCircle.IF_TRUE0)
// {line: 24566}
// push constant 12
@12
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24579}
// call Sys.error nArgs: 1
@1
D=A
@R14
M=D
@Sys.error
D=A
@R15
M=D
@Screen.drawCircle.call.0
D=A
@call
0;JMP
(Screen.drawCircle.call.0)
// {line: 24584}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 24585}
(Screen.drawCircle.IF_FALSE0)
// {line: 24594}
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
// {line: 24603}
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
// {line: 24608}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 24614}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24621}
// lt
@Screen.drawCircle.lt.2
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawCircle.lt.2)
// {line: 24630}
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
// {line: 24639}
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
// {line: 24644}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 24650}
// push constant 511
@511
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24657}
// gt
@Screen.drawCircle.gt.2
D=A
@R14
M=D
@gt
0;JMP
(Screen.drawCircle.gt.2)
// {line: 24662}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 24671}
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
// {line: 24680}
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
// {line: 24685}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 24691}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24698}
// lt
@Screen.drawCircle.lt.3
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawCircle.lt.3)
// {line: 24703}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 24712}
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
// {line: 24721}
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
// {line: 24726}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 24732}
// push constant 255
@255
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24739}
// gt
@Screen.drawCircle.gt.3
D=A
@R14
M=D
@gt
0;JMP
(Screen.drawCircle.gt.3)
// {line: 24744}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 24749}
// if-goto Screen.drawCircle.IF_TRUE1
@SP
AM=M-1
D=M
@Screen.drawCircle.IF_TRUE1
D;JNE
// {line: 24751}
// goto Screen.drawCircle.IF_FALSE1
@Screen.drawCircle.IF_FALSE1
0;JMP
// {line: 24752}
(Screen.drawCircle.IF_TRUE1)
// {line: 24758}
// push constant 13
@13
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24771}
// call Sys.error nArgs: 1
@1
D=A
@R14
M=D
@Sys.error
D=A
@R15
M=D
@Screen.drawCircle.call.1
D=A
@call
0;JMP
(Screen.drawCircle.call.1)
// {line: 24776}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 24777}
(Screen.drawCircle.IF_FALSE1)
// {line: 24786}
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
// {line: 24793}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 24799}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24808}
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
// {line: 24813}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 24821}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 24830}
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
// {line: 24839}
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
// {line: 24848}
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
// {line: 24857}
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
// {line: 24870}
// call Screen.drawSymetric nArgs: 4
@4
D=A
@R14
M=D
@Screen.drawSymetric
D=A
@R15
M=D
@Screen.drawCircle.call.2
D=A
@call
0;JMP
(Screen.drawCircle.call.2)
// {line: 24875}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 24876}
(Screen.drawCircle.WHILE_EXP0)
// {line: 24885}
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
// {line: 24894}
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
// {line: 24901}
// gt
@Screen.drawCircle.gt.4
D=A
@R14
M=D
@gt
0;JMP
(Screen.drawCircle.gt.4)
// {line: 24904}
// not
@SP
A=M-1
M=!M
// {line: 24909}
// if-goto Screen.drawCircle.WHILE_END0
@SP
AM=M-1
D=M
@Screen.drawCircle.WHILE_END0
D;JNE
// {line: 24918}
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
// {line: 24924}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24931}
// lt
@Screen.drawCircle.lt.4
D=A
@R14
M=D
@lt
0;JMP
(Screen.drawCircle.lt.4)
// {line: 24936}
// if-goto Screen.drawCircle.IF_TRUE2
@SP
AM=M-1
D=M
@Screen.drawCircle.IF_TRUE2
D;JNE
// {line: 24938}
// goto Screen.drawCircle.IF_FALSE2
@Screen.drawCircle.IF_FALSE2
0;JMP
// {line: 24939}
(Screen.drawCircle.IF_TRUE2)
// {line: 24948}
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
// {line: 24954}
// push constant 2
@2
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24963}
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
// {line: 24976}
// call Math.multiply nArgs: 2
@2
D=A
@R14
M=D
@Math.multiply
D=A
@R15
M=D
@Screen.drawCircle.call.3
D=A
@call
0;JMP
(Screen.drawCircle.call.3)
// {line: 24981}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 24987}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 24992}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 25000}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 25002}
// goto Screen.drawCircle.IF_END2
@Screen.drawCircle.IF_END2
0;JMP
// {line: 25003}
(Screen.drawCircle.IF_FALSE2)
// {line: 25012}
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
// {line: 25018}
// push constant 2
@2
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25027}
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
// {line: 25036}
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
// {line: 25041}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 25054}
// call Math.multiply nArgs: 2
@2
D=A
@R14
M=D
@Math.multiply
D=A
@R15
M=D
@Screen.drawCircle.call.4
D=A
@call
0;JMP
(Screen.drawCircle.call.4)
// {line: 25059}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 25065}
// push constant 5
@5
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25070}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 25078}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 25087}
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
// {line: 25093}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25098}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 25105}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 25106}
(Screen.drawCircle.IF_END2)
// {line: 25115}
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
// {line: 25121}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25126}
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// {line: 25132}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 25141}
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
// {line: 25150}
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
// {line: 25159}
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
// {line: 25168}
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
// {line: 25181}
// call Screen.drawSymetric nArgs: 4
@4
D=A
@R14
M=D
@Screen.drawSymetric
D=A
@R15
M=D
@Screen.drawCircle.call.5
D=A
@call
0;JMP
(Screen.drawCircle.call.5)
// {line: 25186}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 25188}
// goto Screen.drawCircle.WHILE_EXP0
@Screen.drawCircle.WHILE_EXP0
0;JMP
// {line: 25189}
(Screen.drawCircle.WHILE_END0)
// {line: 25195}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25197}
// return
@return
0;JMP
// {line: 25198}
// function Sys.init nLocals: 0
(Sys.init)
// {line: 25211}
// call Memory.init nArgs: 0
@0
D=A
@R14
M=D
@Memory.init
D=A
@R15
M=D
@Sys.init.call.0
D=A
@call
0;JMP
(Sys.init.call.0)
// {line: 25216}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 25229}
// call Math.init nArgs: 0
@0
D=A
@R14
M=D
@Math.init
D=A
@R15
M=D
@Sys.init.call.1
D=A
@call
0;JMP
(Sys.init.call.1)
// {line: 25234}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 25247}
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
// {line: 25252}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 25265}
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
// {line: 25270}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 25283}
// call Keyboard.init nArgs: 0
@0
D=A
@R14
M=D
@Keyboard.init
D=A
@R15
M=D
@Sys.init.call.4
D=A
@call
0;JMP
(Sys.init.call.4)
// {line: 25288}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 25301}
// call Main.main nArgs: 0
@0
D=A
@R14
M=D
@Main.main
D=A
@R15
M=D
@Sys.init.call.5
D=A
@call
0;JMP
(Sys.init.call.5)
// {line: 25306}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 25319}
// call Sys.halt nArgs: 0
@0
D=A
@R14
M=D
@Sys.halt
D=A
@R15
M=D
@Sys.init.call.6
D=A
@call
0;JMP
(Sys.init.call.6)
// {line: 25324}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 25330}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25332}
// return
@return
0;JMP
// {line: 25333}
// function Sys.halt nLocals: 0
(Sys.halt)
// {line: 25334}
(Sys.halt.WHILE_EXP0)
// {line: 25340}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25343}
// not
@SP
A=M-1
M=!M
// {line: 25346}
// not
@SP
A=M-1
M=!M
// {line: 25351}
// if-goto Sys.halt.WHILE_END0
@SP
AM=M-1
D=M
@Sys.halt.WHILE_END0
D;JNE
// {line: 25353}
// goto Sys.halt.WHILE_EXP0
@Sys.halt.WHILE_EXP0
0;JMP
// {line: 25354}
(Sys.halt.WHILE_END0)
// {line: 25360}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25362}
// return
@return
0;JMP
// {line: 25367}
// function Sys.wait nLocals: 1
(Sys.wait)
@SP
AM=M+1
A=A-1
M=0
// {line: 25376}
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
// {line: 25382}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25389}
// lt
@Sys.wait.lt.0
D=A
@R14
M=D
@lt
0;JMP
(Sys.wait.lt.0)
// {line: 25394}
// if-goto Sys.wait.IF_TRUE0
@SP
AM=M-1
D=M
@Sys.wait.IF_TRUE0
D;JNE
// {line: 25396}
// goto Sys.wait.IF_FALSE0
@Sys.wait.IF_FALSE0
0;JMP
// {line: 25397}
(Sys.wait.IF_TRUE0)
// {line: 25403}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25416}
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
// {line: 25421}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 25422}
(Sys.wait.IF_FALSE0)
// {line: 25423}
(Sys.wait.WHILE_EXP0)
// {line: 25432}
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
// {line: 25438}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25445}
// gt
@Sys.wait.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Sys.wait.gt.0)
// {line: 25448}
// not
@SP
A=M-1
M=!M
// {line: 25453}
// if-goto Sys.wait.WHILE_END0
@SP
AM=M-1
D=M
@Sys.wait.WHILE_END0
D;JNE
// {line: 25459}
// push constant 50
@50
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25465}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 25466}
(Sys.wait.WHILE_EXP1)
// {line: 25475}
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
// {line: 25481}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25488}
// gt
@Sys.wait.gt.1
D=A
@R14
M=D
@gt
0;JMP
(Sys.wait.gt.1)
// {line: 25491}
// not
@SP
A=M-1
M=!M
// {line: 25496}
// if-goto Sys.wait.WHILE_END1
@SP
AM=M-1
D=M
@Sys.wait.WHILE_END1
D;JNE
// {line: 25505}
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
// {line: 25511}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25516}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 25522}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 25524}
// goto Sys.wait.WHILE_EXP1
@Sys.wait.WHILE_EXP1
0;JMP
// {line: 25525}
(Sys.wait.WHILE_END1)
// {line: 25534}
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
// {line: 25540}
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25545}
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// {line: 25551}
// pop argument 0
@SP
AM=M-1
D=M
@ARG
A=M
M=D
// {line: 25553}
// goto Sys.wait.WHILE_EXP0
@Sys.wait.WHILE_EXP0
0;JMP
// {line: 25554}
(Sys.wait.WHILE_END0)
// {line: 25560}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25562}
// return
@return
0;JMP
// {line: 25563}
// function Sys.error nLocals: 0
(Sys.error)
// {line: 25569}
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25582}
// call String.new nArgs: 1
@1
D=A
@R14
M=D
@String.new
D=A
@R15
M=D
@Sys.error.call.0
D=A
@call
0;JMP
(Sys.error.call.0)
// {line: 25588}
// push constant 69
@69
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25601}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Sys.error.call.1
D=A
@call
0;JMP
(Sys.error.call.1)
// {line: 25607}
// push constant 82
@82
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25620}
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
// {line: 25626}
// push constant 82
@82
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25639}
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
// {line: 25652}
// call Output.printString nArgs: 1
@1
D=A
@R14
M=D
@Output.printString
D=A
@R15
M=D
@Sys.error.call.4
D=A
@call
0;JMP
(Sys.error.call.4)
// {line: 25657}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 25666}
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
// {line: 25679}
// call Output.printInt nArgs: 1
@1
D=A
@R14
M=D
@Output.printInt
D=A
@R15
M=D
@Sys.error.call.5
D=A
@call
0;JMP
(Sys.error.call.5)
// {line: 25684}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 25697}
// call Sys.halt nArgs: 0
@0
D=A
@R14
M=D
@Sys.halt
D=A
@R15
M=D
@Sys.error.call.6
D=A
@call
0;JMP
(Sys.error.call.6)
// {line: 25702}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 25708}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25710}
// return
@return
0;JMP
// {line: 25711}
// function Keyboard.init nLocals: 0
(Keyboard.init)
// {line: 25717}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25719}
// return
@return
0;JMP
// {line: 25720}
// function Keyboard.keyPressed nLocals: 0
(Keyboard.keyPressed)
// {line: 25726}
// push constant 24576
@24576
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25739}
// call Memory.peek nArgs: 1
@1
D=A
@R14
M=D
@Memory.peek
D=A
@R15
M=D
@Keyboard.keyPressed.call.0
D=A
@call
0;JMP
(Keyboard.keyPressed.call.0)
// {line: 25741}
// return
@return
0;JMP
// {line: 25750}
// function Keyboard.readChar nLocals: 2
(Keyboard.readChar)
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
// {line: 25756}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25769}
// call Output.printChar nArgs: 1
@1
D=A
@R14
M=D
@Output.printChar
D=A
@R15
M=D
@Keyboard.readChar.call.0
D=A
@call
0;JMP
(Keyboard.readChar.call.0)
// {line: 25774}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 25775}
(Keyboard.readChar.WHILE_EXP0)
// {line: 25784}
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
// {line: 25790}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25797}
// eq
@Keyboard.readChar.eq.0
D=A
@R14
M=D
@eq
0;JMP
(Keyboard.readChar.eq.0)
// {line: 25806}
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
// {line: 25812}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25819}
// gt
@Keyboard.readChar.gt.0
D=A
@R14
M=D
@gt
0;JMP
(Keyboard.readChar.gt.0)
// {line: 25824}
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// {line: 25827}
// not
@SP
A=M-1
M=!M
// {line: 25832}
// if-goto Keyboard.readChar.WHILE_END0
@SP
AM=M-1
D=M
@Keyboard.readChar.WHILE_END0
D;JNE
// {line: 25845}
// call Keyboard.keyPressed nArgs: 0
@0
D=A
@R14
M=D
@Keyboard.keyPressed
D=A
@R15
M=D
@Keyboard.readChar.call.1
D=A
@call
0;JMP
(Keyboard.readChar.call.1)
// {line: 25851}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 25860}
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
// {line: 25866}
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 25873}
// gt
@Keyboard.readChar.gt.1
D=A
@R14
M=D
@gt
0;JMP
(Keyboard.readChar.gt.1)
// {line: 25878}
// if-goto Keyboard.readChar.IF_TRUE0
@SP
AM=M-1
D=M
@Keyboard.readChar.IF_TRUE0
D;JNE
// {line: 25880}
// goto Keyboard.readChar.IF_FALSE0
@Keyboard.readChar.IF_FALSE0
0;JMP
// {line: 25881}
(Keyboard.readChar.IF_TRUE0)
// {line: 25890}
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
// {line: 25897}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 25898}
(Keyboard.readChar.IF_FALSE0)
// {line: 25900}
// goto Keyboard.readChar.WHILE_EXP0
@Keyboard.readChar.WHILE_EXP0
0;JMP
// {line: 25901}
(Keyboard.readChar.WHILE_END0)
// {line: 25914}
// call String.backSpace nArgs: 0
@0
D=A
@R14
M=D
@String.backSpace
D=A
@R15
M=D
@Keyboard.readChar.call.2
D=A
@call
0;JMP
(Keyboard.readChar.call.2)
// {line: 25927}
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
// {line: 25932}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 25941}
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
// {line: 25954}
// call Output.printChar nArgs: 1
@1
D=A
@R14
M=D
@Output.printChar
D=A
@R15
M=D
@Keyboard.readChar.call.4
D=A
@call
0;JMP
(Keyboard.readChar.call.4)
// {line: 25959}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 25968}
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
// {line: 25970}
// return
@return
0;JMP
// {line: 25991}
// function Keyboard.readLine nLocals: 5
(Keyboard.readLine)
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
// {line: 25997}
// push constant 80
@80
D=A
@SP
M=M+1
A=M-1
M=D
// {line: 26010}
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
// {line: 26019}
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
// {line: 26028}
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
// {line: 26041}
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
// {line: 26046}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 26059}
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
// {line: 26066}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 26079}
// call String.backSpace nArgs: 0
@0
D=A
@R14
M=D
@String.backSpace
D=A
@R15
M=D
@Keyboard.readLine.call.3
D=A
@call
0;JMP
(Keyboard.readLine.call.3)
// {line: 26087}
// pop local 2
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
// {line: 26088}
(Keyboard.readLine.WHILE_EXP0)
// {line: 26097}
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
// {line: 26100}
// not
@SP
A=M-1
M=!M
// {line: 26103}
// not
@SP
A=M-1
M=!M
// {line: 26108}
// if-goto Keyboard.readLine.WHILE_END0
@SP
AM=M-1
D=M
@Keyboard.readLine.WHILE_END0
D;JNE
// {line: 26121}
// call Keyboard.readChar nArgs: 0
@0
D=A
@R14
M=D
@Keyboard.readChar
D=A
@R15
M=D
@Keyboard.readLine.call.4
D=A
@call
0;JMP
(Keyboard.readLine.call.4)
// {line: 26127}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 26136}
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
// {line: 26145}
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
// {line: 26152}
// eq
@Keyboard.readLine.eq.0
D=A
@R14
M=D
@eq
0;JMP
(Keyboard.readLine.eq.0)
// {line: 26162}
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
// {line: 26171}
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
// {line: 26174}
// not
@SP
A=M-1
M=!M
// {line: 26179}
// if-goto Keyboard.readLine.IF_TRUE0
@SP
AM=M-1
D=M
@Keyboard.readLine.IF_TRUE0
D;JNE
// {line: 26181}
// goto Keyboard.readLine.IF_FALSE0
@Keyboard.readLine.IF_FALSE0
0;JMP
// {line: 26182}
(Keyboard.readLine.IF_TRUE0)
// {line: 26191}
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
// {line: 26200}
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
// {line: 26207}
// eq
@Keyboard.readLine.eq.1
D=A
@R14
M=D
@eq
0;JMP
(Keyboard.readLine.eq.1)
// {line: 26212}
// if-goto Keyboard.readLine.IF_TRUE1
@SP
AM=M-1
D=M
@Keyboard.readLine.IF_TRUE1
D;JNE
// {line: 26214}
// goto Keyboard.readLine.IF_FALSE1
@Keyboard.readLine.IF_FALSE1
0;JMP
// {line: 26215}
(Keyboard.readLine.IF_TRUE1)
// {line: 26224}
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
// {line: 26237}
// call String.eraseLastChar nArgs: 1
@1
D=A
@R14
M=D
@String.eraseLastChar
D=A
@R15
M=D
@Keyboard.readLine.call.5
D=A
@call
0;JMP
(Keyboard.readLine.call.5)
// {line: 26242}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 26244}
// goto Keyboard.readLine.IF_END1
@Keyboard.readLine.IF_END1
0;JMP
// {line: 26245}
(Keyboard.readLine.IF_FALSE1)
// {line: 26254}
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
// {line: 26263}
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
// {line: 26276}
// call String.appendChar nArgs: 2
@2
D=A
@R14
M=D
@String.appendChar
D=A
@R15
M=D
@Keyboard.readLine.call.6
D=A
@call
0;JMP
(Keyboard.readLine.call.6)
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
// {line: 26286}
(Keyboard.readLine.IF_END1)
// {line: 26287}
(Keyboard.readLine.IF_FALSE0)
// {line: 26289}
// goto Keyboard.readLine.WHILE_EXP0
@Keyboard.readLine.WHILE_EXP0
0;JMP
// {line: 26290}
(Keyboard.readLine.WHILE_END0)
// {line: 26299}
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
// {line: 26301}
// return
@return
0;JMP
// {line: 26310}
// function Keyboard.readInt nLocals: 2
(Keyboard.readInt)
@SP
AM=M+1
A=A-1
M=0
@SP
AM=M+1
A=A-1
M=0
// {line: 26319}
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
// {line: 26332}
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
// {line: 26338}
// pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// {line: 26347}
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
// {line: 26360}
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
// {line: 26367}
// pop local 1
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D
// {line: 26376}
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
// {line: 26389}
// call String.dispose nArgs: 1
@1
D=A
@R14
M=D
@String.dispose
D=A
@R15
M=D
@Keyboard.readInt.call.2
D=A
@call
0;JMP
(Keyboard.readInt.call.2)
// {line: 26394}
// pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
// {line: 26403}
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
// {line: 26405}
// return
@return
0;JMP
