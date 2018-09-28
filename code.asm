; +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
; Programa teste para testar assembler
; Feito por: José Henrique Felipetto, Tiago Paiva e Pedro Gusso
; Disciplina: Tópicos avançados em arquitetura de computadores
; +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

MOV AX,BX        ; MOV_RR
MOV BX,[200]     ; MOV_RM
HALT             ; WAIT
MOV [200],CX     ;    MOV_MR
NOP              ; NECA
MOV DX,-200      ; MOV_RI
MOV [300],  -123 ; MOV_MI
MOV [200],432    ; TESTE
ADD AX, BX;      ; Comentário feito
; Comentário Entre comandos
SUB BX, CX;
CMP BX, CX;
JMP 2;
JZ -5;
JG 10;
JL 200
OUT AX
INC BX
DEC CX
MUL BX,AX
DIV AX,BX


; FIM
