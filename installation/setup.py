import tkinter as tk
import tkinter.ttk as ttk
from os import remove, rename, rmdir

#################This is the encryption tab#####################
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," ",".",",",":",";","1","2","3","4","5","6","7","8","9","0","!","?","#","=","+"]
encrypte = ["3","O","¤","k","£","n","Y","€","j","h","#","M","v","å","2","g","*","c","?","r","e","'","s","z","a","q",">","~","´","Å","ø","N","Ä","ñ","ô","|","@","$","{",")","L","?","6","P","<",'"',"ɇ","ƒ","Œ","¥","¦","ª",";","1","(","Æ","$","¼","§",".","¿","À","ē","Ŧ","ƨ","ǟ","ȼ","¾","Ü","±","³","®"]

def encryptMsg(msg):
    nwMsg = ""
    for x in msg:
        letter = alphabet.index(x)
        nwMsg = nwMsg + encrypte[letter]
    return nwMsg

#################################################################

class MainappApp:
    def __init__(self, master=None):
        # build ui
        self.mainframe = tk.Frame(master)
        self.label_title = tk.Label(self.mainframe)
        self.label_title.config(background='#ffffff', font='{Calibri} 20 {}', justify='left', text="Wind's Password Manager Setup", width='30')
        self.label_title.grid(columnspan='3', padx='20', sticky='n')
        self.cancel = tk.Button(self.mainframe)
        self.cancel.config(compound='top', font='{Calibri} 11 {}', justify='left', text='Cancel', width='20')
        self.cancel.grid(column='0', padx='20', row='3', sticky='w')
        self.cancel.configure(command=self.cancelScript)
        self.install = tk.Button(self.mainframe)
        self.install.config(font='{Calibri} 11 {}', justify='left', text='Continue', width='20')
        self.install.grid(column='1', padx='20', row='3', sticky='ne')
        self.install.configure(command=self.installScript)
        self.frame_1 = tk.Frame(self.mainframe)
        self.frame_1.config(background='#ffffff', height='40', width='200')
        self.frame_1.grid(column='0', row='4')
        self.text_1 = tk.Text(self.mainframe)
        self.text_1.config(background='#e9e9e9', exportselection='true', foreground='#000000', height='13', state='disabled', tabstyle='wordprocessor', width='50', wrap='none')
        _text_ = '''!!
ONLY DOWNLOAD THIS FROM:
https://github.com/Eirik00/Wind-s-Password-Manager
!!

This is a password manager , it's not supposed to 
harm your computer. If you downloaded this from
the correct github, then you should be fine. 
When downloading you understand that any malicous 
issues or problems that occur after the install,
is not my responsibility.
This is just a python application and full source
code can be found on the github!
'''
        self.text_1.configure(state='normal')
        self.text_1.insert('0.0', _text_)
        self.text_1.configure(state='disabled')
        self.text_1.grid(column='0', columnspan='2', row='1')
        self.frame_2 = tk.Frame(self.mainframe)
        self.frame_2.config(background='#ffffff', height='40', width='200')
        self.frame_2.grid(column='0', row='2')
        self.mainframe.config(background='#ffffff', height='200', width='200')
        self.mainframe.pack(side='top')

        # Main widget
        self.mainwindow = self.mainframe

    def cancelScript(self):
        quitMainWindow()

    def installScript(self):
        global tk
        quitMainWindow()
        class SetupApp:
            def __init__(self, master=None):
                # build ui
                self.mainframe = tk.Frame(master)
                self.label_title = tk.Label(self.mainframe)
                self.label_title.config(background='#ffffff', font='{Calibri} 20 {}', justify='left', text='Create your pincode')
                self.label_title.config(width='30')
                self.label_title.grid(columnspan='3', padx='20', sticky='n')
                self.createPin = tk.Button(self.mainframe)
                self.createPin.config(cursor='arrow', font='{Calibri} 11 {}', text='Continue', width='20')
                self.createPin.grid(column='0', columnspan='3', padx='20', row='3')
                self.createPin.configure(command=self.install2)
                self.frame_1 = tk.Frame(self.mainframe)
                self.frame_1.config(background='#ffffff', height='40', width='200')
                self.frame_1.grid(column='0', row='4')
                self.frame_2 = tk.Frame(self.mainframe)
                self.frame_2.config(background='#ffffff', height='40', width='200')
                self.frame_2.grid(column='0', row='2')
                self.pinCode = tk.Entry(self.mainframe)
                self.pinCode.grid(column='0', columnspan='3', row='2')
                self.mainframe.config(background='#ffffff', height='200', width='200')
                self.mainframe.pack(side='top')

                # Main widget
                self.mainwindow = self.mainframe

            def install2(self):
                pinCode = self.pinCode.get()
                f = open("pincode.wpk", mode="w")
                f.write(encryptMsg(pinCode))
                f.close()
                rename("FILELOCATION/WPM.hex", "wpm.exe")
                rmdir("FILELOCATION")
                rename("setup.exe", "DELETEME")
                quiteMainWindow()

            def run(self):
                self.mainwindow.mainloop()

        if __name__ == '__main__':
            import tkinter as tk
            root = tk.Tk()
            def quiteMainWindow():
                root.destroy()
                
            app = SetupApp(root)
            app.run()

    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':
    import tkinter as tk
    root = tk.Tk()
    def quitMainWindow():
        root.destroy()
        
    app = MainappApp(root)
    app.run()

