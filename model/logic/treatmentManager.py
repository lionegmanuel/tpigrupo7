import os
import json
from model.classes.Treatment import Treatment

class TreatmentManager:
    def __init__(self):
        self.data_dir = os.path.join(os.getcwd(), 'data')
        self.file_path = os.path.join(self.data_dir, 'treatments.json')
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        self.treatments = self.load_treatments_from_file()

    def load_treatments_from_file(self):
        current_treatments = []
        max_id = 0
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                treatments_data = json.load(file)
                for current_treatment in treatments_data:
                    treatment = Treatment(
                        current_treatment['name'],
                        current_treatment['description'],
                        current_treatment['duration'],
                        current_treatment['require_vaccine'],
                        current_treatment['id']
                    )
                    current_treatments.append(treatment)
                    if current_treatment['id'] > max_id:
                        max_id = current_treatment['id']
        Treatment.id = max_id
        return current_treatments

    def save_treatment_to_json(self, treatment):
        treatments_data = []
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                treatments_data = json.load(file)

        updated = False
        for current_treatment in treatments_data:
            if current_treatment['id'] == treatment.get_id():
                current_treatment['name'] = treatment.get_name()
                current_treatment['description'] = treatment.get_description()
                current_treatment['duration'] = treatment.get_duration()
                current_treatment['require_vaccine'] = treatment.get_require_vaccine()
                updated = True
                break
        
        if not updated:
            treatment_data = {
                'id': treatment.get_id(),
                'name': treatment.get_name(),
                'description': treatment.get_description(),
                'duration': treatment.get_duration(),
                'require_vaccine' : treatment.get_require_vaccine()
            }
            treatments_data.append(treatment_data)

        with open(self.file_path, 'w') as file:
            json.dump(treatments_data, file, indent=4)

    def delete_treatment_from_file(self, treatment_id):
        treatments_data = []
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                treatments_data = json.load(file)
        treatment_found = False
        for current_treatment in treatments_data:
            if current_treatment['id'] == treatment_id:
                treatments_data.remove(current_treatment)
                treatment_found = True
                break

        with open(self.file_path, 'w') as file:
            json.dump(treatments_data, file, indent=4)

    def add_treatment(self, name: str, description: str, duration: int, is_require_vaccine):
        if self.find_treatment_by_name(name):
            print("\nEl tratamiento ya está registrado.\n")
            return
        new_treatment = Treatment(name, description, duration, is_require_vaccine)
        self.treatments.append(new_treatment)
        self.save_treatment_to_json(new_treatment)
        print("\nTratamiento registrado correctamente.\n")
        return new_treatment

    def modify_treatment(self, new_name: str, new_description: str, new_duration: int, require_vaccine, id : int):
        treatment = self.find_treatment_by_id(id)
        if treatment:
            if new_name and new_name != treatment.get_name():
                treatment.set_name(new_name)
            if new_description and new_description != treatment.get_description():
                treatment.set_description(new_description)
            if new_duration and new_duration != treatment.get_duration():
                treatment.set_duration(new_duration)
            if require_vaccine and ((require_vaccine == True and treatment.get_require_vaccine() == False) or (require_vaccine == False and treatment.get_require_vaccine() == True)):
                treatment.set_require_vaccine(require_vaccine)
            self.save_treatment_to_json(treatment)
            print("\nTratamiento modificado correctamente.\n")
        else:
            print("\nNo se encontró el tratamiento.\n")

    def delete_treatment(self, id: int):
        treatment = self.find_treatment_by_id(id)
        if treatment:
            self.treatments.remove(treatment)
            self.delete_treatment_from_file(id)
            print("\nTratamiento eliminado correctamente.\n")
        else:
            print("\nNo se encontró el tratamiento.\n")

    def find_treatment_by_name(self, name: str):
        for treatment in self.treatments:
            if treatment.get_name().lower().strip() == name.lower().strip():
                return treatment
        return None

    def find_treatment_by_id(self, id: int):
        for treatment in self.treatments:
            if treatment.get_id() == id:
                return treatment
        return None

    def display_treatments(self):
        if not self.treatments:
            print('\nNo hay Tratamientos Registrados.\n')
        else:
            print('Listado de Tratamientos Registrados: ')
            for treatment in self.treatments:
                print(f'\n{treatment}')
            return self.treatments
