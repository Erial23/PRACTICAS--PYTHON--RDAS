lista= [1,2,2,4,5]
nueva=[]
for i in lista:
    if i != 2 :
        nueva.append(i)
print(nueva)

for i in lista:
    try:
        lista.remove(2)
    except ValueError:
        pass
    print(nueva)