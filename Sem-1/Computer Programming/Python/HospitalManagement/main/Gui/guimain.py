import tkinter as tk
from Admin import Admin
from Doctor import Doctor
from Patient import Patient
from databasemanagement import DATABASE


class guiManager:   
    def __init__(self, root):
        self.__Login_Status = False
        self.root = root
        self.root.geometry("800x800")
        self.root.title("Login Form")
        self.root.resizable(width=0, height=0)
        self.widgets = []


    def get_login_status(self):
        return self.__Login_Status
    
    def LoginFrame(self):
        #  Login Frame
        self.LoginFrame = tk.Frame(self.root, width=800, height=800,bg="#1f2640")
        self.LoginFrame.pack()

    def dashboardFrame(self):
        # Canvas for Dashboard screen
        self.Dashboard = tk.Frame(self.root, width=800, height=800,bg="#1f2640")
        self.Dashboard.pack()

        


    def loginSystem(self,admin):
        self.LoginFrame()
        self.username_label = tk.Label(self.LoginFrame, text="Username", font=("Arial", 16, "bold"), fg="white", bg="#1f2640")
        self.username_entry = tk.Entry(self.LoginFrame, font=("Helvetica", 14), fg="white", bg="#34495e")
        self.password_label = tk.Label(self.LoginFrame, text="Password", font=("Arial", 16, "bold"), fg="white", bg="#1f2640")
        self.password_entry = tk.Entry(self.LoginFrame, font=("Helvetica", 14), fg="white", bg="#34495e", show="*")
        self.login_button = tk.Button(self.LoginFrame, text="Login", font=("Arial", 14, "bold"), fg="white", bg="#34495e", command=lambda event: self.login_validation(admin))
        self.result_label = tk.Label(self.LoginFrame, text="", font=("Arial", 16), fg="red", bg="#1f2640")
        self.root.bind('<Return>', lambda event: self.login_validation(admin))


        # Placement
        self.username_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        self.password_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.username_entry.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
        self.password_entry.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
        self.login_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
        self.result_label.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

    def admin_dashboard(self):
        self.Dashboard = tk.Frame(self.root, width=800, height=800,bg="#1f2640")
        self.Dashboard.place(x=0,y=0)

    def login_validation(self,admin):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check the username and password
        if admin.login(username,password):
            self.result_label.config(text="Right password", fg='green')
            self.admin_dashboard()
        else:
            self.result_label.config(text="Wrong password", fg='red')

        # Clear the entry fields
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
    
    



def login(admin):
    root = tk.Tk()
    login_form = guiManager(root)
    login_form.loginSystem(admin)
    root.mainloop()




DB = DATABASE()




def main():
    DB.sort_patients()
    # Initialising the actors
    admin = DB.CreateAdmin() # username is 'root', password is 'root'
    doctors = DB.CreateDoctors()
    patients = DB.CreatePatients()
    discharged_patients = DB.discharged_patients()
    login(admin)

main()
