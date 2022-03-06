from funcion import *
code=leer_json("code_ac.json")
import webbrowser


#--------------------------------------------------------------------------------------------------

print('''1. Listar los objetos de la nook's cranny y sus variantes
2. Total de variantes de cada objeto
3. Filtración por precios
4. Buscador de objetos
5. Listar objetos con opción de imagen
6. Salir del programa''')

opcion=int(input("Introduce una opción: "))

#--------------------------------------------------------------------------------------------------

if opcion == 1:
    lista=listar_nook(code)
    variantes=[]
    novariantes=[]
    for elem in lista:
        
        if elem[1] == None:
            if elem[0] not in novariantes:
                novariantes.append(elem[0])
                print(f"\n{elem[0]}: Este objeto no tiene variantes")
                

        if elem[1] != None:
            if elem[0] not in variantes:
                variantes.append(elem[0])
                print(f"\nLas variantes de |{elem[0]}| son: ")
            if elem[0] in variantes:
                print(elem[1])

#--------------------------------------------------------------------------------------------------

if opcion == 2:

    lista=listar_nook(code)
    variantes=[]
    novariantes=[]
    palabra=""
    contador=1

    for elem in lista:
        auxiliar=[]

        if elem[1] == None:
            if elem[0] not in novariantes:
                novariantes.append(elem[0])
                print(f"\n{elem[0]}: Este objeto no tiene variantes\n")
                

        if elem[1] != None:
            contador+=1

            if elem[0] != palabra:
                print(f"\nEl objeto |{palabra}| tiene {contador} variantes\n")
                contador=1
                palabra=elem[0]

    print(f"\nEl objeto |{palabra}| tiene {contador} variantes\n")

#--------------------------------------------------------------------------------------------------

if opcion == 3:

    filtrar=filtrar_prec(code)

    minimo=int(input("\n·Introduce un precio: "))
    maximo=int(input("·Introduce un segundo precio: "))
    
    while minimo > maximo:
        print("\n-x- ERROR -x-\n -El primer número tiene que ser menor que el segundo-")
        minimo=int(input("\n·Introduce un precio: "))
        maximo=int(input("·Introduce un segundo precio: "))
    
    auxiliar=[]
    for elem in filtrar:
        if elem[1] in range(minimo,maximo):
            if elem[0] not in auxiliar:
                auxiliar.append(elem[0])
                print(f"\n- {elem[0]}:")
                if elem[0] in auxiliar:
                    print(f"    ·Precio de compra: {elem[1]} bayas\n")
        else:
            print(".*· No hay productos en ese rango ·*.")
            break

#--------------------------------------------------------------------------------------------------

if opcion == 4:

    searchvar=buscador(code)
    variante=input("· Introduce una variante: ")
    objetos=[]
    for elem in searchvar:
        if elem[1] != None:
            if elem[1].upper() == variante.upper():
                if elem[0] not in objetos:
                    objetos.append(elem[0])
    print(f"\n·Los objetos con la variante |{variante}| son :")
    for objeto in objetos:
        print(f"\n-{objeto}")

#--------------------------------------------------------------------------------------------------

if opcion == 5:
    listimagen=imagen_web(code)
    variante=input("· Introduce una variante: ")
    objetos=[]
    
    for elem in listimagen:
        if elem[1] != None:
            if elem[1].upper() == variante.upper():
                if elem[0] not in objetos:
                    precios=[]
                    precios.append(elem[0])
                    precios.append(elem[2])
                    precios.append(elem[3])
                    objetos.append(precios)
    print(f"\n·Los objetos con la variante |{variante}| son :")
    
    for objeto in objetos:
        if objeto[1] == None:
            print(f"\n-{objeto[0]}:\n   -Precio de compra: Este objeto no dispone de precio de compra\n   -Precio de venta:{objeto[2]} bayas")
        else:
            print(f"\n-{objeto[0]}:\n   -Precio de compra: {objeto[1]} bayas\n   -Precio de venta:{objeto[2]} bayas")
    verimagen=input("¿Desea ver una imagen del objeto?(s/n)")  
    if verimagen == "s":
        seleccion=input("·Introduce el nombre del producto: ")
        for elem in listimagen:
            if elem[0].upper() == seleccion.upper():
                if elem[1].upper() == variante.upper():
                    webbrowser.open(elem[4])
    else:
        print("\n.*· Bye ·*.")

#--------------------------------------------------------------------------------------------------

if opcion == 6:
    print("\n.*· Bye ·*.")