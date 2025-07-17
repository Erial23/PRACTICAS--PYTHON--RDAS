"""Crea una clase con atributos nombre, carrera, y nota_final. Agrega un método que diga si aprobó (nota ≥ 7).
"""
class Estudiante:
    def __init__(self, nombre, carrera, nota_final):
        self.nombre = nombre
        self.carrera = carrera
        self.nota_final = nota_final
    def description(self):
        return f"Nombre: {self.nombre}, Carrera: {self.carrera}, Nota Final : {self.nota_final}"
    def aprobó(self):
        if self.nota_final >= 7:
            return f"El estudiante {self.nombre} aprobó con una nota de {self.nota_final}"
        else:
            return f"El estudiante {self.nombre} no aprobó con una nota de {self.nota_final}"
        
estudiante1=Estudiante("Erick Moreno", "Ingeniería en Sistemas", 8)
estudiante2=Estudiante("Vicente Palacios", "Ingeniería en Sistemas", 6)

print(estudiante1.description())
print(estudiante1.aprobó())
print(estudiante2.description())
print(estudiante2.aprobó())