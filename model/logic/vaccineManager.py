import os
import json
from model.classes.Vaccine import Vaccine

class VaccineManager:
    def __init__(self):
        self.data_dir = os.path.join(os.getcwd(), 'data')
        self.file_path = os.path.join(self.data_dir, 'vaccines.json')
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        self.vaccines = self.load_vaccines_from_file()

    def load_vaccines_from_file(self):
        current_vaccines = []
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                vaccines_data = json.load(file)
                for current_vaccine in vaccines_data:
                    vaccine = Vaccine(
                        current_vaccine['id'],
                        current_vaccine['name'],
                        current_vaccine['applicationDate']
                    )
                    current_vaccines.append(vaccine)
        return current_vaccines

    def save_vaccine_to_json(self, vaccine):
        vaccines_data = []
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                vaccines_data = json.load(file)

        updated = False
        for current_vaccine in vaccines_data:
            if current_vaccine['id'] == vaccine.get_id():
                current_vaccine['name'] = vaccine.get_name()
                current_vaccine['applicationDate'] = vaccine.get_application_date()
                updated = True
                break
        
        if not updated:
            vaccine_data = {
                'id': vaccine.get_id(),
                'name': vaccine.get_name(),
                'applicationDate': vaccine.get_application_date()
            }
            vaccines_data.append(vaccine_data)

        with open(self.file_path, 'w') as file:
            json.dump(vaccines_data, file, indent=4)

    def delete_vaccine_from_file(self, vaccine_id):
        vaccines_data = []
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                vaccines_data = json.load(file)
        vaccine_found = False
        for current_vaccine in vaccines_data:
            if current_vaccine['id'] == vaccine_id:
                vaccines_data.remove(current_vaccine)
                vaccine_found = True
                break

        with open(self.file_path, 'w') as file:
            json.dump(vaccines_data, file, indent=4)

    def add_vaccine(self, id, name, applicationDate):
        if self.find_vaccine_by_id(id):
            print("\nLa vacuna ya está registrada.\n")
            return
        newVaccine = Vaccine(id, name, applicationDate)
        self.vaccines.append(newVaccine)
        self.save_vaccine_to_json(newVaccine)
        print("\nVacuna registrada correctamente.\n")

    def modify_vaccine(self, id, newName, newApplicationDate):
        vaccine = self.find_vaccine_by_id(id)
        if vaccine:
            if newName != vaccine.get_name():
                vaccine.set_name(newName)
            if newApplicationDate != vaccine.get_application_date():
                vaccine.set_application_date(newApplicationDate)
            self.save_vaccine_to_json(vaccine)
            print("\nVacuna modificada correctamente.\n")
        else:
            print("\nNo se encontró la vacuna.\n")

    def delete_vaccine(self, id):
        vaccine = self.find_vaccine_by_id(id)
        if vaccine:
            self.vaccines.remove(vaccine)
            self.delete_vaccine_from_file(id)
            print("\nVacuna eliminada correctamente.\n")
        else:
            print("\nNo se encontró la vacuna.\n")

    def find_vaccine_by_id(self, id):
        for vaccine in self.vaccines:
            if vaccine.get_id() == id:
                return vaccine
        return None

    def display_vaccines(self):
        if not self.vaccines:
            print('\nNo hay Vacunas Registradas.\n')
        else:
            print('\nListado de Vacunas Registradas:')
            for vaccine in self.vaccines:
                print(f'\n{vaccine}')
