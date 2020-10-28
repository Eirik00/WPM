import defea as en

warned = False
class NewprojectApp:
    def __init__(self, master=None):
        # build ui
        self.create_password_window = ttk.Frame(master)
        self.label_1 = ttk.Label(self.create_password_window)
        self.label_1.config(font='{Calibri} 20 {}', text='Create Password')
        self.label_1.grid(columnspan='2', sticky='nw')
        self.label_1.columnconfigure('0', weight='0')
        self.label_2 = ttk.Label(self.create_password_window)
        self.label_2.config(font='{Courier} 9 {}', text='Creating a new password is really simple!\nJust write inn the name of the password,\nusername and the password!')
        self.label_2.grid(column='0', columnspan='2', row='1')
        self.label_2.columnconfigure('0', weight='0')
        self.entry_1 = ttk.Entry(self.create_password_window)
        self.entry_1.config(width='30')
        self.entry_1.grid(column='0', row='2', sticky='w')
        self.entry_1.columnconfigure('0', weight='0')
        self.label_name = ttk.Label(self.create_password_window)
        self.label_name.config(font='{Calibri} 11 {}', padding='0', relief='flat', text='Name')
        self.label_name.grid(column='1', padx='0', row='2', sticky='w')
        self.label_name.columnconfigure('0', weight='0')
        self.entry_2 = ttk.Entry(self.create_password_window)
        self.entry_2.config(width='30')
        self.entry_2.grid(column='0', row='3', sticky='w')
        self.label_username = ttk.Label(self.create_password_window)
        self.label_username.config(font='{Calibri} 11 {}', text='Username')
        self.label_username.grid(column='1', row='3', sticky='w')
        self.entry_3 = ttk.Entry(self.create_password_window)
        self.entry_3.config(show='•', width='30')
        self.entry_3.grid(column='0', row='4', sticky='w')
        self.label_password = ttk.Label(self.create_password_window)
        self.label_password.config(font='{Calibri} 11 {}', text='Password')
        self.label_password.grid(column='1', row='4', sticky='w')
        self.frame_2 = ttk.Frame(self.create_password_window)
        self.frame_2.config(height='20', width='200')
        self.frame_2.grid(column='0', row='5')
        self.button_cancel = ttk.Button(self.create_password_window)
        self.button_cancel.config(text='Cancel')
        self.button_cancel.grid(column='0', row='6', sticky='w')
        self.button_cancel.configure(command=self.cancel)
        self.button_create = ttk.Button(self.create_password_window)
        self.button_create.config(text='Create')
        self.button_create.grid(column='1', row='6', sticky='e')
        self.button_create.configure(command=self.createpass)
        self.create_password_window.config(height='200', padding='10', width='200')
        self.create_password_window.pack(side='top')

        # Main widget
        self.mainwindow = self.create_password_window

    def cancel(self):
        pass

    def createpass(self):
        name = self.entry_1.get()
        if name == "":
            if warned:
                self.label_warning.destroy()
            else:
                self.label_warning = tk.Label(self.create_password_window)
                self.label_warning.config(font='{Courier} 10 {bold}', foreground='#ff4246', text="Can't save a blank name!!")
                self.label_warning.grid(column='1', row='7', sticky='e')
                warned = True
        else:
            username = self.entry_2.get()
            password = self.entry_3.get()
            f = open("LOCALSAVED/" + name + ".dll", "w")
            f.write(en.encryptMsg(username + ":" + password)
            f.close()
            root.destroy()

    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':
    import tkinter as tk
    root = tk.Tk()
    app = NewprojectApp(root)
    app.run()

