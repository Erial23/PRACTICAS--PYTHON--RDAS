'''
# DEL 0 AL 4
for i in range(5):
    print(i)
#DEL 1 AL 9
for i in range(1,10):
    print(i)
#del 1 al 10 
for i in range(1,10+1):
    print(i)
#Tabla del 5
for i in range(5+1):
    print("Tabla del ", i)
    for j in range(5+1):
        print(i, "*",j, "=", i*j)
#lista
for i in [0,10,2]:
    print("Erick", i)

#operar elementos de la lista
for i in [0,10,2]:
    print("el valor de ", i , "y su cuadrado es", i**2)
#

for i in [1,10,20,30]:
    for j in [1,10,20,30]:
        print(i, "*", j, "=", i*j)
'''
#test
        
#par o impar
for i in [1,2,3,4,5,6,7,8,9,10]:
    if i % 2 == 0:
        print(i, "es par")
    else:
        print(i, "es impar")
for i in range (1,11):
    if i % 2!= 0:
        print(i, "es impar")