from controller.vaccineController import VaccineController

class VaccineView:
    def __init__(self):
        self.controller = VaccineController()

    def show_main_menu(self):
        while True:
            print("\n-- Gestión de Vacunas --")
            print("1. Agregar Vacuna")
            print("2. Modificar Vacuna")
            print("3. Eliminar Vacuna")
            print("4. Mostrar Vacunas")
            print("5. Salir")

            choice = input("Seleccione una opción: ")

            if choice == "1":
                self.add_vaccine()
            elif choice == "2":
                self.modify_vaccine()
            elif choice == "3":
                self.delete_vaccine()
            elif choice == "4":
                self.display_vaccines()
            elif choice == "5":
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    def add_vaccine(self):
        try:
            id = int(input("Ingrese el ID de la vacuna: "))
            name = input("Ingrese el nombre de la vacuna: ")
            application_date = input("Ingrese la fecha de aplicación (DD/MM/AAAA): ")
            self.controller.add_vaccine(id, name, application_date)
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

    def modify_vaccine(self):
        try:
            id = int(input("Ingrese el ID de la vacuna a modificar: "))
            new_name = input("Ingrese el nuevo nombre de la vacuna: ")
            new_application_date = input("Ingrese la nueva fecha de aplicación (DD/MM/AAAA): ")
            self.controller.modify_vaccine(id, new_name, new_application_date)
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

    def delete_vaccine(self):
        try:
            id = int(input("Ingrese el ID de la vacuna a eliminar: "))
            self.controller.delete_vaccine(id)
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

    def display_vaccines(self):
        self.controller.display_vaccines()