# 1)      Escribir un programa que permita validar el ingreso a un sistema. Se deberá solicitar el ingreso por teclado de nombre de usuario y contraseña. Será valido como nombre de usuario “admin” y como contraseña “1234”. Si el ingreso es correcto deberá mostrar por pantalla el mensaje “Ingreso exitoso”.
# Opcional 1: permitir como usuario valido también su propio nombre y su propia contraseña.
# Opcional 2: solamente permitir el ingreso incorrecto de los datos 3 veces, luego de ello, no permitir más ingresos y mostrar por pantalla “Cuenta bloqueada”.

# 2)  	Mostrar por pantalla el siguiente menú:
# CAJERO AUTOMATICO
# ISPC
# Listado de opciones:
# 1)  	Ingreso de dinero
# 2)  	Extracción de dinero
# 3)  	Consulta de salto
# 4)  	Salir
# Ingrese su selección: _
# El programa deberá mostrar luego del ingreso de cada opción “Usted ha seleccionado la opción x”, por ejemplo, en el caso de ingresar un 1, deberá mostrar por pantalla “Usted ha seleccionado la opción 1” y así sucesivamente. Al seleccionar la opción 4 se debe terminar la ejecución del programa.
# 3)  	Deberá continuar con el ejercicio 2 y escribir la lógica del cajero automático de la siguiente manera.
# a.   	Su saldo inicial será de $10000.
# b.   	Al seleccionar la opción 1 se pedirá al usuario que ingrese un importe por teclado el cual se sumará a su saldo inicial.
# c.   	De la misma manera al seleccionar la opción 2, se solicitará un importe por teclado el cual se restará al saldo inicial.
# d.   	Con la opción 3 se consultará su saldo actual.
# e.   	En todo momento se deberá contralar que no se pueda extraer dinero, si no se cuentan con fondos suficientes.
# 4)  	Deberá en un solo programa unir el logueo del sistema con los ejercicios 2 y 3. Esto quiere decir que, si el ingreso al sistema es exitoso, se mostrará el menú del cajero automático y el usuario podrá comenzar a operar.
# Opcional 3: Puede incluir parte de la lógica del programa en una o más funciones.

import os
import sys
import time
os.system('cls')

user = "admin"
password = "1234"

while True:
     
    print("**********************************************")
    print("***********Bienvenido al cajero **************")
    print("**********************************************")
    print("")

    contador = 0

    while contador < 3:
        
 
        usuario = input("Ingresa tu usuario: ")
        contrasena = input("Ingresa tu contraseña: ")
        contador += 1
        if user == usuario and password == contrasena:
            break
        else:
            if usuario=="admin" and user==None:
                os.system('cls')
                print("su usuario está bloqueado!!! contacte al administrador!!!")
                time.sleep(1.5)
                os.system('cls')
                break
            else: 
                
                if contador < 3:
                    os.system('cls')
                    print("Datos incorrectos, ingréselos nuevamente")
                    time.sleep(1.5)
                    os.system('cls')
                    print("**********************************************")
                    print("***********Bienvenido al cajero **************")
                    print("**********************************************")
                else:
                    user = None
                    password = None
                    os.system('cls')
                    print("Su usuario ha sido bloqueado, contacte a su administrador de confianza")
                    time.sleep(1.5)
                    os.system('cls')
                    continue
   
    if user == usuario and password == contrasena:
        break

os.system('cls')
print("*************************************")
print("Bienvenido al sistema elija su opcion")
print("1)  	Ingreso de dinero")
print("2)  	Extracción de dinero")
print("3)  	Consulta de salto")
print("4)  	Salir")
opcion = int(input("Ingrese su elección (1-4): "))
if opcion >= 1 and opcion <= 4:
    print("Usted ha seleccionado la opción ", opcion)
else:
    print("Error: debe ingresar un número entre 1 y 4")
