from funciones import registrar_paciente, buscar_paciente, mostrar_datos_completos,registrar_cita, most_all


def menu():
    while True:
        print("\n--------------- SISTEMA DE GESTIÓN DE CONSULTAS MÉDICAS ---------------")
        print("1. Registrar paciente")
        print("2. Buscar paciente")
        print("3. Agendar cita")
        print("4. Mostrar datos completos")
        print("5. Mostrar todos los pacientes")
        print("6. Salir del programa")

        opcion = input("Ingrese la opción que desea realizar: ")

        if opcion == '1':
            registrar_paciente()
            
        elif opcion == '2':
            try:
                cedula = int(input("Ingrese la cédula del paciente a buscar: "))
                paciente = buscar_paciente(cedula)
                if paciente:
                    paciente.mostrar_datos()
                else:
                    print("Paciente no encontrado.")
            except ValueError:
                print("Cédula inválida.")
        elif opcion == "3":
            registrar_cita()
        elif opcion == '4':
            mostrar_datos_completos()
        elif opcion == '5':
            most_all()
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu()
