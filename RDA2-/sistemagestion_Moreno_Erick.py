"""
Explicación conceptual (teórica)

1. ¿Qué es la búsqueda lineal? ¿Cómo funciona?
La búsqueda lineal es un algoritmo sencillo que se utiliza para localizar un elemento dentro de una lista.
Consiste en recorrer la lista desde el primer elemento hasta el último, comparando cada uno con el valor objetivo. 
Si encuentra una coincidencia, retorna la posición donde se encuentra. Si no lo encuentra tras revisar todos los elementos, 
indica que no está en la lista. No necesita que los elementos estén ordenados, por lo que puede aplicarse en cualquier colección de datos.
Su implementación es simple, pero su eficiencia disminuye cuando la lista es muy grande, ya que en el peor de los casos debe revisar todos 
los elementos. Tiene una complejidad temporal de O(n), lo que significa que el tiempo de ejecución crece linealmente con el tamaño de la lista.
Es útil cuando el conjunto de datos es pequeño o está desordenado, y cuando solo se requiere realizar pocas búsquedas.


2. ¿Qué es la búsqueda binaria? ¿Qué condición especial debe cumplir la lista?
La búsqueda binaria es un algoritmo eficiente diseñado para buscar elementos dentro de listas ordenadas. Su funcionamiento se basa en dividir 
la lista en mitades de forma sucesiva. Comienza comparando el valor buscado con el elemento central. Si es igual, devuelve la posición. Si el
valor buscado es menor, repite el proceso en la mitad izquierda; si es mayor, en la mitad derecha. Esta división sucesiva reduce rápidamente 
el tamaño del problema, lo que lo hace mucho más rápido que la búsqueda lineal. Es fundamental que la lista esté ordenada de forma ascendente 
o descendente antes de aplicar este método; de lo contrario, los resultados no serán válidos. La búsqueda binaria tiene una complejidad temporal 
de O(log n), lo que significa que el número de comparaciones crece de forma logarítmica en función del tamaño de la lista. Esto la convierte en 
una excelente opción cuando se necesita realizar muchas búsquedas en listas grandes y ordenadas.

3. ¿En qué casos conviene usar cada una?
La elección entre búsqueda lineal y binaria depende del contexto. La búsqueda lineal es adecuada cuando se trabaja con listas pequeñas, datos no 
ordenados o cuando se planea hacer una sola búsqueda ocasional. Su simplicidad de implementación la hace práctica en situaciones rápidas o prototipos.
Por otro lado, si se cuenta con una lista ordenada y se van a realizar múltiples búsquedas, la búsqueda binaria es preferible, ya que reduce 
significativamente el tiempo de ejecución. Aunque su implementación es ligeramente más compleja, la eficiencia que ofrece la hace ideal para sistemas
con muchos datos, como catálogos o bases de datos. También puede combinarse con algoritmos de ordenamiento para usar binaria después de ordenar la lista. 
En resumen: usa búsqueda lineal en estructuras pequeñas y no ordenadas; usa binaria en listas ordenadas y grandes donde el rendimiento es prioritario.


"""

print("------------------------------------------------------------------------------")
print("Realizado por Erick Moreno")
print("Fecha: 2023-03-15")
print("------------------------------------------------------------------------------")

print("----------Sistema de gestion de productos----------")
# Lista de productos (desordenada)
productos = [
    "Laptop", "Mouse", "Teclado", "Monitor", "Impresora",
    "Tablet", "Smartphone", "Auriculares", "Webcam", "Router",
    "Camara", "Proyector", "Disco Duro", "Memoria USB", "MicroSD",
    "Altavoces", "Smartwatch", "Cargador", "Bateria", "Cable HDMI"
]

# Historial para guardar resultados de cada busqueda
historial = []

# Funcion de busqueda lineal
def busqueda_lineal(lista, objetivo):
    comparaciones = 0
    for i in range(len(lista)):
        producto = lista[i]
        comparaciones += 1  # Contar cada comparacion realizada
        if producto.lower() == objetivo.lower():  # Comparar ignorando mayusculas/minusculas
            return i, comparaciones  # Retorna posicion y cantidad de comparaciones
    return -1, comparaciones  # Retorna -1 si no encuentra el producto

# Funcion de busqueda binaria
def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1
    comparaciones = 0
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2  # Indice central del rango actual
        comparaciones += 1
        if lista[medio].lower() == objetivo.lower():
            return medio, comparaciones  # Producto encontrado
        elif lista[medio].lower() < objetivo.lower():
            izquierda = medio + 1  # Buscar en la mitad derecha
        else:
            derecha = medio - 1  # Buscar en la mitad izquierda
    return -1, comparaciones  # Producto no encontrado

# Funcion para ordenar la lista usando bubble sort (ordena sin modificar la lista original)
def ordenar_lista(lista):
    lista_ordenada = lista[:]  # Copiamos para no modificar la lista original
    n = len(lista_ordenada)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_ordenada[j].lower() > lista_ordenada[j + 1].lower():
                # Intercambiar elementos si estan en orden incorrecto
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]
    return lista_ordenada

# Bucle principal para pedir productos al usuario hasta que decida salir
while True:
    entrada = input("\nIngrese el nombre del producto a buscar (Enter para salir): ").strip() # Elimina los espacios en blanco
    if entrada == "":  # Si usuario no escribe nada, salir del bucle
        break

    # Ejecutar busqueda lineal en la lista original
    pos_lineal, comp_lineal = busqueda_lineal(productos, entrada)
    print("\n[ Busqueda Lineal ]")
    if pos_lineal != -1:
        print(f"Producto encontrado en la posicion {pos_lineal} (comparaciones: {comp_lineal})")
    else:
        print(f"Producto NO encontrado (comparaciones: {comp_lineal})")

    # Ordenar lista manualmente antes de busqueda binaria
    productos_ordenados = ordenar_lista(productos)

    # Ejecutar busqueda binaria en la lista ordenada
    pos_binaria, comp_binaria = busqueda_binaria(productos_ordenados, entrada)
    print("\n[ Busqueda Binaria ]")
    if pos_binaria != -1:
        print(f"Producto encontrado en la posicion {pos_binaria} (lista ordenada) (comparaciones: {comp_binaria})")
    else:
        print(f"Producto NO encontrado (comparaciones: {comp_binaria})")

    # Guardar los resultados de esta busqueda en el historial
    historial.append({
        "producto": entrada,
        "lineal_pos": pos_lineal,
        "lineal_comp": comp_lineal,
        "binaria_pos": pos_binaria,
        "binaria_comp": comp_binaria
    })

print("\n=== RESUMEN DE BUSQUEDAS ===")
for i in range(len(historial)):
    resultado = historial[i]
    print(f"\nBusqueda {i + 1}: '{resultado['producto']}'")
    print(f" - Lineal: Posicion {resultado['lineal_pos']} / Comparaciones: {resultado['lineal_comp']}")
    print(f" - Binaria: Posicion {resultado['binaria_pos']} / Comparaciones: {resultado['binaria_comp']}")


