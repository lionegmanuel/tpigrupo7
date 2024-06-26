import os
import json
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'classes'))

from model.classes.Breed import Breed
from model.classes.Pet import Pet
from model.logic.personManager import PersonManager
from model.logic.breedManager import BreedManager

class PetManager:
    def __init__(self):
        self.data_dir = os.path.join(os.getcwd(), 'data')
        self.file_path = os.path.join(self.data_dir, 'pets.json')
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        self.personManager = PersonManager()
        self.breedManager = BreedManager()
        self.pets = self.load_pets_from_file()

    def load_pets_from_file(self):
        current_pets = []
        max_id = 0
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                pets_data = json.load(file)
                for current_pet in pets_data:
                    current_owner = self.personManager.find_person_by_first_name(current_pet['owner'])
                    current_breed = self.breedManager.find_breed_by_name(current_pet['breed'])
                    pet = Pet(current_pet['name'], current_pet['specie'], current_breed, current_owner, current_pet['id'])
                    current_pets.append(pet)
                    if current_pet['id'] > max_id:
                        max_id = current_pet['id']
        Pet.id = max_id
        return current_pets
    def save_pet_to_json(self, pet):
        pets_data = []
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                pets_data = json.load(file)

        updated = False
        for current_pet in pets_data:
            if current_pet['id'] == pet.get_id():
                current_pet['name'] = pet.get_name()
                current_pet['specie'] = pet.get_specie()
                current_pet['breed'] = pet.get_breed().get_name()
                current_pet['owner'] = pet.get_owner().get_name()
                updated = True
                break
        
        if not updated:
            pet_data = {
                'id': pet.get_id(),
                'name': pet.get_name(),
                'specie': pet.get_specie(),
                'breed': pet.get_breed().get_name(),
                'owner': pet.get_owner().get_name()
            }
            pets_data.append(pet_data)

        with open(self.file_path, 'w') as file:
            json.dump(pets_data, file, indent=4)
    def delete_pet_from_file(self, pet: Pet):
        pets_data = []
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                pets_data = json.load(file)
        pet_found = False
        for current_pet in pets_data:
            if current_pet['id'] == pet.get_id():
                pets_data.remove(current_pet)
                pet_found = True
                break

        with open(self.file_path, 'w') as file:
            json.dump(pets_data, file, indent=4)

    def add_pet(self, pet: Pet):
        if self.find_pet(pet):
            print('\nLa Mascota Ya Está Registrada en el Sistema.\n')
            return
        if pet.get_owner().get_pet_list() and pet in pet.get_owner().get_pet_list():
            print('\nEste Propietario Ya tiene Registrada a la Mascota.\n')
            return
        self.pets.append(pet)
        self.save_pet_to_json(pet)
        pet.get_owner().get_pet_list().append(pet)
        print("\nMascota registrada correctamente.\n")

    def modify_pet(self, id: int, new_name: str, new_species: str, new_breed: Breed):
        current_pet = self.find_pet_by_id(id)
        if current_pet:
            current_pet.set_name(new_name)
            current_pet.set_species(new_species)
            current_pet.set_breed(new_breed)
            self.save_pet_to_json(current_pet)
            print("\nMascota modificada correctamente.\n")
        else:
            print('\n¡ERROR!\nLa mascota no está Registrada en el Sistema.\n')

    def delete_pet(self, id: int):
        deleted_pet = self.find_pet_by_id(id)
        if deleted_pet:
            self.pets.remove(deleted_pet)
            self.delete_pet_from_file(deleted_pet)
            print('\nMascota Eliminada Correctamente.\n')
        else:
            print('\n¡ERROR!\nLa mascota No está Registrada en el Sistema.\n')

    def find_pet(self, searched_pet: Pet):
        for current_pet in self.pets:
            if current_pet.get_id() == searched_pet.get_id():
                return current_pet
        return None

    def find_pet_by_id(self, id):
        for current_pet in self.pets:
            if current_pet.get_id() == id:
                return current_pet
        return None
    def find_pet_by_name(self, name):
        for current_pet in self.pets:
            if current_pet.get_name().lower().strip() == name.lower().strip():
                return current_pet
        return None

    def display_pets(self):
        if not self.pets:
            print('\nNo hay Mascotas Registradas.\n')
        else:
            print('\nListado de Mascotas Registradas:\n')
            for pet in self.pets:
                print(f"\n{pet}")