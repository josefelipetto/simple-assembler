; Teste de funcionamento eAssembler

NOP				; nenhuma operaÃ§Ã£o
HALT
MOV AX,BX
MOV CX,[123]
MOV [111],DX
MOV AX,789
MOV [321],654
ADD BX,CX
SUB DX,AX
CMP BX,CX
JMP 987
JZ -123
JG -456
JL -768
OUT DX
INC AX			; incrementa
DEC BX;decrementa
MUL CX,DX
DIV AX,BX