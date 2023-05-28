from tkinter import *

class Calculator:
    def __init__(self,root):
        self.__total = 0
        self.root = root
        
        # Setting up the title
        root.title("Calculator")

        self.__total_label_text = IntVar()
        self.__total_label_text.set(self.__total)
        self.__total_label = Label(root, textvariable=self.__total_label_text)
        self.__Tlabel = Label(root, text="Total: ")
        self.__entry = Entry(root)

        self.__addition_button = Button(text='+', command=lambda: self.update("add"))
        self.__subtraction_button = Button(text='-', command=lambda: self.update("sub"))
        self.__reset_button = Button(text='Reset', command=lambda: self.update("reset"))
        
        self.__Tlabel.grid(row=0, column=0)
        self.__total_label.grid(row=0, column=1)
        self.__entry.grid(row=1, column=0)
        self.__addition_button.grid(row=2, column=0)
        self.__subtraction_button.grid(row=2, column=1)
        self.__reset_button.grid(row=2, column=2)
    
    def update(self, method):
        if method == "add":
            self.__total += float(self.__entry.get())
        elif method == "sub":
            self.__total -= float(self.__entry.get())
        else :
            self.__total = 0
        self.__total_label_text.set(self.__total)
        self.__entry.delete(0,END)

root = Tk()
my_gui = Calculator(root)
root.mainloop()

