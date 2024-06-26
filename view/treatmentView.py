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
            name = self.validate_alphabetic_input("Ingrese el nombre del tratamiento: ")
            description = self.validate_alphabetic_input("Ingrese la descripción del tratamiento: ")
            duration = self.validate_integer_input("Ingrese la duración del tratamiento (Días Totales): ")
            is_require_vaccine = input('¿Requiere Vacunar? (En caso de Incerteza o Indecisión, dejar en Blanco): ')
            new_treatment = self.controller.add_treatment(name, description, duration, True if is_require_vaccine.lower() == 'si' else None)
            return new_treatment
        except ValueError:
            print("\nEntrada inválida. Intente nuevamente.\n")

    def modify_treatment(self):
        try:
            self.controller.display_treatments()
            print('')
            id = self.validate_integer_input("Ingrese el ID del tratamiento a modificar: ")
            is_exists_treatment = self.controller.find_by_id(id)
            if is_exists_treatment:
                new_name = self.validate_alphabetic_input("Ingrese el nuevo nombre del tratamiento: ")
                new_description = self.validate_alphabetic_input("Ingrese la nueva descripción del tratamiento: ")
                new_duration = self.validate_integer_input("Ingrese la nueva duración del tratamiento (en días): ")
                current_require_vaccine = self.validate_alphabetic_input('En cuanto a la Vacunación, ¿Es Requerida?: ')
                self.controller.modify_treatment(new_name, new_description, new_duration, True if current_require_vaccine.lower() == 'si' else None, id)
            else: print('El Tratamiento Buscadoo No está Registrado en el Sistema.')
        except ValueError:
            print("\nEntrada inválida. Intente nuevamente.\n")

    def delete_treatment(self):
        try:
            id = self.validate_integer_input("Ingrese el ID del tratamiento a eliminar: ")
            self.controller.delete_treatment(id)
        except ValueError:
            print("\nEntrada inválida. Intente nuevamente.\n")

    def display_treatments(self):
        self.controller.display_treatments()
    def validate_integer_input(self, prompt):
            while True:
                try:
                    input = self.validate_non_empty_input(prompt)
                    return int(input)
                except ValueError:
                    print("\n¡ERROR!\n\tIngrese un Valor Correcto.\n ")

    def validate_alphabetic_input(self, prompt):
        while True:
            input = self.validate_non_empty_input(prompt)
            if input.replace(" ", "").isalpha():
                return input
            else:
                print("\nEntrada inválida. \n\tPor favor, Ingrese Carácteres Válidos.\n")
    def validate_non_empty_input(self, prompt):
        while True:
            input_str = input(prompt)
            if input_str.strip():
                return input_str
            else:
                print("\n¡ERROR!\nCampo Vacío.\n\tIngrese el Valor correspondiente solicitado.\n")