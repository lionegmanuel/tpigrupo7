from controller.personController import PersonController
class PersonView:
    def __init__(self):
        self.controller = PersonController()
        
    def show_main_menu(self):
        while True:
            print("\n---Gestión de Mascotas---\n")
            print("1. Agregar Persona")
            print("2. Modificar Persona")
            print("3. Eliminar Persona")
            print("4. Mostrar Personas")
            print("5. Salir")

            choice = input("Seleccione una Opción: ")

            if choice == "1":
                self.add_person()
            elif choice == "2":
                self.modify_person()
            elif choice == "3":
                self.delete_person()
            elif choice == "4":
                self.display_persons()
            elif choice == "5":
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    def add_person(self):
        try:
            person_name = input("Nombre de la nueva persona: ")
            person_lastname = input("Apellido de la nueva persona: ")
            type_of_person = input("Tipo de Persona (Cliente / Veterinario): ")
            if type_of_person.lower() == 'cliente': type_of_person = 'client'
            elif type_of_person.lower() == 'veterinario': type_of_person = 'veterinarian'
            else: type_of_person = ''
            self.controller.add_person(person_name, person_lastname, type_of_person)
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

    def modify_person(self):
        try:
            self.controller.display_persons()
            print('')
            person_id = int(input("ID de la persona a modificar: "))
            new_name = input("Nuevo nombre de la persona: ")
            new_lastname = input("Nuevo apellido de la persona: ")
            self.controller.modify_person(person_id, new_name, new_lastname)
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

    def delete_person(self):
        try:
            self.controller.display_persons()
            print('')
            person_id = int(input("¿Qué Persona es la que Desea Eliminar?\n\tID: "))
            self.controller.delete_person(person_id)
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

    def display_persons(self):
        self.controller.display_persons()
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