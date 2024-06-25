import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'controller'))

from view.navigationView import NavigationView
from view.breedView import BreedView
from view.petView import PetView
from view.diagnosisView import DiagnosisView
from view.personView import PersonView
from view.treatmentView import TreatmentView
from view.vaccineView import VaccineView
from view.medicalRecordView import MedicalRecordView
from view.appointmentView import AppointmentView

from view.navigationView import NavigationView
from controller.breedController import BreedController
from controller.petController  import PetController
from controller.diagnosisController import DiagnosisController
from controller.personController import PersonController
from controller.treatmentController import TreatmentController
from controller.vaccineController import VaccineController
from controller.medicalRecordController import MedicalRecordController
from model.logic.navigationManager import NavigationModel



class NavigationController:
    def __init__(self, view):
        self.navigationView = NavigationView()
        self.navigationModel = NavigationModel()
        self.breedController = BreedController()
        self.petController = PetController()
        self.diagnosisController = DiagnosisController()
        self.personController = PersonController()
        self.treatmentController = TreatmentController()
        self.vaccineController = VaccineController()
        self.medicalRecordController = MedicalRecordController()

        self.breedView = BreedView()
        self.petView = PetView()
        self.diagnosisView = DiagnosisView()
        self.personView = PersonView()
        self.treatmentView = TreatmentView()
        self.vaccineView = VaccineView()
        self.medicalRecordView = MedicalRecordView()

    def displayMenu(self):
        menu_options = self.navigationModel.get_menu_options()
        self.manage_navigation(menu_options)

    def manage_navigation(self, menu_options):
        while True:
            choice = self.navigationView.show_main_menu(menu_options)
            if choice in menu_options:
                self.internal_option_management(choice)
            else:
                self.navigationView.showInvalidOptionMessage()

    def exit(self):
        self.navigationView.showExitMessage()
        sys.exit(0)
    def internal_option_management(self, choice):
        match choice:
            case '1':
                self.manageBreeds() 
            case '2':
                self.managePets()
            case '3':
                self.managePersons() 
            case '4':
                self.manageDiagnosis()
            case '5':
                self.manageTreatments()
            case '6':
                self.manageVaccine()
            case '7':
                self.manageMedicalRecord()
            case '8':
                self.manageConsults()
            case '0':
                self.exit()    
    def manageBreeds(self):
        self.navigationView.show_breed_menu()
    def managePets(self):
        self.navigationView.show_pet_menu()
    def manageDiagnosis(self):
        self.navigationView.show_diagnosis_menu()
    def managePersons(self):
        self.navigationView.show_person_menu()
    def manageTreatments(self):
        self.navigationView.show_treatment_menu()
    def manageVaccine(self):
        self.navigationView.show_vaccine_menu()
    def manageMedicalRecord(self):
        self.navigationView.show_medical_record_menu()
    def manageAppointment(self):
        self.navigationView.show_appointment_menu()
    def manageConsults(self):
        self.navigationView.show_consult_menu()