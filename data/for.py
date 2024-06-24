numeros = ["Juan", "Jose", "Julian"]
print(len(numeros))

for i in range(len(numeros)):
    print(numeros[i])
    
opcion = 1
while opcion != 0:
    opcion = int(input("Ingresa un numero: "))
    if opcion == 20:
        print("Numero extraño, deteniendo ciclo.")
        break
    elif opcion < 0:
        print("Numero negativo, se continua en el programa.")
    print("Esto es un ciclo")
    
