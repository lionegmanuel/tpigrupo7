import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'managers'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'classes'))

from model.logic.diagnosisManager import DiagnosisManager

class DiagnosisController:
    def __init__(self):
        self.diagnosis_manager = DiagnosisManager()

    def add_diagnosis(self, pet_name, information):
        self.diagnosis_manager.add_diagnosis(pet_name, information)

    def modify_diagnosis(self, id, new_name='', information=''):
        self.diagnosis_manager.modify_diagnosis(id, new_name, information)

    def delete_diagnosis(self, id):
        self.diagnosis_manager.delete_diagnosis(id)

    def display_diagnoses(self):
        return self.diagnosis_manager.display_diagnoses()
    def find_by_id(self, id):
        return self.diagnosis_manager.find_diagnosis_by_id(id)
    def find(self, pet_name):
        return self.diagnosis_manager.find_diagnosis(pet_name)