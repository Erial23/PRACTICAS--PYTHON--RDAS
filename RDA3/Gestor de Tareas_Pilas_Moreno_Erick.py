# Simulacion de tareas de un empleado:
class PilaTareas:
    def __init__(self):
        self.items = []  # lista donde se guardan las tareas

    def agregar_tarea(self, tarea):
        self.items.append(tarea)  # agrega una tarea al final de la lista

    def terminar_tarea(self):   
        self.items.pop()  # elimina la ultima tarea agregada 

    def ver_utima_tarea(self):
        return self.items[-1]  # devuelve la ultima tarea agregada

    def tamaño(self):
        return len(self.items)  # devuelve la cantidad de tareas en la pila

    def ver_todas_tareas(self):
        return self.items  # devuelve la lista completa de tareas
    

def mostrar_menu():
    print("\n------ Tareas de Empleado ------")
    print("1. Agregar tarea")
    print("2. Terminar tarea")
    print("3. Ver ultima tarea")
    print("4. Ver todas las tareas ")
    print("5. Salir")

def menu():
    pila = PilaTareas()  # creo una instancia de la pila

    # agrego 10 tareas iniciales
    pila.agregar_tarea("Preparar informe semanal")
    pila.agregar_tarea("Responder correos urgentes")
    pila.agregar_tarea("Revisar reporte de ventas")
    pila.agregar_tarea("Actualizar base de datos de clientes")
    pila.agregar_tarea("Llamar a proveedor")
    pila.agregar_tarea("Programar reunion de equipo")
    pila.agregar_tarea("Supervisar entrega de pedidos")
    pila.agregar_tarea("Redactar propuesta comercial")
    pila.agregar_tarea("Capacitacion interna")
    pila.agregar_tarea("Analizar feedback de clientes")

    while True:
        mostrar_menu()
        opcion = input("Ingrese la opcion deseada: ")
        if opcion == "1":
            tarea = input("Ingrese la tarea a agregar: ")
            pila.agregar_tarea(tarea)  # agrego nueva tarea
            print(f"Tarea '{tarea}' agregada con exito")
        elif opcion == "2":
            if pila.tamaño() > 0:
                tarea_terminada = pila.ver_utima_tarea()  # guardo tarea a eliminar
                pila.terminar_tarea()                     # elimino la tarea
                print(f"Tarea '{tarea_terminada}' eliminada con exito")
            else:
                print("No hay tareas para terminar")

        elif opcion == "3":
            if pila.tamaño() > 0:
                print(f"La ultima tarea es: {pila.ver_utima_tarea()}")  # muestro ultima tarea
            else:
                print("No hay tareas")      
        elif opcion == "4":
            if pila.tamaño() > 0:
                print(f"Las tareas son: {pila.ver_todas_tareas()}")  # muestro todas las tareas
            else:
                print("No hay tareas")
        elif opcion == "5":
            print("Hasta luego")
            break
        else:
            print("Opcion invalida. Por favor, ingrese una opcion valida.")

menu()



