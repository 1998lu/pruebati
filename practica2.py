# pruebati
texto= "hola mundo python este es mi primer escrito"
cont_a = 0

for i in texto: 
    if (i=="a" or i=="e"):
        if(i=="a"):
            cont_a +=1
        if(i=="e"): 
            cont_e +=1 
        print ("es una vocal")
    elif(i==" "):
        print("es un espacio")
    else:
        print("es una consonante")
        print(f'la cantidad de la vocal a es[cont_a]')
      
