# Lista de productos (desordenada)
productos = [
    "Laptop", "Mouse", "Teclado", "Monitor", "Impresora",
    "Tablet", "Smartphone", "Auriculares", "Webcam", "Router",
    "Camara", "Proyector", "Disco Duro", "Memoria USB", "MicroSD",
    "Altavoces", "Smartwatch", "Cargador", "Bateria", "Cable HDMI"
]

# Historial de busquedas realizadas
historial = []

# Funcion de busqueda lineal
def busqueda_lineal(lista, objetivo):
    comparaciones = 0
    for i, producto in enumerate(lista):
        comparaciones += 1
        if producto.lower() == objetivo.lower():
            return i, comparaciones
    return -1, comparaciones

# Funcion de busqueda binaria (requiere lista ordenada)
def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1
    comparaciones = 0
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        comparaciones += 1
        if lista[medio].lower() == objetivo.lower():
            return medio, comparaciones
        elif lista[medio].lower() < objetivo.lower():
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1, comparaciones

# Funcion para ordenar la lista (usando bubble sort)
def ordenar_lista(lista):
    lista_ordenada = lista[:]  # copiamos la lista para no modificar la original
    n = len(lista_ordenada)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_ordenada[j].lower() > lista_ordenada[j + 1].lower():
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]
    return lista_ordenada

# Bucle principal
while True:
    entrada = input("\nIngrese el nombre del producto a buscar (Enter para salir): ").strip()
    if entrada == "":
        break

    # Ejecutar busqueda lineal
    pos_lineal, comp_lineal = busqueda_lineal(productos, entrada)
    print("\n[ Busqueda Lineal ]")
    if pos_lineal != -1:
        print(f"Producto encontrado en la posicion {pos_lineal} (comparaciones: {comp_lineal})")
    else:
        print(f"Producto NO encontrado (comparaciones: {comp_lineal})")

    # Ordenar la lista manualmente antes de busqueda binaria
    productos_ordenados = ordenar_lista(productos)

    # Ejecutar busqueda binaria
    pos_binaria, comp_binaria = busqueda_binaria(productos_ordenados, entrada)
    print("\n[ Busqueda Binaria ]")
    if pos_binaria != -1:
        print(f"Producto encontrado en la posicion {pos_binaria} (lista ordenada) (comparaciones: {comp_binaria})")
    else:
        print(f"Producto NO encontrado (comparaciones: {comp_binaria})")

    # Guardar resultados en historial
    historial.append({
        "producto": entrada,
        "lineal_pos": pos_lineal,
        "lineal_comp": comp_lineal,
        "binaria_pos": pos_binaria,
        "binaria_comp": comp_binaria
    })

# Mostrar resumen final
print("\n=== RESUMEN DE BUSQUEDAS ===")
for i, resultado in enumerate(historial, 1):
    print(f"\nBusqueda {i}: '{resultado['producto']}'")
    print(f" - Lineal: Posicion {resultado['lineal_pos']} / Comparaciones: {resultado['lineal_comp']}")
    print(f" - Binaria: Posicion {resultado['binaria_pos']} / Comparaciones: {resultado['binaria_comp']}")
