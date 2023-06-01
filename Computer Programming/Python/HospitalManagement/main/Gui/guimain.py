import tkinter as tk
from Admin import Admin
from Doctor import Doctor
from Patient import Patient
from databasemanagement import DATABASE


class guiManager:   
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x800")
        self.root.title("Login Form")
        self.root.resizable(width=0, height=0)
        self.widgets = []


    
    def background(self):
        #  Canvas for login screen
        self.canvasLogin = tk.Canvas(self.root, width=800, height=800)
        self.canvasLogin.pack()
        gradient_id = self.canvasLogin.create_rectangle(0, 0, 800, 800, fill="#1f2640", width=0)
        self.canvasLogin.tag_lower(gradient_id)
    
    def dashboardFrame(self):
        # Canvas for Dashboard screen
        self.canvasDashboard = tk.Canvas(self.root, width=800, height=800)
        self.canvasDashboard.pack()
        gradient_id = self.canvasDashboard.create_rectangle(0, 0, 800, 800, fill="#1f2640", width=0)
        self.canvasDashboard.tag_lower(gradient_id)

        


    def loginSystem(self,admin):
        self.background()
        self.username_label = tk.Label(self.canvasLogin, text="Username", font=("Arial", 16, "bold"), fg="white", bg="#1f2640")
        self.username_entry = tk.Entry(self.canvasLogin, font=("Helvetica", 14), fg="white", bg="#34495e")
        self.password_label = tk.Label(self.canvasLogin, text="Password", font=("Arial", 16, "bold"), fg="white", bg="#1f2640")
        self.password_entry = tk.Entry(self.canvasLogin, font=("Helvetica", 14), fg="white", bg="#34495e", show="*")
        self.login_button = tk.Button(self.canvasLogin, text="Login", font=("Arial", 14, "bold"), fg="white", bg="#34495e", command=lambda event: self.login_validation(admin))
        self.result_label = tk.Label(self.canvasLogin, text="", font=("Arial", 16), fg="red", bg="#1f2640")
        self.root.bind('<Return>', lambda event: self.login_validation(admin))


        # Placement
        self.username_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        self.password_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.username_entry.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
        self.password_entry.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
        self.login_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
        self.result_label.place(relx=0.5, rely=0.65, anchor=tk.CENTER)


    def clear_widgets(self):
        for widget in self.widgets:
            widget.pack_forget()
        self.widgets = []

    
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
    
    def admin_dashboard(self):
        self.dashboardBackground()
        self.username_label = tk.Label(self.canvasDashboard, text="test", font=("Arial", 16, "bold"), fg="white", bg="#1f2640")
        self.username_entry = tk.Entry(self.canvasDashboard, font=("Helvetica", 14), fg="white", bg="#34495e")
        self.password_label = tk.Label(self.canvasDashboard, text="Password", font=("Arial", 16, "bold"), fg="white", bg="#1f2640")
        self.password_entry = tk.Entry(self.canvasDashboard, font=("Helvetica", 14), fg="white", bg="#34495e", show="*")
        # self.login_button = tk.Button(self.canvasLogin, text="test1", font=("Arial", 14, "bold"), fg="white", bg="#34495e", command=lambda event: self.login_validation(admin))
        self.result_label = tk.Label(self.canvasDashboard, text="test2", font=("Arial", 16), fg="red", bg="#1f2640")
        

        self.username_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        self.password_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.username_entry.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
        self.password_entry.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
        # self.login_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
        self.result_label.place(relx=0.5, rely=0.65, anchor=tk.CENTER)


def login(admin):
    root = tk.Tk()
    login_form = guiManager(root)
    # login_form.background()
    login_form.loginSystem(admin)
    root.mainloop()




DB = DATABASE()




def main():
    DB.sort_patients()
    # Initialising the actors
    admin = DB.CreateAdmin() # username is 'admin', password is '123'
    doctors = DB.CreateDoctors()
    patients = DB.CreatePatients()
    discharged_patients = DB.discharged_patients()
    # login(admin)
    if login(admin):
        clear_widget()


main()