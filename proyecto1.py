import os

# Crear el diccionario para almacenar los datos del trabajador
trabajador = {
    'dni': '',
    'nombre_apellido': '',
    'año_de_ingreso': '',
    'sexo': '',
    'edad': '',
    'salario': ''
}

# Lista vacía para almacenar los datos de los trabajadores
lista_trabajadores = []

# ------------ Función consultar
def consultar_trabajadores():
    pass

# ------------ Función registrar
def registrar_trabajadores():
    pass

# ------------ Función eliminar
def eliminar_trabajadores():
    pass

# ------------ Función listar
def listar_trabajadores():
    pass

# ------------ Función menú
def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n\n\033[32m *MENÚ DE OPCIONES*\033[0m")
        print("Opción".rjust(33))
        print("------".rjust(33))
        print("Registrar trabajadores ....... 1")
        print("Consultar trabajadores ....... 2")
        print("Eliminar trabajadores  ....... 3")
        print("Listar trabajadores    ....... 4")
        print("\033[33mSalir ....... 0 \033[0m".rjust(42))
        while True:
            opcion = input("\033[32m¿Elija una opción? \033[0m ".rjust(43))
            if opcion in ['0','1','2','3','4']:
                break
            else:
                print("Opción inválida")

        if   opcion == '1': registrar_trabajadores()
        elif opcion == '2': consultar_trabajadores()
        elif opcion == '3': eliminar_trabajadores()
        elif opcion == '4': listar_trabajadores()
        elif opcion == '0': break

# Cuerpo principl del programa
main()
