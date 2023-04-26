#apertura del archivo

ruta="D:\Desktop\proyecto 2 Leguajes\LFP_Proyecto2_202011212\Entrada.txt"

def LecturaInicial(ruta):
    File=open(ruta,"r", encoding="UTF-8")
    contenido=File.readlines()
    texto=""
    for i in contenido:
        texto+=i

    return texto


result=LecturaInicial(ruta)


def DetectarSimbolo(caracter):
    simbolos_reservados=["(",")",'"',"{","}","”","“",";",":",",","=","\n"," "]
    verdadero=True
    if caracter.isalpha()==False and caracter.isdigit()==False:
        for i in simbolos_reservados:
            if caracter == i:
                verdadero=False

    return verdadero



#verificadores lectura
def VerificadorLexemaDesnudo(char):
    valido=False
    if char.isalpha()==True:
        valido=True

    if char.isdigit()==True:
        valido=True
    
    if DetectarSimbolo(char)==True:
        valido=True
    
    return valido

def VerificadorLexemaEntreComila(char):
    valido=False
    if char.isalpha()==True:
        valido=True

    if char.isdigit()==True:
        valido=True
    
    if DetectarSimbolo(char)==True:
        valido=True
    
    return valido


#pruebas caracteres
simbolos_reservados=["(",")",'"',"{","}"]
digito="9"
simbolo="("
letra="a1X"
#isalpha detecta letras mayusculas y minusculas
print(letra.isalpha())
#isdigit detecta numeros
print(digito.isdigit())
#deteccion simbolos distintos a los reservados
print(DetectarSimbolo(simbolo))


#reconocimiento jsons

contenido_nuevo=""
contenido=result
posicion=0
tope=len(contenido)
while True:
    if posicion>=tope:
        break
    else:
        char=contenido[posicion]
        if char=="{":
            json=char
            posicion_interna=posicion+1
            while True:
                if posicion_interna>=tope:
                    break
                else:
                    char_interno=contenido[posicion_interna]
                    if char_interno=="}":
                        json+=char_interno
                        posicion_interna+=1
                        break
                    else:
                        json+=char_interno
                        posicion_interna+=1
            posicion=posicion_interna
            temp=json.replace("\n","")
            new_txt=temp.replace('"',"'")
            contenido_nuevo+=new_txt
        else:
            contenido_nuevo+=char
            posicion+=1











def ObtencionLexemas(result):
    
    #Obtencion lexemas
    lexemas_crudos=[]


    tope=len(result)
    posicion=0
    while True:
        if posicion==tope:
            break
        else:
            char=result[posicion]
            if char==",":
                lexemas_crudos.append(char)
                posicion+=1
            elif char=="(":
                lexemas_crudos.append(char)
                posicion+=1
            elif char==")":
                lexemas_crudos.append(char)
                posicion+=1
            elif char==";":
                lexemas_crudos.append(char)
                posicion+=1
            elif char=="=":
                lexemas_crudos.append(char)
                posicion+=1
            elif char=='"':
                
                lexema=char
                posicion_interna=posicion+1
                while True:
                    if posicion_interna>=tope:
                        break
                    else:
                        char_interno=result[posicion_interna]
                        if char_interno=='"':
                            lexema+=char
                            posicion_interna+=1
                            break
                        else:
                            lexema+=char_interno
                            posicion_interna+=1
                
                lexemas_crudos.append(lexema)
                posicion=posicion_interna

            elif VerificadorLexemaDesnudo(char):
                lexema=char
                posicion_interna=posicion+1
                while True:
                    if posicion_interna>=tope:
                        break
                    else:
                        char_interno=result[posicion_interna]
                        if VerificadorLexemaDesnudo(char_interno)==False:
                            break
                        else:
                            lexema+=char_interno
                            posicion_interna+=1
                lexemas_crudos.append(lexema)
                posicion=posicion_interna
            else:
                posicion+=1
    return lexemas_crudos

lexemas=ObtencionLexemas(contenido_nuevo)
print(lexemas)
    
        















