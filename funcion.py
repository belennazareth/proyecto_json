import json
import sys

def leer_json(fichero):
    try:
        with open(fichero) as a:
            code=json.load(a)
        return code
    except:
        print("-x- Error -x-")
        sys.exit(0)


def listar_nook(code):
    lista=[]
    for objetos in code.keys():
        for elem in code[objetos]:
            if elem.get("source") == "Nook's Cranny":
                if elem.get("name").get("name-EUes") not in lista:
                    auxiliar=[]
                    auxiliar.append(elem.get("name").get("name-EUes"))
                    auxiliar.append(elem.get("variant"))
                    lista.append(auxiliar)
    return lista


def filtrar_prec(code):
    lista=[]
    for objetos in code:
        for elem in code[objetos]:
            precio=elem.get("buy-price")
            if precio != None:
                if precio not in lista:
                    auxiliar=[]
                    auxiliar.append(elem.get("name").get("name-EUes"))
                    auxiliar.append(elem.get("buy-price"))
                    lista.append(auxiliar)
    return lista


def buscador(code):
    lista=[]
    for objetos in code.keys():
        for elem in code[objetos]:
            if elem.get("name").get("name-EUes") not in lista:
                auxiliar=[]
                auxiliar.append(elem.get("name").get("name-EUes"))
                auxiliar.append(elem.get("variant"))
                lista.append(auxiliar)
    return lista



def imagen_web(code):
    lista=[]
    for objetos in code.keys():
        for elem in code[objetos]:
            if elem.get("name").get("name-EUes") not in lista:
                auxiliar=[]
                auxiliar.append(elem.get("name").get("name-EUes"))
                auxiliar.append(elem.get("variant"))
                auxiliar.append(elem.get("buy-price"))
                auxiliar.append(elem.get("sell-price"))
                auxiliar.append(elem.get("image_uri"))
                lista.append(auxiliar)
    return lista