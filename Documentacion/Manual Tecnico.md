# Manual Técnico
## Obtención de lexemas
Mediante la lectura del contenido del archivo cargado al programa se lee carácter por carácter mediante un ciclo while y con la ayuda de una variable de control posición y mediante sentencia condicionales se identifica si el carácter encaja en un posible lexema como por ejemplo los string que comienzan y finalizan con comillas entonces al encontrar que un carácter sea igual a una comilla el lexema se formaría desde ese carácter hasta volver a encontrar otras comillas o hasta completar la lectura de todo el archivo originando un error.

![a](https://lh3.googleusercontent.com/pw/AJFCJaXWBQpezXZHqKII8VRea5pxI1YgmH53-aRxRK-zDj7agYLb5AyxJjaCQrv-edveEVhsYFBjWwbQ64UNnfR07hZEtFYPxh2IwzDX78XQsxEfW8qtcVMR6Lcu368QH0yYYEYWqb9kZL2BSaZXjJbBPzWoitLfQ_Q2H3F6U7KkX48zKyYF3P5eSw06c_badbsONgtQEJBBfNuK7-a5lXrRN5Jhq3DZ-UM-gJ1dAWcIGmF1UU1tN328EAm-zBFVIBY2TaoWNaxh98wma7nJRuA1GpEJ9yvo0p08AvKYwWejInNaBx97vAZeUcEB_hKNjmWaRxFZ1S_wPLnpS9oBCQXgPMXq0d1uETEGN2hylNpdsyRtrps60lVOvtLNgzdBDJh7EYAz9R1lwkyD1DysIMretuDzgMyVkMy-j9vdxDXfuzD5UGYw56BdD2PIY1mktiylm89hWc3GREh2kGkoQKsmhxBBEnIectRHEm5CkX4rDxicgWjMgBr0DCceXZx-NSVmxmjiwQwDG0ivzSIsThMQWmneogt7DqasXpUmHuNn3g6wS13WKgykJlZFbODrBlZtf7wagwzEEM7tlF6_rjRTmeKi1kLZtZC5mMv1Ol7nlyPwN7hKFMTtyxlzjMUNgLlUZRAZCNBD_bRDYIXUsrkwsClXpLUdhF8ogP4yqOqDnmk2802RZ5fgyY6uRRebIsNBXC5N85SpHAILV14sFwIqkRicdcecCPCEgAJSY1mWYrN41mbf41WyIKFuE6pOa0gJqMUwuMaZoEb9ZoE8z1TdJvJ4HJ4jl1qQpZMRgSK8kV1fFCHoefiC3a3E75sUFnE-YGaJyORn-sPH4xW-iG5nkK3aXqYETijT_PeWGn9FrlcQ0FNHSO9hAqyb1ch2xi83xWCIPFcH8sDMq2eh5ThmByFOt3BMvlFlDLtSljjA0k4n_wOkdOgiy2lrI9Y6bGC5V_1ZYIlIfbdQZX98MN0Zoy_xTQtU85JT8eLMyFzVDBGMd8tGRuBixilKpY2PwQFSALZrZuwfwJ3tJOUJcgSHyp2Q_ZZ5zo1iBJpvrBM=w722-h847-s-no?authuser=1)

## Verificación de lexemas
Con la ayuda de un diccionario se compara cada uno con el diccionario para verificar si este lexema es una palabra reservada de lo contrario se verifica carácter por carácter que este lexema sea válido para un identificador o string asignando el token correspondiente de lo contrario se le asigna el token "Desconocido" el cual genera un error.

![b](https://lh3.googleusercontent.com/pw/AJFCJaXHFWyWwovaWnVWRjwcwLa6QfweDCKeNIVQ1HmRGuC7R5y9nazjMUa4v157P4O1W6_kTBH0TesKXgan1hHHX-BYSCDriIotnDEUNAEVGs4mU4Ty7A6LHE9zmMI0q2kAcIiE0jrbmR-aPIGBuEZ3BSWt-DI72OqcHtyBH61X0In7_Y0UwwIjNWgXnP4GvUY0Xng9EtD_efyKgY4KIxmX8RZRjIye67Fp65nkRFWDPqwceKfaSpqFifcQtddr5cFBcWwib_K5IW55CpTeJI9NrJKX7JAzbhBTnwaib9wrJXZR_jJYO7N-lbrSlcnDNQjbmhO7LQR1NkB_1P3KCd3LdZNmPh9s0F28VuLNI6Rk6pr7KbGkODTsneqRREHt8tt-o8GQqMpXrBMiuuhaSvVgnd0-UIbi1BvPCyW7QRXZExLt1LWvEFXlFceMjBBT_2ifXzqL26K0wFCkG_w0NS2QfTkKPMjqVIohvYnV1suFnWHNLWvEIoYMn6ZUomxK-wh0N9jYCRPJeMrK8dwr3XwRSo4kjBl0l3fmX5Eb_hn3W-Q33ktfPGkmHVduRPpaFe97FfKNFhC5YKHrm3WimOFA-6b8iU6A6MqWqtNgXFmHbjJqPRFx9A32ThYKbq5_N0AmQrlkZ3xjsAlnJPcskfmTMhzc4UAQahCvY87Ta6A-igZiiUAIHL-uD1zk0__jciLqy1ZNfkxsWCxGfo2-0XM3Sao7HcImaip_toa9i079BL-T48qeI0h12p5BeSfFv1y96pQ5w_ukZ3X05NVm_MSAgfS07bOw3Ep-0CCon880h9nRmeZTJ0i5Bnquttb7m5qATZuVp5k-qu2_bF1MNW4vFj4mi3ac3Qxjd_rGCnwIspYfl7fizLlrJT1Z2TV0_KGnksE-04Tepwt4-d9CyO6AD0LT-2xOJC0tiZeL2ks2XrLr9rNHKRsfumO838YhXxzryn9fq8RpvgGkYVQcWcz67JLcqzpeZxaT99l2k9ibmqJtPgUKmEcUof12Jtdx7IcCrnTd0kvIHXh_0CVQBMzPPxZYYxEM8wEZCzhdTPE=w692-h863-s-no?authuser=1)


## Estructura de las ventanas
Por medio de la librería Tkinter se realizó la parte visual del programa cada ventana tiene la siguiente estructura.

![c](https://lh3.googleusercontent.com/pw/AJFCJaW1X-vY9XEGsEl8wYQdHhGCUeBsRpzJvDLGRu0p1sWZw4k6rLOUHfR4fhzUqu78er-U9teijFlcJWjRXzaSIgPceE1c68lA07ELHm_8028DvZxEAV8dAd11tdFx8nv-LW8bomWtUT5N1w4JgY-nFqP1EJeuPv8IPrbCQ6zvI186vAcc1l4g-2Gs-TEwNNlsuH7CA9CuZjCZeGO19jbkbwzhEigoHjjuI3-cVonlIYJ3hj6GWpUqM71uXBrB5_unQCSfylHndw36AquNIiKdY6ybvgSup0hE-pHzaNoGmm38TkvQivU_ncEPAYKQz80bYgStOpQajEfaofiRy7paU1XrkLcfqwgNKw36ce2DotOgP8UxDiq6GEGqbIW3E3JvYkEgzXI6-4XTE6IUdyaDLC7uIgiqtvNa9tZdDndqoPAMTO2qRZfx-ZxQncdz4WxcizptnkPw54z03ujyflEOf_dibrrjbeyzVPCC6slTF4GFQzoYiaHev3MWBP3OmpMHQTlPJ6xHndc1v1irQl_brQG4RJ5TXm6I6u-9Ji9utzHB1JFwVrxWOxquJWv19YDnfAjl0yLvFO5HiVgOtIQFD9PODkiWe_lzO6kJSV05CaryvdYobdPeE8Fe39QV598-GD1VykayVIMrLZ8IvOC6v4S2MEE2ZjQ0OyKdbzxv8a8uBAIM509QRnlPeEbge0gYuFScP7ZRATRuIiI9fJH-A2B9zSow1p43YzKvZbkXuNnMstqBcbGURQOgkvRgUKxRBG0dvTShx65h92HodOL82DCWVNelf0u6Rz3zfFiaVch0G8CXKTVmnJrDgmvZeScnIoXTz3da5UzuR4oYDeoTAZFnkk1gIy_L7xtj4hz_oTCpeRLEJJk1loQFnQ8CtrnHBSvs2O-iQdpMdL5G9oh81uayaw3NLrYQkr-mH52aIFNebbLlN7CYatyzCxHr0HFrlTkLSCZ4yl3CzbRe4QEx-TVVZBWA9IReTXYAgCp6HuTS2hEmv437trdMfsjhk2ZNp-LLTivwKIpmBbimKdJ3hqJG7-9i_Kl__Uzk5N0=w418-h167-s-no?authuser=1)

## Tabla de tokens
| Token | Lexema |Expresion Regular |
| ------ | ------ | ------ |
| nueva | nueva | nueva |
| CrearBD | CrearBD | CrearBD |
| EliminarBD | EliminarBD | EliminarBD |
| CrearColeccion | CrearColeccion | CrearColeccion |
| EliminarColeccion | EliminarColeccion | EliminarColeccion |
| InsertarUnico | InsertarUnico | InsertarUnico |
| ActualizarUnico | ActualizarUnico | ActualizarUnico |
| EliminarUnico | EliminarUnico | EliminarUnico |
| BuscarTodo | BuscarTodo | BuscarTodo |
| BuscarUnico | BuscarUnico | BuscarUnico |
| AperturaParentesis | ( | ( |
| CerraduraParentesis | ) | ) |
| FinSentencia | ; | ; |
| AperturaLlave | { | { |
| CerraduraLlave | } | } |
| set | $set | $set |
| DosPuntos | : | : |
| Igual | = | = |
| Coma | , | , |
| Identificador | Variable1 | [a-zA-Z]+.[a-zA-Z0-9]* |
| String | "tex1to@1" | "[[:ascii:]]+" |
| json | "{ 'hola':'adios'}" | x |

## Metodo del arbol
![Descripción de la imagen](
https://lh3.googleusercontent.com/pw/AJFCJaVkWCKeBnr7Mq2JSB0yczCSIzfvXAUVhmiIN--_9hLslXC2QxlJum7T3imct3YV5hAbGJo1uOJV-yXH4GaeEPkqzV0NGnMxY-6soDpDVkfA2RPUbMpN0lTbhQZReySNboNtis415q5lEBa2a16VqHrFjAU0t2FcbIIkCEScaelkTPd-sgrlqPJG2N62ocOut0vEipS1-Fx7Fs6EbW_RnIRk5EHWzdzJADbeKeQpgsAGPqsLrtN_4JWYvzVWJ_Oei0tmoxW1dHSH0WGrfYORnwKebz6hipkoWoiLnEMHqP-WYVzBI0IfnEBSn5u3014tFxH9HHnXKxIM0lnjQTi9bxno2ATUg56JlRDnzWyhjaOkdj_WGOa4O6Se3XaJ-ofIR3h3JsEtq4A72NiE8X9Djw1qfYZxyHJYLrrjWpMIdE7oAcushHtl-sdgQiuoS1lTlAfzsS_O2nSJpKDIpUHeRijJffvXui101x66oi16nL0WzD7MyIaQa9ot3EmdYGTd2UatZlZdFOfm2Uyy9bgIeoN6dHc40WbQb_MTlfiuAfnDzFQPS2aO7_2WtgmRVbyXAjt32VZs9JYdSvehXYAF9il8VW2T4EGkyK6wdAfdHWATNWWxDZ5uVHk9cYLhVuNNeUkZR-Xv0pRxTNm-rZhrgpiBbsIbTZRynkJPjoLl0X7RMDkDEBZZiy0skzhZHy2nPUG2PvgY6ivzRX0GJ73N6lAgv4lewfz9yqHYpHLVgjFsnmX1uT-GRDAI7NZPy4nu7HQ-IKFW0jFCIg1cubHjs5f4VHQE1a3lBU13LL4PpTarMZOvELiEv6A4Tb6ShBdedDUXDuz3KPsKySPpEHlTQRfF_KBWjq71QhM7gJr24_7UFiZy57AB3Xss9USOdWUbPxKKL0Igh8X3RDvL3VZIkkU8fAqLni1ACva0Lj1Fj2Vkb4FTtqO2CrOlJXFNxm_CFYhLQe1wh1wSWUNWBoWpekLVCzluklXO69NXrRwEbAp3G_Yu22WIAqEw47RFVdRFa3YfKAAmOryaOHvLoc3BI0brA2uCD47Oc01nAA8=w1000-h750-s-no?authuser=1)

### Tabla siguiente
| Indice | Elemento | Siguientes |
| ------ | ------ | ------ |
| 1 | [a-zA-Z] | 1,2,3 |
| 2 | [a-zA-Z0-9] | 2,3 |
| 3 | # | - |

### Tabla de transiciones
| Posiciones | Estado | Transicion con [a-zA-Z] | Transicion con [a-zA-Z0-9] |
| ------ | ------ | ------ | ------ |
| 1,2,3 | S0 | S0 | S1 |
|2,3 | S1 | X | S1 |

### Automata finito determinista
![Descripción de la imagen](
https://lh3.googleusercontent.com/pw/AJFCJaXMwf4gkO-zHHOH84S0j_YwdvNJua9F_oTgywv8xh71S24Yxu3IZnmeOIGpn30T3bxr0lNaqiNr2q3l4FTYhdDOtHYcQDd0CblPugteFvo-oZbW_eJHbp7M3gK-wseHJzyAbWqznzYfCtKCMZZonyrVMxMhHVUCCupKE4g1LxFk6Z09GSo-pPELuSRN_uu_PP5RJzZcmaLC1b1Az1M1O2_YoAsr-bZtS2qH1N8U-HIGozmJ6FJjHDtToc0OS-RZiLbekoLac5BEYEwTDLv_YaPaSA-wptd61efxStUqCYe2khU42IbTehWK_VfLcdV-aoMfTPh_tRHWGdsYCt2NY_TrgH73O0GoYwYMUtDRdHX1i7cRJ-lCtRI-C2a1KDaB3hLsdH108oZJM9miuxXOaajTPhU0nif7LgwLdyT2Pu_FUs6CprHEAjdFMkYm8-IsJDNV5yl1FgnYgNKivSiB12BRhfc31hwmSRGLrunK7miVBGB4dHFOOeRqbIZpCn3sjn8TcgvvEetBvr7I5Dd2kSMn3IGaI1OPQ1h-cQmvxA2KjPc-V-EOsrqThaeOgGAnca-K_kyLDiOUBX7VOeQfqfC5vjdWbZEFpy_v8yDoqUD3nriM20uIwqXwIsYIV-G7fgEbwfYL6KlxNiakrd-UdzfBmSb-2DnXrc2FupeZbnCHqL62g0_ynjUpgCIENANUJa9Ou7zQbnbjuXZ57zRpwxnm_EIwNCLjWpounKfnIJvIymeA9EgseyqjN3JHAUg-PlftWxN9NtuphzzxP4viZvRjBC2DlL1ci_IbyoBhqqC6U6TJGoQy7QLcWv5mqt8hniSmeAa9iWvZp3pExo5tqmu75boqd-kMSNgnSA5WsOyoyj1YT59_7EksBhED8rzVJSZf4QGI7TXjbu8EFbfhVZonxDXAHWEkULH-CeQ3ff7Vl48Vr3fXpv2RcWhxT1WBP1Sx21MxN8gbkq86Pv775nfZQ_ZI9OwBOIUw7qIDVADZsviFfIO_yX-CBWvBShwYsyIEjttlMwVOyT6U7rRJ-8iTqLrq6ZRTFxZYp_U=w569-h208-no?authuser=1)


## Gramática 
### Para L(G)={Funcion.Identificador.Igual.nueva.Funcion.AperturaParentesis.CerraduraParentesis.FinSentencia}

##### Cadenas Validas:
- CrearBD ejemplo = nueva CrearBD(); 
- EliminarBD elimina = nueva EliminarBD();
- CrearColeccion colec = nueva CrearColeccion(“NombreColeccion”);

##### Transiciones
- S -> Funcion.Identificador.Igual.nueva.Funcion.AperturaParentesis.CerraduraParentesis.FinSentencia

### Gramática Resultante
- No terminales = {S}
- Terminales = {Funcion.Identificador.Igual.nueva.Funcion.AperturaParentesis.CerraduraParentesis.FinSentencia}
- Conjunto de producciones:  S -> Funcion.Identificador.Igual.nueva.Funcion.AperturaParentesis.CerraduraParentesis.FinSentencia
- Símbolo inicial = S
