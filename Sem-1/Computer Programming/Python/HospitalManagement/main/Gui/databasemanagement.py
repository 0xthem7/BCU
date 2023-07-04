from Admin import Admin
from Doctor import Doctor
from Patient import Patient

DoctorDB = 'database/doctor.db'
AdminDB = 'database/admin.db'
PatientDB = 'database/patients.db'
Discharged = 'database/dischargedPatients.db'
SortedPatientDB = 'database/patients.db'

class DATABASE:
    def __init__(self):
        self.__username = 'None'
        self.__password = 'None'
        self.__admin_address = 'None'
        self.__doctor_Firstname = 'None'
        self.__doctor_Surname = 'None'
        self.__patient_first_name = 'None'
        self.__patient_surname = 'None'
        self.__patient_age = 'None'
        self.__patient_mobile = 'None'
        self.__patient_postcode = 'None'
        self.__patient_doctor = 'None'
        self.__symptoms = 'None'

    def CreateAdmin(self):
        try:
            self.__username, self.__password, self.__admin_address = open(AdminDB).readline().split(';')
            admin = Admin(username=self.__username, password=self.__password, address=self.__admin_address)
            return admin
        except:
            print("Database Not found")

    def CreateDoctors(self):
        doc = []
        try:
            doctors = open(DoctorDB).readlines()
            for doctor in doctors:
                self.__doctor_Firstname, self.__doctor_Surname, self.__speciality = doctor.split(';')
                doc.append(Doctor(self.__doctor_Firstname,self.__doctor_Surname, self.__speciality.strip()))
            return doc
        except:
            print("Database not found")

    def CreatePatients(self):
        pat = []
        patients = open(PatientDB).readlines()
        for patient in patients:
            self.__patient_first_name, self.__patient_surname, self.__patient_age, self.__mobile, self.__patient_postcode,self.__patient_doctor, self.__symptoms = patient.split(';')
            pat.append(Patient(self.__patient_first_name,self.__patient_surname, self.__patient_age,self.__mobile, self.__patient_postcode, self.__patient_doctor, self.__symptoms.strip()))
        return pat
    

    def UpdateAdmin(self,username, password,address):
        self.__username = username
        self.__password = password
        self.__admin_address = address
        try:
            with open(AdminDB, 'w') as adminFile:
                adminFile.write(f"{username};{password};{address}")
            adminFile.close()
        except:
            print("Database not found")
    
    def UpdateDoctor(self,list):
        try:
            with open(DoctorDB, 'w') as doctorFile:
                for doctor in list:
                    doctorFile.write(f'{doctor.get_first_name()};{doctor.get_surname()};{doctor.get_speciality()}\n')
            doctorFile.close()
        except:
            print("Database not found")

    
    def Updatepatients(self, patientlist):
        try:
            with open(PatientDB, 'w') as patientFile:
                for patient in patientlist:
                    patientFile.write(f'{patient.get_first_name()};{patient.get_surname()};{patient.get_age()};{patient.get_mobile()};{patient.get_postcode()};{patient.get_doctor()};{patient.get_symptoms()}\n')
        except:
            print("Database not found")
            

    def discharged_patients(self):
        try:
            dis_patients =  open(Discharged).readlines()
            strip_patients = [x.split('\n')[0] for x in dis_patients]
            return strip_patients
        except:
            print("Database not found")
            return None

    def add_discharged_patients(self,list):
        with open(Discharged, 'w') as disFile:
            for pat in list:
                disFile.write(f'{pat}\n')
        disFile.close()
        
    
    def sort_patients(self):
        with open(PatientDB, 'r') as patientFile:
            patientList = patientFile.readlines()
        
        sortedPatient = sorted(patientList, key=lambda patient: patient.split(';')[1])
        patientFile.close()

        with open(SortedPatientDB, 'w') as sortedPatientFile:
            for patient in sortedPatient:
                sortedPatientFile.write(f'{patient.strip()}\n')
        sortedPatientFile.close()
