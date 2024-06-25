class Vaccine:
    def __init__(self, id, name, application_date):
        self.__id = id
        self.__name = name
        self.__application_date = application_date

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_application_date(self):
        return self.__application_date

    def set_id(self, new_id):
        self.__id = new_id

    def set_name(self, new_name):
        self.__name = new_name

    def set_application_date(self, new_application_date):
        self.__application_date = new_application_date

    def __str__(self):
        return f"✅ N° Identificador: {self.__id}\n✅ Nombre: {self.__name}\n✅ Fecha de Aplicatión: {self.__application_date}"

    def __repr__(self):
        return f"Vaccine(ID: {self.__id}, Name: {self.__name}, Application Date: {self.__application_date})"
