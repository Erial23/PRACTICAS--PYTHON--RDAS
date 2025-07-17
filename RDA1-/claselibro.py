"""Crea una clase que tenga los atributos: titulo, autor, anio. Agrega un método que imprima un mensaje con los datos del libro.

"""

class libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año
    def description(self):
        return f"El libro {self.titulo} fue escrito por {self.autor} en el año {self.año}."
libro1= libro("El señor de los anillos", "J.R.R. Tolkien", 1995)
libro2= libro("La Sombra del Viento", "Carlos Ruiz Zafón", 2001)

print(libro1.description())
print(libro2.description())