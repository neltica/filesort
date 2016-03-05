# -*- coding:utf-8 -*-
import Tkinter
import random

textList=[]

app=Tkinter.Tk()

content=Tkinter.StringVar()
content.set("test")
hangulLabel=Tkinter.Label(app,textvariable=content)
hangulLabel.grid(row=0,column=0,columnspan=2)

answerEntry=Tkinter.Entry(app)
answerEntry.grid(row=1,column=0,columnspan=2)


def settingButtonCallback():
    settingWindow=Tkinter.Toplevel(app)

    Tkinter.Label(settingWindow,text='영어').grid(row=0,column=0)
    Tkinter.Label(settingWindow,text='한글').grid(row=0,column=1)
    enlistBox=Tkinter.Listbox(settingWindow,exportselection=0)
    enlistBox.grid(row=1,column=0)
    def enListBoxCallback(event):
        if len(hanlistBox.curselection())!=0:
            hanlistBox.select_clear(hanlistBox.curselection()[0],hanlistBox.curselection()[0])
        hanlistBox.select_set(enlistBox.curselection()[0],enlistBox.curselection()[0])
    enlistBox.bind('<<ListboxSelect>>',enListBoxCallback)
    hanlistBox=Tkinter.Listbox(settingWindow,exportselection=0)
    hanlistBox.grid(row=1,column=1)
    def hanListBoxCallback(event):
        if len(enlistBox.curselection())!=0:
            enlistBox.select_clear(enlistBox.curselection()[0],enlistBox.curselection()[0])
        enlistBox.select_set(hanlistBox.curselection()[0],hanlistBox.curselection()[0])
    hanlistBox.bind('<<ListboxSelect>>',hanListBoxCallback)

    enlistBox.insert('end','123')
    enlistBox.insert('end','456')
    hanlistBox.insert('end','123')
    hanlistBox.insert('end','456')


    def delButtonCallback():
        if len(hanlistBox.curselection())!=0:
            hanlistBox.delete(hanlistBox.curselection()[0],hanlistBox.curselection()[0])
            enlistBox.delete(enlistBox.curselection()[0],enlistBox.curselection()[0])
    delButton=Tkinter.Button(settingWindow,text='삭제',command=delButtonCallback)
    delButton.grid(row=1,column=2)

    Tkinter.Label(settingWindow,text='영어').grid(row=2,column=0)
    enEntry=Tkinter.Entry(settingWindow)
    enEntry.grid(row=2,column=1)
    Tkinter.Label(settingWindow,text='해석').grid(row=3,column=0)
    hanEntry=Tkinter.Entry(settingWindow)
    hanEntry.grid(row=3,column=1)


    def addButtonCallback():
        if enEntry.get()!='' and hanEntry.get()!='':
            textList.append([enEntry.get(),hanEntry.get()])
            hanlistBox.insert('end',hanEntry.get())
            enlistBox.insert('end',enEntry.get())
    addButton=Tkinter.Button(settingWindow,text='추가',command=addButtonCallback)
    addButton.grid(row=2,column=2,rowspan=2)

    def enterCallback(event):
        if enEntry.get()!='' and hanEntry.get()!='':
            textList.append([enEntry.get(),hanEntry.get()])
            hanlistBox.insert('end',hanEntry.get())
            enlistBox.insert('end',enEntry.get())

    enEntry.bind('<Return>',enterCallback)
    hanEntry.bind('<Return>',enterCallback)

settingButton=Tkinter.Button(app,text='설정',command=settingButtonCallback)
settingButton.grid(row=2,column=0)
app.mainloop()