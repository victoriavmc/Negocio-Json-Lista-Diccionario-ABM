dProductos = {1234567890123: {'Descripcion': 'Manzana',
                              'PrecioCosto': 50,
                              'PrecioVenta': 100,
                              'Existencia': 100,
                              'StockMinimo': 200},
              1234567890144: {'Descripcion': 'Manteca',
                              'PrecioCosto': 130,
                              'PrecioVenta': 210,
                              'Existencia': 155,
                              'StockMinimo': 105},
              1234567890133: {'Descripcion': 'Mandioca',
                              'PrecioCosto': 150,
                              'PrecioVenta': 200,
                              'Existencia': 150,
                              'StockMinimo': 100},
              1234567890122: {'Descripcion': 'Pera',
                              'PrecioCosto': 100,
                              'PrecioVenta': 150,
                              'Existencia': 50,
                              'StockMinimo': 100},
              1234567890111: {'Descripcion': 'Pepsi',
                              'PrecioCosto': 160,
                              'PrecioVenta': 220,
                              'Existencia': 500,
                              'StockMinimo': 100},
              1234567890100: {'Descripcion': 'Pepitos',
                              'PrecioCosto': 190,
                              'PrecioVenta': 260,
                              'Existencia': 25,
                              'StockMinimo': 55}, }

# Estetico
def separador():
    print("══ ☆ ══════ ☆ ══════ ☆ ══════ ☆ ══════ ☆ ══════ ☆ ══════ ☆ ══════ ☆ ══════ ☆ ══════ ☆ ══════ ☆ ══")

# Mensaje Separador Arriba Abajo
# vIngreso hace referencia a que quiere ingresar
def mensajeSeparadorArribaAbajo(vIngreso):
    separador()
    print(
        f'               {vIngreso}')
    separador()

# Mensaje Separador Abajo
# pTexto hace referencia a que quiere ingresar
def mensajeSeparadorAbajo(pTexto):
    print(
        f'               {pTexto}')
    separador()

# PedirNumeros.
# Text hace referencia a que quiere ingresar
# (Una opcion, precio de venta, costo de venta, existencia, stock minimo).
def pedirNumero(text):
    while True:
        try:
            numero = int(input(f'  ★ Ingrese {text}: '))
        except ValueError:
            mensajeSeparadorArribaAbajo(
                ' ★ Debe ingresar número enteros. \n                          ★ Intente nuevamente!')
        else:
            if numero >= 1:
                return numero
            else:
                mensajeSeparadorArribaAbajo(
                    ' ★ Debe ingresar número enteros. \n                          ★ Intente nuevamente!')

# MENU
def menu():
    print(f"""                            MENU DE PRODUCTOS
        ★ 1 - Añadir/Modificar Productos
        ★ 2 - Buscar Productos
        ★ 3 - Productos a Pedir
        ★ 4 - Borrar Productos
        ★ 5 - Actualizar datos Productos
        ★ 6 - Listar Productos
        ★ 7 - Salir""")
    separador()
    while True:
        selec = pedirNumero('una opcion')
        if 1 <= selec <= 6:
            return selec
        elif selec == 7:
            mensajeSeparadorArribaAbajo('          Adios!')
            exit()
        else:
            mensajeSeparadorArribaAbajo(
                ' ★ Debe ingresar un número del 1 al 7. \n                          ★ Intente nuevamente!')

# CodigoBarraId
# Verifica si el codigo de barras presenta la cantidad de numeros que correspode:
def codigoBarraId(id):
    if len(str(id)) != 13:
        mensajeSeparadorArribaAbajo(
            ' ★ Debe ingresar un codigo de barra de 13 digitos. Sin espacio. \n                          ★ Intente nuevamente!')
        return False
    else:
        return True

# descripcionProducto
# pParametro hace referencia a que quiere ingresar
# (La descripcion o una parte de la descripción).
def descripcionProducto(pParametro):
    while True:
        try:
            caracter = input(f'  ★ Ingrese {pParametro}: ')
        except ValueError:
            mensajeSeparadorArribaAbajo(
                ' ★ Debe ingresar caracteres validos. \n                          ★ Intente nuevamente!')
        else:
            return caracter.capitalize()

# existeVar
# Verifica si existe el codigo de barras ingresada esta dentro del diccionario
def existeVar(pProducto):
    if pProducto in dProductos.keys():
        return True

# Verifica si existe la descripcion ingresado esta dentro del diccionario
def existeProducto(letra):
    for producto in dProductos.values():
        if producto['Descripcion'].startswith(letra.capitalize()):
            return True
    return False

# Verifica si existe la descripcion ingresado especifica esta dentro del diccionario
def existeProductoEspecifico(letra):
    for producto in dProductos.values():
        if producto['Descripcion'] == letra:
            return True
    return False

# añadirModificar
# Permite pedir el codigo de barras, verifica si esta la cantidad de numeros que corresponde (13 digitos), y si existe muetra los datos, sino permite cargar al sistema.
def añadirModificar():
    while True:
        codi = pedirNumero('el codigo de barras')
        if codigoBarraId(codi):
            if existeVar(codi):
                mensajeSeparadorArribaAbajo(
                    f'  ★ Ya existe el codigo de barra: {codi}.')
                print('                ★ Los datos del producto son:')
                for clave, valoresdiccio in dProductos.items():
                    if clave == codi:
                        for key, valores in valoresdiccio.items():
                            print(f'       ★ {key}: {valores}.')
                        separador()
                break
            else:
                mensajeSeparadorAbajo(f'El {codi} no existe todavia')
                print("Ingrese los datos del producto: ")
                descrip = descripcionProducto('la descripcion')
                pCosto = pedirNumero('el precio de costo')
                pVentas = pedirNumero('el precio de venta')
                existencia = pedirNumero('el n° existencia')
                stockMinimo = pedirNumero('el stock Minimo')
                dProductos[codi] = dict(Descripcion=descrip, PrecioCosto=pCosto,
                                        PrecioVenta=pVentas, Existencia=existencia, StockMinimo=stockMinimo)
                mensajeSeparadorArribaAbajo('★ Se ha guardado con exito!')
            break

# BuscarProductos
def buscarProductos():
    while True:
        print('Desea buscar el producto por codigo de barra o por descripcion? \n           ★ 1-Codigo de barra.\n            ★ 2-Descripcion')
        separador()
        opcion = pedirNumero('una opcion')
        separador()
        if opcion == 1:
            while True:
                codi = pedirNumero('el codigo de barras')
                if codigoBarraId(codi):
                    if codi in dProductos.keys():
                        mensajeSeparadorArribaAbajo(
                            f"     ★ Descripcion: {dProductos[codi]['Descripcion']}\n        ★ Existencia: {dProductos[codi]['Existencia']}")
                        break
                    else:
                        mensajeSeparadorArribaAbajo(
                            f'    El codigo de barras: {codi} no existe.')
                        break
                else:
                    mensajeSeparadorAbajo(
                        f'   No es un codigo de barras: {codi}.')
            break
        elif opcion == 2:
            descP = descripcionProducto('una parte de la descripción')
            separador()
            if existeProducto(descP):
                mensajeSeparadorAbajo(
                    f'      ★ Los productos encotrados con la cadena de caracteres {descP} son:')
                for clave, valores in dProductos.items():
                    if valores['Descripcion'].startswith(descP.capitalize()):
                        print('     ★ Descripción:', valores['Descripcion'])
                        print('         ★ Existencia:', valores['Existencia'])
                separador()
                break
            else:
                mensajeSeparadorAbajo(
                    f"No existe ningun producto con esos caracteres: {descP}")
                break
        else:
            mensajeSeparadorAbajo(
                ' ★ Seleccione una opcion valida. 1- Codigo de Barras. 2- Descripcion')

# Productos a pedir.
#  Se compara el valor de existencia <= que el stock minimo.
def productosAPedir():
    hayProductos = False
    concatenar = ''
    for keys, valores in dProductos.items():
        if valores['Existencia'] <= valores['StockMinimo']:
            hayProductos = True
            concatenar += (
                f'      ★ Codigo de Barra: {keys}.\n       ★ Detalle:'f' {valores["Descripcion"]}.\n        ★ Stock en Existencia: 'f'{valores["Existencia"]}\n         ★ Stock Minimo: {valores["StockMinimo"]}\n══ ☆ ══════ ☆ ══════ ☆ ══════ ☆ ══════ ☆ ══════ ☆ ══════ ☆ ══════ ☆ ══════ ☆ ══════ ☆ ══════ ☆ ══\n')
    if hayProductos:
        mensajeSeparadorAbajo(
            ' Los productos que se encuentran debajo del stock minimo son:')
        print(concatenar)
    else:
        print('No hay productos por debajo del stock mínimo')

# borrarProducto
# Actualiza los datos de un codigo de barras especifico.
def borrarProducto():
    while True:
        codi = pedirNumero('el codigo de barras')
        if codigoBarraId(codi):
            if existeVar(codi):
                for keys, valores in dProductos.items():
                    if keys == codi:
                        separador()
                        print(
                            f'Seguro que quiere eliminar el producto: ★ 'f' {valores["Descripcion"]}? \n           ★ 1 - Si.\n            ★ 2 - No.')
                        while True:
                            opcion = pedirNumero('una opcion')
                            if opcion == 1:
                                del dProductos[codi]
                                mensajeSeparadorArribaAbajo(
                                    '★ Se ha borrado con exito!')
                                break
                            elif opcion == 2:
                                mensajeSeparadorArribaAbajo(
                                    '★ Se ha cancelado los cambios!')
                                break
                            else:
                                mensajeSeparadorArribaAbajo(
                                    ' ★ Debe ingresar una opcion valida! 1 - Si o 2 - No. \n                          ★ Intente nuevamente!')
                        break
            else:
                mensajeSeparadorAbajo(f'El {codi} no existe.')
            break

# actualizarDatos
# Actualiza los datos de una descripcion especifica.
def actualizarDatos():
    while True:
        descP = descripcionProducto('La descripción')
        if existeProductoEspecifico(descP):
            for producto in dProductos.values():
                if descP in producto['Descripcion']:
                    mensajeSeparadorArribaAbajo(
                        " ★ El precio de venta es: " + str(producto['PrecioVenta']))
                    porcentaje = pedirNumero(
                        'el porcentaje a aumentar. Sin % ni coma (,)')
                    elPorcentaje = (producto['PrecioVenta']*porcentaje)/100
                    nuevoPrecio = producto['PrecioVenta']+elPorcentaje
                    mensajeSeparadorArribaAbajo(
                        " ★ El nuevo precio de venta es: $" + str(int(nuevoPrecio)))
                    # Actualizacion de precio
                    nuevoPrecio = int(nuevoPrecio)
                    producto['PrecioVenta'] = nuevoPrecio
                    break
        else:
            mensajeSeparadorAbajo(
                f"No existe ningun producto con esa descripción: {descP}")
            break
        break

# Listar los productos.
def listarProductos():
    print(f"Productos Cargados: ")
    for key, dValores in dProductos.items():
        print(f'               ★ Codigo de Barras: {key}')
        for clave, valor in dValores.items():
            if clave == 'StockMinimo':
                mensajeSeparadorAbajo(f'★ {clave}: {valor}.')
            else:
                print(f'               ★ {clave}: {valor}.')

# programaPrincipal
# Ejecucion de menu.
def programaPrincipal():
    while True:
        eleccionUsuario = menu()
        if eleccionUsuario == 1:
            añadirModificar()
        elif eleccionUsuario == 2:
            separador()
            buscarProductos()
        elif eleccionUsuario == 3:
            separador()
            productosAPedir()
        elif eleccionUsuario == 4:
            separador()
            borrarProducto()
        elif eleccionUsuario == 5:
            separador()
            actualizarDatos()
        elif eleccionUsuario == 6:
            listarProductos()
