meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
 
salir = False
cont=1 

print("\n") 
print("**Para salir del programa ingrese el numero cero**") 
while(not salir):
    
    numero = int(input("Ingrese un numero entre el 1 y el 12 \n"))
   
    if(numero==0):
        salir= True
    else:
        if(numero>=1 and numero<=len(meses)):
            print("El mes es: ", meses[numero-1])
            print("\n")
        else:
            print("\n")
            print("Ingrese solo numeros entre el 1 y el ",len(meses))
            print("\n")