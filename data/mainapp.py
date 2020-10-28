import tkinter as tk
import tkinter.ttk as ttk
import defea as en

class NewprojectApp:
    def __init__(self, master=None):
        # build ui
        self.mainframe = tk.Frame(master)
        self.label_title = tk.Label(self.mainframe)
        self.label_title.config(background='#c2fcfc', font='{Calibri} 20 {}', justify='left', text="Wind's Password Manager")
        self.label_title.config(width='30')
        self.label_title.grid(columnspan='3', padx='20', sticky='n')
        self.frame_13 = tk.Frame(self.mainframe)
        self.frame_13.config(background='#c2fcfc', height='40', width='200')
        self.frame_13.grid(column='0', row='1')
        self.button_createPassword = tk.Button(self.mainframe)
        self.button_createPassword.config(font='{Calibri} 11 {}', text='Create New', width='20')
        self.button_createPassword.grid(column='0', padx='20', row='2', sticky='w')
        self.button_createPassword.configure(command=self.createPass)
        self.button_8 = tk.Button(self.mainframe)
        self.button_8.config(font='{Calibri} 11 {}', text='Show Selected', width='20')
        self.button_8.grid(column='0', padx='20', row='2', sticky='nw')
        self.button_8.configure(command=self.showPass)
        self.listbox_4 = tk.Listbox(self.mainframe)
        self.listbox_4.grid(column='2', row='2')
        self.button_deletePassword = tk.Button(self.mainframe)
        self.button_deletePassword.config(font='{Calibri} 11 {}', foreground='#f5010a', text='Delete', width='20')
        self.button_deletePassword.grid(column='0', padx='20', row='2', sticky='sw')
        self.button_deletePassword.configure(command=self.deletePass)
        self.frame_15 = tk.Frame(self.mainframe)
        self.frame_15.config(background='#c2fcfc', height='40', width='200')
        self.frame_15.grid(column='0', row='3')
        self.mainframe.config(background='#c2fcfc', height='200', width='200')
        self.mainframe.pack(side='top')

        # Main widget
        self.mainwindow = self.mainframe

    def createPass(self):
        print(en.encryptMsg("cool"))
        pass

    def showPass(self):
        pass

    def deletePass(self):
        pass

    def run(self):
        self.mainwindow.mainloop()
        

if __name__ == '__main__':
    import tkinter as tk
    root = tk.Tk()
    root.resizable(False,False)
    app = NewprojectApp(root)
    app.run()

