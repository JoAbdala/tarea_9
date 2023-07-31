


lista2=[]
suma = 0
print("Ingrese un valor, con el 0 salir")
ingreso=int(input("valor-->:"))
while ingreso != 0:
    lista2.append(ingreso)
    ingreso = int(input("valor-->"))
    if ingreso == 0:
        
        for i in lista2:
            suma += i
        lista2.sort()
       
        promedio = suma/ i
         
        print(f"Lista Ordenada -->",lista2)
        print(f"El Total de la suma es:" ,suma)
        print(f"El Promedio de los valores es:" ,promedio)
'''

lista = []  
opc= True
while opc:
    print("---->MENU<---- ")
    print("1-Agregar nombre: ")
    print("2-Eliminar nombre: ")
    print("3-Modificar un nombre: ")
    print("4-Eliminar la lista completa")
    print("5-Salir")

    numero = int(input("iNGRESE LA OPCION DESEADA:->"))
    if numero == 1:
        nombre = input("Ingrese un nombre para la lista: ")
        lista.append(nombre)
        print (lista)
    
    elif numero == 2:
        nombre = input("Ingrese el nombre que desea eliminar: ")
        if nombre in lista:
            lista.remove(nombre)
            print(f"{nombre} fue eliminado correctamente")
        else:
            print(f"{nombre} no está en la lista.")
        print(lista)
        
    elif numero == 3:
        nombre = input("Ingrese un  nombre a cambiar: ")
        verificar = False
        for i in range(len(lista)):
                lista [i] == nombre
                nombre_nuevo=input("Ingrese el nuevo nombre: ")
                lista[i] = nombre_nuevo
                print(f"{nombre_nuevo} agregado correctamente")
                verificar = True
                break
        if verificar :
            print(f"{nombre} no esta en la lista")
        else:
            nombre_nuevo = input("Ingrese el nuevo nombre: ")
    elif numero == 4:
        lista.clear()
        print("La lista fue eliminada correctamente.")
        print(lista)         
                
    elif numero == 5:
        print("Saliendo")
        break

    else:
        print("Opción no válida. Por favor, ingrese un número válido del menú.")       
    
'''
            
    

     
    
        
   

  
