from Admin import Admin
from Doctor import Doctor
from Patient import Patient

class DATABASE:
    def __init__(self):
        self.__username = 'None'
        self.__password = 'None'
        self.__admin_address = 'None'
        self.__doctor_Firstname = 'None'
        self.__doctor_Surname = 'None'
    def CreateAdmin(self):
        self.__username, self.__password, self.__admin_address = open('database/admin.db').readline().split(';')
        admin = Admin(username=self.__username, password=self.__password, address=self.__admin_address)
        return admin

    def CreateDoctors(self):
        doc = []
        doctors = open('database/doctor.db').readlines()
        for doctor in doctors:
            self.__doctor_Firstname, self.__doctor_Surname, self.__speciality = doctor.split(';')
            doc.append(Doctor(self.__doctor_Firstname,self.__doctor_Surname, self.__speciality))
        return doc

    def CreatePatients(self):
        pat = []
        patients = open('database/patients.db').readlines()
        for patient in patients:
            self.__patient_Firstname, self.__patient_Surname, self.__age, self.__mobile, self.__postcode = patient.split(';').strip()
            pat.append(Patient(self.__patient_Firstname, self.__patient_Surname, self.__age, self.__mobile, self.__postcode))
        return pat

    def UpdateUser(self,username, password,address):
        self.__username = username
        self.__password = password
        self.__admin_address = address
        with open('database/admin.db', 'w') as adminFile:
            adminFile.write(f"{username};{password};{address}")
        adminFile.close()
# DB = DATABASE()