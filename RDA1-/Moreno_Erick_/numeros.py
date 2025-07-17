print("Realizado por Erick Moreno")
# Lista ordenada de numeros del 10 al 100
numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Pedir al usuario un número
numero_buscado = int(input("Escribe un número (de 10 a 100): "))

# Busqueda binaria
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

# Mostrar resultado
if posicion != -1:
    print("El número está en la posición", posicion)
else:
    print("El número no está en la lista")

print("Veces que se partió la lista:", particiones)
