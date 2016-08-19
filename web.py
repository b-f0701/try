# -*- coding:utf-8 -*-

import tkinter
import urllib.request

class Window:
    def __init__(self,root):
        self.root = root
        self.entryUrl = tkinter.Entry(root)
        self.entryUrl.place(x=5,y=15)
        self.get = tkinter.Button(root,
                                  text='下载页面',
                                  command =self.Get)
        self.get.place(x= 160,y=12)
        self.edit = tkinter.Text (root)
        self.edit.place(x=5,y=50)
    def Get(self):
        url = self.entryUrl.get()
        page = urllib.request.urlopen(url)
        data = page.read()
        self.edit.insert(tkinter.END,data)
        page.close()
root= tkinter.Tk()
window = Window(root)
root.minsize(580,380)
root.mainloop()
                         
