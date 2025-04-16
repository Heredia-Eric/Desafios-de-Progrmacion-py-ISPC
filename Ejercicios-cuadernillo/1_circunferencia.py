# Escriba un programa que pida al usuario el radio de un círculo y calcule el área.

radio = input("Ingrese el radio del círculo: ")

if radio < 0:
    print("El radio no puede ser negativo.")
else:
    area = 3,1416 * ({radio}**2)
    print(f'El área del círculo con radio: {radio}, es: {area}')

