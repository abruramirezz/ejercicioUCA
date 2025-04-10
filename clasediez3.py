'''
import random

numero = random.randint(1,100)
#crear una lista de 20 posiciones, agregarle a la lista numeros aleatorios del 1 y 200

lista=[]
for i in range(20):
    numero= random.randint(1,100)
    if numero not in lista:
       lista.append(numero)
    print(lista)
'''

persona= {"nombre":"Abril","edad":19,"ciudad":"Parana"}
print(persona["ciudad"])

#crear una lista con numeros del 8 al 45 y una lista de 6 numeros elegidos por nosotros.
#simular del 1 al 45 con el random, y a su vez guardar en otra lista los numeros que van saliendo hasta que ganemos.
#poner 2 jugadores y un ganador

