# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json
from re import M
import requests
import numpy as np

import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Ejercicio de consumo de datos por API
    url = "https://jsonplaceholder.typicode.com/todos"

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general:
    # 1) Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # 2) Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # 3) En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".


    # Alumno, de cada usuario en el total de las 200 entradas
    # debe contar cuantos títulos completó cada usuario (de los 10 posibles)
    # y armar un gráfico de barras resumiendo la información.
    # gráfico en el eje "x" está cada uno de los 10 usuarios y en el eje
    # "y" la cantidad de títulos completados

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.

    # Debe poder graficar dicha información en un gráfico de barras.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.


    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    data = response.json()
    print('Imprimir los datos traídos de la nube')
    print(json.dumps(data, indent=4))

    
    
        
    titulos_completados = [user['userId'] if user['completed'] == True else 0 for user in data]

    usuarios = []

    lista_titulos = []
    

    for i in range(1,11):

        print('El usuario',i, 'ha completado ', titulos_completados.count(i), 'títulos')

        usuario = str(i)
        usuarios.append(usuario)

        
        titulos = titulos_completados.count(i)
        lista_titulos.append(titulos)

    print(usuarios, lista_titulos)

    

    #Voy a crear el gráfico con las dos listas
    
    

    fig = plt.figure()
    fig.suptitle('Títulos obtenidos por usuario', fontsize=16)
    
    ax = fig.add_subplot()


    ax.bar(usuarios, lista_titulos, label='Títulos')
    ax.set_facecolor('whitesmoke')
    ax.legend()
    plt.show()



    print("terminamos")