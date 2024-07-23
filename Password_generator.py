import string
import random
import pyperclip
import os

def generar_contraseña(longitud=12, incluir_mayusculas=True, incluir_minusculas=True, incluir_digitos=True, incluir_simbolos=True):
    caracteres = ''
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_digitos:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Debe incluir al menos un tipo de carácter para generar la contraseña.")

    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return contraseña

def copiar_al_portapapeles(contraseña):
    pyperclip.copy(contraseña)
    print("La contraseña ha sido copiada al portapapeles.")

def guardar_en_escritorio(contraseña):
    escritorio = os.path.join(os.path.expanduser('~'), 'Desktop')
    ruta_archivo = os.path.join(escritorio, "contraseña_generada con éxitos.txt")
    
    with open(ruta_archivo, 'w') as archivo:
        archivo.write(contraseña)
    
    print(f"La contraseña ha sido guardada en {ruta_archivo}")
    copiar_al_portapapeles(ruta_archivo)

def clasificar_contraseña(contraseña):
    longitud = len(contraseña)
    tiene_mayusculas = any(c.isupper() for c in contraseña)
    tiene_minusculas = any(c.islower() for c in contraseña)
    tiene_digitos = any(c.isdigit() for c in contraseña)
    tiene_simbolos = any(c in string.punctuation for c in contraseña)

    puntuacion = longitud
    if tiene_mayusculas:
        puntuacion += 2
    if tiene_minusculas:
        puntuacion += 2
    if tiene_digitos:
        puntuacion += 2
    if tiene_simbolos:
        puntuacion += 2

    if puntuacion >= 16:
        return "Muy Fuerte"
    elif puntuacion >= 12:
        return "Fuerte"
    elif puntuacion >= 8:
        return "Moderada"
    else:
        return "Débil"

def interfaz_bienvenida():
    print("Bienvenidos al Generador de Contraseñas Seguras de Arturo Cochea, comenzaremos en realizarte preguntas simples y concretas!")
    respuesta = input("¿Deseas crear una contraseña segura? (si/no): ").lower()
    
    if respuesta == 'si':
        longitud = int(input("Introduce la longitud de la contraseña: "))
        incluir_mayusculas = input("¿Incluir letras mayúsculas? (si/no): ").lower() == 'si'
        incluir_minusculas = input("¿Incluir letras minúsculas? (si/no): ").lower() == 'si'
        incluir_digitos = input("¿Incluir dígitos? (si/no): ").lower() == 'si'
        incluir_simbolos = input("¿Incluir símbolos? (si/no): ").lower() == 'si'

        try:
            contraseña = generar_contraseña(longitud, incluir_mayusculas, incluir_minusculas, incluir_digitos, incluir_simbolos)
            print("Contraseña generada:", contraseña)
            clasificacion = clasificar_contraseña(contraseña)
            print(f"Clasificación de la contraseña: {clasificacion}")
            guardar_en_escritorio(contraseña)
        except ValueError as e:
            print(f"Error: {e}")
    elif respuesta == 'no':
        print("Vuelva pronto!. Estaremos disponibles si necesitas ayuda.")
    else:
        print("Respuesta no válida. Por favor, elija la respuesta con un 'si' o 'no'.")

if __name__ == "__main__":
    interfaz_bienvenida()
