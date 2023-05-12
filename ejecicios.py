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
print("obtener una lista con todas las claves método keys ")
print(edades.keys())

print("----------------------------")
print("obtener una lista con todos los valores método values ")
print(edades.values())

print("----------------------------")
print("obtener una lista con clave y valor método items")
print(edades.items())

print("----------------------------")
print(" ")

print("----------------------------")
print(" ")

print("#######################################################")
print("#####ESTRUCTURAS ALTERNATIVAS O CONDICIONALES #########")
print("#######################################################")

print("sentencia if")
a=1
b=2

if b>a:
    print("b es mayor que a")
    
print("----------------------------")
print("sentencia if else")

if b>a:
    print("b es mayor que a")
else:   
    print("a es mayor que b")
    
print("----------------------------")
print("sentencia elif")

print("Si esto no es verdadero, intenta esto otro, y si todas las condiciones fallan en")
print("ser verdaderas, entonces haz esto.")

x=20
if x<20:
    print("x es menor a 20")

elif x>20:
    print("x es mayor que 20")
    
else: 
    print("x = 20")
    
print("#######################################################")
print("#############Ejercitación CONDICIONALES ###############")
print("#######################################################")    

print("1- Realice un programa que solicite dos letras ingresadas por el usuario y")
print("verifique si son iguales o no, mostrando un mensaje.")

letra1=input("ingrese una letra: ")
letra2=input("ingrese otra letra: ")

if letra1==letra2:
    print("las letras son iguales ")
else:
    print("las letras no son iguales ")

print("----------------------------")
print("2. Hacer un programa que permita decidir si dos palabras son iguales o")
print("diferentes. Mostrar mensaje por pantalla.")

palabra1=input("ingrese una palabra: ")
palabra2=input("ingrese otra palabra: ")

if palabra1==palabra2:
    print("las palabras son iguales ")
else:
    print("las palabras no son iguales ")

print("----------------------------")
print("3. Realizar un programa que permita ingresar “f” o “m” y determinar si vota")
print("en mesa femenina o masculina.")

sexo=input("Ingrese f para feminino y m para masculino: ")
if sexo=="f":
    print("usted vota en mesa femenina ")
elif (x!="v" or x!= "f"):
    print("no ingreso una opción correcta ")
else:
    print("usted vota en mesa masculina ")
    
print("----------------------------")
print("4. Realice un programa que lea dos números y diga cuál es el mayor.")

numero1=input("Ingrese el primer número")
numero2=input("Ingrese el segundo número")

if numero1>numero2:
    print(numero1," es mayor que ", numero2)
elif numero2>numero1:
    print(numero1," es menor que ", numero2)
elif numero1==numero2:
    print("los números son iguales")
    
else:
    print("no ingresó números válidos")
    
print("----------------------------")
print("5. Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo ")
print("el cambio de dólares a pesos y que sea el usuario quién decida qué tipo ")
print("de cambio quiere, si de dólares a pesos o viceversa. ")

moneda=input("ingresa la moneda que quiere vender. D para dolar y P para pesos: ")
vdolar=float(input("ingresa el valor actual del dolar: "))
monto=float(input("Ingresa la cantidad: "))
if moneda=="D":
    print("Te damos por tus  dólares ", monto * vdolar," pesos")
else:
    print("Te damos por tus  pesos ", monto / vdolar," dólares")



# Definimos los tipos de cambio
peso_a_dolar = 0.00217391
dolar_a_peso = 460

# Pedimos al usuario que seleccione el tipo de conversión
tipo_conversion = input("¿Qué tipo de conversión deseas hacer?\n1. De pesos a dólares\n2. De dólares a pesos\n")

# Verificamos la selección del usuario y pedimos el monto a convertir
if tipo_conversion == "1":
    monto = float(input("Ingresa el monto en pesos: "))
    resultado = monto * peso_a_dolar
    print("El monto de", monto, "pesos equivale a", resultado, "dólares.")
elif tipo_conversion == "2":
    monto = float(input("Ingresa el monto en dólares: "))
    resultado = monto * dolar_a_peso
    print("El monto de", monto, "dólares equivale a", resultado, "pesos.")
else:
    print("Selección inválida. Debe ingresar 1 o 2 para seleccionar el tipo de conversión.")


print("----------------------------")
print("6. Realice un programa donde el usuario ingrese su edad. Si es mayor de")
print("16 años, muestre un mensaje diciendo “puede votar”, sino “no vota”.")

edad=int(input("ingresa tu edad: "))
if edad <=16:
    print("no puedes votar")
else:
    print("puedes votar")