from Doctor import Doctor



class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address
    
    #Created by user to handle file management
    def get_username(self):
        return self.__username
    def get_password(self):
        return self.__password
    def get_address(self):
        return self.__address

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        #Get the details of the admin

        username = input('Enter the username: ')
        password = input('Enter the password: ')

        # check if the username and password match the registered ones
        #ToDo1
    # My work 1
        if self.__username == username and self.__password==password:
            return True
    

    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        #ToDo2
        self.__first_name = input('First name: ')
        self.__surname = input('Surname: ')
        self.__speciality = input('Speciality: ')
        return [self.__first_name, self.__surname, self.__speciality]

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """
        

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        #ToDo3
        op = input('> ')


        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            first_name, surname, speciality = self.get_doctor_details()


            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    print('Name already exists.')
                    #ToDo5
                    name_exists = True
                    break # save time and end the loop

            #ToDo6
            if name_exists == False:
                doctors.append(Doctor(first_name, surname, speciality))
                                                         # ... to the list of doctors
                print('Doctor registered.')

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            # ToDo7
            for doc in doctors:
                print(doc)


        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(index,doctors)
                    if doctor_index!=False:
                        
                        break
                        
                    else:
                        print("Doctor not found")

                    
                        # doctor_index is the ID mines one (-1)
                        

                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            op = int(input('Input: ')) # make the user input lowercase

            #ToDo8
            if op == 1:
                first_name = input('First name: ')
                doctors[index].set_first_name(first_name)
            elif op == 2:
                surname = input('Surname: ')
                doctors[index].set_surname(surname)
            elif op == 3:
                speciality = input('Speciality: ')
                doctors[index].set_speciality(speciality)

        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            doctor_index = int(input('Enter the ID of the doctor to be deleted: ')) -1
            #ToDo9
            
            if doctor_index >= 0 and doctor_index <= len(doctors):
                del doctors[doctor_index]
                print("Doctor Deleted")
            else:
                print('The id entered is incorrect')
        # if the id is not in the list of patients
        else:
            print('Invalid operation choosen. Check your spelling!')



    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)
    
    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        noDoctorPatients = []
        DoctorPatients = []
        for patient in patients:
            if patient.get_doctor() == 'None':
                noDoctorPatients.append(patient)
            else:
                DoctorPatients.append(patient)

        # print('Choose the field to be updated:')
        print(' 1 Assign a Doctor')
        print(' 2 Reassign new Doctor')
        option = input(' > ')
        if option == '1':
            print("-----Assign-----")

            print("-----Patients-----")
            print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
            self.view(noDoctorPatients)
            patient_index = input('Please enter the patient ID: ')
            symptoms = input('Please enter symptoms of the patients: ')
            patients[int(patient_index) - 1].set_symptoms(symptoms)
            try:
                # patient_index is the patient ID mines one (-1)
                patient_index = int(patient_index) -1

                # check if the id is not in the list of patients
                if patient_index not in range(len(patients)):
                    print('The id entered was not found.')
                    return # stop the procedures

            except ValueError: # the entered id could not be changed into an int
                print('The id entered is incorrect')
                return # stop the procedures

            print("-----Doctors Select-----")
            print('Select the doctor that fits these symptoms:')
            noDoctorPatients[patient_index].print_symptoms() # print the patient symptoms
            print('--------------------------------------------------')
            print('ID |          Full Name           |  Speciality   ')
            self.view(doctors)
            doctor_index = input('Please enter the doctor ID: ')

            try:
                # doctor_index is the patient ID mines one (-1)
                doctor_index = int(doctor_index) -1

                # check if the id is in the list of doctors
                if self.find_index(doctor_index,doctors)!=False:
                        
                    # link the patients to the doctor and vice versa
                    #ToDo11

                    noDoctorPatients[patient_index].link(doctors[doctor_index].full_name())
                    doctors[doctor_index].add_patient(patients[patient_index].full_name())
                    print('The patient is now assign to the doctor.')

                # if the id is not in the list of doctors
                else:
                    print('The id entered was not found.')

            except ValueError: # the entered id could not be changed into an in
                print('The id entered is incorrect')

        elif option == '2':
            print("-----Assign-----")

            print("-----Patients-----")
            print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
            self.view(DoctorPatients)
            patient_index = input('Please enter the patient ID: ')
            symptoms = input('Please enter symptoms of the patients: ')
            DoctorPatients[int(patient_index) - 1].set_symptoms(symptoms)
            try:
                # patient_index is the patient ID mines one (-1)
                patient_index = int(patient_index) -1

                # check if the id is not in the list of patients
                if patient_index not in range(len(patients)):
                    print('The id entered was not found.')
                    return # stop the procedures

            except ValueError: # the entered id could not be changed into an int
                print('The id entered is incorrect')
                return # stop the procedures

            print("-----Doctors Select-----")
            print('Select the doctor that fits these symptoms:')
            DoctorPatients[patient_index].print_symptoms() # print the patient symptoms

            print('--------------------------------------------------')
            print('ID |          Full Name           |  Speciality   ')
            self.view(doctors)
            doctor_index = input('Please enter the doctor ID: ')

            try:
                # doctor_index is the patient ID mines one (-1)
                doctor_index = int(doctor_index) -1

                # check if the id is in the list of doctors
                if self.find_index(doctor_index,doctors)!=False:
                        
                    # link the patients to the doctor and vice versa
                    #ToDo11

                    DoctorPatients[patient_index].link(doctors[doctor_index].full_name())
                    doctors[doctor_index].add_patient(patients[patient_index].full_name())
                    print('The patient is now assign to the doctor.')

                # if the id is not in the list of doctors
                else:
                    print('The id entered was not found.')

            except ValueError: # the entered id could not be changed into an in
                print('The id entered is incorrect')
        else:
            print('Something went wrong')
        
        patients = noDoctorPatients + DoctorPatients


    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----")
        #ToDo12
        self.view(patients)
        patient_index = int(input('Please enter the patient ID: ')) - 1 
        return patient_index
        


    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        #ToDo13
        self.view(discharged_patients)


    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
            #ToDo14
            self.__username = input("Enter the new Username: ")
        elif op == 2:
            password = input('Enter the new password: ')
            # validate the password
            if password == input('Enter the new password again: '):
                self.__password = password

        elif op == 3:
            #ToDo15
            self.__address = input("Enter the new address: ")

        else:
            #ToDo16
            print("Invalid input")

