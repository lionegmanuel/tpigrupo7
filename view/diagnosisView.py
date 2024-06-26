from controller.diagnosisController import DiagnosisController

class DiagnosisView:
    def __init__(self):
        self.controller = DiagnosisController()

    def show_main_menu(self):
        while True:
            print("\n---Gestión de Diagnósticos---\n")
            print("1. Agregar Diagnóstico")
            print("2. Modificar Diagnóstico")
            print("3. Eliminar Diagnóstico")
            print("4. Mostrar Todos los Diagnósticos")
            print("5. Salir")

            choice = input("Seleccione una Opción: ")

            if choice == "1":
                self.add_diagnosis()
            elif choice == "2":
                self.modify_diagnosis()
            elif choice == "3":
                self.delete_diagnosis()
            elif choice == "4":
                self.display_diagnoses()
            elif choice == "5":
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    def add_diagnosis(self):
        try:
            pet_name = self.validate_alphabetic_input("Nombre de la mascota: ")
            information = self.validate_alphabetic_input("Información del diagnóstico: ")
            self.controller.add_diagnosis(pet_name, information)
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

    def modify_diagnosis(self):
        try:
            self.controller.display_diagnoses()
            print('')
            diagnosis_id = self.validate_integer_input("ID del diagnóstico a modificar: ")
            new_name = self.validate_alphabetic_input("Nuevo nombre de la mascota (deje en blanco para no modificar): ")
            new_information = self.validate_alphabetic_input("Nueva información del diagnóstico (deje en blanco para no modificar): ")
            self.controller.modify_diagnosis(diagnosis_id, new_name, new_information)
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

    def delete_diagnosis(self):
        try:
            self.controller.display_diagnoses()
            print('')
            diagnosis_id = self.validate_integer_input("ID del diagnóstico a eliminar: ")
            self.controller.delete_diagnosis(diagnosis_id)
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

    def display_diagnoses(self):
        self.controller.display_diagnoses()
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