class Estudiante: # Objeto
    def __init__(self, id, nombre, edad, telefono): #Declaración de Atributos
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
    
    # Métodos.
    def di_hola(self):
        print(f"El estudiante {self.nombre} a dicho hola.")
        
    def info(self):
        print(f"Identificación: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Teléfono: {self.telefono}")
    
    def guardar_estudiante(self):
        print("Guardar estudiante.")
        self.__eliminar_estudiante()
    
    def __eliminar_estudiante(self):
        print("Estudiante eliminado.")
    
    def __str__(self):
        return f"Identificación: {self.id} \nNombre: {self.nombre} \nEdad: {self.edad} \nTelefono: {self.telefono}"
        
        
estudiante1 = Estudiante(10,"Juan", 18, "123456789")
estudiante1.guardar_estudiante()
