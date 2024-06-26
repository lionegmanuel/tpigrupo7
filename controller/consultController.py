from model.logic.consultManager import ConsultManager

class ConsultController:
    def __init__(self):
        self.consult_manager = ConsultManager()

    def addConsult(self, pet, veterinarian, diagnosis, treatment, vaccines, reason):
        self.consult_manager.addConsult(pet, veterinarian, diagnosis, treatment, vaccines, reason)

    def find_consult_by_id(self, id):
        return self.consult_manager.find_consult_by_id(id)

    def deleteConsult(self, consult_id):
        self.consult_manager.deleteConsult(consult_id)

    def displayConsults(self):
        self.consult_manager.displayConsults()
    def vaccines_petition(self):
        return self.consult_manager.vaccines_petition()
    def vaccines_find(self, id):
        return self.consult_manager.vaccines_find(id)
    def verify_client(self, full_name):
        return self.consult_manager.verify_client(full_name)
    def verify_treatment(self, treatment_name):
        return self.consult_manager.verify_treatment(treatment_name)
    def verify_breed(self, breed_name):
        return self.consult_manager.verify_breed(breed_name)
    def verify_veterinarian(self, vterinarian_name):
        return self.consult_manager.verify_veterinarian(vterinarian_name)
    def verify_pet(self, pet_name):
        return self.consult_manager.verify_pet(pet_name)