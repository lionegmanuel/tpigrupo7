# navigation_view.py
from view.breedView import BreedView
from view.petView import PetView
from view.diagnosisView import DiagnosisView
from view.personView import PersonView
from view.treatmentView import TreatmentView
from view.vaccineView import VaccineView
from view.medicalRecordView import MedicalRecordView
from view.consultView import ConsultView
from view.appointmentView import AppointmentView

class NavigationView:

    def __init__(self):
        self.breed_view = BreedView()
        self.pet_view = PetView()
        self.diagnosis_view = DiagnosisView()
        self.person_view = PersonView()
        self.treatment_view = TreatmentView()
        self.vaccine_view = VaccineView()
        self.medical_record_view = MedicalRecordView()
        self.appointment_view = AppointmentView()
        self.consult_view = ConsultView()

    def show_main_menu(self, options):
        print("\n---MENÚ---\n")
        for key, value in options.items():
            print(f"{key}: {value}")
        choice = input("\n=> ")
        return choice


    def showInvalidOptionMessage(self):
        print("\nOpción inválida. Por favor, ingrese un Número Válido.\n")

    def showExitMessage(self):
        print("---SESIÓN DE EJECUCIÓN FINALIZADA---")

    def showMessage(self, message):
        print(message)
    def show_breed_menu(self):
        self.breed_view.show_main_menu()
    def show_pet_menu(self):
        self.pet_view.show_main_menu()
    def show_diagnosis_menu(self):
        self.diagnosis_view.show_main_menu()
    def show_person_menu(self):
        self.person_view.show_main_menu()
    def show_treatment_menu(self):
        self.treatment_view.show_main_menu()
    def show_vaccine_menu(self):
        self.vaccine_view.show_main_menu()
    def show_medical_record_menu(self):
        self.medical_record_view.show_main_menu()
    def show_appointment_menu(self):
        self.appointment_view.show_main_menu()
    def show_consult_menu(self):
        self.consult_view.show_main_menu()

    def getInput(self, prompt):
        return input(prompt)
