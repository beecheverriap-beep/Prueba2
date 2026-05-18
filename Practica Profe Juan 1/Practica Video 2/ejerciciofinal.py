num1 = int(input("Ingrese limite inferior: "))
num2 = int(input("Ingrese limite superior: "))

from random import randint
numero = randint(num1, num2)

if numero % 2 != 0:  
    if numero + 1 <= num2:
        numero_final = numero + 1
    else:
        numero_final = numero - 1
else:
    numero_final = numero


intento1 = int(input("Intente adivinar: "))

if intento1 == numero_final:
    print("Felicitaciones, pudiste adivinar.")
else:
    if intento1 < numero_final:
        print("El número es mayor.")
    else:
        print("El número es menor.")
        
    
    intento2 = int(input("Intente de nuevo: "))
    
    if intento2 == numero_final:
        print("Felicitaciones, pudiste adivinar.")
    else:
        if intento2 < numero_final:
            print("El número es mayor.")
        else:
            print("El número es menor.")
            
        
        dist1 =(numero_final - intento1)
        dist2 =(numero_final - intento2)
        
        print("Te daré una pista:")
        if dist2 < dist1:
            print(f"El número que buscas está más cerca de {intento2} que de {intento1}")
        else:
            print(f"El número que buscas está más cerca de {intento1} que de {intento2}")
            

        intento3 = int(input("Intente la última vez: "))
        
        if intento3 == numero_final:
            print("Felicitaciones, pudiste adivinar.")
        else:
            print("Perdiste.")
            print(f"El número era: {numero_final}")