listaConductores = ["Hola", "Gato", "Pp"]
listaKms = [3, 5, 1]


def pedirNombre():
    while True:
        try:
            nombre = str(input("Ingrese el nombre del conductor:"))
            nombre = nombre.capitalize()
        except ValueError:
            print("Solo ingrese letras.")
        else:
            break
    return nombre


def pedirDistancia():
    while True:
        try:
            distancias = int(input("Ingrese la distancia recorrida:"))
        except ValueError:
            print("Solo ingrese numeros")
        else:
            if distancias > 0:
                break
            else:
                print("Ingrese numeros enteros mayores a 0.")
    return distancias


while True:
    print("""
    1- Mostrar distancia recorrida de c/u de los conductores:
        (Nombre y Distancia). Ordenado alfabeticamente.
        
    2- Mostrar el conductor que recorrio mas distancia, incluye la distancia.

    3- Agregar nuevo conductor y su distancia recorrida.

    4- Eliminar un conductor y su distancia recorrida.

    5- Buscar conductor con su nombre.

    6- Salir del programa""")
    while True:
        try:
            opcion = int(input("Ingrese una opcion:"))
        except ValueError:
            print("Solo ingrese numeros")
        else:
            if opcion >= 1 and opcion <= 6:
                break
            else:
                print("Solo debe ingresar numeros del 1 al 6.")
                print("Se lo devolvera al menu!")
    if opcion == 1:
        if len(listaConductores) > 0:
            conductoresyDistancias = list(zip(listaConductores, listaKms))
            conductoresyDistancias.sort()
            print("Distancia recorrida por cada conductor:")
            for conductor, distancia in conductoresyDistancias:
                print(f"+ {conductor}: realizo {distancia} km")
        else:
            print("No hay conductores registrados.")

    elif opcion == 2:
        if len(listaConductores) > 0:
            maxDistancia = max(listaKms)
            indexDistanciaM = listaKms.index(maxDistancia)
            nombreConductorMD = listaConductores[indexDistanciaM]
            print(
                f"El conductor que recorrió la mayor distancia es {nombreConductorMD} con {maxDistancia} km.")
        else:
            print("No hay conductores registrados.")
    elif opcion == 3:
        nombreConductor = pedirNombre()
        distancia = pedirDistancia()
        listaConductores.append(nombreConductor)
        listaKms.append(distancia)
        print("Se ha agregado el nuevo conductor.")
    elif opcion == 4:
        nombreConductor = pedirNombre()
        if nombreConductor in listaConductores:
            indice = 0
            while indice < len(listaConductores):
                if nombreConductor == listaConductores[indice]:
                    listaConductores.pop(indice)
                    listaKms.pop(indice)
                    print(f"Se ha eliminado el conductor {nombreConductor}.")
                else:
                    indice += 1
        else:
            print(
                f"No se ha eliminado el conductor {nombreConductor}. No existe en la lista.")
    elif opcion == 5:
        if len(listaConductores) > 0:
            nombreConductor = pedirNombre()
            if nombreConductor in listaConductores:
                indice = listaConductores.index(nombreConductor)
                mensaje = f"Conductor encontrado. Su distancia recorrida es: {listaKms[indice]} km."
            else:
                mensaje = "No se encontró un conductor con ese nombre."
            print(mensaje)
        else:
            print("No hay conductores registrados.")
    elif opcion == 6:
        exit()
