from fpdf import FPDF

print("====================================")
print("CREACIÓN DE HOJA DE VIDA ")
print("====================================\n")

# Datos personales
nombre = input("Ingresa tu nombre completo: ")
edad = input("Ingresa tu edad: ")
ciudad = input("Ingresa tu ciudad y departamento: ")
correo = input("Ingresa tu correo electrónico: ")
telefono = input("Ingresa tu número de teléfono: ")

# Perfil
perfil = input("\n Escribe tu perfil profesional: ")

# Estudios
print("\n Vamos a registrar tu formación académica.")
titulo = input("  - ¿Qué título tienes o estás estudiando?: ")
institucion = input("  - ¿En qué institución?: ")
anio_estudio = input("  - ¿En qué año fue o será?: ")

# Experiepncia
print("\nAhora tu experiencia laboral.")
cargo = input("  - ¿Qué cargo tuviste?: ")
empresa = input("  - ¿Dónde trabajaste?: ")
anio_exp = input("  - ¿En qué año?: ")

# Habilidades
print("\n Escribe 3 habilidades personales o técnicas.")
hab1 = input("  - Habilidad 1: ")
hab2 = input("  - Habilidad 2: ")
hab3 = input("  - Habilidad 3: ")

# Idiomas
idioma = input("\n ¿Qué idiomas hablas y en qué nivel?: ")

# Proyecto
proyecto = input("\n ¿Has hecho algún proyecto importante? Describe uno: ")

# Mostrar hoja de vida en pantalla
print("\n============================")
print("       HOJA DE VIDA         ")
print("============================\n")

print(f" Nombre: {nombre}")
print(f" Edad: {edad}")
print(f"Ciudad: {ciudad}")
print(f"Correo: {correo}")
print(f"Teléfono: {telefono}")

print(f"\n Perfil profesional:\n{perfil}")

print(f"\nFormación académica:\n- {titulo} en {institucion} ({anio_estudio})")

print(f"\nExperiencia laboral:\n- {cargo} en {empresa} ({anio_exp})")

print("\nHabilidades:")
print(f"- {hab1}")
print(f"- {hab2}")
print(f"- {hab3}")

print(f"\nIdiomas:\n- {idioma}")

print(f"\nProyecto destacado:\n- {proyecto}")

# Exportar a archivo de texto
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Título
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="HOJA DE VIDA", ln=True, align='C')

pdf.ln(10)  # Espacio vertical

# Contenido
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt=f"Nombre: {nombre}", ln=True)
pdf.cell(200, 10, txt=f"Edad: {edad}", ln=True)
pdf.cell(200, 10, txt=f"Ciudad: {ciudad}", ln=True)
pdf.multi_cell(0, 10, txt=f"Perfil Profesional:\n{perfil}")

# Guardar archivo
nombre_archivo = f"hoja_de_vida_{nombre.lower().replace(' ', '_')}.pdf"
pdf.output(nombre_archivo)

print(f"\nPDF generado como '{nombre_archivo}'")