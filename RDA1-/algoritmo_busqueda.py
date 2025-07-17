lista= [10,11,15,20,45,10]
for i in range (len(lista)-1):
    for j in range(len(lista)-1-i):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]
            print(lista[j], lista[j+1], end=" ")
            


print(lista)


