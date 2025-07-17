from libro import Libro

num_isbn=[]
prestamos=[]

def registrar_libro():
    try:
        titulo = input("Ingrese el nombre del libro: ")
        autor = input("Ingrese el nombre del autor: ")
        ISBN = int(input("Ingrese la identificacion del libro: "))
        fecha = input("Ingrese la fecha de registro (dd/mm/aaaa): ")
        lib = Libro(titulo , autor, ISBN, fecha)
        num_isbn.append(lib)
        print("Libro registrado exitosamente")
    except ValueError:
        print("Ingrese valores validos")

def buscar_libro(ISBN):
        for ne in num_isbn:
            if ne.ISBN == ISBN:
                return ne
        return None 


def mostar_libros():
    try:
        ISBN= int(input("Ingrese la identificacion del libro: "))
        lib = buscar_libro(ISBN)
        if lib:
            print(f"Titulo: {lib.titulo}, Autor: {lib.autor}, Identificacion del libro: {lib.ISBN}")
            print("Libro encontrado.")
        else:
            print("Libro no encontrado.")
    except ValueError:
        print("Error: Ingrese una identificacion valida.")



def registrar_prestamos():
    try:
        ISBN=int(input("Ingrese la identificacion del libro: "))
        lib= buscar_libro(ISBN)
        if lib:
            fecha= input("Ingrese la fecha de registro (dd/mm/aaaa): ")
            prestamos.append(prestamos)
            print("Prestamo de libro registrado")
        else:
            print("Libro inexistente")
    except ValueError:
        print("Ingrese una identificacion correcta. ")
def most_all():
    if not num_isbn:
        print("No hay libros registrados. ")
    else :
        for ne in num_isbn:
            ne.mostrar_datos()


