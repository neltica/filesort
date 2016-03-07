# -*- coding:utf-8 -*-
import Tkinter
import random

textList=[]
nowText=[]
startFlag=False

import os
if os.path.isfile('setting.set'):
    file=open('setting.set','rt')
    for i in file:
        i=i.split('\n')[0]
        textList.append([i.split('  ')[0],i.split('  ')[1]])
    file.close()
app=Tkinter.Tk()

content=Tkinter.StringVar()
content.set("test")
hangulLabel=Tkinter.Label(app,textvariable=content)
hangulLabel.grid(row=0,column=0,columnspan=2)

englishContent=Tkinter.StringVar()
#englishContent.set('123')
englishLabel=Tkinter.Label(app,textvariable=englishContent)
englishLabel.grid(row=1,column=0,columnspan=2)

answerEntry=Tkinter.Entry(app)
answerEntry.grid(row=2,column=0,columnspan=2)


def answerEnterCallback(event):
    englishContent.set(nowText[0])
    answerText=answerEntry.get().split('\n')[0].strip()
    questionText=nowText[0].split('\n')[0].strip()


    print answerText+" "+questionText
    if answerText.lower()==questionText.lower():
        print "정답"
    else:
        print "틀림"
answerEntry.bind('<Return>',answerEnterCallback)


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

    """enlistBox.insert('end','123')
    enlistBox.insert('end','456')
    hanlistBox.insert('end','123')
    hanlistBox.insert('end','456')"""
    import os
    if os.path.isfile('setting.set'):
        file=open('setting.set','rt')

        for i in file:
            i=i.split('\n')[0]
            enlistBox.insert('end',i.split('  ')[0])
            hanlistBox.insert('end',i.split('  ')[1])
        file.close()


    def delButtonCallback():
        if len(hanlistBox.curselection())!=0:
            nowIndex=hanlistBox.curselection()[0]
            if hanlistBox.size()!=0:
                enlistBox.select_set(nowIndex+1)
                hanlistBox.select_set(nowIndex+1)
            hanlistBox.delete(nowIndex,nowIndex)
            enlistBox.delete(nowIndex,nowIndex)
            file=open('setting.set','wt')
            for i in xrange(0,enlistBox.size(),1):
                file.write(enlistBox.get(i)+"  "+hanlistBox.get(i).encode('utf-8')+"\n")
            file.close()
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

            file=open('setting.set','at')
            file.write(enEntry.get().strip()+"  "+hanEntry.get().strip().encode('utf-8')+"\n")
            file.close()
            enEntry.delete(0,'end')
            hanEntry.delete(0,'end')
    addButton=Tkinter.Button(settingWindow,text='추가',command=addButtonCallback)
    addButton.grid(row=2,column=2,rowspan=2)

    def enterCallback(event):
        if enEntry.get()!='' and hanEntry.get()!='':
            textList.append([enEntry.get(),hanEntry.get()])
            hanlistBox.insert('end',hanEntry.get())
            enlistBox.insert('end',enEntry.get())

            file=open('setting.set','at')
            file.write(enEntry.get().strip()+"  "+hanEntry.get().strip().encode('utf-8')+"\n")
            file.close()
            enEntry.delete(0,'end')
            hanEntry.delete(0,'end')
    enEntry.bind('<Return>',enterCallback)
    hanEntry.bind('<Return>',enterCallback)


def startButtonCallback():
    startFlag=True
    if startFlag:
        startButton.config(text='다음')
    global nowText
    if len(textList)!=0:
        nowText=random.choice(textList)
        content.set(nowText[1])
        englishContent.set('')
startButton=Tkinter.Button(app,text='시작',command=startButtonCallback)
startButton.grid(row=3,column=0)


def answerButton():
    englishContent.set(nowText[0])

answerButton=Tkinter.Button(app,text='정답보기',command=answerButton)
answerButton.grid(row=3,column=1)

settingButton=Tkinter.Button(app,text='설정',command=settingButtonCallback)
settingButton.grid(row=3,column=2)
app.mainloop()