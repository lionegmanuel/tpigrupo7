from model.classes.Breed import Breed
from model.classes.Person import Person

class Pet:
    id = 0
    def __init__(self, name: str, specie: str, breed: Breed, owner: Person, id = None):
        if not isinstance(owner, Person):
            raise TypeError("El propietario es un tipo de Dato Incorrecto.")
        if id is None:
            Pet.id+=1
            self.__id = Pet.id
        else: self.__id = id
        self.__name = name
        self.__specie = specie
        self.__breed = breed
        self.__owner = owner

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_specie(self):
        return self.__specie

    def get_breed(self):
        return self.__breed

    def get_owner(self):
        return self.__owner

    def set_id(self, new_id: int):
        self.__id = new_id

    def set_name(self, new_name: str):
        self.__name = new_name

    def set_species(self, new_specie: str):
        self.__specie = new_specie

    def set_breed(self, new_breed: Breed):
        self.__breed = new_breed

    def to_dict(self):
        return {
            'name': self.__name,
            'specie': self.__specie,
            'breed': self.__breed.get_name(),
            'owner': self.__owner.to_dict(),
            'id': self.__id
        }

    def set_owner(self, new_owner: Person):
        if not isinstance(new_owner, Person):
            raise TypeError("El nuevo Propietario Tiene un tipo de Dato Incorrecto.")
        self.__owner = new_owner

    def __str__(self):
        return f"✅ Nombre de la Mascota: {self.__name}\n\t📌 Identificación de Mascota: {self.__id}\n\t📌 Raza: {self.__breed.get_name()}\n\t📌 Dueño/a: {self.__owner.get_name()}"

    def __repr__(self):
        return self.__str__()
