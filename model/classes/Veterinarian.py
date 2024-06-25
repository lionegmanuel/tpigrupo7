from Person import Person

class Veterinarian(Person):
    def __init__(self, name: str, last_name: str, specialization: str, contact_data=None):
        super().__init__(name, last_name, "veterinarian", contact_data)
        self.__specialization = specialization

    def get_specialization(self):
        return self.__specialization

    def set_specialization(self, new_specialization):
        self.__specialization = new_specialization

    def to_dict(self):
        return {
            'name': self.get_name(),
            'last_name': self.get_last_name(),
            'specialization': self.__specialization,
            'id': self.get_id()
        }

    def __str__(self):
        return f"✅ Veterinario: {self.get_name()} {self.get_last_name()}\n✅ Especialización: {self.__specialization}"

    def __repr__(self):
        return self.__str__()
