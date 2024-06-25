class NavigationModel:
    def __init__(self):
        self.menu_options = {
            '1': 'Gestionar Razas',
            '2': 'Gestionar Mascotas',
            '3': 'Gestionar Personas',
            '4': 'Gestionar Diagnósticos',
            '5': 'Gestionar Tratamientos',
            '6': 'Gestionar Vacunas',
            '7': 'Gestionar Fichas Médicas',
            '8': 'Gestionar Consultas',
            '0': 'SALIR'
        }

    def get_menu_options(self):
        return self.menu_options

    def exit_program(self):
        return "Programa Finalizado."
