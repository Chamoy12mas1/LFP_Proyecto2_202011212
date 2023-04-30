from clases import Lexema
import ast

#apertura del archivo

ruta="D:\Desktop\proyecto 2 Leguajes\LFP_Proyecto2_202011212\Entrada.txt"

def LecturaInicial(ruta):
    File=open(ruta,"r", encoding="UTF-8")
    contenido=File.readlines()
    texto=""
    for i in contenido:
        texto+=i

    return texto





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
def TransFormacionJsons(result):
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
                
                new_txt=json.replace('"',"'")
                contenido_nuevo+=new_txt
            else:
                contenido_nuevo+=char
                posicion+=1
    return contenido_nuevo










def ObtencionLexemas(result):
    
    #Obtencion lexemas
    lexemas_crudos=[]
    columna=1
    linea=1

    tope=len(result)
    posicion=0
    while True:
        if posicion==tope:
            break
        else:
            char=result[posicion]
            char1=""
            char2=""
            if (posicion+1)<tope:
                char1=result[posicion+1]
                if (posicion+2)<tope:
                    char2=result[posicion+2]
            

            if char=="-" and char1=="-" and char2 == "-":
                ini=columna
                posicion+=3
                posicion_interna=posicion
                lexe=char+char1+char2
                while True:
                    if posicion_interna>=tope:
                        break
                    else:
                        char_interno=result[posicion_interna]
                        if char_interno=="\n":
                            break
                        else:
                            lexe+=char_interno
                            columna+=1
                            posicion_interna+=1
                lexemas_crudos.append(Lexema(lexe,linea,ini))

                posicion=posicion_interna
                columna+=3
            elif char=="/" and char1=="*":
                ini1=linea
                ini=columna
                posicion+=2
                posicion_interna=posicion
                lexe=char+char1
                while True:
                    if posicion_interna>=tope:
                        break
                    else:
                        char_interno=result[posicion_interna]
                        char1_interno=""
                        if (posicion+1)<tope:
                            char1_interno=result[posicion_interna+1]
                        if char_interno=="*" and char1_interno=="/":
                            posicion_interna+=2
                            lexe+=char_interno+char1_interno
                            break
                        elif char_interno=="\n":
                            linea+=1
                            columna=0
                            lexe+=char_interno
                            posicion_interna+=1
                        else:
                            lexe+=char_interno
                            columna+=1
                            posicion_interna+=1
                lexemas_crudos.append(Lexema(lexe,ini1,ini))

                posicion=posicion_interna
                columna+=2


            elif char=="\n":
                linea+=1
                columna=1
                posicion+=1
            elif char==",":
                lexemas_crudos.append(Lexema(char,linea,columna))
                columna+=1
                posicion+=1
            elif char=="(":
                lexemas_crudos.append(Lexema(char,linea,columna))
                columna+=1
                posicion+=1
            elif char==")":
                lexemas_crudos.append(Lexema(char,linea,columna))
                columna+=1
                posicion+=1
            elif char==";":
                lexemas_crudos.append(Lexema(char,linea,columna))
                columna+=1
                posicion+=1
            elif char=="=":
                lexemas_crudos.append(Lexema(char,linea,columna))
                columna+=1
                posicion+=1
            elif char=="{":
                lexemas_crudos.append(Lexema(char,linea,columna))
                columna+=1
                posicion+=1
            elif char=="}":
                lexemas_crudos.append(Lexema(char,linea,columna))
                columna+=1
                posicion+=1    
            elif char=='"':
                
                lexema=char
                
                posicion_interna=posicion+1
                columna_interna=(columna+1)
                linea_interna=linea
                while True:
                    if posicion_interna>=tope:
                        break
                    else:
                        char_interno=result[posicion_interna]
                        if char_interno=='"':
                            lexema+=char_interno
                            posicion_interna+=1
                            columna_interna+=1
                            break
                        elif char_interno=="\n":
                            lexema+=char_interno
                            linea_interna+=1
                            columna_interna=1
                            posicion_interna+=1

                        else:
                            lexema+=char_interno
                            posicion_interna+=1
                            columna_interna+=1
                lexemas_crudos.append(Lexema(lexema,linea,columna))
                posicion=posicion_interna
                linea=linea_interna
                columna=columna_interna

            elif VerificadorLexemaDesnudo(char):
                inicio=[linea,columna]
                lexema=char
                columna+=1
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
                            columna+=1
                lexemas_crudos.append(Lexema(lexema,inicio[0],inicio[1]))
                posicion=posicion_interna
            else:
                posicion+=1
                columna+=1
    
    
    return lexemas_crudos






    
#verificacion lexemas
Diccionario=[
    ["nueva","nueva"],
    ["CrearBD","CrearBD"],
    ["EliminarBD","EliminarBD"],
    ["CrearColeccion","CrearColeccion"],
    ["EliminarColeccion","EliminarColeccion"],
    ["InsertarUnico","InsertarUnico"],
    ["ActualizarUnico","ActualizarUnico"],
    ["EliminarUnico","EliminarUnico"],
    ["BuscarTodo","BuscarTodo"],
    ["BuscarUnico","BuscarUnico"],
    ["(","AperturaParentesis"],
    [")","CerraduraParentesis"],
    [";","FinSentencia"],
    ["{","AperturaLlave"],
    ["}","CerraduraLlave"],
    ["$set","set"],
    [":","DosPuntos"]
]

#Verificar identificador retorna false si es identificador
def VerificarIdentificador(lexema):
    valido=True
    if lexema[0].isdigit():
        return False
    
    tope=len(lexema)
    posicion=0
    while True:
        if posicion>=tope:
            break
        else:
            char=lexema[posicion]
            if char.isdigit() | char.isalpha():
                posicion+=1
            else:
                valido=False
                break
    return valido


def PosibleJson(lexema):
    posicion=0
    tope=len(lexema)
    while True:
        if posicion>=tope:
            return False
        else:
            char=lexema[posicion]
            if char=="{":
                return True
            elif char=="}":
                return True
            else:
                posicion+=1
            


def VerificarLexemas(lista_lexemas):
    Errores_lexicos=[]
    Errores_sintacticos=[]
    Diccionario=[
    ["nueva","nueva"],
    ["CrearBD","CrearBD"],
    ["EliminarBD","EliminarBD"],
    ["CrearColeccion","CrearColeccion"],
    ["EliminarColeccion","EliminarColeccion"],
    ["InsertarUnico","InsertarUnico"],
    ["ActualizarUnico","ActualizarUnico"],
    ["EliminarUnico","EliminarUnico"],
    ["BuscarTodo","BuscarTodo"],
    ["BuscarUnico","BuscarUnico"],
    ["(","AperturaParentesis"],
    [")","CerraduraParentesis"],
    [";","FinSentencia"],
    ["{","AperturaLlave"],
    ["}","CerraduraLlave"],
    ["$set","set"],
    [":","DosPuntos"],
    ["=","Igual"],
    [",","Coma"]
    ]
    
    for lexema in lista_lexemas:
        for reservada in Diccionario:
            if lexema.lexema == reservada[0]:
                lexema.token = reservada[1]

        if lexema.lexema[0]=='"':
            if lexema.lexema[len(lexema.lexema)-1]=='"':
                if PosibleJson(lexema.lexema):
                    lexema.token="json"
                else:
                    lexema.token="Identificador"
                    print("Edentificador",lexema.lexema)
            else:
                lexema.error="No se cerraron las comillas"
                lexema.token="Desconocido"
        else:
            if lexema.token=="":
                print("Este no tiene token es palabra desnuda",lexema.lexema)
                tope=len(lexema.lexema)
                indice=0
                if lexema.lexema[0].isalpha():

                    while True:
                        if indice>=tope:
                            lexema.token="Identificador"
                            break
                        else:
                            char=lexema.lexema[indice]
                            if char.isalpha() or char.isdigit():
                                indice+=1
                            else:
                                lexema.token="Desconocido"
                                break
                else:
                    encontro=False
                    try:
                        if lexema.lexema[0:3]=="---":
                            lexema.token="Comentario"
                            encontro=True
                        elif lexema.lexema[0:2]=="/*":
                            if lexema.lexema[len(lexema.lexema)-2:len(lexema.lexema)]=="*/":
                                lexema.token="Comentario"
                                encontro=True
                            else:
                                encontro=True
                                lexema.token="Desconocido"
                                lexema.error="No se cerro el comentario"
                        else:
                            lexema.token="Desconocido"
                            encontro=True
                    except:
                        lexema.token="Desconocido"
                        encontro=True
                    if encontro==False:
                        lexema.token="Desconocido"

    errores=[]                   
    for x in lista_lexemas:
        if x.error!="":
            errores.append(x.error)
    
    return errores



#Ejecucion del analizador
result=LecturaInicial(ruta)
contenido_nuevo=TransFormacionJsons(result)
lexemas=ObtencionLexemas(contenido_nuevo)
VerificarLexemas(lexemas)


for j in lexemas:
    print("->",j.lexema,j.token,j.linea,j.columna,"<--")


#Transformacion de las sentencias iniciales a mongo db

salida=[]
errores_sintacticos=[]


broke=len(lexemas)
apuntador=0
while True:
    if apuntador>=broke:
        break
    else:
        i=lexemas[apuntador]
        if i.token=="CrearBD":
            linea=i.linea
            indice=lexemas.index(i)
            if lexemas[indice+1].token=="Identificador":
                if lexemas[indice+1].linea==linea:
                    if lexemas[indice+2].token=="Igual":
                        if lexemas[indice+2].linea==linea:
                            if lexemas[indice+3].token=="nueva":
                                if lexemas[indice+3].linea==linea:
                                    if lexemas[indice+4].token=="CrearBD":
                                        if lexemas[indice+4].linea==linea:
                                            if lexemas[indice+5].token=="AperturaParentesis":
                                                if lexemas[indice+5].linea==linea:
                                                    if lexemas[indice+6].token=="CerraduraParentesis":
                                                        if lexemas[indice+6].linea==linea:
                                                            if lexemas[indice+7].token=="FinSentencia":
                                                                if lexemas[indice+7].linea==linea:
                                                                    salida.append("use('"+str(lexemas[indice+1].lexema)+"');")
                                                                    apuntador=indice+8
                                                                else:
                                                                    apuntador=indice+8
                                                                    errores_sintacticos.append(["Error Sintactico",lexemas[indice+7].linea,lexemas[indice+7].columna,"FinSentencia","Fuera de la posicion esperada"])
                                                            else:
                                                                apuntador=indice+8
                                                                errores_sintacticos.append(["Error Sintactico",lexemas[indice+7].linea,lexemas[indice+7].columna,"FinSentencia","Se esperaba un punto y coma para la funcion CrearDB"])
                                                        else:
                                                            apuntador=indice+7
                                                            errores_sintacticos.append(["Error Sintactico",lexemas[indice+6].linea,lexemas[indice+6].columna,"CerraduraParentesis","Fuera de la posicion esperada"])
                                                    else:
                                                        apuntador=indice+7
                                                        errores_sintacticos.append(["Error Sintactico",lexemas[indice+6].linea,lexemas[indice+6].columna,"CerraduraParentesis","Se esperaba un parentesis para la funcion CrearDB"])
                                                else:
                                                    apuntador=indice+6
                                                    errores_sintacticos.append(["Error Sintactico",lexemas[indice+5].linea,lexemas[indice+5].columna,"AperturaParentesis","Fuera de la posicion esperada"])
                                            else:
                                                apuntador=indice+6
                                                errores_sintacticos.append(["Error Sintactico",lexemas[indice+5].linea,lexemas[indice+5].columna,"AperturaParentesis","Se esperaba un parentesis para la funcion CrearDB"])
                                        else:
                                            apuntador=indice+5
                                            errores_sintacticos.append(["Error Sintactico",lexemas[indice+4].linea,lexemas[indice+4].columna,"CrearDB","Fuera de la posicion esperada"])
                                    else:
                                        apuntador=indice+5
                                        errores_sintacticos.append(["Error Sintactico",lexemas[indice+4].linea,lexemas[indice+4].columna,"CrearDB","Se esperaba la palabra reserbada CrearDB para la funcion CrearDB"])
                                else:
                                    apuntador=indice+4
                                    errores_sintacticos.append(["Error Sintactico",lexemas[indice+3].linea,lexemas[indice+3].columna,"nueva","Fuera de la posicion esperada"])
                            else:
                                apuntador=indice+4
                                errores_sintacticos.append(["Error Sintactico",lexemas[indice+3].linea,lexemas[indice+3].columna,"nueva","Se esperaba la palabra reservada nueva para la funcion CrearDB"])
                        else:
                            apuntador=indice+3
                            errores_sintacticos.append(["Error Sintactico",lexemas[indice+2].linea,lexemas[indice+2].columna,"Igual","Fuera de la posicion esperada"])
                    else:
                        apuntador=indice+3
                        errores_sintacticos.append(["Error Sintactico",lexemas[indice+2].linea,lexemas[indice+2].columna,"Igual","Se esperaba un signo igual para la funcion CrearDB"])
                else:
                    apuntador=indice+2
                    errores_sintacticos.append(["Error Sintactico",lexemas[indice+1].linea,lexemas[indice+1].columna,"Identificador","Fuera de la posicion esperada"])
            else:
                errores_sintacticos.append(["Error Sintactico",lexemas[indice+1].linea,lexemas[indice+1].columna,"Identificador","Se esperaba un identificador para la funcion CrearDB"])
                apuntador=indice+2

        else:
            apuntador+=1
print(salida)
print(errores_sintacticos)







