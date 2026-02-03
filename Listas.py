#Ejercicio 1
#Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y 
#posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.
import random

lista: list[int] = [ ]

for i in range(10):
    lista.append(random.randint(1,10))

for numero in lista:
    print(f'El numero de posicion {lista.index(numero) + 1} es {numero}, su cuadrado es {numero*numero} y su cubo es {numero*numero*numero}')

#Ejercicio 2
#Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado. Copia los elementos de 
#la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.

lista1:list[str] = []
for i in range(5):
    x = input("Ingrese una cadena de caracteres")
    lista1.append( x )

lista2:list[str] = []

for i in range (5):
    lista2.append(lista1[-i-1])

print(lista1, lista2)

#Ejercicio 3
#Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). 
# A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.

lista3:list[int] = []

for i in range(5):
    x = -1
    while(x < 0 or x >10):
        x = int(input(f"Ingrese su nota {i+1}: "))
    lista3.append(x)

max = -1
min = 10
prom = 0

for notas in lista3:
    print(f"La nota {lista3.index(notas)} es {notas}")
    if (notas > max):
        max = notas
    if ( notas < min):
        min = notas
    prom = prom + notas

prom = prom/5
print(f"La nota media fue {prom}, la nota mas alta fue {max} y la nota menor fue {min}")

    