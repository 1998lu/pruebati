a=int(input("ingrese el primer numero: "))
b=int(input("ingrese el segundo numero: "))
c=int(input("ingrese el tercer numero: "))

lista=[]

lista.append(a)
lista.append(b)
lista.append(c)

lista.sort(reverse=True)
print("lista ordenada", lista)
