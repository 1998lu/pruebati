a=int(input("ingrese el primer numero: "))
b=int(input("ingrese el segundo numero: "))
c=int(input("ingrese el tercer numero: "))

if (a>b and a>c):
    print("el numero mayor es: ",a)
elif (b>a and b>c):
    print("el numero mayor es: ",b)
elif (c>a and c>b):
    print("el numero es mayor: ",c)

if (a<b and a<c):
    print("el numero menor es: ",a)
elif (b<a and b<c):
    print("el numero menor es: ",b)
elif (c<a and c<b):
    print("el numero menor es: ",c)
