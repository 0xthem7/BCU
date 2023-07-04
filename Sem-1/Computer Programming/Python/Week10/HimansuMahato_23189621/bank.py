class Customer:
    def __init__(self, cID, first_name, second_name, address, balance):
        self.__cID = cID
        self.__first_name = first_name
        self.__second_name = second_name
        self.__address = address
        self.__balance = balance
    
    def get_cID(self):
        return self.__cID

    def set_cID(self, c_id):
        self.__cID = c_id

    def get_first_name(self):
        return self.__first_name


    def set_(self,  f_name):
        self.__first_name = f_name
        

    def get_second_name(self):
        return self.__second_name


    def set_second_name(self, s_name):
        self.__second_name = s_name

    def get_address(self):
        return self.__address

    def set_address(self, addObj):
        self.__address =addObj

    def get_balance(self):
        return self.__balance
   
    def set_balance(self, value):
        self.__balance = value

    def deposite(self,value):
        self.__balance+=value

    def withdraw(self,value):
        self.__balance-=value

    def check_balnce(self):
        return self.__balance 

class Address:
    def __init__(self, number, street, town, post_code):
        self.__number = number
        self.__street = street
        self.__town = town
        self.__post_code = post_code
  
    def get_number(self):
        return self.__number
  
    def set_number(self, value):
        self.__number = value

  
    def get_street(self):
        return self.__street
    
    def set_street(self, value):
        self.__street = value

 
    def get_town(self):
        return self.__town
 
    def set_town(self, value):
        self.__town = value

  
    def get_post_code(self):
        return self.__post_code
    
    def set_post_code(self, value):
        self.__post_code = value

    def change_address(self,new_address):
        self.number = new_address.number
        self.street = new_address.street
        self.town = new_address.town
        self.post_code= new_address.post_code

    def __str__(self):
        return f"{self.__number},{self.__street},{self.__town},{self.__post_code}"

def new_customer():

    cid= int(input("Enter customer id number: "))
    f_name= input( "Enter first name: ")
    s_name= input("Enter second name: ")
    adres = input("Enter address (number, street, town, postCode): ")
    while len(adres.split(',')) != 4:
        adres = input( "Please re-enter address (number, street, town, postCode): ")
    a = adres.split(',')
    print(a)
    balance = float(input( "Enter balance: "))
    return Customer(cID, first_name, second_name, Address(a), balance)
    

c = Customer('12A','Anna','Duka',Address(42,'Curzon Street','Birmingham', 'B4 2SU'),888)


def save_cRecords(lst):
    try: 
        with open('customerList.txt','a') as file:
            for client in lst:
                file.write(f"{client.get_cID()},{client.get_first_name()},{client.get_second_name()},{str(client.get_address())},{client.get_balance()}\n")
        file.close()
    except:
        return False
    else:
        return True




c1 = Customer('12A','Rea','Koci',Address('42','Curzon Street','Birmingham', 'B4 2SU'),888)
c2 = Customer('11A','Liora','Koci',Address('42b','Curzon Street2','Birmingham2', 'B4 2SU'),33)

save_cRecords([c1,c2])


def read_customerRecords(from_file):
    try:
        with open(from_file,'r') as file:
            data = file.readlines()
        file.close()
        return data
    except FileNotFoundError:
        print('File not found')


print(read_customerRecords('client_list.txt'))
print(read_customerRecords('customerList.txt'))





