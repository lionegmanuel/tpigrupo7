from controller.treatmentController import TreatmentController

class TreatmentView:
    def __init__(self):
        self.controller = TreatmentController()

    def show_main_menu(self):
        while True:
            print("\n---Gestión de Tratamientos---\n")
            print("1. Agregar Tratamiento")
            print("2. Modificar Tratamiento")
            print("3. Eliminar Tratamiento")
            print("4. Mostrar Tratamientos")
            print("5. Salir")

            choice = input("Seleccione una opción: ")

            if choice == "1":
                self.add_treatment()
            elif choice == "2":
                self.modify_treatment()
            elif choice == "3":
                self.delete_treatment()
            elif choice == "4":
                self.display_treatments()
            elif choice == "5":
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    def add_treatment(self):
        try:
            name = input("Ingrese el nombre del tratamiento: ")
            description = input("Ingrese la descripción del tratamiento: ")
            duration = int(input("Ingrese la duración del tratamiento (Días Totales): "))
            is_require_vaccine = input('¿Requiere Vacunar? (En caso de Incerteza o Indecisión, dejar en Blanco): ')
            new_treatment = self.controller.add_treatment(name, description, duration, True if is_require_vaccine.lower() == 'si' else None)
            return new_treatment
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

    def modify_treatment(self):
        try:
            self.controller.display_treatments()
            print('')
            id = int(input("Ingrese el ID del tratamiento a modificar: "))
            is_exists_treatment = self.controller.find_by_id(id)
            if is_exists_treatment:
                new_name = input("Ingrese el nuevo nombre del tratamiento: ")
                new_description = input("Ingrese la nueva descripción del tratamiento: ")
                new_duration = int(input("Ingrese la nueva duración del tratamiento (en días): "))
                current_require_vaccine = input('En cuanto a la Vacunación, ¿Es Requerida?: ')
                self.controller.modify_treatment(new_name, new_description, new_duration, True if current_require_vaccine.lower() == 'si' else None, id)
            else: print('El Tratamiento Buscadoo No está Registrado en el Sistema.')
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

    def delete_treatment(self):
        try:
            id = int(input("Ingrese el ID del tratamiento a eliminar: "))
            self.controller.delete_treatment(id)
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

    def display_treatments(self):
        self.controller.display_treatments()
