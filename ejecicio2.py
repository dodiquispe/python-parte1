# '''Ejercicio 2
# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
# Nota.- una palabra es palindromo cuando se lee igual de izquierda a derecha como de derecha a izquierda, ejemplo:
# anitalavalatina
# Se lee igual empezando de izquierda o de derecha.
# Respuesta Esperada:
# Introduce una palabra:  arañara
# Es un palíndromo'''
palabra = input("Introduce una palabra: ")
palabra = palabra.replace(" ", "").lower()
if palabra == palabra[::-1]:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")

