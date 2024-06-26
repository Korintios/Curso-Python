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

def getInputId():
    return int(input("Ingresar ID:"))

def getStudents():
    os.system("cls")
    cursor.execute("SELECT * FROM estudiantes")
    students = cursor.fetchall()
    for student in students:
        print("===========================")
        print("ID", student[0])
        print("Nombre:", student[1])
        print("Edad:", student[2])
        print("===========================\n")

def insertStudent():
    while True:
        id = getInputId()
        cursor.execute(f"SELECT * FROM estudiantes WHERE id = ?", (id,))
        findStudent = cursor.fetchall()
        if len(findStudent) != 0:
            print(Fore.RED + "Ya existe un estudiante con esa Identificación.")
            print(Style.RESET_ALL)
        else:
            name = input("Ingresar Nombre:")
            age = int(input("Ingresar Edad:"))

            cursor.execute('''
                INSERT INTO estudiantes (id, name, age) VALUES (?,?,?)        
            ''', (id,name, age))
            connection.commit()
            os.system("cls")
            break
    
def deleteStudent():
    while True:
        id = getInputId()
        cursor.execute(f"SELECT * FROM estudiantes WHERE id = ?", (id,))
        findStudent = cursor.fetchall()
        if len(findStudent) == 0:
            print(Fore.RED + "El estudiante no fue encontrado.")
            print(Style.RESET_ALL)
        else:
            cursor.execute('''
                DELETE FROM estudiantes WHERE id = ?
            ''', (id,))
            connection.commit()
            os.system("cls")
            break
    
def updateStudent():
    while True:
        id = getInputId()
        cursor.execute(f"SELECT * FROM estudiantes WHERE id = ?", (id,))
        findStudent = cursor.fetchall()
        if len(findStudent) == 0:
            print(Fore.RED + "El estudiante no fue encontrado.")
            print(Style.RESET_ALL)
        else:
            name = input("Ingresar Nombre:")
            age = int(input("Ingresar Edad:"))
            cursor.execute('''
            UPDATE estudiantes SET name = ?, age = ? WHERE id = ?
            ''', (name, age, id))
            connection.commit()
            os.system("cls")
            break

def menu():
    opt = 1
    while opt != 0:
        print(Style.RESET_ALL)
        print("1. Ver Estudiantes")
        print("2. Crear Estudiantes")
        print("3. Eliminar Estudiantes")
        print("4. Actualizar Estudiantes")
        print("0. Salir")
        opt = input(Fore.MAGENTA + "Selecciona una Opción: ")
        print(Style.RESET_ALL)
        opt = int(opt)
        match opt:
            case 1:
                getStudents()
            case 2:
                insertStudent()
            case 3:
                deleteStudent()
            case 4:
                updateStudent()
        
menu()
connection.close()