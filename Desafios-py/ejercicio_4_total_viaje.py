tiempoTotalMin = 0

print("Ingrese la duración de cada tramo del viaje en minutos.")
print("Para finalizar, ingrese 0.")

while True:
    duracionTramo = int(input("Duración tramo: "))
    if duracionTramo == 0:
        break  # Salir del bucle si se ingresa 0
    tiempoTotalMin = tiempoTotalMin + duracionTramo

horas = tiempoTotalMin // 60  # Calcula la cantidad de horas enteras
minRestantes = tiempoTotalMin % 60  # Calcula los minutos restantes

print(f'Tiempo total de viaje: {horas} horas y {minRestantes} minutos.')