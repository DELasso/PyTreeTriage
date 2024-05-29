from MinHeap import GestionUrgencias

class GestionUrgenciasMenu:
    def __init__(self):
        self.gestion = GestionUrgencias()

    def mostrar_menu(self):
        while True:
            print("\n╔══════════════════════════════════╗")
            print("║         Sala de Urgencias        ║")
            print("╠══════════════════════════════════╣")
            print("║ 1. Registrar paciente            ║")
            print("║ 2. Consultar próximo paciente    ║")
            print("║ 3. Atender siguiente paciente    ║")
            print("║ 4. Consultar lista de espera     ║")
            print("║ 5. Consultar lista de espera por ║")
            print("║    triaje                        ║")
            print("║ 6. Eliminar paciente             ║")
            print("║ 7. Imprimir árbol                ║")
            print("║ 0. Salir                         ║")
            print("╚══════════════════════════════════╝")
            opcion = input("\nSeleccione una opción: ")

            if opcion == "1":
                genero = input("Género del paciente: ")
                nombre = input("Nombre del paciente: ")
                edad = int(input("Edad del paciente: "))
                triaje = int(input("Nivel de triaje del paciente: "))
                self.gestion.registrar_paciente(genero, nombre, edad, triaje)
            elif opcion == "2":
                proximo = self.gestion.consultar_proximo()
                if proximo:
                    print(f"Próximo paciente: {proximo}")
                else:
                    print("No hay pacientes en espera.")
            elif opcion == "3":
                atendido = self.gestion.atender_siguiente()
                if atendido:
                    pass
                else:
                    print("No hay pacientes en espera.")
            elif opcion == "4":
                lista_espera = self.gestion.consultar_espera()
                if lista_espera:
                    print("Lista de espera:")
                    for paciente in lista_espera:
                        print(paciente)
                else:
                    print("No hay pacientes en espera.")
            elif opcion == "5":
                triaje = int(input("Ingrese el nivel de triaje a consultar: "))
                lista_espera = self.gestion.consultar_espera_por_triaje(triaje)
                if lista_espera:
                    print(f"Lista de espera para triaje {triaje}:")
                    for paciente in lista_espera:
                        print(paciente)
                else:
                    print(f"No hay pacientes en espera con triaje {triaje}.")
            elif opcion == "6":
                id_paciente = input("Ingrese el ID del paciente a eliminar (o dejar en blanco): ")
                nombre_paciente = input("Ingrese el nombre del paciente a eliminar (o dejar en blanco): ")
                eliminado = self.gestion.eliminar_paciente(id_paciente, nombre_paciente)
                if eliminado:
                    pass
                else:
                    print("Paciente no encontrado.")
            elif opcion == "7":
                print("Árbol de pacientes:")
                self.gestion.imprimir_arbol()
            elif opcion == "0":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")


menu = GestionUrgenciasMenu()
menu.mostrar_menu()
