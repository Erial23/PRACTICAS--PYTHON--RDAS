class Paciente:
    def __init__(self, nombre, cedula, edad, sangre, fecha):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.sangre = sangre
        self.fecha = fecha
        
    def mostrar_datos(self):
        print(f"\nNombre: {self.nombre}")
        print(f"Cédula: {self.cedula}")
        print(f"Edad: {self.edad}")
        print(f"Sangre: {self.sangre}")
        print(f"Fecha de registro: {self.fecha}")
        print("---------------")
