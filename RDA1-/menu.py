#Menu de opciones
#1.sumar
#2. restar
#3. multiplicar
#4. dividir
#5. seleccionar opciones
#6. Ingresar por teclado 2 numeros verifique el tipo de dato
#7. validar que el segundo numero no sea cero
#8. Realizar la operacion seleccionada
#9. Mostar el resultado
#10 Validar que la opcion seleccionada sea correcta
#11. Mostrar un mensaje de error si la opcion no es correcta

print("1. Sumar: ")
print("2. Restar: ")
print("3. Multiplicar: ")
print("4. Dividir: ")
opcines=int(input("Ingrese la operacion que desea realizar: "))
num1=float(input("INGRESE EL PRIMER NUMERO: "))
num2=float(input("INGRESE EL SEGUNDO NUMERO: "))  
if opcines> 4 or opcines < 1:
     
    print("INGRESE UNA OPCION CORRECTA")
    opcines=int(input("Ingrese la opcion que desea realizar: "))
if opcines==1:
    print(num1+num2)
elif opcines==2:
    print(num1-num2)
elif opcines==3:  
    print(num1*num2)
elif opcines==4:   
    if num2==0:
        print("NO SE PUEDE REALIZAR LA OPERACION")
        num2=float(input("INGRESE EL SEGUNDO NUMERO: "))
        print(num1/num2)
        
    

    
    

    


