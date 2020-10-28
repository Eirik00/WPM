import tkinter as tk
import tkinter.ttk as ttk
import sys


pinCode = ""
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
        pinCode = self.entry_pincode.get()
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
        
        self.main_frame.config(background='#beeffa', cursor='arrow', height='200', width='200')
        self.main_frame.grid()

        # Main widget
        self.mainwindow = self.main_frame


    def run(self):
        self.mainwindow.mainloop()

    def pinCodeEntered(self):
        f = open("pincode.txt", "r")
        print(f.read()) #uuuh, why does this has to be here for it to work!?
        if pinCode == f.read():
            print("correct")
            root.destroy()
            sys.path.append("data/")
            #setting new path
            import defea as en
            
            stream = open("data/mainapp.py")
            read_file = stream.read()
            exec(read_file)
        else:
            print("failed")

if __name__ == '__main__':
    import tkinter as tk
    root = tk.Tk()
    root.resizable(False,False)
    app = NewprojectApp(root)
    app.run()
