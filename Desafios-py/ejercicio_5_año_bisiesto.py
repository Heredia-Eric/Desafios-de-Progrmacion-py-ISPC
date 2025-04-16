# Programa que evalua si el Año ingresado por el usuario es bisiesto o no.

año = int(input("Ingrese el año a evaluar: "))

esBisiesto = False  # variable para indicar si es bisiesto o no

if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            esBisiesto = True
        else:
            esBisiesto = False
    else:
        esBisiesto = True
else:
    esBisiesto = False

if esBisiesto:
    print("El año", año, "es bisiesto")
else:
    print("El año", año, "No es bisiesto")
