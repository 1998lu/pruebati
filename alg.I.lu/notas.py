a=int(input("ingrese la primera nota: "))
b=int(input("ingrese la segunda nota: "))
c= int(input("ingrese la tercer nota: "))
d= int(input("ingrese la cuaryta nota: "))

promedio = (a+b+c+d)/4
redondeado = round(promedio)

print(redondeado)

if redondeado>=11:
    print("aprobado")
else: 
    print("desaprobado")