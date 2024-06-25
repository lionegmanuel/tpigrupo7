from controller.appointmentController import AppointmentController

class AppointmentView:
    def __init__(self):
        self.controller = AppointmentController()

    def show_main_menu(self):
        while True:
            print("\n---Gestión de Citas---\n")
            print("1. Agregar Cita")
            print("2. Modificar Cita")
            print("3. Eliminar Cita")
            print("4. Mostrar Todas las Citas")
            print("5. Salir")

            choice = input("Seleccione una Opción: ")

            if choice == "1":
                self.add_appointment()
            elif choice == "2":
                self.modify_appointment()
            elif choice == "3":
                self.delete_appointment()
            elif choice == "4":
                self.display_all_appointments()
            elif choice == "5":
                break
            else:
                self.show_invalid_option()

    def add_appointment(self):
        try:
            pet_id = int(input("ID de la mascota para agendar una cita: "))
            client_id = int(input("ID del cliente para agendar la cita: "))
            date = input("Fecha de la cita (formato DD/MM/AAAA): ")
            hour = input("Hora de la cita (formato HH:MM): ")
            self.controller.add_appointment(pet_id, client_id, date, hour)
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

    def modify_appointment(self):
        try:
            appointment_id = int(input("ID de la cita a modificar: "))
            new_date = input("Nueva fecha de la cita (formato DD/MM/AAAA): ")
            new_hour = input("Nueva hora de la cita (formato HH:MM): ")
            self.controller.modify_appointment(appointment_id, new_date, new_hour)
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

    def delete_appointment(self):
        try:
            appointment_id = int(input("ID de la cita a eliminar: "))
            self.controller.delete_appointment(appointment_id)
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

    def display_all_appointments(self):
        appointments =  self.controller.get_all_appointments()
        if not appointments:
            print("No hay citas registradas.")
        else:
            print("\nListado de Citas:")
            for appointment in appointments:
                print(appointment)

    def show_invalid_option(self):
        print("Opción inválida. Por favor, ingrese una opción válida.")
