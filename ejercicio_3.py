# Escriba unprograma que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

n = int(input("Ingrese un número entero: "))

if n <= 1:
    print(f"El número {n} no es primo.")
else:
    esPrimo = True  # Asumimos que el número es primo inicialmente
    for i in range(2, int(n**0.5) + 1):  # Optimizamos el bucle
        if n % i == 0:
            esPrimo = False
            break

    if esPrimo:
        print(f"El número {n} es primo.")
    else:
        print(f"El número {n} no es primo.")

