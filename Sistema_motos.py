from moto import moto



marca = input("indicar la marca: ")
modelo = input("indicar el modelo: ")
patente = input("indicar la patente: ")
kilometraje =input("indicar kilometraje: ")

moto1=moto(marca,modelo,patente,kilometraje)


print(str(moto1))