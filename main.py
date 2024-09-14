from Estudiante import Estudiante
from Curso import Curso

print("***Bienvenido***")

nombre = input("Ingresa el nombre: ")
edad =int(input("Ingresa edad: "))
id_estudiante=int(input("Ingresa el id: "))
curso=input("Ingresa curso: ")

Estudiante_uno = Estudiante("Jonathan", 25, "Analisis de fluidos")
Estudiante_dos = Estudiante("Ricardo", 22, "Calculo Diferencial")
Estudiante_tres = Estudiante("Linda", 20, "Programacion")

print("Información de los estudiantes:")
Estudiante_uno.mostrar_info()
Estudiante_dos.mostrar_info()
Estudiante_tres.mostrar_info()

curso1 = Curso("Programacion", "Prof. García")
curso2 = Curso("Calculo Diferencial", "Prof. Sergio")
curso3 = Curso("Analisis de fluidos", "Prof. Eli")

print("Información de los cursos:")
curso1.mostrar_info()
curso2.mostrar_info()
curso3.mostrar_info()

