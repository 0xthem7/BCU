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
    DB.sort_patients()
    # Initialising the actors
    admin = DB.CreateAdmin() # username is 'admin', password is '123'
    doctors = DB.CreateDoctors()
    patients = DB.CreatePatients()
    discharged_patients = DB.discharged_patients()
    
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
            DB.UpdateDoctor(doctors)
        elif op == '2':
            # 2- View or discharge patients
            #ToDo2
            try:
                patient_index = admin.discharge(patients, discharged_patients)
                while True:
                    op = input('Do you want to discharge a patient(Y/N):').lower()

                    if op == 'yes' or op == 'y':
                        #ToDo3
                        discharged_patients.append(patients[patient_index])
                        DB.add_discharged_patients(discharged_patients)
                        del patients[patient_index]
                        DB.Updatepatients(patients)
                        DB.sort_patients()
                        break

                    elif op == 'no' or op == 'n':
                        break

                    # unexpected entry
                    else:
                        print('Please answer by yes or no.')
            except:
                print('Something went wrong! Please check your input and Database')
            
        elif op == '3':
            admin.view_discharge(discharged_patients)
            

        elif op == '4':
            # 4- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)
            DB.Updatepatients(patients)
        elif op == '5':
            # 5- Update admin detais
            admin.update_details()
            DB.UpdateAdmin(admin.get_username(), admin.get_password(), admin.get_address())
        elif op == '6':
            # 6 - Quit
            #ToDo5
            exit()

        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()
