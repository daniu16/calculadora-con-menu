# calculadora con menú

from math import log 

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

opcion=int(input("\nDame la opcion"))
