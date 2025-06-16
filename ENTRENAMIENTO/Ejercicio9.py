print('Ejercicio 9')
import string
texto: string = 'La tecnologia avanza rapidamente. La tecnologia esta cambiando el mundo.'

contador_a: string = texto.count('a')
print("La palabra 'tecnologia' aparece:",contador_a,"veces repetida en el texto")

posicion_palabra: string = texto.find('mundo')
print("La palabra 'mundo' esta en la posicion:",posicion_palabra)

palabra_remplazada: string = texto.replace('tecnologia','tierra')
print("La plabra'tecnologia' se remplaza por 'tierra'")
print(palabra_remplazada)
