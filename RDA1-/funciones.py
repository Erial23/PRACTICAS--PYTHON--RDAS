"""
# print("**Estructura de una función**")
def erick (): #arrión
    print("Hola Erick como estas") #bLoque de código que se ejecutara cuando se invoque la función
erick () #ensocactor de La función
print ("\n")

# print("**Parámetros y argumentos de una función**")
def funcion (nombre):
    print ("Estamos estudiando Python", nombre)
funcion ("Edison")
print ("\n")

# print("**Parámetros y argumentos de una función**")
def funcion (nombre):
    print( "Estamos estudiando Python", nombre)
funcion ("Edison")
print ("\n")

#Los argumentos a puedos pagar de dos formas:
# Argumentos posicionales.se esocian a los parámetros de la función en el mismo orden que asurecen en la definición de la función.
# Argumentos nominares: Se indico explicitamente el nombre del parámetro el que se asocia un argumento de la forma parametro = argumento.
print("Paso de argumentosja una función")
def datos (nombre, apellido):
    print("Estanos estudiando Python", nombre, apellido)
datos ("Edison", "Meneses")# Argumentos posicionales
datos (nombre="Edison",apellido="Meneses")# Argumentos nominales
print ("\n")

#area triangulo
def area_triangulo(base, altura):
    area = (base * altura) / 2
    print(area)
area_triangulo(2,3)
area_triangulo(4,5)
print("\n")

#
print("argumentos por defecto")
def welcome (nombre, lenguaje= "Python"):
    print("Bienvenido a", lenguaje, nombre)
welcome ("Erick")
welcome("Erick", "Java")


#
print("pasar de un numero indeterminado de argumentos")
def menu (*platos):
    print("Menu del dia: ", end="")
    for plato in platos:
        print(plato, end=", ")
menu("pasta", "pizza", "ensalada")
print("\n")


def contacto(**info):
    print("Datos del contacto")
    for clave, valor in info.items():
        print(clave,":", valor)
contacto(nombre="Erick", telefono= 123456, correo="erick@gmail.com")
print("\n")
contacto(nombre = "Erick", email= "erick@gmail.com", direccion= "Pelileo-Ecuador")
print("\n")






for i  in range (0,5+1):
    print ("Tabla del ", i)
    for j in range (0,5+1):
        for k in range(0,5+1):
            print(i, "*", j, "*", k, "=", i*j*k)


for t in [1,2,3] :
    print("La tabla del ", t)
    for p in [1,2,3]:
        print(t, "*", p, "=", t*p)
        
        
for t in [10,20,30] :
    print("La tabla del ", t)
    for p in [9,5,1]:
        print(t, "*", p, "=", t*p)


for q in [1,2,3,4,5,6,7,8,9,10]:
    if q%2==0:
        print(q, "es par")
   
for q in [1,2,3,4,5,6,7,8,9,10]:
    if q%2==1:
        print(q, "es impar")
        
        
print("Las funciones son objetos")


#def saludo(nombre este es un parametro)
#argumento


#Funciones recursivas: es cuendo puedo invocar la funcion dentro de la misma funcion
print("funciones recuersivas")
def cuentaregresiva(numero):
    numero -=1
    if numero >0:
        print(numero)
        cuentaregresiva(numero)
    else:
        print("Boooommmmmm")
    print("Fin de la funcion", numero)
cuentaregresiva(5)
print("\n")



def erick():
    return("Hola Erick como estas")
print(erick())
print("\n")


class persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
    def description(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Sexo: {self.sexo}"
    
persona1= persona("Juan", 30 , "Ingeniero")
persona2= persona("Maria", 25, "Ingeniera")

print(persona1.description())
print(persona2.description())
print("\n")


class persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
    def description(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Sexo: {self.sexo}"
nombre= input("Ingresa tu nombre: ")
edad= int(input("Ingresa tu edad: "))
sexo= input("Ingresa tu sexo: ")

nuevapersona=persona(nombre,edad, sexo)
print(nuevapersona.description())
print("\n")
"""

class persona:
    def __init__(self, nombre, edad, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion
    def description(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Ocupacion: {self.ocupacion}"
    
    
def mostrar_menu():
    print("*** Gestion de personas***")
    print("1. Agregar persona")
    print("2. Mostrar personas")
    print("3. Buscar persona por nombre ")
    print("4. Salir")
    
    
personas=[]

while True:
    mostrar_menu()
    
    opcion=input("Ingrese la opcion a realizar: ")
    
    if opcion=="1":
        nombre= input("Ingresa tu nombre: ")
        edad= int(input("Ingresa tu edad: "))
        ocupacion= input("Ingresa tu ocupacion: ")
        nueva_persona=persona(nombre, edad, ocupacion)
        personas.append(nueva_persona)
        print(f"La persona '{nombre}' ha sido agregada con exito. ")
    
    elif opcion=="2":
        if len(personas)>0:
            print("\n ---Lista de personas---")
            for persona in personas:
                print(persona.description())
        else:
            print("No hay personas registradas")
    elif opcion=="3":
        if len(personas)>0:
            nombre_buscar= input("Ingrese el nombre de la persona a buscar: ")
            encontrada=False
            for persona in personas:
                if persona.nombre.lower()==nombre_buscar.lower():
                    print("Persona encontrada")
                    print(persona.description())
                    encontrada=True
                    break
            if not encontrada:
                print("Persona no encontrada")
        else:
            print("No hay personas registradas")
    elif opcion=="4":
        print("Saliendo del programa")
        break
    else:
        print("Opcion invalida. Por favor, ingrese una opcion valida")
        
        
                