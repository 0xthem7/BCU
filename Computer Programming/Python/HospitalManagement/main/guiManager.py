from tkinter import *


class GUI(Tk):
    def __init__(self):
        super().__init__()
        
        # Configuring windows
        self.title('Doctor Mangement')
        self.geometry('300x200')

        #Login screen Widget creation
        self.LoginLabel = Label(self, text="Login Screen")
        
        self.UsernameLabel = Label(self, text="Username")
        self.PasswordLabel = Label(self, text="Password")
        # self.label

        # Placement
        self.LoginLabel.grid(row=1,column=1)
        self.UsernameLabel.place(relx=0.5, rely=5, anchor=CENTER)
        self.PasswordLabel.place(relx=0.5, rely=10, anchor=CENTER)


if __name__ == "__main__":
    app = GUI()
    app.mainloop()