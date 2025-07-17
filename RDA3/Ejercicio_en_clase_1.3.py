historial=[]
historial.append("www.google.com")
historial.append("www.python.org")
historial.append("www.stackoverflow.com")
print("Historial:", historial)
while True:
    print("1.Agregar nuevas paginas")
    print("2.Mostrar historial")
    print("3.Eliminar pagina del historial")
    print("4.Mostrar ultima pagina del historial")
    print("5.Eliminar el ultimo url agregado al historial")
    print("6.Eliminar todo el historial")
    print("7.Salir")
    
    opcines=int(input("Ingrese la opcion que desea realizar: "))
    if opcines==1:
        url=input("Ingrese la url de la pagina que desea agregar: ")
        historial.append(url)
    elif opcines==2:
        print("Ver historial de navegacion: ")
        print(historial)
    elif opcines==3:
        url=input("Ingrese la url de la pagina que desea eliminar: ")
        if url in historial:
            historial.remove(url)
            print("Pagina eliminada con exito")
        else:
            print("Pagina no encontrada")
    elif opcines==4:
        if historial:
            print("Mostrar ultima pagina", historial[-1])
        else:
            print("No hay paginas en el historial")
    elif opcines==5:
        if historial:
            print("Eliminar el ultimo url agregado al historial", historial.pop())
        else:
            print("No hay paginas en el historial")
    elif opcines==6:
        historial.clear()
        print("Historial eliminado con exito")
    elif opcines==7:
        print("Gracias nos vemos , hasta la proxima")
        break
    else:
        print("Opcion invalida, por favor ingrese una opcion valida")
    
    
        
        



