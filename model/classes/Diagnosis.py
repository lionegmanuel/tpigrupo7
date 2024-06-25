from datetime import datetime

class Diagnosis:
    id = 0
    
    def __init__(self, pet_name, information: str, id = None):
        if id is None:
            Diagnosis.id += 1
            self.__id = Diagnosis.id
        else: self.__id = id
        self.__pet_name = pet_name
        self.__date = datetime.now()
        self.__information = information

    def get_id(self):
        return self.__id
    
    def get_pet_name(self):
        return self.__pet_name
    
    def get_date(self):
        return self.__date
    
    def get_information(self):
        return self.__information
    
    def set_pet_name(self, new_name):
        self.__pet_name = new_name
    
    def set_information(self, new_information):
        self.__information = new_information

    def to_dict(self):
        return {
            'pet_name': self.__pet_name,
            'information': self.__information,
            'id': self.__id
        }

    def __str__(self):
        return f"✅ Diagnóstico N° {self.__id}\n✅ Fecha: {self.__date.strftime('%d/%m/%Y - %H:%M:%S')}\n✅ Mascota a la cual se le Generó el Diagnóstico: {self.__pet_name}\n✅ Información del Diagnóstico:\n\t📌 {self.__information}"
    
    def __repr__(self):
        return self.__str__()
