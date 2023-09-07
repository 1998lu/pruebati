
obrero = int(input("ingrese el numero de horas: "))

if obrero<=40:
    salario = obrero * 16 
else: 
    salario = (40*16) + ((obrero-40)*20)
print("el salario es:",salario)