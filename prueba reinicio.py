import sys

def reiniciar_programa():
    # Aquí debes colocar el código que deseas que se ejecute antes de reiniciar el programa
    print("Reiniciando programa...")
    # Salir del programa
    sys.exit()

# Aquí comienza el programa principal
while True:
    print("Iniciando programa...")
    # Coloca aquí el código que deseas ejecutar antes de reiniciar el programa

    # Ejemplo: Preguntar si desea reiniciar el programa
    respuesta = input("¿Desea reiniciar el programa? (S/N): ")
    if respuesta == "S":
        reiniciar_programa()

    # Aquí continua el resto del programa
    print("Programa finalizado.")