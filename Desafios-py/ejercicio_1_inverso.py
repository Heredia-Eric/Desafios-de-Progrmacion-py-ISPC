# Escriba un programa que pida al usuario un entero de tres digitos y entregue el número con los digitos en orden inverso:

"""n = str(input("Ingrese un número de tres digitos: "))

unidad = n[2]
decena = n[1]
centena = n[0]

print(unidad + decena + centena)"""

# Opción 2
n = input("Ingrese un valor de 3 digitos: ")
n = n[::-1]
print(n)