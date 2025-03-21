'''Ejercicio 4
Escribir un programa que pida al usuario una frase y cuente cuántas vocales (a, e, i, o, u) tiene.
Respuesta Esperada:
Introduce una frase:  frase se prueba para conteo de palabras
La vocal 'a' aparece 7 veces.
La vocal 'e' aparece 5 veces.
La vocal 'i' aparece 0 veces.
La vocal 'o' aparece 2 veces.
La vocal 'u' aparece 1 veces.'''
frase = input('Introduce una frase: ')
print (frase)
vocales = 'aeiou'
for vocal in vocales:
    print(f'La vocal \'{vocal}\' aparece {frase.count(vocal)}')