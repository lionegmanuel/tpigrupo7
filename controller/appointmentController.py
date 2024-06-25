import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'logic'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'classes'))

from model.logic.appointmentManager import AppointmentManager
from model.classes.Appointment import Appointment

class AppointmentController:
    def __init__(self):
        self.appointment_manager = AppointmentManager()

    def add_appointment(self, appointment):
        self.appointment_manager.add_appointment(appointment)

    def modify_appointment(self, id, new_date=None, new_veterinarian=None, new_client=None, new_pet=None):
        self.appointment_manager.modify_appointment(id, new_date, new_veterinarian, new_client, new_pet)

    def delete_appointment(self, id):
        self.appointment_manager.delete_appointment(id)

    def get_all_appointments(self):
        return self.appointment_manager.display_appointments()
