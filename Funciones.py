# En este archivo se definen todas las funciones del programa.
# se importa la lista registros

from datos import comprobarDNI
from Personas import Usuario

# Esta función muestra las opciones del menú.


def menu():
    print("Bienvenido al menú")
    print("Seleccione una opción:")
    print("1. Agregar un registro")
    print("2. Buscar un registro")
    print("3. Modificar un registro")
    print("4. Eliminar un registro")
    print("0. Salir del programa")


def agregarRegistro(registros):
    while True:
        try:
            DNI = int(input("Ingrese su DNI: "))
        except ValueError:
            print("Por favor, ingrese un número válido para el DNI.")
            continue

        if comprobarDNI(registros, DNI):
            print("El DNI ya está registrado.")
            return

        print("El DNI no está registrado. Proceda a ingresar los datos.")
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        edad = input("Ingrese su edad: ")
        localidad = input("Ingrese su localidad: ")

        nuevoRegistro = Usuario(DNI, nombre, apellido, edad, localidad)
        registros.append(nuevoRegistro)
        print("Registro agregado con éxito.")

        respuesta = input("¿Desea agregar otro registro? (s/n): ").lower()
        if respuesta == "n":
            print("Volviendo al menú principal.")
            break


def buscarRegistro(registros):
    while True:
        try:
            DNI = int(input("Ingrese el DNI del registro que desea buscar: "))
        except ValueError:
            print("Por favor, ingrese un número válido para el DNI.")
            continue

        usuario = comprobarDNI(registros, DNI)

        if usuario is not None:
            print("Registro encontrado:")
            print(f"DNI: {usuario.DNI}")
            print(f"Nombre: {usuario.nombre}")
            print(f"Apellido: {usuario.apellido}")
            print(f"Edad: {usuario.edad}")
            print(f"Localidad: {usuario.localidad}")
        else:
            print("El DNI no existe en la lista de registros.")

        mensaje = "¿Desea buscar otro registro?"
        respuesta = input(mensaje).strip().lower()
        if respuesta != "s":
            break

        # Aca se define la funcion para modificar un registro.


def modifRegistro(registros):
    while True:
        DNI = input("Ingrese el DNI del registro que desea modificar:")
        usuario = comprobarDNI(registros, DNI)
        if usuario:
            print("Registro encontrado:")
            print(f"DNI: {usuario.dni}")
            print(f"Nombre: {usuario.nombre}")
            print(f"Apellido: {usuario.apellido}")
            print(f"Edad: {usuario.edad}")
            print(f"Localidad: {usuario.localidad}")

            # Preguntar que dato desea modificar el usuario
            print("¿Qué dato desea modificar?")
            print("1. Nombre")
            print("2. Apellido")
            print("3. Edad")
            print("4. Localidad")
            mensaje = input("Ingrese el número del dato que desea modificar: ")
            opcion = input(mensaje).strip()

            if opcion == "1":
                usuario.nombre = input("Ingrese el nuevo nombre: ")
            elif opcion == "2":
                usuario.apellido = input("Ingrese el nuevo apellido: ")
            elif opcion == "3":
                usuario.edad = input("Ingrese la nueva edad:")
            elif opcion == "4":
                usuario.localidad = input("Ingrese la nueva localidad:")
            else:
                print("Opción no válida.No se relizó ninguna modificación.")

                # Mostrar el registro modificado.
                print("Registro modificado:")
                print(f"DNI: {usuario.dni}")
                print(f"Nombre: {usuario.nombre}")
                print(f"Apellido: {usuario.apellido}")
                print(f"Edad: {usuario.edad}")
                print(f"Localidad: {usuario.localidad}")
        else:
            print("No se encontró el registro con el DNI ingresado.")

        # Preguntar al usuario si desea modificar otro registro.
            pregunta = "¿Desea modificar otro registro?:(s/n)"
            respuesta = input(pregunta).strip().lower()
            if respuesta != "s":
                break  # sale del bucle. Termina la Función

# Aca termina la función para modificar un registro.


def elimRegistro(registros):
    DNI = input("Ingrese el DNI del registro que desea eliminar:")

    usuario = comprobarDNI(registros, DNI)
    if usuario:
        print("Registro encontrado:")
        print(f"DNI: {usuario.dni}")
        print(f"Nombre: {usuario.nombre}")
        print(f"Apellido: {usuario.apellido}")
        print(f"Edad: {usuario.edad}")
        print(f"Localidad: {usuario.localidad}")

    else:
        print("No se encontro el registro con el DNI ingresado.")
        return

    pregunta = "¿Desea eliminar los datos del registro?(s/n)"
    respuesta = input(pregunta).strip().lower()

    if respuesta == "s":
        registros.remove(usuario)
        print("Registro eliminado con éxito.")
    else:
        print("No se eliminó el registro.")

# Aca termina la función para eliminar un registro.
