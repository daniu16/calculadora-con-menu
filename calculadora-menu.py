# calculadora con menú

from math import log
from operator import truediv
from tkinter import Y 

print("--------------------------------------")
print("----------calculadora-menu------------")
print("--------------------------------------")

# input
bandera= False
x = float(input("dame el valor del numero x: "))
y = float(input("dame el valor del numero y: "))

print("dame la opcion que deseas realizar: \n")
# se despliega el menú para seleccionar la opcion que deseas realizar:
print("1. sumar (el primero mas el segundo)")
print("2. restar (el primero menos el segundo)")
print("3. multiplicar (el primero por el segundo)")
print("4. dividir (el primero sobre el segundo)")
print("5. potencia(el primero a la potencia del segundo)")
print("6. logaritmo (el logaritmo del primero)")

opcion=int(input("\nDame la opcion: "))

#processing
if(opcion) == 1:
    z=x + y
    print(x,"+",y)
elif (opcion == 2):
    z = x - y
    print(x ,"-", y)
elif (opcion == 3):
    z= x * y
    print(x,"*",y)
elif (opcion == 4):
    z= x/y 
    print(x,"/",y)
elif (opcion == 4 and y ==0):
    print("el denomindor es igual a cero y")
    print("NO se puede realizar la divicion")
elif(opcion == 5):
    z = pow (x,y)
    print(x,"^",y)
elif(opcion == 6 and x>0):
    z = log(x)
    print("logaritmo de", x)
elif (opcion == 6 and x <=0):
    print("el valorde c es <= a cero y")
    print("NO se puede calcular el logaritmo")
    bandera= True
else:
    print("opcion no valida")
#se escribe el resultado con otra condicion
if(opcion <7 and bandera == False):
    print("resultado=", z)

# fin 
