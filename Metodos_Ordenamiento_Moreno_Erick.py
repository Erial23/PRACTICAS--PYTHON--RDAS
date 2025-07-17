import random  #generar numeros aleatorios

# Variables globales

precios = []  #Lista vacía donde se almacenarán los 10 precios ingresados por el usuario

#Funciones de ordenamiento
def bubble_sort(lista):
    """Ordena una lista usando el algoritmo Bubble Sort y cuenta comparaciones e intercambios"""
    comparaciones = 0  #Contador de comparaciones entre elementos
    intercambios = 0   #Contador de intercambios realizados
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):  #Se va reduciendo el rango con cada iteración
            comparaciones += 1
            if lista[j] > lista[j + 1]:  #Si el elemento actual es mayor al siguiente, se intercambian
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambios += 1
    return lista, comparaciones, intercambios  #Devuelve la lista ordenada y los contadores

def insertion_sort(lista):
    """Ordena una lista usando el algoritmo Insertion Sort y cuenta comparaciones e intercambios"""
    comparaciones = 0
    intercambios = 0
    for i in range(1, len(lista)):
        valor = lista[i]  #Elemento actual a insertar
        j = i - 1
        #Recorre hacia atrás comparando y moviendo elementos mayores
        while j >= 0 and lista[j] > valor:
            lista[j + 1] = lista[j]
            j -= 1
            intercambios += 1
            comparaciones += 1
        if j >= 0:
            comparaciones += 1  #Una comparación extra cuando se rompe el while
        lista[j + 1] = valor  #Inserta el elemento en su posición correcta
    return lista, comparaciones, intercambios

def selection_sort(lista):
    """Ordena una lista usando el algoritmo Selection Sort y cuenta comparaciones e intercambios"""
    comparaciones = 0
    intercambios = 0
    n = len(lista)
    for i in range(n):
        minimo = i  #Se asume que el elemento actual es el menor
        for j in range(i + 1, n):  #Se busca un valor menor en el resto de la lista
            comparaciones += 1
            if lista[j] < lista[minimo]:
                minimo = j  #Se encuentra un nuevo mínimo
        if minimo != i:  #Si el mínimo no está en la posición actual, se intercambia
            lista[i], lista[minimo] = lista[minimo], lista[i]
            intercambios += 1
    return lista, comparaciones, intercambios

#Menú principal que se repite hasta que el usuario elija salir
while True:
    print("\n===== MENU DE OPCIONES =====")
    print("1. Ingresar exactamente 10 precios")
    print("2. Ordenar precios con Bubble, Insertion y Selection Sort")
    print("3. Generar automaticamente una lista de 10 numeros ")
    print("4. Salir")

    opcion = input("Selecciona una opcion : ")

    if opcion == "1":
        #Solicita al usuario 10 precios separados por coma
        while True:
            entrada = input("Ingresa exactamente 10 precios separados por coma: ")
            lista = entrada.split(",")
            if len(lista) != 10:
                print("Debes ingresar exactamente 10 precios. Intenta de nuevo.\n")
            else:
                try:
                    #Convierte los valores a tipo float, eliminando espacios
                    precios = [float(x.strip()) for x in lista]
                    print("Precios guardados correctamente.")
                    break
                except ValueError:
                    #Captura errores si alguno de los valores no es numérico
                    print("Error: Asegúrate de ingresar solo números. Intenta de nuevo.\n")

    elif opcion == "2":
        #Verifica que ya se hayan ingresado los 10 precios
        if len(precios) != 10:
            print("Primero debes ingresar exactamente 10 precios (opción 1).")
        else:
            print("\nLista original:", precios)

            #Aplica Bubble Sort
            lista_b = precios[:]  # Copia de la lista original
            ordenado, comps, interc = bubble_sort(lista_b)
            print("\nBubble Sort:")
            print("Ordenado:", ordenado)
            print("Comparaciones:", comps, "Intercambios:", interc)

            #Aplica Insertion Sort
            lista_i = precios[:]  # Copia de la lista original
            ordenado, comps, interc = insertion_sort(lista_i)
            print("\nInsertion Sort:")
            print("Ordenado:", ordenado)
            print("Comparaciones:", comps, "Intercambios:", interc)

            #Aplica Selection Sort
            lista_s = precios[:]  # Copia de la lista original
            ordenado, comps, interc = selection_sort(lista_s)
            print("\nSelection Sort:")
            print("Ordenado:", ordenado)
            print("Comparaciones:", comps, "Intercambios:", interc)
    elif opcion == "3":
        # Genera 10 precios aleatorios entre 1.0 y 100.0
        precios = [round(random.uniform(1.0, 100.0), 2) for _ in range(10)]
        print("Lista aleatoria generada exitosamente:")
        print(precios)


    elif opcion == "4":
        #Sale del programa
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        #Opción inválida
        print("Opción inválida. Intenta nuevamente.")

# -------------------------------------------------------
# Algoritmos de Ordenamiento
# -------------------------------------------------------

# Bubble Sort:
# Compara elementos adyacentes en la lista y los intercambia si estan en el orden incorrecto.
# Repite este proceso varias veces hasta que la lista este ordenada.
# Es facil de entender, pero ineficiente con listas grandes por la cantidad de comparaciones e intercambios.

# Insertion Sort:
# Recorre la lista desde el segundo elemento e inserta cada uno en su lugar correcto
# dentro de la parte ya ordenada. Es mas eficiente si la lista esta casi ordenada.
# Hace menos intercambios que Bubble Sort y suele ser mas rapido en listas pequenas.

# Selection Sort:
# Encuentra el valor minimo de la parte no ordenada de la lista y lo coloca al principio.
# Repite esto hasta que toda la lista este ordenada.
# Hace pocas permutaciones (util si mover datos es costoso), pero muchas comparaciones.

# -------------------------------------------------------
# Comparacion de Rendimiento 
# -------------------------------------------------------

# En este caso, Insertion Sort fue el mas eficiente en numero de comparaciones e intercambios
# para la lista de 10 precios. Esto ocurre porque se adapta mejor cuando la lista esta
# parcialmente ordenada.

# Bubble Sort fue el que mas intercambios necesito.
# Selection Sort tuvo menos intercambios, pero mas comparaciones que Insertion.

# -------------------------------------------------------
# Cuando usar cada uno
# -------------------------------------------------------

# - Bubble Sort: solo con fines educativos o en listas muy pequenas donde la eficiencia no es importante.
# - Insertion Sort: util para listas pequenas o casi ordenadas (por ejemplo, insertar nuevos precios en un catalogo).
# - Selection Sort: recomendable si intercambiar elementos es costoso (como mover archivos fisicos o registros pesados).
