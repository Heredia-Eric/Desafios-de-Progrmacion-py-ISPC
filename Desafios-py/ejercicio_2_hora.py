# Escriba un programa que pregunte al usuario la hora actual horaActual del reloj y un número entero de horas horasSumar, que indique qué hora marcará el reloj dentro de horasSumar horas:

# Pedir la hora actual y las horas a sumar
horaActual = input("Introduce la hora actual (hh:mm): ")
horasSumar = int(input("Introduce el número de horas a sumar: "))

# Calcular la hora futura
horas, minutos = map(int, horaActual.split(':'))
horasTotales = horas + horasSumar
horasFuturas = horasTotales % 24

# Imprimir el resultado
print(f"Dentro de {horasSumar} horas, el reloj marcará las {horasFuturas:02d}:{minutos:02d}")

