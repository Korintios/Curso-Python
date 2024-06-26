class Human:
    def __init__(self, nombre, edad, altura, cedula) -> None:
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.cedula = cedula
        
    def info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Altura: {self.altura}")
        print(f"Cedula: {self.cedula}")
        
    def hola(self):
        return f"El humano {self.nombre} a dicho hola!"
        
class Doctor(Human):
    def __init__(self, nombre, edad, altura, cedula, especialidad, rango) -> None:
        super().__init__(nombre, edad, altura, cedula)
        self.especialidad = especialidad
        self.rango = rango
        
    def info(self):
        super().info()
        print(f"Especialidad: {self.especialidad}")
        print(f"Rango: {self.rango}")
        
    def hola(self):
        return f"El doctor {self.nombre} a dicho hola!"
    
class Master(Human):
    def __init__(self, nombre, edad, altura, cedula, clase, nivel) -> None:
        super().__init__(nombre, edad, altura, cedula)
        self.clase = clase
        self.nivel = nivel
        
    def info(self):
        super().info()
        print(f"Clase: {self.clase}")
        print(f"Nivel: {self.nivel}")
        
    def hola(self):
        return f"El maestro {self.nombre} a dicho hola!"
        
humano = Human("Juan", 18, 1.70, "12345")
doctor = Doctor("Pepito", 18, 1.70, "12345", "Psicologia", 3)
maestro = Master("Pablito", 18, 1.70, "12345", "Tecnologia", 5)

def saludar(human: Human):
    print(human.hola())

saludar(humano)
saludar(doctor)
saludar(maestro)