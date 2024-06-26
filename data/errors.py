""" try:
    num = int(input("Ingresa un numero: "))
    print(num)
except:
    print("Error inesperado.") """

try:
    num = 10 / 0
except TypeError:
    print("Error en el tipo.")
except ZeroDivisionError:
    print("El numero no se puede dividir con cero.")