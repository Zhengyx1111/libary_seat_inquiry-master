#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
try:
    from tkinter import *
except ImportError:  #Python 2.x
    PythonVersion = 2
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else:  #Python 3.x
    PythonVersion = 3
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('Form1')
        self.master.geometry('1350x730')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('Label1.TLabel',anchor='w', font=('宋体',9))
        self.Label1 = Label(self.top, text='图书馆学生座位实时统计', style='Label1.TLabel')
        self.Label1.place(relx=0., rely=0.011, relwidth=0.107, relheight=0.023)

        self.Text1Var = StringVar(value='')
        self.Text1 = Entry(self.top, textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.place(relx=0.047, rely=0.044, relwidth=0.125, relheight=0.034)

        self.style.configure('Command1.TButton',font=('宋体',9))
        self.Command1 = Button(self.top, command=self.Command1_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.261, rely=0.044, relwidth=0.042, relheight=0.045)

        self.style.configure('Label2.TLabel',anchor='w', font=('宋体',9))
        self.vaffff = StringVar(value='212121')
        self.Label2 = Label(self.top, text='选择时间',textvariable=self.vaffff, style='Label2.TLabel')
        self.Label2.place(relx=0.006, rely=0.044, relwidth=0.042, relheight=0.034)

        self.Text2Var = StringVar(value='')
        self.Text2 = Entry(self.top, textvariable=self.Text2Var, font=('宋体',9))
        self.Text2.place(relx=0.178, rely=0.044, relwidth=0.048, relheight=0.034)

        self.style.configure('Label3.TLabel',anchor='w', font=('宋体',9))
        self.Label3 = Label(self.top, text='label3', style='Label3.TLabel')
        self.Label3.place(relx=0.16, rely=0.263, relwidth=0.238, relheight=0.199)

        self.style.configure('Label4.TLabel',anchor='w', font=('宋体',9))
        self.Label4 = Label(self.top, text='Label4', style='Label4.TLabel')
        self.Label4.place(relx=0.587, rely=0.263, relwidth=0.226, relheight=0.21)

        self.style.configure('Label5.TLabel',anchor='w', font=('宋体',9))
        self.Label5 = Label(self.top, text='Label5', style='Label5.TLabel')
        self.Label5.place(relx=0.142, rely=0.559, relwidth=0.273, relheight=0.21)

        self.style.configure('Label6.TLabel',anchor='w', font=('宋体',9))
        self.Label6 = Label(self.top, text='Label6', style='Label6.TLabel')
        self.Label6.place(relx=0.581, rely=0.57, relwidth=0.226, relheight=0.188)

        self.style.configure('Label7.TLabel',anchor='w', font=('宋体',9))
        self.Label7 = Label(self.top, text='Label7楼层', style='Label7.TLabel')
        self.Label7.place(relx=0.361, rely=0.822, relwidth=0.208, relheight=0.056)




class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)
        self.var=StringVar(value='111111111111111')


    def Command1_Cmd(self, event=None):
        #TODO, Please finish the function here!
        self.str1=self.Text1Var.get()
        self.vaffff.set(self.str1)
        #print( int('213213'))

        pass

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
    try: top.destroy()
    except: pass
