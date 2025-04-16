# triangulo rectangulo con la cantidad de renglones que indica el usuario

numRenglones = int(input("Ingrese cantidad de renglones: "))

for i in range(1, numRenglones + 1):
    linea = ""
    numeroInicial = i * 2
    for j in range(i):
        linea = str(numeroInicial) + " " + linea
        numeroInicial -= 2
    print(linea.strip())