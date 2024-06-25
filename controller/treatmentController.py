import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'managers'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'classes'))

from model.logic.treatmentManager import TreatmentManager

class TreatmentController:
    def __init__(self):
        self.treatment_manager = TreatmentManager()

    def add_treatment(self, name: str, description: str, duration: int, is_require_vaccine):
        current_treatment = self.treatment_manager.add_treatment(name, description, duration, is_require_vaccine)
        return current_treatment #necesary for after use

    def modify_treatment(self, new_name: str, new_description: str, new_duration: int, is_require_vaccine, id: int):
        self.treatment_manager.modify_treatment(new_name, new_description, new_duration, is_require_vaccine, id)

    def delete_treatment(self, id: int):
        self.treatment_manager.delete_treatment(id)

    def display_treatments(self):
        return self.treatment_manager.display_treatments()

    def find_by_id(self, id):
        return self.treatment_manager.find_treatment_by_id(id)