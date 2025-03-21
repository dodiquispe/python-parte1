'''Ejercicio 3
Escribir un programa que pida al usuario un número entero mayor a 0 (se debe validar el número) y muestre por pantalla la cuenta hacia atrás desde ese número hasta llegar a cero separados por comas.
Respuesta Esperada:
Introduce un número entero:  8

8, 7, 6, 5, 4, 3, 2, 1, 0,'''
try:
    numero = int(input('ingrese un numero entero mayor a cero'))
    if numero >= 0:
        for i in range(numero, -1, -1):
           print(i)
    else:
      print("no es mayor a cero")
except:
   print("no es un numero entero")