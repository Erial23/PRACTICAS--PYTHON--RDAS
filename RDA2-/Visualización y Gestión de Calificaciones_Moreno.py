import random
import time
import matplotlib.pyplot as plt
import pandas as pd

print("////////////////////////////////////////////////////////////////////////////////////")
print("Realizado por Erick Moreno")
print("Fecha: 02/06/2025")
print("////////////////////////////////////////////////////////////////////////////////////")

# Generar lista de notas aleatorias
notas = random.sample(range(0, 21), 15)
print('Notas Originales:', notas)

# Bubble Sort animado
def animar_bubble_sort(lista_original, pausa=0.3):
    lista = lista_original.copy()
    pasos = [lista.copy()]
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                pasos.append(lista.copy())

    plt.ion()
    fig, ax = plt.subplots(figsize=(8, 4))
    barras = ax.bar(range(len(lista_original)), lista_original, color='skyblue')
    ax.set_ylim(0, max(lista_original) + 5)
    ax.set_title("Bubble Sort")

    for k, paso in enumerate(pasos):
        for rect, h in zip(barras, paso):
            rect.set_height(h)
        ax.set_title(f"Bubble Sort - Paso {k + 1}")
        plt.pause(pausa)

    plt.ioff()
    plt.show()

# Mostrar resultado final de sorted() (sin animación)
def mostrar_sorted_directo(lista_original):
    lista_ordenada = sorted(lista_original)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(range(len(lista_ordenada)), lista_ordenada, color='lightgreen')
    ax.set_ylim(0, max(lista_ordenada) + 5)
    ax.set_title("sorted() - Resultado final")
    plt.show()

# Comparación animada lado a lado
def animar_comparacion_sorted_bubble_simulada(lista_original, pausa=0.3):
    # Bubble Sort
    lista_bubble = lista_original.copy()
    pasos_bubble = [lista_bubble.copy()]
    n = len(lista_bubble)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_bubble[j] > lista_bubble[j + 1]:
                lista_bubble[j], lista_bubble[j + 1] = lista_bubble[j + 1], lista_bubble[j]
                pasos_bubble.append(lista_bubble.copy())

    # sorted() simulada
    lista_sorted_final = sorted(lista_original)
    lista_simulada = lista_original.copy()
    pasos_sorted = []
    for i in range(len(lista_sorted_final)):
        if lista_simulada[i] != lista_sorted_final[i]:
            lista_simulada[i] = lista_sorted_final[i]
        pasos_sorted.append(lista_simulada.copy())

    total_pasos = max(len(pasos_bubble), len(pasos_sorted))

    plt.ion()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

    barras_bubble = ax1.bar(range(len(lista_original)), lista_original, color='skyblue')
    ax1.set_title("Bubble Sort - Paso 1")
    ax1.set_ylim(0, max(lista_original) + 5)

    barras_sorted = ax2.bar(range(len(lista_original)), lista_original, color='lightgreen')
    ax2.set_title("sorted() - Paso 1")
    ax2.set_ylim(0, max(lista_original) + 5)

    for k in range(total_pasos):
        # Bubble Sort
        if k < len(pasos_bubble):
            for rect, h in zip(barras_bubble, pasos_bubble[k]):
                rect.set_height(h)
            ax1.set_title(f"Bubble Sort - Paso {k + 1}")
        else:
            for rect, h in zip(barras_bubble, pasos_bubble[-1]):
                rect.set_height(h)
            ax1.set_title("Bubble Sort - Final")

        # sorted()
        if k < len(pasos_sorted):
            for rect, h in zip(barras_sorted, pasos_sorted[k]):
                rect.set_height(h)
            ax2.set_title(f"sorted() - Paso {k + 1}")
        else:
            for rect, h in zip(barras_sorted, lista_sorted_final):
                rect.set_height(h)
            ax2.set_title("sorted() - Final")

        plt.pause(pausa)

    plt.ioff()
    plt.show()

# Menú principal
def menu():
    while True:
        print("\n--- MENÚ DE ANIMACIÓN DE ORDENAMIENTO ---")
        print("1. Ver Bubble Sort")
        print("2. Ver sorted() (resultado final sin animación)")
        print("3. Comparar ambos lado a lado")
        print("4. Salir")

        opcion = input("Elige una opción: ")
        if opcion == '1':
            animar_bubble_sort(notas)
        elif opcion == '2':
            mostrar_sorted_directo(notas)
        elif opcion == '3':
            animar_comparacion_sorted_bubble_simulada(notas)
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar menú
menu()
# produccion 