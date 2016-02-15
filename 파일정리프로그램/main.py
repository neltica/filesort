# -*- coding: utf-8 -*-


import Tkinter
import tkFileDialog
from PIL import ImageTk,Image

def searchButtonCallback():
    global imageListBox
    global filePathEntry
    global extension
    global path
    path=tkFileDialog.askdirectory()
    print path
    import os
    if path!='':
        filePathEntry.delete(0,'end')
        filePathEntry.insert('end',path)
        imageListText = os.listdir(unicode(path))
        imageListBox.delete(0, 'end')

        regular=''
        for i in extension:
            regular+='.{1,}\.'+i +"|"
        regular=regular[:len(regular)-1]+""
        import re
        splitValue=re.compile(regular)
        print 'regular Extension: '+regular


        for i in imageListText:
            i=splitValue.findall(i)
            if len(i)!=0:
                imageListBox.insert('end', i[0])


def addFolderButtonCallback():
    global folderListBox
    global folderListText
    path=tkFileDialog.askdirectory()
    folderListText.append(path)
    if path!="":
        path=str(folderListBox.size()+1)+'. '+path
        folderListBox.insert('end',path)

    for i in folderListText:
        print i

def deleteFolderButtonCallback():
    global folderListBox
    folderListBox.delete(folderListBox.index('active'))
    del folderListText[folderListBox.index('active')]

    for i in folderListText:
        print i

def folderInsertEntryCallback(event):
    global renameEntry
    global folderListBox
    folderName=event.widget.get()
    if folderName!="":
        index=folderListBox.index('active')
        folderListBox.delete(index)
        folderListBox.insert(index,str(index+1)+':'+folderName)

    event.widget.master.destroy()




def folderRenameButtonCallback():
    global folderListBox
    global folderListText
    renameInsertWindow=Tkinter.Toplevel()
    renameInsertWindow.focus_set()

    originFolderPathLabel=Tkinter.Label(renameInsertWindow,text="origin path name:"+folderListText[folderListBox.index('active')])
    originFolderPathLabel.pack()
    folderPathLabel=Tkinter.Label(renameInsertWindow,text="symbol path name: "+folderListBox.get(folderListBox.index('active')))
    folderPathLabel.pack()
    renameEntry=Tkinter.Entry(renameInsertWindow)
    renameEntry.pack(side='left')
    renameEnterButton=Tkinter.Button(renameInsertWindow,text="ok")
    renameEnterButton.pack(side='left')

    renameEntry.bind('<Return>',folderInsertEntryCallback)

def askFileNameCallback(event):
    fileName=event.widget.get()
    if fileName!="":
        originFile=open(path+"/"+imageListBox.get(int(imageListBox.curselection()[0])),'rb')
        copyFile=open(fileName,'wb')

        for i in originFile:
            copyFile.write(i)

        originFile.close()
        copyFile.close()
        pass
    event.widget.master.destroy()
    pass



def folderSelectCallback(event):
    global folderListText
    global imageListBox
    global path

    print event.keysym

    print folderListText[int(event.keysym)-1]+"/"+imageListBox.get(int(imageListBox.curselection()[0]))

    import os

    if os.path.exists(folderListText[int(event.keysym)-1]+"/"+imageListBox.get(int(imageListBox.curselection()[0]))):
        print "already exists!!!"

        askFileNameWindow=Tkinter.Toplevel()
        askFIleNameLabel=Tkinter.Label(askFileNameWindow,text="already exists!\ninsert file Name")
        askFileNameEntry=Tkinter.Entry(askFileNameWindow)
        askFIleNameLabel.pack()
        askFileNameEntry.pack()
        askFileNameEntry.focus_set()

        for i in xrange(1,1024,1):
            fileName=(folderListText[int(event.keysym)-1]+"/"+imageListBox.get(int(imageListBox.curselection()[0])))
            dotIndex=fileName.rfind('.')
            if not os.path.exists( fileName[:dotIndex]+"("+str(i)+")"+fileName[dotIndex:] ):
                print fileName[:dotIndex]+"("+str(i)+")"+fileName[dotIndex:]
                fileName=fileName[:dotIndex]+"("+str(i)+")"+fileName[dotIndex:]
                break

        askFileNameEntry.delete(0,'end')
        askFileNameEntry.insert(0,fileName)

        askFileNameEntry.bind('<Return>',askFileNameCallback)

        pass
    else:
        originFile=open(path+"/"+imageListBox.get(int(imageListBox.curselection()[0])),'rb')
        copyFile=open(folderListText[int(event.keysym)-1]+"/"+imageListBox.get(int(imageListBox.curselection()[0])),'wb')

        for i in originFile:
            copyFile.write(i)

        originFile.close()
        copyFile.close()
        pass

    event.widget.destroy()


    pass


def resizeImage(width,height):

    if width>=height:
        if width>=300:
            resultWidth=300
            resultHeight=height*(300/float(width))
            pass
        else:
            resultWidth=width
            resultHeight=height
            pass
        pass
    else:
        if height>=300:
            resultHeight=300
            resultWidth=width*(300/float(height))
            pass
        else:
            resultWidth=width
            resultHeight=height
            pass
        pass
    return (int(resultWidth),int(resultHeight))

def imageListClick(event):
    print "click"
    global imageListBox
    global folderListBox
    global imageLabel
    global path
    global folderListText

    print path+"/"+imageListBox.get(int(imageListBox.curselection()[0]))
    image=Image.open(unicode(path+"/"+imageListBox.get(int(imageListBox.curselection()[0]))))

    print image.width,image.height
    imageSize=resizeImage(image.width,image.height)
    print imageSize
    image=image.resize((imageSize[0],imageSize[1]),Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(image)
    imageLabel.config(image=photo)
    imageLabel.image=photo

    folderNameSelectWindow=Tkinter.Toplevel()
    folderNameSelectWindow.focus_set()

    print folderListBox.get(0,'end')

    number=1
    for i in folderListBox.get(0,'end'):
        Tkinter.Label(folderNameSelectWindow,text=i).pack()
        number+=1

    folderNameSelectWindow.bind('<Key>',folderSelectCallback)




extension = ['jpg', 'gif', 'jpeg','png']
folderListText=[]
path=''


baseRow=0
baseColumn=0

app = Tkinter.Tk()

imageFrame=Tkinter.Frame(app,width=300,height=300)
imageFrame.grid_propagate(False)

imageLabel=Tkinter.Label(imageFrame)


controlFrame=Tkinter.Frame(app)

folderRenameButton=Tkinter.Button(controlFrame,text="Rename",command=folderRenameButtonCallback)

filePathEntry = Tkinter.Entry(controlFrame)

imageListBox = Tkinter.Listbox(controlFrame,selectmode='single')

folderListBox=Tkinter.Listbox(controlFrame)

searchButton=Tkinter.Button(controlFrame,text="...",command=searchButtonCallback)

folderAddButton=Tkinter.Button(controlFrame,text="Add",command=addFolderButtonCallback)
folderDeleteButton=Tkinter.Button(controlFrame,text="Del",command=deleteFolderButtonCallback)


imageFrame.grid(row=0,column=0)

imageLabel.grid(row=0, column=0)

controlFrame.grid(row=0, column=1)

filePathEntry.grid(row=baseRow+0,column=baseColumn+0)
searchButton.grid(row=baseRow+0,column=baseColumn+1)
imageListBox.grid(row=baseRow+1, column=baseColumn+0, columnspan=2)

folderListBox.grid(row=baseRow+0,column=baseColumn+2,rowspan=2)
folderAddButton.grid(row=baseRow+0,column=baseColumn+3)
folderDeleteButton.grid(row=baseRow+1,column=baseColumn+3)
folderRenameButton.grid(row=baseRow+2,column=baseColumn+3)


imageListBox.bind('<<ListboxSelect>>',imageListClick)

app.mainloop()