class Breed:
    id = 0
    
    def __init__(self, name, id = None):
        if id is None:
            Breed.id += 1
            self.__id = Breed.id
        else: self.__id = id
        self.__name = name

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def set_name(self, new_name):
        self.__name = new_name

    def __str__(self):
        return f"✅ {(self.__name).upper()}\n\t📌 N° Identificador de Raza: {self.__id}\n"
    
    def __repr__(self):
        return self.__str__()
