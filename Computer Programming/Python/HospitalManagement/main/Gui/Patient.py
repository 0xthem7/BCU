class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode, doctor,symptoms):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """

        #ToDo1
        self.__first_name = first_name
        self.__surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__doctor = doctor
        self.__symptoms = symptoms
       

    
    def full_name(self) :
        """full name is first_name and surname"""
        #ToDo2
        return f'{self.__first_name} + {self.__surname}'

    def get_doctor(self) :
        #ToDo3
        return f'{self.__doctor}'

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor
    
    def set_symptoms(self, new_sympotms):
        self.__symptoms = new_sympotms

    def print_symptoms(self):
        """prints all the symptoms"""
        print(self.__symptoms)

    
    #User created function
    def get_first_name(self):
        return self.__first_name
    def get_surname(self):
        return self.__surname
    def get_age(self):
        return self.__age
    def get_mobile(self):
        return self.__mobile
    def get_postcode(self):
        return self.__postcode
    def get_symptoms(self):
        return self.__symptoms
    

    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'
