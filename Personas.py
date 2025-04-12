# aca se crea la clase persona.
# la clase contiene todas las caracteristicas de la "persona"


class Usuario:
    def __init__(self, DNI, nombre, apellido, edad, localidad):
        self.DNI = DNI
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.localidad = localidad

# Como siempre, una linea en blanco al final del archivo.
