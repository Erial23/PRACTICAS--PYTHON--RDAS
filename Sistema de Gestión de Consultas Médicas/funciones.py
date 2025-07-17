from paciente import Paciente

new_paciente = []
cita = []

def registrar_paciente():
    try:
        nombre = input("Ingrese el nombre del paciente: ")
        edad = int(input("Ingrese la edad del paciente: "))
        cedula = int(input("Ingrese su número de cédula: "))
        sangre = input("Ingrese su tipo de sangre: ")
        fecha = input("Ingrese la fecha de registro (dd/mm/aaaa): ")
        paci = Paciente(nombre, cedula, edad, sangre, fecha)
        new_paciente.append(paci)
        print("Paciente registrado exitosamente.")
    except ValueError:
        print("Error: Ingrese valores válidos (números para edad y cédula).")

def buscar_paciente(cedula):
    for ne in new_paciente:
        if ne.cedula == cedula:
            return ne
    return None

def mostrar_datos_completos():
    try:
        cedula = int(input("Ingrese la cédula del paciente: "))
        paci = buscar_paciente(cedula)
        if paci:
            print(f"Nombre: {paci.nombre}, Edad: {paci.edad}, Tipo de Sangre: {paci.sangre}")
            print(f"Fecha de registro: {paci.fecha}")
            print("Paciente encontrado.")
        else:
            print("Paciente no encontrado.")
    except ValueError:
        print("Error: Ingrese una cédula válida.")

def registrar_cita():
    try:
        cedula = int(input("Ingrese la cédula del paciente para agendar la cita: "))
        paci = buscar_paciente(cedula)
        if paci: 
            fecha = input("Ingrese la fecha de la cita (dd/mm/aaaa): ")
            cita.append(cita)
            print("Cita agendada con éxito.")
        else:
            print("Paciente no encontrado.")
    except ValueError:
        print("Error: Ingrese una cédula válida.")
    

def most_all():
    if not new_paciente:
        print("No hay pacientes registrados.")
    else:
        for ne in new_paciente:
            ne.mostrar_datos()
