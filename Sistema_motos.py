from moto import moto


# Crear una lista vacía para almacenar las motos
motos = []

# Variable para controlar si se deben cargar más motos
cargar_moto = True

while cargar_moto:
    marca = input("Indicar la marca: ")
    modelo = input("Indicar el modelo: ")
    patente = input("Indicar la patente: ")
    kilometraje = input("Indicar kilometraje: ")
    patentado = input("Indicar el año de patentamiento: ")
    color = input("Indicar el color: ")
    litros = input("Indicar capacidad del tanque de combustible: ")

    # Crear una nueva instancia de la clase moto con los datos ingresados
    nueva_moto = moto(marca, modelo, patente, int(kilometraje), int(patentado), color, int(litros))

    # Agregar la nueva moto a la lista de motos
    motos.append(nueva_moto)

    # Preguntar si se desea cargar otra moto
    respuesta = input("¿Deseas cargar otra moto? (s/n): ")
    if respuesta.lower() != 's':
        cargar_moto = False

# Mostrar las motos ingresadas
for index, moto in enumerate(motos, start=1):
    print(f"Moto {index}: {moto}")
    


