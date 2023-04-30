def DetectarSimbolo(caracter):
    simbolos_reservados=["(",")",'"',"{","}","”","“",";",":",",","=","\n"," ","'"]
    verdadero=True
    if caracter.isalpha()==False and caracter.isdigit()==False:
        for i in simbolos_reservados:
            if caracter == i:
                verdadero=False

    return verdadero


def VerificadorLexemaDesnudo(char):
    valido=False
    if char.isalpha()==True:
        valido=True

    if char.isdigit()==True:
        valido=True
    
    if DetectarSimbolo(char)==True:
        valido=True
    
    return valido
from clases import Lexema
lex="{\n 'nombre' : 'Obra Literaria'\n},\n{\n $set: {'autor' : 'Mario Vargas'}\n}"

json=Lexema(lex,1,1)


lexema=json.lexema
tope=len(lexema)
columna=json.columna
linea=json.linea
posicion=0
lexemas_internos=[]
while True:
    if posicion>=tope:
        break
    else:
        char=lexema[posicion]
        if char=="{":
            lexemas_internos.append(Lexema(char,linea,columna))
            posicion+=1
            columna+=1
        elif char==":":
            lexemas_internos.append(Lexema(char,linea,columna))
            posicion+=1
            columna+=1
        elif char==",":
            lexemas_internos.append(Lexema(char,linea,columna))
            posicion+=1
            columna+=1
        elif char=="'":
            lexe=char
            posicion_interna=posicion+1
            columna_interna=columna+1
            linea_interna=linea
            while  True:
                if posicion_interna>=tope:
                    break
                else:
                    char_interno=lexema[posicion_interna]
                    if char_interno=="'":
                        lexe+=char_interno
                        posicion_interna+=1
                        columna_interna+=1
                        break
                    elif char_interno=="\n":
                        lexe+=char_interno
                        linea_interna+=1
                        columna_interna=1
                        posicion_interna+=1
                    else:
                        lexe+=char_interno
                        posicion_interna+=1
                        columna_interna+=1
            lexemas_internos.append(Lexema(lexe,linea,columna))
            linea=linea_interna
            columna=columna_interna
            posicion=posicion_interna
        elif VerificadorLexemaDesnudo(char)==True:
                inicio=[linea,columna]
                lexe=char
                columna+=1
                posicion_interna=posicion+1
                while True:
                    if posicion_interna>=tope:
                        break
                    else:
                        char_interno=lexema[posicion_interna]
                        if VerificadorLexemaDesnudo(char_interno)==False:
                            break
                        else:
                            lexe+=char_interno
                            posicion_interna+=1
                            columna+=1
                lexemas_internos.append(Lexema(lexe,inicio[0],inicio[1]))
                posicion=posicion_interna
        else:
            posicion+=1


for t in lexemas_internos:
    print("-->",t.lexema,"<--")


