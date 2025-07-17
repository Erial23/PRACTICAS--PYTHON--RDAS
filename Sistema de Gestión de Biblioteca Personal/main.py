from funciones import registrar_libro,buscar_libro, registrar_prestamos, mostar_libros, most_all

def menu():
    while True:
        print("\n--------------- Sistema de Gestión de Biblioteca Personal ---------------")
        print("1. Registrar libro")
        print("2. Registrar prestamo de libro")
        print("3. Mostrar libros")
        print("4. Buscar Libro")
        print("5. Mostrar todos los libros")
        print("6. Salir del programa")

        opcion= input("Ingrese la opcion que desea realizar: ")

        if opcion=="1":
            registrar_libro()

        elif opcion== "2":
            registrar_prestamos()
        elif opcion== "3":
            mostar_libros()
        elif opcion == "4":
            try:
                ISBN= int(input("Ingrese el numero de identificacion del libro a buscar: "))
                libro= buscar_libro(ISBN)
                if libro:
                    libro.mostrar_datos()
                else:
                    print("Libro no encontrado")
            except ValueError:
                print("Identificacion ISBN incorrecta")
        elif opcion== "5":
            most_all()
        elif opcion=="6":
            print("Saliendo del programa.....")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
            
if __name__=="__main__":
    menu()
