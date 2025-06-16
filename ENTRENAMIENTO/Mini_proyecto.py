import datetime

nombre = input("Ingresa tu nombre: ")
apellido =input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
correo = input("Ingresa tu correo electrónico: ")
numero_favorito= int(input("Ingrese su numero favorito: "))

print("\n------------Datos registrados--------------")
print(f"\nPerfil registrado:\nNombre completo: {nombre} {apellido}\nEdad: {edad} \nEmail: {correo} \nnumero_favorito:{numero_favorito}")

print("\n------------Numero favorito--------------")
resultado_numero_favorito=numero_favorito + 5
print("\nEl resultado de su numero favortio al sumarle 5 es:", resultado_numero_favorito)

print("\n-----------Creacion de usuarios------------")
usuario =f"{nombre[0].lower()}{apellido.lower()}{edad[-2:]}"
print("\nUsuario:",usuario)

print("\n-----------Verificacion de correo----------")
if'@' in correo:
    print('\nEl correo es valido.')
else:
    print("\nError: el correo debe tener'@'.")

resumen=f"""
=== Perfil ===
Nombre completo:{nombre} {apellido}
Edad:{edad}
Correo:{correo}
"""
print(resumen)

print("\n-----------Aviso----------")
fecha_actual = datetime.datetime.now()
anio_actual = fecha_actual.year
print(f"\nRegistro completado en el año {anio_actual}")

print("\n----------Programa de conteo----------")
nombre_completo =f"{nombre} {apellido}"
caracteres_sin_espacios=len(nombre_completo.replace(" ",""))
cantidad_a = nombre_completo.lower().count("a")
cantidad_palabras = len(nombre_completo.split())
print("\n=== Análisis del nombre completo ===")
print(f"Nombre completo: {nombre_completo}")
print(f"Cantidad de caracteres (sin espacios): {caracteres_sin_espacios}")
print(f"Cantidad de veces que aparece la letra 'a': {cantidad_a}")
print(f"Cantidad de palabras: {cantidad_palabras}")

print("\n Taller finalizado")
