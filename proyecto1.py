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

# ------------ Función registrar
def registrar_trabajadores():
    global trabajador

    # Ciclo para ingresar los dats de múltiples trabajadores
    while True:        os.system("cls")
        print("\n\n\033[32m** MODULO REGISTRO DE TRABAJADORES **\033[0m\n]")

        # Solicitar al usuario que ingrese los datos del trabajador
        dni_a_buscar = input("Ingrese el dni ó '\033[33m000\033[0m' para volver al Menú: ")

        # Si el usuario ingresa "000", se rompe el ciclo
        if dni_a_buscar == '000':
            break
        else:
            resultado_busqueda = buscar_dni(dni_a_buscar)
            if resultado_busqueda[0]:
                print(f"\DNI \033[32m{dni_a_buscar}\033[0m ya está registrado.")
                trabajador = resultado_busqueda[2]
                input(f"\nPertenece al trabajador: {trabajador['nombre_apellido']}")
                continue
            else:
                trabajador['dni'] = dni_a_buscar
                trabajador['nombre_apellid'] = input("Nombre y apellid: ").lower().title()
                trabajador['año_de_ingresos'] = validar_anio()
                trabajador['sexo'] = validar_sexo()
                trabajador['edad'] = validar_edad()
                trabajador['salario'] = validar_salario()

                # Agregar una copia del diccionario <trabajador> a la lista de trabajadores
                lista_trabajadores.append(trabajador.copy())
                input("\nTrabajador Registrado, presione <enter>")

# ------------ Función consultar
def consultar_trabajadores():
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
