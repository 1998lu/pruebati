producto = {"nombre": "", "marca": "", "costo": 0, "cantidad": 0,}
#lista = [1,2,3,"uno"]
#print(auto.keys())
#print(auto.get("modelo"))
#print(auto.items())
#for llave, valor in  auto.items():
    #print(llave, valor)
#auto["estado"] = False
#lista_colores = auto. get("colores")
#lista_colores.append("azul")
#print(lista_colores)
#auto["colores"]=lista_colores
#print(auto)
#print(auto.get("colores"))

#auto["transmision"] = "automatico"
#print(auto)
lista_productos=[]
bandera=True
while bandera:
    try:
        producto_nombre =input("ingrese el nombre del producto: ")
        producto_marca=input("ingrese la marca del producto: ")
        producto_costo=int(input("ingrese el costo del producto: "))
        producto_cantidad=int(input("ingrese la cantidad del producto: "))
        #print("desea agregar mas productos? si/no")
    except ValueError:
        print("algo salio mal intentalo otra vez")
    else:
        producto["nombre"]=producto_nombre
        producto["marca"]=producto_marca
        producto["costo"]=producto_costo
        producto["cantidad"]=producto_cantidad
        lista_productos.append(producto)
        producto= {}
        pregunta=input("desea a gregar mas productos? si/no")
        if str(pregunta) != "si":
            bandera: False

        print(lista_productos)
print(""" 
      supermercado elija la opcion 
listar los producto
agregar mas producto_costo
hacer la venta. 
      """)

opcion = input("elija la opcion del menu: ")
