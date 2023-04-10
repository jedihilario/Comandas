import os
from pui import *
from comanda import Comanda
from db import Query

comandas = []

def upload ():
    os.system('cls')

    form = Form(['orden', 'cliente', 'monto', 'para llevar'])
    data = form.render()

    comanda = Comanda(*(i for i in data))
    comandas.append(comanda)
    Query.insert(comanda.getAttributesAsDict())

    mainMenu()

def delete ():
    os.system('cls')

    target = (input('Ingrese el apellido de la comanda que quiere eliminar: ')).lower()
    
    for i, comanda in enumerate(comandas):
        if (target == comanda.client):
            target = i; break

    try: 
        comandas.pop(target)
        print('Comanda eliminada!')
    except:
        print('No se encontro la comanda para eliminar :(')

    input()
    mainMenu()

def modify ():
    pass

def listar ():
    os.system('cls')

    for comanda in comandas:
        print(f'''\n {'-' * 8} 
|
| Orden: {comanda.order}
| Cliente: {comanda.client}
| Precio: {comanda.amount}
|
| Para llevar: {comanda.delivery}
|
 {'-' * 8} ''')

    input()
    mainMenu()

def listarEnvios ():
    res = Query.selectDelivery()

    deliveries = [Comanda(*i) for i in res]

    for delivery in deliveries:
        print(f'''\n {'-' * 8} 
|
| Orden: {delivery.order}
| Cliente: {delivery.client}
| Precio: {delivery.amount}
|
 {'-' * 8} ''')
        
    input()
    mainMenu()

def revenue ():
    os.system('cls')

    result = 0

    for comanda in Query.selectAll():
        result += comanda['amount']

    res = Title(f'La ganancia del dia es de: {result}', 'green', 2, 2, '*')
    res.render()
    input()
    mainMenu()

def mainMenu ():
    os.system('cls')

    title = Title('Gestor de Comandas', 'yellow', 2, 2)
    
    options = OptionsMenu(['Cargar', 'Modificar', 'Eliminar', 'Listar', 'Listar envios', 'Ingreso total', 'Salir'],
                          [
                            upload,
                            modify,
                            delete,
                            listar,
                            listarEnvios,
                            revenue,
                            lambda: exit()
                          ], ' <', 'green')
    
    title.render()
    options.render([title])
