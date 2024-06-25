import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'managers'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'classes'))

from model.logic.medicalRecordManager import MedicalRecordManager

class MedicalRecordController:
    def __init__(self):
        self.medical_record_manager = MedicalRecordManager()

    def add_medical_record(self, pet, consult_date, diagnosis, treatment):
        self.medical_record_manager.add_medical_record(pet, consult_date, diagnosis, treatment)

    def find_medical_record(self, record_id):
        return self.medical_record_manager.find_medical_record_by_id(record_id)

    def get_pet_medical_records(self, pet):
        return self.medical_record_manager.get_pet_medical_records(pet)

    def display_medical_records(self):
        self.medical_record_manager.display_medical_records()

    def delete_medical_record(self, id):
        self.medical_record_manager.delete_medical_record(id)