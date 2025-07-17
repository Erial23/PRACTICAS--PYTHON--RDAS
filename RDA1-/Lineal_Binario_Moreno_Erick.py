print("Realizado por Erick Moreno")
print("MENÚ DE BÚSQUEDA")
print("1. Buscar una fruta (búsqueda lineal)")
print("2. Buscar un número (búsqueda binaria)")

opcion = input("Elige una opción 1 o 2: ")

if opcion == "1":
    # Busqueda lineal
    # Lista de frutas
    frutas = ["manzana", "plátano", "naranja", "uva", "sandía", "pera", "melón", "fresa", "mango", "kiwi"]
    fruta_buscada = input("Escribe el nombre de una fruta: ")

    posicion = -1
    comparaciones = 0

    for i in range(len(frutas)):
        comparaciones += 1
        if frutas[i] == fruta_buscada:
            posicion = i
            break

# Resultado final
    if posicion != -1:
        print("La fruta está en la posición", posicion)
    else:
        print("La fruta no está en la lista")

    print("Comparaciones realizadas:", comparaciones)

elif opcion == "2":
    # Busqueda binaria
    # Lista ordenada de numeros del 10 al 100
    numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # Pedir al usuario un numero
    numero_buscado = int(input("Escribe un número (de 10 a 100): "))

    inicio = 0
    fin = len(numeros) - 1
    posicion = -1
    particiones = 0

    while inicio <= fin:
        particiones += 1
        medio = (inicio + fin) // 2
        if numeros[medio] == numero_buscado:
            posicion = medio
            break
        elif numero_buscado < numeros[medio]:
            fin = medio - 1
        else:
            inicio = medio + 1
# Resultado Final
    if posicion != -1:
        print("El número está en la posición", posicion)
    else:
        print("El número no está en la lista")

    print("Veces que se partió la lista:", particiones)

else:
    print("Opción no válida")
