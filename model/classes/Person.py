class Person:
    id = 0
    
    def __init__(self, name, last_name, type, id = None, contact_data=None):
        if id is None:
            Person.id += 1
            self.__id = Person.id
        else: self.__id = id
        self.__name = name
        self.__last_name = last_name
        self.__type = type
        self.__contact_data = contact_data if contact_data is not None else []

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_last_name(self):
        return self.__last_name
    def get_full_name(self):
        return self.__name.strip() + ' ' + self.__last_name.strip()
    
    def get_type(self):
        return self.__type
    
    def get_contact_data(self):
        return self.__contact_data if self.__contact_data is not None else '-'
    
    def set_name(self, new_name):
        self.__name = new_name
    
    def set_last_name(self, new_last_name):
        self.__last_name = new_last_name
    
    def update_type(self, new_type):
        self.__type = new_type
    
    def set_contact_data(self, new_contact_data):
        self.__contact_data = new_contact_data

    def to_dict(self):
        return {
            'name': self.__name,
            'last_name': self.__last_name,
            'type': self.__type,
            'contact_data': self.__contact_data if self.__contact_data != None else ' - ',
            'id': self.__id
        }
    def __str__(self):
        return f"✅ Nombre: {self.__name}\n✅ Apellido: {self.__last_name}\n✅ Tipo: {'Cliente' if self.__type == 'client' else 'Veterinario'}\n\t📌 N° Identificador: {self.__id}"
    
    def __repr__(self):
        return f"Person(id={self.__id}, name={self.__name}, lastName={self.__last_name}, type={self.__type})"
