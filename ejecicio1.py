'''Ejercicio 1
Escribir un programa que almacene en una lista los siguientes precios,
lista = [50, 75, 46, 22, 80, 65, 3, 15]
y muestre por pantalla el menor y el mayor de los precios.
Respuesta Esperada:
El mínimo es:   3
El máximo es:   80'''
lista = [50, 75, 46, 22, 80, 65, 3, 15]
# lista = [50, 75, 46, 22, 80,-2, 65, 3, 15,99,1]
menor = min(lista)
mayor = max(lista)
print("El mínimo es:", menor)
print("El máximo es:", mayor)
# otra forma
min=999999
max=0
for elemento in lista:
    if elemento>max:
        max=elemento
    if elemento<min:
        min=elemento
print('maximo de la lista es:',max,'el menor de la lista es:',min)