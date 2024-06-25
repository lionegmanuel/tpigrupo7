from Pet import Pet
from Consult import Consult
from Diagnosis import Diagnosis
from Treatment import Treatment

class MedicalRecord:
    id = 0
    
    def __init__(self, pet: Pet, consult_date, diagnosis : Diagnosis, treatment : Treatment, id = None):
        if id is None:
            MedicalRecord.id += 1
            self.__id = MedicalRecord.id
        else: self.__id = id
        self.__pet = pet
        self.__consult_date = consult_date
        self.__diagnosis = diagnosis
        self.__treatment = treatment

    def get_id(self):
        return self.__id
    
    def get_pet(self):
        return self.__pet
    
    def set_pet(self, new_pet):
        self.__pet = new_pet
    

    def add_consult(self, consult: Consult):
        self.__consults_list.append(consult)
    
    def find_consult_by_id(self, consult_id: int):
        for consult in self.__consults_list:
            if consult.get_id() == consult_id:
                return consult
        return None
    def get_diagnosis(self):
        return self.__diagnosis
    def get_treatment(self):
        return self.__treatment
    def get_pet_consults(self):
        return [str(consult) for consult in self.__consults_list]
    def get_consult_date(self):
        return self.__consult_date
    def __str__(self):
        return f"✅ Mascota: {self.__pet}\n✅ Fecha de Consulta: {self.__consult_date}\n✅ Diagnóstico: {'-' if self.__diagnosis is None else self.__diagnosis.get_information()}\n✅ Tratamiento Asignado: {'-' if self.__treatment is None else self.__treatment.get_name()} / ¿Requiere Vacunación? => {'-' if self.__treatment is None else self.__treatment.get_require_vaccine()}\n✅ N° de Identificación de Ficha Médica: {self.__id}"
    
    def __repr__(self):
        return f"MedicalRecord(id={self.__id}, pet={self.__pet}, consults_list={self.__consults_list})"
