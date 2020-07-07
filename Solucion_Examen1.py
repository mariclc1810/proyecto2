def dec_to_oct(num):
    if isinstance(num,int):
        return conv_int(num)
    elif isinstance(num,float):
        return conv_int(num//1) + 0.1 * conv_float(num%1)
    else:
        return "Error en tipos de dato"

def conv_int(num):
    if num == 0:
        return 0
    else:
        return num%8 + 10 * conv_int(num//8)

def conv_float(num):
    if num*8//1 == 0:
        return 0
    else:
        decimal = num*8
        return decimal//1 + 0.1 * conv_float(decimal%1)

def cumples(lista):
    if isinstance(lista, list):
        d = {"ene":1, "feb":2, "mar":3, "abr":4, "may":5, "jun":6, "jul":7, "ago":8, "set":9, "oct":10, "nov":11, "dic":12}
        primer_mitad = lambda mes : 1 <= mes <= 6
        segunda_mitad = lambda mes: 7 <= mes <= 12
        return [cumples_aux(lista, primer_mitad, d)] + [cumples_aux(lista, segunda_mitad, d)]
    else:
        return "Error"

def cumples_aux(lista, func, d):
    if lista == []:
        return []
    elif func(d[lista[0][3:]]):
        return [lista[0]] + cumples_aux(lista[1:], func, d)
    else:
        return cumples_aux(lista[1:], func, d)

def roman2dec(numero):
    if isinstance(numero, str):
        if verificar_romano(numero):
            d = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
            return roman2dec_aux(numero, d)
        else:
            return "Numero no romano"
    else:
        return "No es cadena de texto"

def verificar_romano(numero):
    if numero == "":
        return True
    elif numero[0] != "M" and numero[0] != "D" and numero[0] != "C" and numero[0] != "L" and numero[0] != "X" and numero[0] != "V" and numero[0] != "I":
        return False
    else:
        return verificar_romano(numero[1:])

def roman2dec_aux(numero, d):
    if numero == "":
        return 0
    elif numero[1:] == "":
        return d[numero[0]]

    numero1 = d[numero[0]]
    numero2 = d[numero[1]]

    if numero1 < numero2:
        return (numero2 - numero1) + roman2dec_aux(numero[2:], d)
    else:
        return numero1 + roman2dec_aux(numero[1:], d)

def contar(lista):
    if isinstance(lista, list):
        return contar_aux(lista)
    else:
        return "Error"

def contar_aux(lista):
    if lista == []:
        return 0
    elif isinstance(lista[0], list):
        return contar_aux(lista[0]) + contar_aux(lista[1:])
    else:
        return 1 + contar_aux(lista[1:])
        
