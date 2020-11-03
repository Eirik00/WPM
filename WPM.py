import tkinter as tk
import tkinter.ttk as ttk
from os import walk, remove, mkdir, path

#################This is the encryption tab#####################
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," ",".",",",":",";","1","2","3","4","5","6","7","8","9","0","!","?","#","=","+"]
encrypte = ["3","O","¤","k","£","n","Y","€","j","h","#","M","v","å","2","g","*","c","?","r","e","'","s","z","a","q",">","~","´","Å","ø","N","Ä","ñ","ô","|","@","$","{",")","L","?","6","P","<",'"',"ɇ","ƒ","Œ","¥","¦","ª",";","1","(","Æ","$","¼","§",".","¿","À","ē","Ŧ","ƨ","ǟ","ȼ","¾","Ü","±","³","®"]

def encryptMsg(msg):
    nwMsg = ""
    for x in msg:
        letter = alphabet.index(x)
        nwMsg = nwMsg + encrypte[letter]
    return nwMsg

def decryptMsg(msg):
    nwMsg = ""
    for x in msg:
        i = encrypte.index(x)
        nwMsg = nwMsg + alphabet[i]
    return nwMsg
#################################################################

pinCode = ""
passwarned = False
passwordsArray = []
ShowPasshidden = 1
class NewprojectApp:
    def __init__(self, master=None):
        # build ui
        self.main_frame = tk.Frame(master)
        self.title = tk.Label(self.main_frame)
        self.title.config(activebackground='#beeffa', background='#beeffa', compound='top', font='{Calibri} 20 {}')
        self.title.config(foreground='#000000', justify='center', text="Wind's Password Manager")
        self.title.grid(column='0', row='1', sticky='n')
        self.title.rowconfigure('1', minsize='0')
        
        self.pincode_button = tk.Button(self.main_frame)
        self.pincode_button.config(compound='bottom', font='{Calibri} 10 {bold}', foreground='#000000', justify='center')
        self.pincode_button.config(takefocus=False, text='Enter', width='7')
        self.pincode_button.grid(column='0', row='3', sticky='se')
        
        self.entry_pincode = tk.Entry(self.main_frame)
        self.entry_pincode.config(background='#ffffff', borderwidth='2', font='{Times New Roman Baltic} 11 {}', foreground='#000000')
        self.entry_pincode.config(relief='raised', show='•', validate='none', width='8')
        self.entry_pincode.grid(column='0', row='3', sticky='s')
        self.pincode_button.configure(command=self.pinCodeEntered)
        
        self.pincode = tk.Label(self.main_frame)
        self.pincode.config(background='#beeffa', compound='top', font='{Segoe UI} 12 {}', text='Enter your PIN')
        self.pincode.grid(column='0', row='3', sticky='sw')
        
        self.info = ttk.Label(self.main_frame)
        self.info.config(anchor='center', background='#beeffa', compound='top', font='{Calibri} 12 {}')
        self.info.config(justify='center', text='Login')
        self.info.grid(column='0', row='2')
        self.info_creator = ttk.Label(self.main_frame)
        self.info_creator.config(text='Made by Wind 2020')
        self.info_creator.grid(column='0', row='5', sticky='se')
        
        self.frame_6 = tk.Frame(self.main_frame)
        self.frame_6.config(background='#beeffa', height='20', width='200')
        self.frame_6.grid(column='0', row='4')
        self.label_warning = tk.Label(self.main_frame)
        self.label_warning.destroy()
        
        self.main_frame.config(background='#beeffa', cursor='arrow', height='200', width='200')
        self.main_frame.grid()

        # Main widget
        self.mainwindow = self.main_frame


    def run(self):
        if not path.isfile("LOCALSAVE/"):
            mkdir("LOCALSAVE/")
        self.mainwindow.mainloop()

    def pinCodeEntered(self):
        global tk
        pinCode = self.entry_pincode.get()
        f = open("pincode.txt", "r")
        testcode = f.read()
        if pinCode == testcode:
            print("correct")
            qutiMainWindow()
            
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
                    self.button_createPassword.grid(column='0', padx='20', row='2', sticky='nw')
                    self.button_createPassword.configure(command=self.createsPass)
                    self.button_8 = tk.Button(self.mainframe)
                    self.button_8.config(font='{Calibri} 11 {}', text='Show Selected', width='20')
                    self.button_8.grid(column='0', padx='20', row='2', sticky='w')
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
                    self.button_1 = tk.Button(self.mainframe)
                    self.button_1.config(font='{Calibri} 10 {bold}', text='Refresh')
                    self.button_1.grid(column='2', padx='22', row='3', sticky='nw')
                    self.button_1.configure(command=self.refreshList)
                    self.mainframe.config(background='#c2fcfc', height='200', width='200')
                    self.mainframe.pack(side='top')

                    # Main widget
                    self.mainwindow = self.mainframe

                def createsPass(self):
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
                            global passwarned
                            name = self.entry_1.get()
                            if name == "":
                                if passwarned == True:
                                    self.label_warning.destroy()
                                else:
                                    self.label_warning = tk.Label(self.create_password_window)
                                    self.label_warning.config(font='{Courier} 10 {bold}', foreground='#ff4246', text="Can't save a blank name!!")
                                    self.label_warning.grid(column='1', row='7', sticky='e')
                                    passwarned = True
                            else:
                                username = self.entry_2.get()
                                password = self.entry_3.get()
                                f = open("LOCALSAVE/" + name + ".dll", "w")
                                f.write(encryptMsg(username + ":" + password))
                                f.close()
                                root.destroy()

                        def run(self):
                            self.mainwindow.mainloop()

                    if __name__ == '__main__':
                        import tkinter as tk
                        root = tk.Tk()
                        root.resizable(False,False)
                        root.title("WPM Create Password")
                        app = NewprojectApp(root)
                        app.run()
                    pass

                def showPass(self):
                    if self.listbox_4.get(self.listbox_4.curselection()):
                        active = self.listbox_4.get(self.listbox_4.curselection())
                        class ShowPass:
                            def __init__(self, master=None):
                                # build ui
                                self.frame_1 = tk.Frame(master)
                                self.label_1 = tk.Label(self.frame_1)
                                self.label_1.config(text='Username')
                                self.label_1.grid(sticky='w')
                                self.entry_1 = tk.Entry(self.frame_1)
                                self.entry_1.grid(column='0', row='1')
                                _text_ = active.split(":")[0]
                                self.entry_1.delete('0', 'end')
                                self.entry_1.insert('0', _text_)
                                self.label_2 = tk.Label(self.frame_1)
                                self.label_2.config(text='Password')
                                self.label_2.grid(column='0', row='3', sticky='w')
                                self.entry_2 = tk.Entry(self.frame_1)
                                self.entry_2.config(show='*')
                                self.entry_2.grid(column='0', row='4')
                                passfile = open("LOCALSAVE/" + active.split(":")[1])
                                passwordeaf = decryptMsg(passfile.read())
                                _text_ = passwordeaf.split(":")[1]
                                self.entry_2.delete('0', 'end')
                                self.entry_2.insert('0', _text_)
                                self.button_2 = tk.Button(self.frame_1)
                                self.button_2.config(text='show')
                                self.button_2.grid(column='0', row='3')
                                self.button_2.configure(command=self.changeVisibility)
                                self.frame_2 = tk.Frame(self.frame_1)
                                self.frame_2.config(height='20', width='200')
                                self.frame_2.grid(column='0', row='2')
                                self.frame_1.config(borderwidth='20', height='200', width='200')
                                self.frame_1.pack(side='top')

                                # Main widget
                                self.mainwindow = self.frame_1

                            def changeVisibility(self):
                                global ShowPasshidden
                                if ShowPasshidden == 1:
                                    self.entry_2.config(show='')
                                    self.button_2.config(text="hide")
                                    ShowPasshidden = 0
                                else:
                                    self.entry_2.config(show='*')
                                    self.button_2.config(text="show")
                                    ShowPasshidden = 1
                            
                            def run(self):
                                self.mainwindow.mainloop()

                        if __name__ == '__main__':
                            import tkinter as tk
                            root = tk.Tk()
                            root.resizable(False,False)
                            root.title("WPM Show Password")
                            app = ShowPass(root)
                            app.run()

                def deletePass(self):
                    active = self.listbox_4.get(self.listbox_4.curselection())
                    if active.split(":")[1] == "":
                        print("file name error")
                    else:
                        remove("LOCALSAVE/" + active.split(":")[1])
                        self.listbox_4.delete(self.listbox_4.get(0, tk.END).index(active))

                def refreshList(self):
                    self.listbox_4.delete(0, tk.END)
                    for root, dirs, files in walk("LOCALSAVE/"):
                        for file in files:
                            if file.endswith(".dll"):
                                fb = open("LOCALSAVE/" + file, "r")
                                passwordsArray.append("file")
                                eafe = decryptMsg(fb.read())
                                self.listbox_4.insert(tk.END, eafe.split(":")[0] + ":" + file)
                                fb.close()
                    
                def run(self):
                    for root, dirs, files in walk("LOCALSAVE/"):
                        for file in files:
                            if file.endswith(".dll"):
                                fb = open("LOCALSAVE/" + file, "r")
                                passwordsArray.append("file")
                                eafe = decryptMsg(fb.read())
                                self.listbox_4.insert(tk.END, eafe.split(":")[0] + ":" + file)
                                fb.close()
                    print("test")
                    self.mainwindow.mainloop()
                    

            if __name__ == '__main__':
                import tkinter as tk
                root = tk.Tk()
                root.resizable(False,False)
                root.title("Wind's Password Manager")
                app = NewprojectApp(root)
                app.run()

            
        else:
            print("failed")
            if self.label_warning.winfo_exists():
                self.label_warning.destroy()
                
                self.label_warning = tk.Label(self.main_frame)
                self.label_warning.config(background='#beeffa', font='{Courier} 10 {}', foreground='#ff0000', text='Wrong PIN')
                self.label_warning.grid(column='0', row='4', sticky='w')
            else:
                self.label_warning = tk.Label(self.main_frame)
                self.label_warning.config(background='#beeffa', font='{Courier} 10 {}', foreground='#ff0000', text='Wrong PIN')
                self.label_warning.grid(column='0', row='4', sticky='w')

if __name__ == '__main__':
    import tkinter as tk
    root = tk.Tk()
    root.resizable(False,False)
    root.title("WPM Log Inn")
    def qutiMainWindow():
        root.destroy()
    
    app = NewprojectApp(root)
    app.run()
