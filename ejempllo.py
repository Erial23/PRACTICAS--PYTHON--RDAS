# Lista fija de precios desordenados
precios = [29.99, 15.50, 39.90, 12.75, 42.30, 9.99, 18.00, 33.33, 24.99, 5.49]

# Bubble Sort
def bubble_sort(lista):
    comparaciones = 0
    intercambios = 0
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            comparaciones += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambios += 1
    return lista, comparaciones, intercambios