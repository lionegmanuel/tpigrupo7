import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'classes'))

from model.classes.Appointment import Appointment

class AppointmentManager:
    def __init__(self):
        self.appointments = []

    def add_appointment(self, appointment):
        if self.find_appointment_by_id(appointment.get_id()):
            print("La cita ya está registrada.")
            return
        self.appointments.append(appointment)
        print("Cita registrada correctamente.")

    def modify_appointment(self, id, new_date=None, new_veterinarian=None, new_client=None, new_pet=None):
        appointment = self.find_appointment_by_id(id)
        if appointment:
            if new_date:
                appointment.set_datetime(new_date)
            if new_veterinarian:
                appointment.set_veterinarian(new_veterinarian)
            if new_client:
                appointment.set_reason(new_client)
            if new_pet:
                appointment.set_pet(new_pet)
            print("Cita modificada correctamente.")
        else:
            print("No se encontró la cita.")

    def delete_appointment(self, id):
        appointment = self.find_appointment_by_id(id)
        if appointment:
            self.appointments.remove(appointment)
            print("Cita eliminada correctamente.")
        else:
            print("No se encontró la cita.")

    def find_appointment_by_id(self, id):
        for appointment in self.appointments:
            if appointment.get_id() == id:
                return appointment
        return None

    def display_appointments(self):
        return self.appointments

