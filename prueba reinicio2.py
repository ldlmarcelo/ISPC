import time
import sys
import os

# función para reiniciar el programa
def reiniciar_programa():
    python = sys.executable
    os.execl(python, python, *sys.argv)

# el programa principal
while True:
    # aquí colocas el código que deseas ejecutar continuamente
    print("El programa está funcionando...")

    # esperar durante 10 segundos antes de volver a ejecutar el código
    time.sleep(1)

    # aquí puedes colocar una condición que determine cuándo reiniciar el programa
    if 1!=2:
        reiniciar_programa()
