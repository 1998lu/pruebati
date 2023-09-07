import math

a=int(input("ingrese el primer datp: "))
b=int(input("ingrese el segundo dato: "))
c= int(input("ingrese el tercer dato: "))

J=(b**2)+4*a*c
X= (-b+math.sqrt(J))/2*a
X1= (-b-math.sqrt(J))/2*a

print(J)
print("la ecuacion de segundo grado es:",X)
print("la ecuacion de segundo grado es:",X1)