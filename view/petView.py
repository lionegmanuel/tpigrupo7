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
            user_response = input('¿Desea Asignar un ID Personalizado? (S/N)')
            if user_response.lower() == 's':
                id = int(input("Ingrese el ID de la mascota: "))
            else: id = 0
            name = input("Ingrese el nombre de la mascota: ")
            specie = input("Ingrese la especie de la mascota: ")
            breed = input("Ingrese la raza de la mascota: ")
            owner_name = input("Ingrese el nombre del propietario: ")
            owner_lastname = input("Ingrese el apellido del propietario: ")
            self.controller.add_pet(id, name, specie, breed, owner_name, owner_lastname)
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

    def modify_pet(self):
        try:
            id = int(input("Ingrese el ID de la mascota a modificar: "))
            new_name = input("Ingrese el nuevo nombre de la mascota: ")
            new_specie = input("Ingrese la nueva especie de la mascota: ")
            new_breed = input("Ingrese la nueva raza de la mascota: ")
            self.controller.modify_pet(id, new_name, new_specie, new_breed)
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

    def delete_pet(self):
        try:
            id = int(input("Ingrese el ID de la mascota a eliminar: "))
            self.controller.delete_pet(id)
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

    def display_pets(self):
        self.controller.display_pets()

