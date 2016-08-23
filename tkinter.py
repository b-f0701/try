from tkinter import *

class Application (Frame):
    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.pack()
        self.creatWidgets()


    def creatWidgets(self):

        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self,text = 'hello',command = self.hello)
        self.alertButton.pack()
    def hello(self):
        name = self.nameInput.get()or'world'
        messagebox.showinfo('Message','hello,%s'%name)
'''     self.helloLaber = Label(self,text = 'hello world')
        self.helloLaber.pack()
        self.quitButton = Button(self,text = 'Quite')
        self.quitButton.pack()
'''

        
        
app = Application()
app.master.title('Hello World')
app.mainloop()
