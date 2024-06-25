import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'managers'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'classes'))

from model.logic.vaccineManager import VaccineManager

class VaccineController:
    def __init__(self):
        self.vaccineManager = VaccineManager()

    def add_vaccine(self, id, name, application_date):
        self.vaccineManager.add_vaccine(id, name, application_date)

    def modify_vaccine(self, id, new_name, new_application_date):
        self.vaccineManager.modify_vaccine(id, new_name, new_application_date)

    def delete_vaccine(self, id):
        self.vaccineManager.delete_vaccine(id)

    def display_vaccines(self):
        self.vaccineManager.display_vaccines()
