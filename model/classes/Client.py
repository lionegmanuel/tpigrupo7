import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from typing import List, TYPE_CHECKING
from model.classes.Person import Person

if TYPE_CHECKING:
    from model.classes.Pet import Pet

class Client(Person):
    def __init__(self, name: str, last_name: str, contact_data=None):
        super().__init__(name, last_name, "client", contact_data)
        self.__pets: List['Pet'] = []

    def get_pet_list(self):
        return self.__pets

    def set_pet_list(self, new_pet_list):
        self.__pets = new_pet_list

    def __str__(self):
        return f"✅ Nombre: {self.get_name()}\n✅ Apellido: {self.get_last_name()}]"

    def __repr__(self):
        return self.__str__()
