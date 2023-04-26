import os
from pui import *
from comanda import Comanda
from db import Query

delivery_senteneces = {
    'False': 'Comanda sin envio',
    'True' : 'Comanda con envio'
}

def upload ():
    os.system('cls')

    form = Form(['orden', 'cliente', 'monto', 'para llevar'])
    data = form.render()

    comanda = Comanda(*(i for i in data))
    comanda.applyDiscount()
    Query.insert(comanda.getAttributesAsDict())

    mainMenu()

def delete ():
    os.system('cls')

    target = (input('Ingrese el apellido de la comanda que quiere eliminar: ')).lower()

    Query.delete(target)

    input()
    mainMenu()

def modify ():
    os.system('cls')

    

    input()
    mainMenu()

def listar ():
    os.system('cls')
    try:
        res = Query.selectAll()

        data = []

        for com in res:
                values = com.values()
                data.append(values)

        comandas = [Comanda(*i) for i in data]

        for comanda in comandas:
            print(f'''\n {'-' * 8}
|
| Orden: {comanda.order}
| Cliente: {comanda.client}
| Precio: {comanda.amount}
|
| {delivery_senteneces[str(comanda.delivery)]}
|
{'-' * 8} ''')
    except:
        print('No hay comandas cargadas!')

    input()
    mainMenu()

def listarEnvios ():
    os.system('cls')
    res = Query.selectDelivery()

    comandas = [Comanda(*i) for i in res]

    for delivery in comandas:
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
    try:
        for comanda in Query.selectAll():
            result += comanda['amount']

        res = Title(f'La ganancia del dia es de: {result}', 'green', 2, 2, '*')
        res.render()
    except:
        print('No hay comandas cargadas!')

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
