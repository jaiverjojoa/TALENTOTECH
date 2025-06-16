print('Ejercicio 6')
import string

nombre_completo: string = 'Jaiver jojoa'
nombre_mayusculas: string = nombre_completo.upper()
nombre_remplazado: string = nombre_completo.replace('a','@')
nombre_sin_espacios: string = nombre_completo.strip()

print('Nombre en mayusculas',nombre_mayusculas)
print('Nombre remplazado',nombre_remplazado)
print('Nombre sin espacios:', nombre_sin_espacios)

