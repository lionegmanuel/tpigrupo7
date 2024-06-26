import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'managers'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'classes'))

from model.logic.breedManager import BreedManager
from model.classes.Breed import Breed

class BreedController:
    def __init__(self):
        self.breed_manager = BreedManager()

    def add_breed(self, name):
        new_breed = Breed(name)
        self.breed_manager.add_breed(new_breed)

    def modify_breed(self, id, new_name):
        self.breed_manager.modify_breed(id, new_name)

    def delete_breed(self, id):
        self.breed_manager.delete_breed(id)

    def display_breeds(self):
        return self.breed_manager.display_breeds()
    def find_breed_by_name(self, name):
        return self.breed_manager.find_breed_by_name(name)
