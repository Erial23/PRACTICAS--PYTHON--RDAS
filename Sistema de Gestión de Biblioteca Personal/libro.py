class Libro:
    def __init__(self,titulo,autor,ISBN,fecha):
        self.titulo= titulo
        self.autor= autor
        self.ISBN= ISBN
        self.fecha = fecha

    def mostrar_datos(self):
        print(f"\nTitulo: {self.titulo}")
        print(f"\nAutor: {self.autor}")
        print(f"\nNumero ISBN: {self.ISBN}")
        print(f"Fecha de registro: {self.fecha}")
        print("-----------------------------------")

        