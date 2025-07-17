print("///////////////////////////////////////////////////////////////////////")
print("///////////////////////////////////////////////////////////////////////")
print("Realizado por Erick Moreno")
print("Programacion ll")
print("///////////////////////////////////////////////////////////////////////")
print("///////////////////////////////////////////////////////////////////////")  
"""# Parte 3: Preguntas de reflexión

# ¿Por qué es necesario ordenar antes de realizar la búsqueda binaria?
 Porque la búsqueda binaria funciona dividiendo el conjunto en mitades
y comparando el valor central con el valor buscado. Si los datos no están
 ordenados, no se puede saber en qué mitad buscar, lo que haría que el algoritmo no funcione correctamente.

# ¿Qué pasaría si usamos búsqueda binaria sin ordenar primero?
 El algoritmo podría devolver un resultado incorrecto o no encontrar el valor
aunque sí esté presente, ya que las decisiones que toma se basan en un supuesto orden.

# ¿Qué ventajas viste entre la búsqueda binaria y la búsqueda lineal?
La búsqueda binaria es mucho más eficiente cuando los datos están ordenados,
ya que reduce el número de comparaciones a medida que descarta la mitad del conjunto en cada paso (complejidad O(log n)).
En cambio, la búsqueda lineal revisa uno por uno hasta encontrar el valor (complejidad O(n)).

# ¿Cuál de los dos ordenamientos te pareció más intuitivo de implementar y por qué?
El ordenamiento por burbuja me pareció más intuitivo, ya que su lógica es sencilla:
comparar dos elementos vecinos y cambiarlos si están en el orden incorrecto.
Es fácil de seguir y programar, aunque no sea el más rápido para listas grandes."""

# Sistema Inteligente de Gestión de Clientes (Versión básica)

# Lista de clientes (nombre, saldo)
clientes = [
    ("Carlos", 100.0),
    ("Ana", 50.5),
    ("Luis", 75.0),
    ("Marta", 200.0),
    ("Pedro", 60.0),
    ("Lucía", 40.0),
    ("David", 120.0),
    ("Elena", 90.0),
    ("Raúl", 30.0),
    ("Sofía", 150.0)
]

# Insertion Sort para ordenar por nombre
def insertion_sort_nombre(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and actual[0] < lista[j][0]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual

# Selection Sort para ordenar por saldo
def selection_sort_saldo(lista):
    for i in range(len(lista)):
        min_index = i
        for j in range(i + 1, len(lista)):
            if lista[j][1] < lista[min_index][1]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]

# Búsqueda binaria por nombre
def busqueda_binaria(lista, nombre):
    izquierda = 0
    derecha = len(lista) - 1
    comparaciones = 0

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        comparaciones += 1
        if lista[medio][0] == nombre:
            return medio, comparaciones
        elif lista[medio][0] < nombre:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1, comparaciones

# Búsqueda lineal
def busqueda_lineal(lista, nombre):
    comparaciones = 0
    for i, cliente in enumerate(lista):
        comparaciones += 1
        if cliente[0] == nombre:
            return i, comparaciones
    return -1, comparaciones

# Permitir agregar un nuevo cliente
def agregar_cliente(lista):
    nombre = input("Ingrese el nombre del nuevo cliente: ")
    saldo = float(input("Ingrese el saldo del cliente: "))
    lista.append((nombre, saldo))

# Menú principal
def menu():
    while True:
        print("\nMenú:")
        print("1. Ordenar por nombre (Insertion Sort)")
        print("2. Ordenar por saldo (Selection Sort)")
        print("3. Buscar cliente por nombre (Búsqueda binaria)")
        print("4. Agregar nuevo cliente")
        print("5. Buscar cliente sin ordenar (Búsqueda lineal)")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            insertion_sort_nombre(clientes)
            print("Clientes ordenados por nombre:")
            for c in clientes:
                print(c)

        elif opcion == "2":
            selection_sort_saldo(clientes)
            print("Clientes ordenados por saldo:")
            for c in clientes:
                print(c)

        elif opcion == "3":
            insertion_sort_nombre(clientes)
            nombre = input("Ingrese el nombre del cliente a buscar: ")
            pos, comp = busqueda_binaria(clientes, nombre)
            if pos != -1:
                print(f"Cliente encontrado en la posición {pos}: {clientes[pos]}")
            else:
                print("Cliente no encontrado.")
            print(f"Comparaciones realizadas: {comp}")

        elif opcion == "4":
            agregar_cliente(clientes)
            print("Cliente agregado.")

        elif opcion == "5":
            nombre = input("Ingrese el nombre del cliente a buscar: ")
            pos, comp = busqueda_lineal(clientes, nombre)
            if pos != -1:
                print(f"Cliente encontrado en la posición {pos}: {clientes[pos]}")
            else:
                print("Cliente no encontrado.")
            print(f"Comparaciones realizadas: {comp}")

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
