from random import Random

class Estudiante:
    nombre = ""
    edad = 0
    id_estudiante = 0
    cursos = ""

    def __init__(self, nombre, edad, id_estudiante, cursos):
        self.nombre = nombre
        self.edad = edad
        self.id_estudiante = Random.randint(1, 10001)
        self.cursos = cursos

    def agregar_curso(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"\nId_estudiante: {self.id_estudiante}")
        print(f"cursos: {self.cursos}")

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"\nId_estudiante: {self.id_estudiante}")
        print(f"cursos: {self.cursos}")

   