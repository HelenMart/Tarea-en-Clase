from collections import deque


class Pacientes:
    def __init__(self, nombre, edad, dpi, tipoS, nombreen, descripcion, prioridad):
        self.nombre = nombre
        self.edad = str(edad)  # Convertimos en string para evitar errores en __str__
        self.dpi = str(dpi)
        self.tipoS = tipoS
        self.nombreen = nombreen
        self.descripcion = descripcion
        self.prioridad = prioridad

    def __str__(self):
        return (f"Paciente | Nombre: {self.nombre}, Edad: {self.edad}, DPI: {self.dpi}, Tipo de Sangre: {self.tipoS}\n"
                f"Enfermedad | Nombre: {self.nombreen}, Descripción: {self.descripcion}, Prioridad: {self.prioridad}")


class Asignar:
    def __init__(self):
        self.baja = deque()
        self.media = deque()
        self.alta = deque()

    def distribuir(self, pacientes):
        for paciente in pacientes:
            if paciente.prioridad.lower() == 'alta':
                self.alta.append(paciente)
            elif paciente.prioridad.lower() == 'media':
                self.media.append(paciente)
            elif paciente.prioridad.lower() == 'baja':
                self.baja.append(paciente)
            else:
                print(f"Error: {paciente.nombre} tiene una prioridad inválida ({paciente.prioridad}).")

    def mostrar(self):
        print("\nPacientes a atender segun prioridad")
        print(f"\nPacientes con prioridad Alta:")
        for paciente in self.alta:
            print(paciente)

        print("\nPacientes con prioridad Media:")
        for paciente in self.media:
            print(paciente)

        print("\nPacientes con prioridad Baja:")
        for paciente in self.baja:
            print(paciente)


pacientes_lista = [
    Pacientes("Diego Armando Villalobos", 20, 124548, "AB negativo", "Fiebre", "Fiebre normal, no mayor a 20", "Baja"),
    Pacientes("Maria Perez", 35, 987654, "O positivo", "Hipertensión", "Presión arterial alta", "Alta"),
    Pacientes("Juan López", 42, 456789, "A positivo", "Diabetes", "Niveles de glucosa elevados", "Media")
]


print("Pacientes a clasificar:")
for paciente in pacientes_lista:
    print(paciente)
lista = Asignar()
lista.distribuir(pacientes_lista)
lista.mostrar()
