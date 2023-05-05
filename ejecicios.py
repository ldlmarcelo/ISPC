#Colecciones de datos
print("#######################################################")
print("#########################LISTAS########################")
print("#######################################################")

print("----------------------------")
print("Lista de números")
numeros=[1,2,3,4,5]
print(numeros)


print("----------------------------")
print("Listas de cadenas")
nombres=["Ana","Jorge","Ariel","Paula"]
print(nombres)

 
print("----------------------------")
print("Lista de elementos de diferentes tipos")
datos =["1","hola",True,"3.14","True"]
print(datos)


print("----------------------------")
print("Lista vacía")
lista_vacia=[]
print(lista_vacia)

print("----------------------------")
print("imprimir nombres por índice")
print(nombres[0])
print(nombres[1])
print(nombres[2])
print(nombres[3])


print("----------------------------")
print("Actualizar por índice modifico indice 1")
nombres[1]="María111111111111111111111111"

print(nombres[0])
print(nombres[1])
print(nombres[2])
print(nombres[3])

nombres[-1]="asdlfkjañlkdfjñak"

print("imprimir por indice negativo modifico último")
print(nombres)



print("----------------------------")
print("acceder  por rebanada slicing")
print(numeros)
print("imprimir rebanado 2:4")
print(numeros[2:4])
print("imprimir rebanado :3 (desdel el principio hasta)")
print(numeros[:3])
print("imprimir rebanado 3: (desde el 3 hasta el fin)")
print(numeros[3:])


print("----------------------------")
print("imprimir cada 2 indices")
print(numeros[::2])


print("----------------------------")
print("listas anidadas")
matriz=[[1,2,3],[4,5,6],[7,8,9]]
print(matriz)
print("por índice")
print(matriz[1])
print(matriz[1][0]) 
print(matriz[0]) 

#OPERACIONES CON LISTAS

print("----------------------------")
print("Agregar elementos a una lista método append")
numeros.append(6)
print(numeros)
matriz.append([10,11,12])
print(matriz)

print("----------------------------")
print("Agregar varios elementos a una lista método extend")
numeros.extend([13,14,14])
print(numeros)
matriz.extend([[12,12,12],[13,13,13]])
print(matriz)

print("----------------------------")
print("método insert un elemento en un índice específico")
print(numeros)
numeros.insert(4,"insertado")
print(numeros)

print("----------------------------")
print("eliminar elementos de una lista")
numeros.remove("insertado")
print(numeros)
numeros.remove(14)
print(numeros)
numeros.remove(7+7)
print(numeros)

print("----------------------------")
print("Eliminar elementos de una lista por indice método del ")
print(numeros)
del numeros[-1]
print(numeros)


print("----------------------------")
print("CONCATENAR LISTAS OPERADOR + ")
lista1=[1,2,3]
print(lista1)
lista2=[3,4,5]
print(lista2)
lista3=lista1+lista2
print(lista3)



print("----------------------------")
print("ORDENAR UNA LISTA METODO SORT ")
lista=[3,5,11,6,23,18]
lista.sort()
print(lista)


print("----------------------------")
print("ORDENAR METODO REVERSE ")
lista=[3,5,11,6,23,18]
lista.sort(reverse=True)
print(lista)
lista.reverse()
print(lista)


print("----------------------------")
print("Contar elementos metodo count ")

lista=[1,1,1,1,1,1,2,2,3,1,0,1,2,3,5]
print(lista,"cuenta la cantidad de 1")
cantidad=lista.count(1)
print(cantidad)

print("----------------------------")
print("Contar TODOS elementos metodo len ")

lista=[1,1,1,1,1,1,2,2,3,1,0,1,2,3,5]
print(lista,"cuenta todos los elementos")
cantidad=len(lista)
print(cantidad)


print("#######################################################")
print("#########################TUPLAS########################")
print("#######################################################")



print("----------------------------")
print("esto es una tupla")
tupla=(1,2,3,"cuatro",5.0)
print(tupla)

print("----------------------------")
print("Acceder a un elemento de la tupla mediante índice [3] ")
print(tupla[3])


print("----------------------------")
print("tupla vacia")
tupla=()
print(tupla)


print("----------------------------")
print("tupla con 1 elemento ")
tupla=(12000,)
print(tupla)

print("----------------------------")
print("tupla con 1 elemento ")
tupla=(12000)
print(tupla)

print("----------------------------")
print("Acceder a elementos de una tupla mediante índice [3] ")
tupla=(1,2,3,"cuatro",5.0)
print(tupla[3])

print("----------------------------")
print("Acceder al último elemento mediante índice negativo [-1] ")
tupla=(1,2,3,"cuatro",5.0)
print(tupla[-1])


print("#######################################################")
print("#########################DICCIONARIOS##################")
print("#######################################################")


print("----------------------------")
print("Esto es un diccionario")
edades={'juan':25,'pedro':38,'anaines':23}
print(edades)


print("----------------------------")
print("acceso al valor y clave ")
print(edades)
print(edades['juan'])


print("----------------------------")
print("Agregar una nueva clave y valor ")
print(edades)
edades['Francisco']=22
print(edades)

print("----------------------------")
print(" ")


print("----------------------------")
print(" ")

print("----------------------------")
print(" ")
