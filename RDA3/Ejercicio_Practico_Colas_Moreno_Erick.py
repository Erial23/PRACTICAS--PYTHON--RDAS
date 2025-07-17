# Clase que implementa una cola de prioridad para un hospital
class ColaPrioridadHospital:
    def __init__(self):
        self.items = []
        # Diccionario que relaciona prioridad con descripcion
        self.descripciones_prioridad = {
            1: "Critico (muy urgente)",
            2: "Urgente",
            3: "Moderado",
            4: "Leve"
        }

    # Metodo para encolar pacientes (opcional, no se usa en esta version pero se puede probar)
    def encolar(self, paciente, prioridad):
        self.items.append((prioridad, paciente))

    # Verifica si la cola esta vacia
    def esta_vacia(self):
        return len(self.items) == 0

    # Devuelve el tamano de la cola
    def tamaño(self):
        return len(self.items)

    # Muestra los pacientes sin ordenar
    def mostrar_pendientes(self):
        if self.esta_vacia():
            print("No hay pacientes pendientes")
        else:
            print("Pacientes pendientes (orden de ingreso):")
            for prioridad, paciente in self.items:
                print(f"  - {paciente} (Prioridad {prioridad}: {self.descripciones_prioridad[prioridad]})")

    # Muestra los pacientes ordenados por prioridad
    def mostrar_por_prioridad(self):
        if self.esta_vacia():
            print("No hay pacientes en la cola")
        else:
            print("Pacientes ordenados por prioridad:")
            for prioridad, paciente in sorted(self.items, key=lambda x: x[0]):
                print(f"  - {paciente} (Prioridad {prioridad}: {self.descripciones_prioridad[prioridad]})")


# Funcion para mostrar el menu
def mostrar_menu():
    print("\n------ Hospital ------")
    print("1. Mostrar pacientes pendientes")
    print("2. Mostrar cola por prioridad")
    print("3. Mostrar cantidad de pacientes")
    print("4. Salir")

# Funcion principal
def menu():
    #Creamos la cola con prioridad
    hospital = ColaPrioridadHospital()

    #Encolamos algunos clientes
    hospital.encolar("Juan", 1)
    hospital.encolar("Pedro", 2)
    hospital.encolar("Ana", 3)
    hospital.encolar("Pepe", 4)
    hospital.encolar("Jose", 2)
    hospital.encolar("Lana", 3)
    hospital.encolar("Anabel", 4)
    hospital.encolar("Erick", 1)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            hospital.mostrar_pendientes()
            
        elif opcion == "2":
            hospital.mostrar_por_prioridad()
        elif opcion == "3":
            print(f"Total de pacientes en espera: {hospital.tamaño()}")
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion invalida. Intente de nuevo.")

# Ejecutamos el sistema de hospital
menu()

        
    
    