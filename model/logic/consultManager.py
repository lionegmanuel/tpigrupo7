import os
import sys
import json
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'classes'))

from model.classes.Consult import Consult
from model.classes.Pet import Pet
from model.classes.Veterinarian import Veterinarian
from model.classes.Diagnosis import Diagnosis
from model.classes.Treatment import Treatment
from model.logic.vaccineManager import VaccineManager
from model.classes.Breed import Breed
from model.classes.Person import Person

class ConsultManager:
    def __init__(self):
        self.data_dir = os.path.join(os.getcwd(), 'data')
        self.file_path = os.path.join(self.data_dir, 'consults.json')
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        self.consults = self.load_consults_from_file()
        self.vaccine_manager = VaccineManager()

    def load_consults_from_file(self):
        current_consults = []
        max_id = 0
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                consults_data = json.load(file)
                for current_consult in consults_data:
                    breed = Breed(current_consult['pet']['breed']) 
                
                    owner_data = current_consult['pet']['owner'] 
                    owner = Person(  
                        owner_data['name'],  
                        owner_data['last_name'],  
                        owner_data['type'],  
                        owner_data['contact_data'],  
                        owner_data['id']  
                    )  
                    pet_data = current_consult['pet']  
                    pet = Pet(  
                        pet_data['name'],  
                        pet_data['specie'],  
                        breed,  
                        owner,  
                        pet_data['id']  
                    )  
                    
                    veterinarian_data = current_consult['veterinarian']
                    veterinarian = Veterinarian(
                        veterinarian_data['name'],
                        veterinarian_data['last_name'],
                        veterinarian_data['specialization'],
                        veterinarian_data['id']
                    )
                    
                    diagnosis_data = current_consult['diagnosis']
                    diagnosis = Diagnosis(
                        diagnosis_data['pet_name'],
                        diagnosis_data['information'],
                        diagnosis_data['id']
                    )
                    
                    treatment_data = current_consult['treatment']
                    treatment = Treatment(
                        treatment_data['name'],
                        treatment_data['description'],
                        treatment_data['duration'],
                        treatment_data['is_require_vaccine'],
                        treatment_data['id']
                    )
                    consult = Consult(
                        pet,
                        veterinarian,
                        diagnosis,
                        treatment,
                        current_consult['vaccines'],
                        current_consult['reason'],
                        current_consult['id']
                    )
                    current_consults.append(consult)
                    if current_consult['id'] > max_id:
                        max_id = current_consult['id']
        Consult.id = max_id
        return current_consults

    def save_consult_to_json(self, consult):
        consults_data = []
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                consults_data = json.load(file)

        updated = False
        for current_consult in consults_data:
            if current_consult['id'] == consult.get_id():
                current_consult['pet'] = consult.get_pet().to_dict()
                current_consult['veterinarian'] = consult.get_veterinarian().to_dict()
                current_consult['diagnosis'] = consult.get_diagnosis().to_dict()
                current_consult['treatment'] = consult.get_treatment().to_dict()
                current_consult['vaccines'] = consult.get_vaccines()
                current_consult['reason'] = consult.get_reason()
                updated = True
                break

        if not updated:
            consult_data = {
                'id': consult.get_id(),
                'pet': consult.get_pet().to_dict(),
                'veterinarian': consult.get_veterinarian().to_dict(),
                'diagnosis': consult.get_diagnosis().to_dict(),
                'treatment': consult.get_treatment().to_dict(),
                'vaccines': consult.get_vaccines(),
                'reason': consult.get_reason()
            }
            consults_data.append(consult_data)

        with open(self.file_path, 'w') as file:
            json.dump(consults_data, file, indent=4)

    def delete_consult_from_file(self, consult):
        consults_data = []
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                consults_data = json.load(file)
        consult_found = False
        for current_consult in consults_data:
            if current_consult['id'] == consult.get_id():
                consults_data.remove(current_consult)
                consult_found = True
                break

        with open(self.file_path, 'w') as file:
            json.dump(consults_data, file, indent=4)

    def addConsult(self, pet, veterinarian, diagnosis, treatment, vaccines, reason):
        vaccines_data = []
        for vaccine in vaccines:
            vaccines_data.append(vaccine.get_name())
        new_consult = Consult(pet, veterinarian, diagnosis, treatment, vaccines_data, reason)
        if self.findConsultById(new_consult.get_id()):
            print(f"\nUna consulta con el ID {new_consult.get_id()} está registrada en el Sistema.\n")
            return
        self.consults.append(new_consult)
        self.save_consult_to_json(new_consult)
        print("\nConsulta registrada correctamente.\n")
        return new_consult


    def deleteConsult(self, consult_id):
        consult = self.find_consult_by_id(consult_id)
        if consult:
            self.consults.remove(consult)
            self.delete_consult_from_file(consult)
            print("\nConsulta eliminada correctamente.\n")
            return
        print("\nNo se encontró la consulta.\n")

    def find_consult_by_id(self, consult_id):
        for consult in self.consults:
            if consult.get_id() == consult_id:
                return consult
        return None

    def displayConsults(self):
        if not self.consults:
            print("\nNo hay Consultas Registradas.")
        else:
            print("\nListado de Consultas Registradas:\n")
            for consult in self.consults:
                print(f'\n{consult}')
    def vaccines_petition(self):
        return self.vaccine_manager.display_vaccines()
    def vaccines_find(self, id):
        return self.vaccine_manager.find_vaccine_by_id(id)