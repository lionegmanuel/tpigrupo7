class Treatment:
    id = 0
    def __init__(self,name: str, description: str, duration: int, is_require_vaccine = None, id = None):
        if id is None:
            self.__id = Treatment.id
            Treatment.id += 1
        else:
            self.__id = id
        self.__name = name
        self.__description = description
        self.__duration = duration
        self.__is_require_vaccine = False if is_require_vaccine is None else is_require_vaccine

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_duration(self):
        return self.__duration
    def get_require_vaccine(self):
        return 'SI' if self.__is_require_vaccine else 'NO'
    def set_id(self, new_id: int):
        self.__id = new_id

    def set_name(self, new_name: str):
        self.__name = new_name

    def set_description(self, new_description: str):
        self.__description = new_description

    def set_duration(self, new_duration: int):
        self.__duration = new_duration
    def set_require_vaccine(self, new_require_vaccine):
        self.__is_require_vaccine = new_require_vaccine

    def to_dict(self):
        return {
            'name': self.__name,
            'description': self.__description,
            'duration': self.__duration,
            'is_require_vaccine' : self.__is_require_vaccine,
            'id': self.__id
        }
    
    def __str__(self):
        return f"✅ Identificacion del Tratamiento: {self.__id}\n✅ Nombre: {self.__name}\n✅ Descripción: {self.__description}\n✅ Duración de Tratamiento: {self.__duration} DÏA/S\n✅ Requerimento de Vacunación: {'SI' if self.__is_require_vaccine == True else 'NO'}"

    def __repr__(self):
        return self.__str__()
