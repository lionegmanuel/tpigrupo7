from datetime import datetime
from Pet import Pet
from Veterinarian import Veterinarian
from Diagnosis import Diagnosis
from Treatment import Treatment
from Vaccine import Vaccine

class Consult:
    id_counter = 0

    def __init__(self, pet: Pet, veterinarian: Veterinarian, diagnosis: Diagnosis, treatment: Treatment, vaccines: list[Vaccine], reason: str, id = None):
        Consult.id_counter += 1
        self.__id = Consult.id_counter if id is None else id
        self.__datetime = datetime.now()
        self.__pet = pet
        self.__veterinarian = veterinarian
        self.__diagnosis = diagnosis
        self.__treatment = treatment
        self.__vaccines = vaccines
        self.__reason = reason

    # Getters
    def get_id(self):
        return self.__id
    
    def get_datetime(self):
        return self.__datetime.strftime("%d/%m/%Y - %H:%M:%S")
    
    def get_pet(self):
        return self.__pet
    
    def get_veterinarian(self):
        return self.__veterinarian
    
    def get_diagnosis(self):
        return self.__diagnosis
    
    def get_treatment(self):
        return self.__treatment
    
    def get_vaccines(self):
        return self.__vaccines
    
    def get_reason(self):
        return self.__reason

    # Setters
    def set_datetime(self, new_datetime):
        self.__datetime = new_datetime
    
    def set_pet(self, new_pet):
        self.__pet = new_pet
    
    def set_veterinarian(self, new_veterinarian):
        self.__veterinarian = new_veterinarian
    
    def set_diagnosis(self, new_diagnosis):
        self.__diagnosis = new_diagnosis
    
    def set_treatment(self, new_treatment):
        self.__treatment = new_treatment
    
    def set_vaccines(self, new_vaccines):
        self.__vaccines = new_vaccines
    
    def set_reason(self, new_reason):
        self.__reason = new_reason

    def to_dict(self):
        return {
            'id': self.__id,
            'pet': self.__pet.to_dict(),
            'veterinarian': self.__veterinarian.to_dict(),
            'diagnosis': self.__diagnosis.to_dict(),
            'treatment': self.__treatment.to_dict(),
            'vaccines': self.__vaccines,
            'reason': self.__reason
        }
    # String representation
    def __str__(self):
        formatted_datetime = self.__datetime.strftime("%d/%m/%Y - %H:%M:%S")
        vaccines_str = ', '.join([vaccine for vaccine in self.__vaccines])
        return (f"ID: {self.__id}\n"
                f"Fecha y Hora: {formatted_datetime}\n"
                f"Mascota: {self.__pet.get_name()}\n"
                f"Veterinario: {self.__veterinarian.get_name()}\n"
                f"Diagnóstico: {self.__diagnosis.get_information()}\n"
                f"Tratamiento: {self.__treatment.get_name()}\n"
                f"Vacunas: {vaccines_str}\n"
                f"Motivo: {self.__reason}")
    
    def __repr__(self):
        return self.__str__()

