from controller.petController import PetController
from controller.personController import PersonController

class PetView:
    def __init__(self):
        self.controller = PetController()

    def show_main_menu(self):
        while True:
            print("\n---Gestión de Mascotas---\n")
            print("1. Agregar Mascota")
            print("2. Modificar Mascota")
            print("3. Eliminar Mascota")
            print("4. Mostrar Mascotas")
            print("5. Salir")

            choice = input("Seleccione una Opción: ")

            if choice == "1":
                self.add_pet()
            elif choice == "2":
                self.modify_pet()
            elif choice == "3":
                self.delete_pet()
            elif choice == "4":
                self.display_pets()
            elif choice == "5":
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    def add_pet(self):
        try:
            while True:
                user_response = self.validate_alphabetic_input('¿Desea Asignar un ID Personalizado? (S/N)\n\t=> ').upper()
                if user_response in ['S', 'N']:
                    break
                else:
                    print("Respuesta inválida.\nIngrese una Respuesta Correcta.")
            if user_response.lower() == 's':
                id = self.validate_integer_input("Ingrese el ID de la mascota: ")
            else: id = 0
            name = self.validate_alphabetic_input("Ingrese el nombre de la mascota: ")
            if self.controller.find_by_name(name) is not None:
                print(f'\nYa hay una Mascota con el nombre "{name}" registrada en el Sistema.\n')
                return
            specie = self.validate_alphabetic_input("Ingrese la especie de la mascota: ")
            breed = self.validate_alphabetic_input("Ingrese la raza de la mascota: ")
            owner_name = self.validate_alphabetic_input("Ingrese el nombre del propietario: ")
            owner_lastname = self.validate_alphabetic_input("Ingrese el apellido del propietario: ")
            self.controller.add_pet(id, name, specie, breed, owner_name, owner_lastname)
        except ValueError:
            print("\nEntrada inválida. Intente nuevamente.\n")

    def modify_pet(self):
        try:
            id = self.validate_integer_input("Ingrese el ID de la mascota a modificar: ")
            new_name = self.validate_alphabetic_input("Ingrese el nuevo nombre de la mascota: ")
            new_specie = self.validate_alphabetic_input("Ingrese la nueva especie de la mascota: ")
            new_breed = self.validate_alphabetic_input("Ingrese la nueva raza de la mascota: ")
            self.controller.modify_pet(id, new_name, new_specie, new_breed)
        except ValueError:
            print("\nEntrada inválida. Intente nuevamente.\n")

    def delete_pet(self):
        try:
            print('')
            self.controller.display_pets()
            print('')
            id = self.validate_integer_input("Ingrese el ID de la mascota a eliminar: ")
            self.controller.delete_pet(id)
        except ValueError:
            print("\nEntrada inválida. Intente nuevamente.\n")

    def display_pets(self):
        self.controller.display_pets()

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