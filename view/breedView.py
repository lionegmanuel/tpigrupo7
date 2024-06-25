from controller.breedController import BreedController

class BreedView:
    def __init__(self):
        self.controller = BreedController()

    def show_main_menu(self):
        while True:
            print("\n---Gestión de Razas---\n")
            print("1. Agregar Raza")
            print("2. Modificar Raza")
            print("3. Eliminar Raza")
            print("4. Mostrar Todas las Razas")
            print("5. Salir")

            choice = input('Seleccione una Opción: ')

            if choice == "1":
                self.add_breed()
            elif choice == "2":
                self.modify_breed()
            elif choice == "3":
                self.delete_breed()
            elif choice == "4":
                self.display_breeds()
            elif choice == "5": break
            else:
                print("Opción inválida. Intente nuevamente.")

    def add_breed(self):
        try:
            breed_name = input('Nombre de la Raza: ')
            self.controller.add_breed(breed_name)
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

    def modify_breed(self):
        try:
            self.controller.display_breeds()
            breed_id = int(input("ID de la raza a modificar: "))
            new_name = input("Nuevo nombre de la raza: ")
            self.controller.modify_breed(breed_id, new_name)
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

    def delete_breed(self):
        try:
            breed_id = int(input("ID de la raza a eliminar: "))
            self.controller.delete_breed(breed_id)
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

    def display_breeds(self):
        self.controller.display_breeds()
