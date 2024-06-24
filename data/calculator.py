def calcular(num1,num2,calculo = "suma"):
    
    suma = lambda: num1 + num2
    resta = lambda: num1 - num2
    multiplicar = lambda: num1 * num2
    dividir = lambda: num1 / num2
    
    if calculo == "suma":
        print(suma())
    elif calculo == "resta":
        print(resta())
    elif calculo == "multiplicar":
        print(multiplicar())
    elif calculo == "dividir":
        print(dividir())
    else:
        print("Ingresaste una opción errónea.")
        
operacion = ""   
while operacion != "salir":
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input("Ingresa el segundo numero: "))
    operacion = input("Ingresa una operacion: ")
    calcular(num1,num2,operacion)