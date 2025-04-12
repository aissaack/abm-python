from Funciones import agregarRegistro, buscarRegistro, modifRegistro
from Funciones import elimRegistro, menu
from datos import registros
# Este es el archivo main
# desde aca se accede al menú y desde ahi a las demas funciones
import os


def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        menu()
        try:
            opcion = int(input("Seleccione una opcion: "))

            if opcion == 1:
                agregarRegistro(registros)
                input("\nPresione Enter para continuar... ") 
                # Evita que la pantalla se limpie inmediatamente

            elif opcion == 2:
                buscarRegistro(registros)
                input("\nPresione Enter para continuar... ")

            elif opcion == 3:
                modifRegistro(registros)
                input("\nPresione Enter para continuar... ")

            elif opcion == 4:
                elimRegistro(registros)
                input("\nPresione Enter para continuar... ")

            elif opcion == 0:
                print("Saliendo del programa.")
                break

            else:
                print("Opción no válida.Intente otra vez.")
                input("\nPresione Enter para continuar... ")
                # Pausa antes de limpiar

        except Exception as e:
            print(f"Ocurrió un error: {e}")
            input("Presione Enter para continuar... ")
            # Para leer el error antes de limpiar la pantalla


if __name__ == "__main__":
    main()
