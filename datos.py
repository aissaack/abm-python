# Se incia al la lista de registros
from Personas import Usuario

registros = [
    # Se agregan instancias de la clase Persona
    Usuario(45058451, "Isaac", "Alvarez", "21", "Capitán Bermudéz"),
    Usuario(27432887, "Daniel", "Alvarez", "51", "Capitán Bermudéz")
]

# Esta función sirve para verificar si un DNI ya está registrado o no.


def comprobarDNI(registros, DNI):
    for usuario in registros:
        if usuario.DNI == DNI:
            print("El DNI ya está registrado.")
            return usuario
    return None  # Devuelve None si no se encuentra el DNI


# Debe haber una linea vacia al final de cada archivo
