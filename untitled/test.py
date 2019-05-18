#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
import datetime
import search as sea
import tkinter.messagebox


from tkinter import *
#import tkinter.messagebox
from tkinter.font import Font
from tkinter.ttk import *
#from tkinter.messagebox import *


class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None,**kwargs):
        Frame.__init__(self, master)
        self.master.title('Form1')
        self.master.geometry('1225x698')
        self.master["bg"] = "OldLace"
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.Text2Var = StringVar(value='月（1-12）')
        self.Text2 = Entry(self.top, text='月',textvariable=self.Text2Var, font=('宋体',9))
        self.Text2.place(relx=0.111, rely=0.046, relwidth=0.05, relheight=0.036)

        self.style.configure('Command1.TButton',font=('宋体',9))
        self.Command1 = Button(self.top, command=self.Command1_Cmd, text='确定', style='Command1.TButton')
        self.Command1.place(relx=0.366, rely=0.046, relwidth=0.047, relheight=0.047)

        self.Text1Var = StringVar(value='年（2019）')
        self.Text1 = Entry(self.top, text='年', textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.place(relx=0.058, rely=0.046, relwidth=0.049, relheight=0.036)

        self.style.configure('Label7.TLabel',anchor='center', font=('宋体',9))
        self.varlabel7 = StringVar(value='')
        self.Label7 = Label(self.top, text='Label7roomid' , background = 'BlanchedAlmond',textvariable=self.varlabel7 , style='Label7.TLabel')
        self.Label7.place(relx=0.338, rely=0.92, relwidth=0.229, relheight=0.059)

        self.style.configure('Label6.TLabel',anchor='center', font=('宋体',9))
        self.varlabel6 = StringVar(value='')
        self.Label6 = Label(self.top, text='Label6',background = 'white',textvariable=self.varlabel6 ,style='Label6.TLabel')
        self.Label6.place(relx=0.547, rely=0.596, relwidth=0.351, relheight=0.219)

        self.style.configure('Label5.TLabel',anchor='center', font=('宋体',9))
        self.varlabel5 = StringVar(value='')
        self.Label5 = Label(self.top, text='Label5',background = 'white', textvariable=self.varlabel5 ,style='Label5.TLabel')
        self.Label5.place(relx=0.076, rely=0.585, relwidth=0.351, relheight=0.219)

        self.style.configure('Label4.TLabel',anchor='center', font=('宋体',9))
        self.varlabel4 = StringVar(value='')
        self.Label4 = Label(self.top, text='',background = 'white',textvariable=self.varlabel4 ,style='Label4.TLabel')
        self.Label4.place(relx=0.547, rely=0.275, relwidth=0.351, relheight=0.219)

        self.style.configure('Label3.TLabel',anchor='center', font=('宋体',9))
        self.varlabel3 = StringVar(value='')
        self.Label3 = Label(self.top, text='label3', background = 'white',textvariable=self.varlabel3 , style='Label3.TLabel')
        self.Label3.place(relx=0.076, rely=0.275, relwidth=0.351, relheight=0.219)

        self.style.configure('Label2.TLabel',anchor='w', font=('宋体',9))
        self.Label2 = Label(self.top, text='选择时间', style='Label2.TLabel')
        self.Label2.place(relx=0.007, rely=0.046, relwidth=0.047, relheight=0.036)

        self.style.configure('Label1.TLabel',anchor='w', font=('宋体',9))
        self.Label1 = Label(self.top, text='图书馆学生座位实时统计', style='Label1.TLabel')
        self.Label1.place(relx=0., rely=0.011, relwidth=0.118, relheight=0.024)

        self.Text3Var = StringVar(value='日（1-31）')
        self.Text3 = Entry(self.top, text='日', textvariable=self.Text3Var, font=('宋体',9))
        self.Text3.place(relx=0.176, rely=0.046, relwidth=0.057, relheight=0.037)

        self.Text4Var = StringVar(value='时（0-24）')
        self.Text4 = Entry(self.top, text='时', textvariable=self.Text4Var, font=('宋体',9))
        self.Text4.place(relx=0.235, rely=0.046, relwidth=0.05, relheight=0.036)

        self.Text5Var = StringVar(value='分(0-60)')
        self.Text5 = Entry(self.top, text='分', textvariable=self.Text5Var, font=('宋体',9))
        self.Text5.place(relx=0.307, rely=0.046, relwidth=0.053, relheight=0.036)

        self.Text6Var = StringVar(value='roomid(1-12)')
        self.Text6 = Entry(self.top, text='roomid', textvariable=self.Text6Var, font=('宋体',9))
        self.Text6.place(relx=0.307, rely=0.089, relwidth=0.093, relheight=0.036)

        self.style.configure('Label8.TLabel',anchor='center', font=('宋体',9))
        self.varlabel8 = StringVar(value='')
        self.Label8 = Label(self.top, text='Label8',background = 'BlanchedAlmond', textvariable=self.varlabel8 ,style='Label8.TLabel')
        self.Label8.place(relx=0.135, rely=0.504, relwidth=0.171, relheight=0.047)

        self.style.configure('Label9.TLabel',anchor='center', font=('宋体',9))
        self.varlabel9 = StringVar(value='')
        self.Label9 = Label(self.top, text='Label9', background = 'BlanchedAlmond', textvariable=self.varlabel9 ,style='Label9.TLabel')
        self.Label9.place(relx=0.592, rely=0.504, relwidth=0.171, relheight=0.047)

        self.style.configure('Label10.TLabel',anchor='center', font=('宋体',9))
        self.varlabel10 = StringVar(value='')
        self.Label10 = Label(self.top, text='Label10',background = 'BlanchedAlmond',  textvariable=self.varlabel10 ,style='Label10.TLabel')
        self.Label10.place(relx=0.135, rely=0.825, relwidth=0.171, relheight=0.047)

        self.style.configure('Label11.TLabel',anchor='center', font=('宋体',9))
        self.varlabel11 = StringVar(value='')
        self.Label11 = Label(self.top, text='Label11',background = 'BlanchedAlmond',  textvariable=self.varlabel11 ,style='Label11.TLabel')
        self.Label11.place(relx=0.592, rely=0.825, relwidth=0.171, relheight=0.047)



class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)
        # self.var1 = StringVar()
        # self.var2 = StringVar()
        # self.var3 = StringVar()
        # self.var4 = StringVar()
        # self.var5 = StringVar()
        # self.var6 = StringVar()
        # self.var7 = StringVar()
        # self.var8 = StringVar()
        # self.var9 = StringVar()
        # self.var10 = StringVar()
        # self.var11 = StringVar()
        self.studentID = 0


    def Student_state(self,arr):
        if(arr == 0):
            self.m = '未分配'
            self.n=1
        if(arr > 0):
            self.m = '空闲'+ str(arr) +'分钟'
            self.n=2
        if(arr < 0):
            self.m = '占用'
            self.n=3
        return (self.m,self.n)
    pass


    def Command1_Cmd(self):
        #TODO, Please finish the function here!
        self.Label3["background"] = "white"
        self.Label4["background"] = "white"
        self.Label5["background"] = "white"
        self.Label6["background"] = "white"

        self.var1 =  self.Text1.get()#年
        self.var2 =  self.Text2.get()#月
        self.var3 =  self.Text3.get()#日
        self.var4 =  self.Text4.get()#时
        self.var5 =  self.Text5.get()#分
        self.var6 =  self.Text6.get()#房间

        if (int(self.var1)!=2019):
            tkinter.messagebox.showerror('错误', '时间是2019年')
        if (int(self.var2)<=0 & int(self.var2)>12):
            tkinter.messagebox.showerror('错误', '月份出错')
        if (int(self.var3)<=0 & int(self.var3)>31):
            tkinter.messagebox.showerror('错误', '日期出错')
        if (int(self.var4)<0 & int(self.var4)>=12):
            tkinter.messagebox.showerror('错误', '小时出错')
        if (int(self.var5)<=0 & int(self.var5)>60):
            tkinter.messagebox.showerror('错误', '分钟出错')
        if (int(self.var6)<=0 ):
            tkinter.messagebox.showerror('错误', '房间号是正整数')


        self.roomID=int(self.var6)
        self.varlabel7.set(self.roomID)
        #print(self.roomID)

        self.studentID = (self.roomID - 1) * 4 + 1
        #print(self.studentID)
        self.zhongjian='学号'+str(self.studentID)
        self.varlabel3.set(self.zhongjian)

        self.studentID = (self.roomID - 1) * 4 + 2
        #print(self.studentID)
        self.zhongjian = '学号' + str(self.studentID)
        self.varlabel4.set(self.zhongjian)

        self.studentID = (self.roomID - 1) * 4 + 3
        #print(self.studentID)
        self.zhongjian = '学号' + str(self.studentID)
        self.varlabel5.set(self.zhongjian)

        self.studentID = (self.roomID - 1) * 4 + 4
        #print(self.studentID)
        self.zhongjian = '学号' + str(self.studentID)
        self.varlabel6.set(self.zhongjian)

        self.date = datetime.datetime(int(self.var1), int(self.var2), int(self.var3), int(self.var4) , int(self.var5))
        self.seats=sea.check(self.roomID , self.date)
        print(len(self.seats))
        print(self.seats)

        self.varlabel8.set(self.Student_state(self.seats[0])[0])
        if(self.Student_state(self.seats[0])[1]==3):
            self.Label3["background"]="#ffffe0"

        self.varlabel9.set(self.Student_state(self.seats[1])[0])
        if (self.Student_state(self.seats[1])[1] == 3):
            self.Label4["background"]="#ffffe0"

        self.varlabel10.set(self.Student_state(self.seats[2])[0])
        if (self.Student_state(self.seats[2])[1] == 3):
            self.Label5["background"]="#ffffe0"
        self.varlabel11.set(self.Student_state(self.seats[3])[0])
        if (self.Student_state(self.seats[3])[1] == 3):
            self.Label6["background"]="#ffffe0"

    pass






if __name__ == "__main__":
    top = Tk()
    # tkinter.messagebox.showinfo('提示', '人生苦短')
    # tkinter.messagebox.showerror('错误', '出错了')
    Application(top).mainloop()
    try: top.destroy()
    except: pass
