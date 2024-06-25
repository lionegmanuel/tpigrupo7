class Appointment:
    def __init__(self, identification, datetime, pet, veterinarian, reason):
        self.__identification = identification
        self.__datetime = datetime
        self.__pet = pet
        self.__veterinarian = veterinarian
        self.__reason = reason

    def get_id(self):
        return self.__identification
    
    def get_datetime(self):
        return self.__datetime
    
    def get_pet(self):
        return self.__pet
    
    def get_veterinarian(self):
        return self.__veterinarian
    
    def get_reason(self):
        return self.__reason

    def set_id(self, new_identification):
        self.__identification = new_identification
    
    def set_datetime(self, new_datetime):
        self.__datetime = new_datetime
    
    def set_pet(self, new_pet):
        self.__pet = new_pet
    
    def set_veterinarian(self, new_veterinarian):
        self.__veterinarian = new_veterinarian
    
    def set_reason(self, new_reason):
        self.__reason = new_reason

    def __str__(self):
        return f"✅ Identificación de Turno: {self.__id}\n✅ Fecha: {self.__date.strftime('%d/%m/%Y - %H:%M:%S')}✅ Mascota para la cual se solicita el TUrno Médico: {self.__pet}\n✅ Veterinario a Cargo: {self.__veterinarian}\n✅ Motivo de Consulta: {self.__reason}"

