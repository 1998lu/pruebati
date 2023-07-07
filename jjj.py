#lista_num = [1,2,5,8]
#print(len(lista_num))
#print(7 in lista_num)
#lista_num.append(9)
#print(lista_num)
#https://github.com/pquispev/TI-Senati/blob/main/string_methods.py

def cant_vc(n):
    cantidad_vocales=0
    cantidad_consonantes=0
    n= n.lower()
    for letra in n:
        if letra=="a" or letra=="e" or letra== "i" or letra== "o" or letra== "u":
            cantidad_vocales+=1
        else:
            cantidad_consonantes+=1
    r = f"""nombre:{n.capitalize()}
            numero de vocales:{cantidad_vocales}
            numero de consonantes: {cantidad_consonantes}
            numero de letras: {len(n)}"""
    return r

lista_nombres=[]
while True:
    nombres=input("ingrese nombre o para terminar escribe x: ")
    if nombres == "x":
        break
    else:
        if nombres in lista_nombres:
            pass
        else:
            cnombre=nombres.capitalize()
            if nombres in lista_nombres:
                pass
            else:
                lista_nombres.append(cnombre)


lista_nombres.sort()
print(lista_nombres)
print(len(lista_nombres))
print(f"la cantidad de nombres son {len(lista_nombres)}")

for i in lista_nombres:
    print(f"{i} el numero de letras {len(i)} ")
    print(cant_vc(i))
