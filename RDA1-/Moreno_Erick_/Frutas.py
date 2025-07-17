print("Realizado por Erick Moreno")


# Lista de frutas
frutas = ["manzana", "plátano", "naranja", "uva", "sandía", "pera", "melón", "fresa", "mango", "kiwi"]

# Pedir al usuario una fruta
fruta_buscada = input("Escribe el nombre de una fruta: ")

# Busqueda lineal
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


