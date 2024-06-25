import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'managers'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'classes'))

from model.logic.personManager import PersonManager
from model.classes.Client import Client
from model.classes.Veterinarian import Veterinarian

class PersonController:
    def __init__(self):
        self.person_manager = PersonManager()

    def add_person(self, name, last_name, type, contact_data=None, specialization=None):
        if type.lower() == 'client':
            new_person = Client(name, last_name, contact_data)
        elif type == 'veterinarian':
            if specialization is None:
                print("Se requiere una especialización para el veterinario.")
                return
            new_person = Veterinarian(name, last_name, specialization, contact_data)
        else:
            print("Tipo de persona no válido.")
            return
        added_person = self.person_manager.add_person(new_person)
        return added_person

    def modify_person(self, id, new_name='', new_last_name='', new_type=None, new_contact_data=None, new_specialization=None):
        person = self.person_manager.find_person(id)
        if isinstance(person, Veterinarian) and new_specialization:
            person.set_specialization(new_specialization)
        self.person_manager.modify_person(id, new_name, new_last_name, new_type, new_contact_data)

    def delete_person(self, id):
        self.person_manager.delete_person(id)

    def display_persons(self):
        self.person_manager.display_persons()
