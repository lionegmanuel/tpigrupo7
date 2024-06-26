import json
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'classes'))

from model.classes.Breed import Breed

class BreedManager:
    def __init__(self):
        self.data_dir = os.path.join(os.getcwd(), 'data') #files register
        self.file_path = os.path.join(self.data_dir, 'breeds.json')
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        self.breeds = self.load_breeds_from_file()

    def add_breed(self, new_breed: Breed):
        for current_breed in self.breeds:
            if new_breed.get_id() == current_breed.get_id():
                print(f"\nLa raza {new_breed.get_name()} ya está registrada.")
                return
        self.breeds.append(new_breed)
        print(f'\nLa Raza "{new_breed.get_name()}" fue Agregada Correctamente.\n')
        self.save_breed_to_json(new_breed) #file register process

    def save_breed_to_json(self, breed: Breed): 
        file_path = os.path.join(self.data_dir, 'breeds.json')
        breeds_data = []
        # if file exists, load currently data
        if os.path.exists(self.file_path):
            with open(file_path, 'r') as file:
                breeds_data = json.load(file)

        # update
        updated = False
        for current_breed in breeds_data:
            if current_breed['id'] == breed.get_id():
                current_breed['name'] = breed.get_name()
                updated = True
                break
        
        if not updated:
            breed_data = {
                'name': breed.get_name(),
                'id': breed.get_id(),
            }
            breeds_data.append(breed_data)

        # save
        with open(file_path, 'w') as file:
            json.dump(breeds_data, file, indent=4)


    def load_breeds_from_file(self):
        current_breeds = []
        max_id = 0
        if os.path.exists(self.file_path):  
            with open(self.file_path, 'r') as file:
                breeds_data = json.load(file)
                for breed_info in breeds_data:
                    breed = Breed(breed_info['name'], breed_info['id'])
                    current_breeds.append(breed)
                    if breed_info['id'] > max_id:
                        max_id = breed_info['id']
        Breed.id = max_id
        return current_breeds

    def delete_breed_from_file(self, breed : Breed):
        breeds_data = []
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                breeds_data = json.load(file)
        breed_found = False
        for current_breed in breeds_data:
            if current_breed['id'] == breed.get_id():
                breeds_data.remove(current_breed)
                breed_found = True
                break

        with open(self.file_path, 'w') as file:
            json.dump(breeds_data, file, indent=4)

    def modify_breed(self, breed_id, breed_name):
        for current_breed in self.breeds:
            if current_breed.get_id() == breed_id:
                old_name = current_breed.get_name()
                current_breed.set_name(breed_name)
                self.save_breed_to_json(current_breed)
                print(f"\n¡Modificación Realizada!\nDetalles:\n\t📌 Nombre Antiguo: {old_name}\n\t📌 Nombre Actualizado: {breed_name}")
                return
        print(f"No se encontró la raza específica. Detalles:\n\t1- ID: {breed_id}\n\t2- Nombre: {breed_name}")

    def delete_breed(self, breed_id: int):
        current_breed = self.find_breed_by_id(breed_id)
        if current_breed:
            deleted_breed_name = current_breed.get_name()
            self.breeds.remove(current_breed)
            self.delete_breed_from_file(current_breed)
            print(f'\nLa Raza "{(deleted_breed_name).upper()}" se eliminó correctamente.')
        else: print(f"\n¡ERROR!\nLa Raza no fue Encontrada en el Sistema\n")

    def display_breeds(self):
        if not self.breeds:
            print("\n!NO hay razas registradas!\n")
        else:
            print("\nListado de Razas Registradas:\n")
            for breed in self.breeds:
                print(f'\n{breed}')
    def find_breed_by_id(self, id):
        for breed in self.breeds:
            if breed.get_id() == id:
                return breed
        return None
    def find_and_create_breed(self, breed_name):
        for current_breed in self.breeds:
            if current_breed.get_name() == breed_name:
                return current_breed
        print(f'\nLa Raza {breed_name} no está registrada. ¿Desea Crearla?')
        user_response = input('(S/N): ')
        if user_response.upper() == 'S':
            new_current_breed = Breed(breed_name)
            self.add_breed(new_current_breed)
            return new_current_breed
    def find_breed_by_name(self, name):
        for breed in self.breeds:
            if breed.get_name().lower().strip() == name.lower().strip():
                return breed
        return None
