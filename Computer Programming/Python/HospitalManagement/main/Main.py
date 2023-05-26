# Imports
from tkinter import *
from Admin import Admin
from Doctor import Doctor
from Patient import Patient
from databasemanagement import DATABASE

#GUI Part


DB = DATABASE()



# Creating Objects using Database

    
def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    admin = DB.CreateAdmin() # username is 'admin', password is '123'
    doctors = DB.CreateDoctors()
    patients = [Patient('Sara','Smith', 20, '07012345678','B1 234'), Patient('Mike','Jones', 37,'07555551234','L2 2AB'), Patient('Daivd','Smith', 15, '07123456789','C1 ABC')]
    discharged_patients = []

    # keep trying to login tell the login details are correct
    while True:
        if admin.login():
            running = True # allow the program to run
            break
        else:
            print('Incorrect username or password.')

    while running:
        # print the menu
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Discharge patients')
        print(' 3- View discharged patient')
        print(' 4- Assign doctor to a patient')
        print(' 5- Update admin detais')
        print(' 6- Quit')

        # get the option
        op = input('Option: ')

        if op == '1':
            # 1- Register/view/update/delete doctor
         #ToDo1
            admin.doctor_management(doctors)
        elif op == '2':
            # 2- View or discharge patients
            #ToDo2
            patient_index = admin.discharge(patients, discharged_patients)
            while True:
                op = input('Do you want to discharge a patient(Y/N):').lower()

                if op == 'yes' or op == 'y':
                    #ToDo3
                    discharged_patients.append(patients[patient_index])
                    del patients[patient_index]
                    break

                elif op == 'no' or op == 'n':
                    break

                # unexpected entry
                else:
                    print('Please answer by yes or no.')
        
        elif op == '3':
            admin.view_discharge(discharged_patients)
            #ToDo4
            pass

        elif op == '4':
            # 4- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '5':
            # 5- Update admin detais
            admin.update_details()
            DB.UpdateUser(admin.get_username(), admin.get_password(), admin.get_address())
        elif op == '6':
            # 6 - Quit
            #ToDo5
            exit()

        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()
