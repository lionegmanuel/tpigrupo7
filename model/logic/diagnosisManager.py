import os
import sys
import json
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'classes'))

from model.classes.Diagnosis import Diagnosis

class DiagnosisManager:
    def __init__(self):
        self.data_dir = os.path.join(os.getcwd(), 'data')
        self.file_path = os.path.join(self.data_dir, 'diagnoses.json')
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        self.diagnoses = self.load_diagnoses_from_file()

    def load_diagnoses_from_file(self):
        current_diagnoses = []
        max_id = 0
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                diagnoses_data = json.load(file)
                for current_diagnosis in diagnoses_data:
                    diagnosis = Diagnosis(current_diagnosis['pet_name'], current_diagnosis['information'], current_diagnosis['id'])
                    current_diagnoses.append(diagnosis)
                    if current_diagnosis['id'] > max_id:
                        max_id = current_diagnosis['id']
        Diagnosis.id = max_id
        return current_diagnoses

    def save_diagnosis_to_json(self, diagnosis):
        diagnoses_data = []
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                diagnoses_data = json.load(file)

        updated = False
        for current_diagnosis in diagnoses_data:
            if current_diagnosis['id'] == diagnosis.get_id():
                current_diagnosis['pet_name'] = diagnosis.get_pet_name()
                current_diagnosis['information'] = diagnosis.get_information()
                updated = True
                break

        if not updated:
            diagnosis_data = {
                'id': diagnosis.get_id(),
                'pet_name': diagnosis.get_pet_name(),
                'information': diagnosis.get_information()
            }
            diagnoses_data.append(diagnosis_data)

        with open(self.file_path, 'w') as file:
            json.dump(diagnoses_data, file, indent=4)

    def delete_diagnosis_from_file(self, diagnosis : Diagnosis):
        diagnoses_data = []
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                diagnoses_data = json.load(file)
        diagnosis_found = False
        for current_diagnosis in diagnoses_data:
            if int(current_diagnosis['id']) == diagnosis.get_id():
                diagnoses_data.remove(current_diagnosis)
                diagnosis_found = True
                break

        with open(self.file_path, 'w') as file:
            json.dump(diagnoses_data, file, indent=4)

    def add_diagnosis(self, pet_name, information): 
        if self.find_diagnosis(pet_name):
            print("El diagnóstico ya está registrado.")
            return
        new_diagnosis = Diagnosis(pet_name, information)
        self.diagnoses.append(new_diagnosis)
        self.save_diagnosis_to_json(new_diagnosis)
        print("\nDiagnóstico registrado correctamente.\n")

    def modify_diagnosis(self, id, new_name='', information=''):
        diagnosis = self.find_diagnosis_by_id(id)
        if diagnosis:
            if new_name:
                diagnosis.set_pet_name(new_name)
            if information:
                diagnosis.set_information(information)
            self.save_diagnosis_to_json(diagnosis)
            print("\nDiagnóstico modificado correctamente.\n")
            if not new_name and not information:
                print('\nNo hay datos ingresados para modificar.\n')
        else:
            print("\nNo se encontró el diagnóstico.\n")

    def delete_diagnosis(self, id):
        for diagnosis in self.diagnoses:
            if diagnosis.get_id() == id:
                self.diagnoses.remove(diagnosis)
                self.delete_diagnosis_from_file(diagnosis)
                print("\nDiagnóstico eliminado correctamente.\n")
                return
        print("\nNo se encontró el diagnóstico deseado para eliminar.\n")

    def find_diagnosis(self, searched_name):
        for diagnosis in self.diagnoses:
            if diagnosis.get_pet_name().lower().strip() == searched_name.lower().strip():
                return diagnosis
        return None

    def find_diagnosis_by_id(self, id):
        for diagnosis in self.diagnoses:
            if diagnosis.get_id() == id:
                return diagnosis
        return None
    def find_diagnosis_by_information(self, information):
        for diagnosis in self.diagnoses:
            if diagnosis.get_information() == information:
                return diagnosis
        return None
    def display_diagnoses(self):
        if not self.diagnoses:
            print('\nNo hay Diagnósticos Registrados.\n')
        else:
            print('\nListado de Diagnósticos:\n')
            for diagnosis in self.diagnoses:
                print(f'\n{diagnosis}')

    