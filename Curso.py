class Curso:
    nombre_curso = ""
    codigo_curso = 0
    instructor= ""

    def __init__(self, nombre_curso, codigo_curso, instructor):
        self.nombre_curso = nombre_curso
        self.codigo_curso = codigo_curso
        self.instructor =instructor

    def mostrar_info(self):
        print(f"nombre_curso: {self.nombre_curso}")
        print(f"codigo_curso: {self.codigo_curso}")
        print(f"instructor: {self.instructor}")