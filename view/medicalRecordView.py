from controller.medicalRecordController import MedicalRecordController
from controller.diagnosisController import DiagnosisController
from controller.treatmentController import TreatmentController
from controller.petController import PetController
from view.treatmentView import TreatmentView

class MedicalRecordView:
    def __init__(self):
        self.medical_record_controller = MedicalRecordController()
        self.diagnosis_controller = DiagnosisController()
        self.treatment_controller = TreatmentController()
        self.pet_controller = PetController()
        self.treatment_view = TreatmentView()

    def show_main_menu(self):
        while True:
            print("\n---Gestión de Fichas Médicas---\n")
            print("1. Agregar Ficha Médica")
            print("2. Buscar Ficha Médica por ID")
            print("3. Mostrar Todas las Fichas Médicas")
            print("4. Mostrar Fichas Médicas por Mascota")
            print("5. Eliminar Ficha Médica")
            print('6. Salir')

            choice = input("Seleccione una Opción: ")

            if choice == "1":
                self.add_medical_record()
            elif choice == "2":
                self.find_medical_record_by_id()
            elif choice == "3":
                self.display_all_medical_records()
            elif choice == "4":
                self.display_medical_records_by_pet()
            elif choice == '5':
                self.delete_medical_record()
            elif choice == "6":
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    def add_medical_record(self):
        try:
            pet_id = int(input("ID de la mascota para agregar la ficha médica: "))
            pet = self.pet_controller.find_by_id(pet_id)
            if pet:
                consult_date = input("Fecha de la consulta (formato DD/MM/AAAA): ")
                diagnosis = input("Diagnóstico (Descripción): ")
                self.diagnosis_controller.add_diagnosis(pet.get_name(), diagnosis)
                treatment_register = False
                print('---')
                treatments = self.treatment_controller.display_treatments()
                if treatments:
                    current_select = input('¿Desea Seleccionar un Tratamiento Registrado? (S/N)\n\t¡En caso de indicar que no, se procederá con el registro de un tratamiento nuevo: ')
                    if current_select.lower() == 's':
                        treatment_id = int(input("ID del tratamiento a asignar: "))
                        new_treatment = self.treatment_controller.find_by_id(treatment_id) if treatment_id else None
                    else: treatment_register = True
                else: treatment_register = True
                if treatment_register:
                    print('\nProceso de Registro de un Tratamiento Nuevo para asignar a la Ficha Médica.\n')
                    new_treatment = self.treatment_view.add_treatment()
                    current_diagnosis = self.diagnosis_controller.find(pet.get_name())
                self.medical_record_controller.add_medical_record(pet, consult_date, current_diagnosis, new_treatment)
            else:
                print("No se encontró la mascota con el ID especificado.")
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

    def find_medical_record_by_id(self):
        try:
            record_id = int(input("ID de la ficha médica a buscar: "))
            record = self.medical_record_controller.find_medical_record(record_id)
            if record:
                print('\nResultado:\n')
                print(record)
            else: print('\nLa Ficha Médica Solicitada no fue Encontrada. ')
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

    def display_all_medical_records(self):
        try:
            self.medical_record_controller.display_medical_records()
        except ValueError:
            print('Error al Listar las Fichas Médicas.')
    def display_medical_records_by_pet(self):
        try:
            pet_id = int(input("ID de la mascota para mostrar sus fichas médicas: "))
            pet = self.pet_controller.find_by_id(pet_id)
            if pet:
                pet_records = self.medical_record_controller.get_pet_medical_records(pet)
                if not pet_records:
                    print("\nNo hay fichas médicas registradas para esta mascota.\n")
                else:
                    print('\nResultado: ')
                    for record in pet_records:
                        print(record)
            else:
                print("\nNo se encontró la Mascota Buscada.\n")
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")
    def delete_medical_record(self):
        try:
            print('')
            self.medical_record_controller.display_medical_records()
            id = int(input('\nIngrese el ID de la Ficha Médica a Eliminar: '))
            self.medical_record_controller.delete_medical_record(id)

        except ValueError:
            print("Entrada inválida. Intente nuevamente.")
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