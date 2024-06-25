import os
import json
from model.classes.MedicalRecord import MedicalRecord
from model.classes.Pet import Pet
from model.logic.treatmentManager import TreatmentManager
from model.logic.diagnosisManager import DiagnosisManager

class MedicalRecordManager:
    def __init__(self):
        self.data_dir = os.path.join(os.getcwd(), 'data')
        self.file_path = os.path.join(self.data_dir, 'medical_records.json')
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        
        self.treatment_manager = TreatmentManager()
        self.diagnosis_manager = DiagnosisManager()
        self.medical_records = self.load_medical_records_from_file()
        

    def load_medical_records_from_file(self):
        current_medical_records = []
        max_id = 0
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                medical_records_data = json.load(file)
                for current_record in medical_records_data:
                    treatment_name = current_record['treatment'].split(" - ")[0].strip()
                    diagnosis_information = current_record['diagnosis']

                    current_treatment = self.treatment_manager.find_treatment_by_name(treatment_name)
                    current_diagnosis =  self.diagnosis_manager.find_diagnosis_by_information(diagnosis_information)

                    #validacion:
                    ##if current_treatment is None:
                   ##     print(f"Error: Tratamiento '{treatment_name}' no encontrado para el registro con ID {current_record['id']}")
                   ##     print(f"El tratamiento registrado es: {current_record['treatment']}")
                   ## if current_diagnosis is None:
                   ##     print(f"Error: Diagnóstico '{diagnosis_information}' no encontrado para el registro con ID {current_record['id']}")

                    medical_record = MedicalRecord(
                        current_record['pet'],
                        current_record['consult_date'],
                        current_diagnosis,
                        current_treatment,
                        current_record['id']
                    )
                    current_medical_records.append(medical_record)
                    if current_record['id'] > max_id:
                        max_id = current_record['id']
        MedicalRecord.id = max_id
        return current_medical_records

    def save_medical_record_to_json(self, medical_record):
        records_data = []
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                records_data = json.load(file)

        record_data = {
            'pet': medical_record.get_pet().get_name(),
            'consult_date': medical_record.get_consult_date(),
            'diagnosis': medical_record.get_diagnosis().get_information(),
            'treatment': f'{medical_record.get_treatment().get_name()} - {medical_record.get_treatment().get_description()}',
            'require_vaccine': medical_record.get_treatment().get_require_vaccine(),
            'id': medical_record.get_id()
        }
        records_data.append(record_data)

        with open(self.file_path, 'w') as file:
            json.dump(records_data, file, indent=4)

    def delete_medical_record_from_file(self, medical_record : MedicalRecord):
        records_data = []
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                records_data = json.load(file)
        record_found = False
        for current_record in records_data:
            if current_record['id'] == medical_record.get_id():
                records_data.remove(current_record)
                record_found = True
                break

        with open(self.file_path, 'w') as file:
            json.dump(records_data, file, indent=4)

    def add_medical_record(self, pet, consult_date, diagnosis, treatment):
        new_medical_record = MedicalRecord(pet, consult_date, diagnosis, treatment)
        self.medical_records.append(new_medical_record)
        self.save_medical_record_to_json(new_medical_record)
        print("\nFicha médica agregada correctamente.\n")

    def get_pet_medical_records(self, pet: Pet):
        return self.find_medical_records_by_pet(pet)
    def find_medical_records_by_pet(self, pet: Pet):
        medical_records = []
        if pet:
            for medical_record in self.medical_records:
                if medical_record.get_pet() == pet.get_name():
                    medical_records.append(medical_record)
            return medical_records
        return None
    def find_medical_record_by_id(self, id):
        for medical_record in self.medical_records:
            if medical_record.get_id() == id:
                return medical_record
        return None

    def display_medical_records(self):
        if not self.medical_records:
            print('\nNo hay Fichas Médicas Registradas.\n')
        else:
            print('\nListado de Fichas Médicas Registradas: ')
            for medical_record in self.medical_records:
                print(f'\n{medical_record}')
    def delete_medical_record(self, id: int):
        for current in self.medical_records:
            if current.get_id() == id:
                self.medical_records.remove(current)
                self.delete_medical_record_from_file(current)
                print('\nFicha Médica Eliminada Correctamente.\n')
                return
        print('\nLa Ficha Médica Solicitada No fue Encontrada.\n')