import os
import sys
import json
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'classes'))

from model.classes.Person import Person

class PersonManager:
    def __init__(self):
        self.data_dir = os.path.join(os.getcwd(), 'data')
        self.file_path = os.path.join(self.data_dir, 'persons.json')
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        self.persons = self.load_persons_from_file()

    def load_persons_from_file(self):
        current_persons = []
        max_id = 0
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                pets_data = json.load(file)
                for current_person in pets_data:
                    person = Person(current_person['name'], current_person['lastname'], current_person['type'], current_person['id'])
                    current_persons.append(person)
                    if current_person['id'] > max_id:
                        max_id = current_person['id']
        Person.id = max_id
        return current_persons


    def save_person_to_json(self, person):
        persons_data = []
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                persons_data = json.load(file)

        updated = False
        for current_person in persons_data:
            if current_person['id'] == person.get_id():
                current_person['name'] = person.get_name()
                current_person['lastname'] = person.get_last_name()
                current_person['type'] = person.get_type()
                updated = True
                break
        
        if not updated:
            pet_data = {
                'id': person.get_id(),
                'name': person.get_name(),
                'lastname': person.get_last_name(),
                'type': person.get_type()
            }
            persons_data.append(pet_data)

        with open(self.file_path, 'w') as file:
            json.dump(persons_data, file, indent=4)

    def delete_person_from_file(self, person : Person):
        persons_data = []
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                persons_data = json.load(file)
        person_found = False
        for current_person in persons_data:
            if current_person['id'] == person.get_id():
                persons_data.remove(current_person)
                person_found = True
                break

        with open(self.file_path, 'w') as file:
            json.dump(persons_data, file, indent=4)



    def add_person(self, person):
        if self.find_person(person.get_id()):
            print("\nLa persona ya está registrada en el Sistema.\n")
            return
        self.persons.append(person)
        self.save_person_to_json(person)
        print("\nPersona registrada correctamente.\n")
        return person
    
    def modify_person(self, id, new_name='', new_last_name='', new_type=None, new_contact_data=None):
        person = self.find_person(id)
        if person:
            if new_name.strip():
                person.set_name(new_name)
            if new_last_name.strip():
                person.set_last_name(new_last_name)
            if new_type:
                if new_type.strip() != person.get_type():
                    person.update_type(new_type)
            if new_contact_data:
                person.set_contact_data(new_contact_data)
            self.save_person_to_json(person)
            print("\nPersona modificada correctamente.\n")
        else:
            print("\nNo se encontró la persona.\n")

    def delete_person(self, id):
        person = self.find_person(id)
        if person:
            self.persons.remove(person)
            self.delete_person_from_file(person)
            print("\nPersona eliminada correctamente.\n")
            return
        print("\nNo se encontró la persona.\n")

    def find_person(self, id):
        for person in self.persons:
            if person.get_id() == id:
                return person
        return None
    def find_person_by_name(self, name):
        #name is first name
        for person in self.persons:
            if person.get_name() == name:
                return person
        return None
    def display_persons(self):
        if not self.persons:
            print('\nNo hay Personas Registradas.')
        else:
            print('\nListado de Personas Registradas:\n')
            for person in self.persons:
                print(f'\n{person}')    
