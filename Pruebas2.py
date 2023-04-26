alpha="  "

def DetectarSimbolo(caracter):
    simbolos_reservados=["(",")",'"',"{","}","”","“",";",":",",","=","\n"]
    verdadero=True
    if caracter.isalpha()==False and caracter.isdigit()==False:
        for i in simbolos_reservados:
            if caracter == i:
                verdadero=False

    return verdadero

def VerificadorLexemaDesnudo(char):
    valido=False
    if char.isalpha():
        valido=True

    if char.isdigit():
        valido=True
    
    if DetectarSimbolo(char)==True:
        valido=True
    
    return valido

print(VerificadorLexemaDesnudo(alpha))