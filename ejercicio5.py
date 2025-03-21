'''Ejercicio 5
Escribir un programa que pida al usuario un número entero mayor a 0 (se debe validar el número) y se calcule el factorial de ese número.
el factorial de un número n se calcula multiplicando los números enteros empezando desde 1 hasta el número n ejemplo:.
5! = 5 × 4 × 3 × 2 × 1 = 120
Respuesta Esperada:
Introduce un número entero:  5
El factorial de 5 es: 120'''

factorial=1
numero = int(input('ingrese un numero entero mayor a cero'))
if numero >= 0:
    for i in range(numero, 0, -1):
        factorial*=i
    print ('El factorial de 5 es: ',factorial)
else:
    print("no es mayor a cero")