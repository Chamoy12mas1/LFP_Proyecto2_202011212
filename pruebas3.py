from clases import Lexema
from Pruebas import VerificadorLexemaDesnudo,PosibleJson

json="{\n 'nombre' : 'Obra Literaria'\n},\n{\n $set: {'autor' : 'Mario Vargas'}\n}"

#Separacjion del json
lexemas_crudos=[]

#aqui la posicion del lexema
columna=1
linea=1

tope=len(json)
posicion=0
while True:
    if posicion==tope:
        break
    else:
        char=json[posicion]
        if char=="{":
            lexemas_crudos.append(Lexema(char,linea,columna))
            columna+=1
            posicion+=1
        elif char=="}":
            lexemas_crudos.append(Lexema(char,linea,columna))
            columna+=1
            posicion+=1
        elif char==",":
            lexemas_crudos.append(Lexema(char,linea,columna))
            columna+=1
            posicion+=1
        elif char=="\n":
            linea+=1
            columna=1
            posicion+=1
        elif char==":":
            lexemas_crudos.append(Lexema(char,linea,columna))
            columna+=1
            posicion+=1
        elif char=="'": 
            lexema=char
            
            posicion_interna=posicion+1
            columna_interna=(columna+1)
            linea_interna=linea
            while True:
                if posicion_interna>=tope:
                    break
                else:
                    char_interno=json[posicion_interna]
                    if char_interno=="'":
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
                    char_interno=json[posicion_interna]
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
lexemas=[]
for lexema in lexemas_crudos:
    for reservada in Diccionario:
        if lexema.lexema == reservada[0]:
            lexema.token = reservada[1]

    if lexema.lexema[0]=="'":
        if lexema.lexema[len(lexema.lexema)-1]=="'":
            if PosibleJson(lexema.lexema):
                txt=lexema.lexema[1:len(lexema.lexema)-1]
                print("Json",txt)
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
                    elif lexema.lexema[0:2]=="/*" and lexema.lexema[len(lexema.lexema)-2:len(lexema.lexema)]=="*/":
                        lexema.token="Comentario"
                        encontro=True
                    else:
                        lexema.token="Desconocido"
                        encontro=True
                except:
                    lexema.token="Desconocido"
                    encontro=True
                if encontro==False:
                    lexema.token="Desconocido"

print("XXXXXXXXXXXXXXXXXXXXXXX")
for i in lexemas_crudos:
    print(i.lexema,i.token)

valido=True

for i in lexemas_crudos:
    if i.token=="set":
        
        try:
            indice=lexemas_crudos.index(i)
            
            if lexemas_crudos[indice-1].token=="AperturaLlave":
                
                if lexemas_crudos[indice+1].token=="DosPuntos":
                    print("Aperturo puntos")
                    if lexemas_crudos[indice+2].token=="AperturaLlave":
                        print("aperturo otravez llaves")
                        valido=True
                    else:
                        valido=False
                else:
                    valido=False
            else:
                valido=False
        except:
            valido=False   


print("----------->",valido)

        

