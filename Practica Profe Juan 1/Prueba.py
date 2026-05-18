opcion = 0

while opcion != 4:
    print("---Menu Principal ---")
    print("1. Saludar")
    print("2. Sumar dos numeros")
    print("3. Mostrar numeros del 1 al 5")
    print("4. Salir")


    try:
        opcion = int(input("Ingrese una opcion: "))
    
        if opcion == 1:
            nombre = input("Ingrese su nombre: ")
            print(f"Hola {nombre}!")
        elif opcion == 2:
            n1 = float(input("Numero 1:"))
            n2 = float(input("Numero 2:"))
            print(f"La suma es: {n1 + n2}")
        elif opcion == 3:
            contador = 1
            while contador <= 5:
                print(contador)
                contador += 1
        elif opcion == 4:
            print("Programa finalizado-.")
        else:
            print("Opcion invalida")
    except:
        print("Debe ingresar un numero")