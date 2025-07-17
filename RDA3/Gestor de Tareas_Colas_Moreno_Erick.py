# Cola de prioridad sin librerias
class ColaPrioridadTareas:
    def __init__(self):
        self.cola = []  # lista de tareas 
        self.contador = 0  # orden de llegada

    def agregar_tarea(self, tarea, prioridad):
        self.cola.append((prioridad, self.contador, tarea))
        self.contador += 1
        self.cola.sort(key=lambda x: (x[0], x[1]))  # ordeno por prioridad y llegada

    def terminar_tarea(self):
        if self.cola:
            return self.cola.pop(0)[2]  # saco la tarea mas urgente
        return None

    def ver_proxima_tarea(self):
        if self.cola:
            return self.cola[0][2]  # veo tarea mas urgente
        return None

    def tamaño(self):
        return len(self.cola)

    def ver_todas_tareas(self):
        return [t[2] for t in self.cola]  # solo tareas


def mostrar_menu():
    print("\n------ Tareas Empleado (Cola Prioridad) ------")
    print("1. Agregar tarea")
    print("2. Terminar tarea")
    print("3. Ver proxima tarea")
    print("4. Ver todas las tareas")
    print("5. Salir")

def menu():
    cola = ColaPrioridadTareas()

    # tareas iniciales
    cola.agregar_tarea("Preparar informe semanal", 3)
    cola.agregar_tarea("Responder correos urgentes", 1)
    cola.agregar_tarea("Revisar reporte de ventas", 2)
    cola.agregar_tarea("Actualizar base de datos de clientes", 4)
    cola.agregar_tarea("Llamar a proveedor", 2)
    cola.agregar_tarea("Programar reunion de equipo", 3)
    cola.agregar_tarea("Supervisar entrega de pedidos", 3)
    cola.agregar_tarea("Redactar propuesta comercial", 4)
    cola.agregar_tarea("Capacitacion interna", 2)
    cola.agregar_tarea("Analizar feedback de clientes", 1)

    while True:
        mostrar_menu()
        opcion = input("Ingrese opcion: ")
        if opcion == "1":
            tarea = input("Ingrese tarea: ")
            try:
                prioridad = int(input("Prioridad (1 mas urgente - 4 menos): "))
                if prioridad < 1 or prioridad > 4:
                    print("Prioridad invalida")
                    continue
            except:
                print("Valor no valido")
                continue
            cola.agregar_tarea(tarea, prioridad)
            print(f"Tarea '{tarea}' agregada")
        elif opcion == "2":
            if cola.tamaño() > 0:
                tarea_terminada = cola.terminar_tarea()
                print(f"Tarea '{tarea_terminada}' eliminada")
            else:
                print("No hay tareas")
        elif opcion == "3":
            proxima = cola.ver_proxima_tarea()
            if proxima:
                print(f"Proxima tarea: {proxima}")
            else:
                print("No hay tareas")
        elif opcion == "4":
            if cola.tamaño() > 0:
                print("Tareas (ordenadas):")
                for t in cola.ver_todas_tareas():
                    print(f"- {t}")
            else:
                print("No hay tareas")
        elif opcion == "5":
            print("Adios")
            break
        else:
            print("Opcion invalida")

menu()
