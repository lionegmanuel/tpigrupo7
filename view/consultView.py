from controller.consultController import ConsultController
from datetime import datetime
from model.classes.Veterinarian import Veterinarian
from model.classes.Diagnosis import Diagnosis
from model.classes.Treatment import Treatment
from model.classes.Pet import Pet
from model.classes.Breed import Breed
from model.classes.Client import Client
class ConsultView:
    def __init__(self):
        self.controller = ConsultController()

    def show_main_menu(self):
        while True:
            print("\n-- Gestión de Consultas --")
            print("1. Agregar Consulta")
            print("2. Buscar Consulta por ID")
            print("3. Eliminar Consulta")
            print("4. Mostrar Consultas")
            print("5. Salir")

            choice = input("Seleccione una opción: ")

            if choice == "1":
                self.add_consult()
            elif choice == "2":
                self.find_consult_by_id()
            elif choice == "3":
                self.delete_consult()
            elif choice == "4":
                self.display_consults()
            elif choice == "5":
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    def add_consult(self):
        try:
            pet_name = input("Ingrese el nombre de la Mascota: ")
            breed_name = input('Ingrese el nombre de la Raza de la Mascota: ')
            veterinarian_name = input("Ingrese el nombre del veterinario: ")
            veterinaria_specialization = input('Especialización del Veterinario/a (En caso de no contar, dejar en Blanco): ')
            print('Ingrese los siguientes Datos del Dueño de la Mascota (Nombre, Apellido y Teléfono de Contacto):')
            owner_name = input('\t=> ')
            owner_last_name = input('\t=> ')
            owner_phone = input('\t=> ')
            diagnosis_information = input(f'Ingrese a Continuación la Información y Datos del Diagnóstico correspondiente a la Mascota "{pet_name}": \n\t=> ')
            treatment_name = input('Ingrese el Nombre del Tratamiento a Asignar: ')
            treatment_description = input('Descripción mas Detallada del Tratamiento: ')
            treatment_duration = int(input('Duración Total del Tratamiento: (Días) '))
            is_require_vaccine = '0'
            while(is_require_vaccine.lower() != 's' or is_require_vaccine.lower() != 'n'):
                is_require_vaccine = input('¿El tratamiento requiere Vacunación? (S/N): ')
                if (is_require_vaccine.lower() == 's'):
                    response = '0'
                    while response.lower() != 's' or response.lower() != 'n':
                        response = input('El tratamiento requiere mas de una Vacuna? (S/N): ')
                        if (response.lower() == 's'):
                            vaccines = [] #list of vaccines object type
                            amount_of_vaccines = int(input('Ingrese la Cantidad Total de Vacunas necesarias para este Tratamiento: '))
                            print('')
                            self.controller.vaccines_petition()
                            print(f'A continuación, ingrese el ID correspondiente de la vacuna a Registrar para dicho Tratamiento, para un total de "{amount_of_vaccines}" vacunas.\n')
                            for c in range(amount_of_vaccines):
                                current_id_vaccine = int(input(f'Vacuna N° {c+1} (ID): '))
                                current_result = self.controller.vaccines_find(current_id_vaccine)
                                while not current_result:
                                    current_id_vaccine = input(f'¡ERROR!\nLa Vacuna Solicitada no Está Registrada.\nVacuna N° {c+1} (ID): ')
                                vaccines.append(current_result)
                        break
                break    

            owner = Client(owner_name, owner_last_name, owner_phone)
            reason = input("Ingrese el motivo de la consulta: ")
            breed = Breed(breed_name)
            pet = Pet(name=pet_name, specie="Perro", breed=breed, owner=owner)
            veterinarian = Veterinarian(veterinarian_name, "-", "General" if veterinaria_specialization == '' else veterinaria_specialization)
            diagnosis = Diagnosis(pet_name, diagnosis_information)
            treatment = Treatment(treatment_name, treatment_description, treatment_duration, 
                                  None if is_require_vaccine.lower() == 'n' else is_require_vaccine)
            self.controller.addConsult(pet, veterinarian, diagnosis, treatment, vaccines, reason)
        except Exception as e:
            print(f"Error al agregar consulta: {e}")

    def find_consult_by_id(self):
        try:
            consult_id = int(input('Ingrese el ID de la consulta que desesa buscar: '))
            #validar ID
            consult_result = self.controller.find_consult_by_id(consult_id)
            if consult_result: 
                print(f'\nDatos de la Consulta Solicitada:\n📌\n{consult_result}\n📌') 
            else:
                print('\nLa Consulta Buscada No se encuentra Registrada en el Sistema.')
        except Exception as e:
            print(f"Error al buscar la consulta consulta: {e}")

    def delete_consult(self):
        try:
            consult_id = int(input("Ingrese el ID de la consulta a eliminar: "))
            self.controller.deleteConsult(consult_id)
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

    def display_consults(self):
        self.controller.displayConsults()