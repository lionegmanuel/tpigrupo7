import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'managers'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'classes'))

from model.logic.petManager import PetManager
from model.logic.breedManager import BreedManager
from controller.personController import PersonController
from model.classes.Pet import Pet
from model.classes.Breed import Breed

class PetController:
    def __init__(self):
        self.pet_manager = PetManager()
        self.breed_manager = BreedManager()
        self.person_controller = PersonController()

    def add_pet(self, id: int, name: str, species: str, breed_name: str, owner_name: str, owner_last_name: str):
        breed_to_new_pet = self.breed_manager.find_and_create_breed(breed_name)
        client = self.person_controller.add_person(owner_name, owner_last_name, 'client')
        new_pet = Pet(name, species, breed_to_new_pet, client, id if id != 0 else None)
        self.pet_manager.add_pet(new_pet)

    def modify_pet(self, id: int, new_name: str, new_species: str, new_breed_name: str):
        new_breed = self.breed_manager.find_and_create_breed(new_breed_name)
        self.pet_manager.modify_pet(id, new_name, new_species, new_breed)
        
    def delete_pet(self, id: int):
        self.pet_manager.delete_pet(id)

    def display_pets(self):
        self.pet_manager.display_pets()
    def find_by_id(self, id):
        return self.pet_manager.find_pet_by_id(id)
    def find_by_name(self, name):
        return self.pet_manager.find_pet_by_name(name)

