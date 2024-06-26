import sqlite3
import os
from colorama import init, Fore, Style

init()

connection = sqlite3.connect("database.sqlite")
cursor = connection.cursor()

# Crear tabla si no existe.
cursor.execute('''
CREATE TABLE IF NOT EXISTS estudiantes(
    id INTEGER PRIMARY KEY,
    name VARCHAR(64),
    age INTEGER
)
''')

class Student:
    def __init__(self, id, name, age) -> None:
        self.id = id 
        self.name = name 
        self.age = age
        
    def create(self):
        while True:
            cursor.execute(f"SELECT * FROM estudiantes WHERE id = ?", (self.id,))
            findStudent = cursor.fetchall()
            if len(findStudent) != 0:
                os.system("cls")
                print(Fore.RED + "Ya existe un estudiante con esa Identificación.")
                print(Style.RESET_ALL)
                break
            else:
                cursor.execute('''
                    INSERT INTO estudiantes (id, name, age) VALUES (?,?,?)        
                ''', (self.id,self.name, self.age))
                connection.commit()
                os.system("cls")
                break

def getInputId():
    return int(input("Ingresar ID:"))

def getStudents():
    os.system("cls")
    print(Style.RESET_ALL)
    cursor.execute("SELECT * FROM estudiantes")
    students = cursor.fetchall()
    for student in students:
        print("===========================")
        print("ID", student[0])
        print("Nombre:", student[1])
        print("Edad:", student[2])
        print("===========================\n")

def menu():
    opt = 1
    while opt != 0:
        print(Style.RESET_ALL)
        print("1. Ver Lista de Estudiantes")
        print("2. Guardar Estudiante")
        print("0. Salir")
        try:
            opt = int(input(Fore.MAGENTA + "Selecciona una Opción: "))
            if opt == 1:
                getStudents()
            else:
                id = input("Ingresar ID:")
                name = input("Ingresar Nombre:")
                age = int(input("Ingresar Edad:"))
                estudiante = Student(id,name,age)
                if opt == 2: estudiante.create()
        except ValueError:
            os.system("cls")
            print(Fore.RED + "El tipo de valor que ingresaste es erroneo, ingresalo nuevamente.")
            print(Style.RESET_ALL)
        except KeyboardInterrupt:
            print(Fore.YELLOW + "\nCerrando Aplicación...")
            break
        
menu()
connection.close()