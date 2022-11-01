class Account: 
    def __init__(self, name, phone, email, person_id):
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__person_id = person_id

    #setter group
    def set_name(self, name):
        self.__name = name
    def set_phone(self, phone):
        self.__phone = phone
    def set_email(self, email):
        self.__email = email
    def set_person_id(self, person_id):
        self.__person_id = person_id

    #getter group
    def get_name(self):
        return self.__name
    def get_phone(self):
        return self.__phone
    def get_email(self):
        return self.__email
    def get_person_id(self):
        return self.__person_id


    def __str__(self):
        return 'Name: ' + self.__name + \
               '\nphone: ' + self.__phone +\
               '\nEmail: ' + self.__email