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

    if len(folderListText)==0:
        path=tkFileDialog.askdirectory()
        print 'add folder path='+path

    else:
        path= folderListText[len(folderListText)-1][:folderListText[len(folderListText)-1].rfind('/')]
        print "add folder path="+ path


    askFolderNameWindow=Tkinter.Toplevel(app)
    askFolderNameLabel=Tkinter.Label(askFolderNameWindow,text="insert folder Name")
    content=Tkinter.StringVar()
    askFolderNameEntry=Tkinter.Entry(askFolderNameWindow,textvariable=content)
    askFolderNameLabel.pack()
    askFolderNameEntry.pack()
    askFolderNameEntry.focus_set()

    askFolderNameEntry.bind('<Return>',folderNameInsertEntryCallback)

    app.wait_window(askFolderNameWindow)

    path=path+"/"+content.get()
    import os
    if not os.path.isdir(path):
        os.mkdir(path)
        folderListText.append(path)
        if path!="":
            path=str(folderListBox.size()+1)+'. '+path[path.rfind('/')+1:]
            folderListBox.insert('end',path)

    else:
        print "already folder exist."

    for i in folderListText:
            print i
def deleteFolderButtonCallback():
    global folderListBox
    folderListBox.delete(folderListBox.index('active'))
    del folderListText[folderListBox.index('active')]

    end=len(folderListText)
    for i in xrange(0,end,1):
        folderListBox.delete(0)
        folderListBox.insert('end',str(i+1)+'. '+folderListText[i])


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
    event.widget.master.destroy()

def folderNameInsertEntryCallback(event):
    event.widget.master.destroy()

def folderSelectCallback(event):
    global folderListText
    global imageListBox
    global path
    global flag
    nowIndex=int(imageListBox.curselection()[0])
    print "press key is "+event.keysym


    if event.keysym == 'Escape':
        flag=True
        event.widget.destroy()
        pass
    elif event.keysym == 'space':
        imageListBox.select_clear(nowIndex,nowIndex)
        imageListBox.select_set(nowIndex+1)
        event.widget.destroy()
        pass

    elif event.keysym=='c':
        folderNameInsertWindow=Tkinter.Toplevel(event.widget)
        folderNameInsertLabel=Tkinter.Label(folderNameInsertWindow,text='Insert folder name')
        content=Tkinter.StringVar()
        folderNameInsertEntry=Tkinter.Entry(folderNameInsertWindow,textvariable=content)
        folderNameInsertLabel.pack()
        folderNameInsertEntry.pack()
        folderNameInsertEntry.focus_set()

        folderNameInsertEntry.bind('<Return>',folderNameInsertEntryCallback)


        event.widget.wait_window(folderNameInsertWindow)

        folderPath= folderListText[len(folderListText)-1][:folderListText[len(folderListText)-1].rfind('/')]
        print "add folder path="+ folderPath

        folderPath=folderPath+"/"+content.get()
        import os
        if not os.path.isdir(folderPath):
            os.mkdir(folderPath)
            folderListText.append(folderPath)
            if folderPath!="":
                folderPath=str(folderListBox.size()+1)+'. '+folderPath[folderPath.rfind('/')+1:]
                folderListBox.insert('end',folderPath)

                print "original image file path is "+folderListText[folderListBox.size()-1]+"/"+imageListBox.get(nowIndex)
                print "copy image file path is "+folderListText[folderListBox.size()-1]+"/"+imageListBox.get(nowIndex)
                originFile=open(path+"/"+imageListBox.get(nowIndex),'rb')
                copyFile=open(folderListText[folderListBox.size()-1]+"/"+imageListBox.get(nowIndex),'wb')

                for i in originFile:
                    copyFile.write(i)

                originFile.close()
                copyFile.close()

                for i in folderListText:
                    print i

                imageListBox.select_clear(nowIndex,nowIndex)
                imageListBox.select_set(nowIndex+1)
                event.widget.destroy()
                pass

        else:
            print "already folder exist."

        pass
    elif int(event.keysym)-1<len(folderListText):
        import os
        if os.path.exists(folderListText[int(event.keysym)-1]+"/"+imageListBox.get(nowIndex)):
            print "already exists!!!"

            askFileNameWindow=Tkinter.Toplevel(event.widget)
            askFIleNameLabel=Tkinter.Label(askFileNameWindow,text="already exists!\ninsert file Name")
            content=Tkinter.StringVar()
            askFileNameEntry=Tkinter.Entry(askFileNameWindow,textvariable=content)
            askFIleNameLabel.pack()
            askFileNameEntry.pack()
            askFileNameEntry.focus_set()

            for i in xrange(1,1024,1):
                fileName=(folderListText[int(event.keysym)-1]+"/"+imageListBox.get(nowIndex))
                dotIndex=fileName.rfind('.')
                if not os.path.exists( fileName[:dotIndex]+"("+str(i)+")"+fileName[dotIndex:] ):
                    print "new file name is "+fileName[:dotIndex]+"("+str(i)+")"+fileName[dotIndex:]
                    fileName=fileName[:dotIndex]+"("+str(i)+")"+fileName[dotIndex:]
                    break

            askFileNameEntry.delete(0,'end')
            endIndex=fileName.rfind('/')
            fileName=fileName[endIndex+1:]
            askFileNameEntry.insert(0,fileName)

            askFileNameEntry.bind('<Return>',askFileNameCallback)

            event.widget.wait_window(askFileNameWindow)

            copyPath=folderListText[int(event.keysym)-1]+"/"+content.get()

            if content.get()!="":
                originFile=open(path+"/"+imageListBox.get(int(imageListBox.curselection()[0])),'rb')
                copyFile=open(copyPath,'wb')

                print "original image file path is "+path+"/"+imageListBox.get(int(imageListBox.curselection()[0]))
                print "copy image file path is "+copyPath

                for i in originFile:
                    copyFile.write(i)

                originFile.close()
                copyFile.close()
                pass


            imageListBox.select_clear(nowIndex,nowIndex)
            imageListBox.select_set(nowIndex+1)
            pass

        else:
            print "original image file path is "+folderListText[int(event.keysym)-1]+"/"+imageListBox.get(nowIndex)
            print "copy image file path is "+folderListText[int(event.keysym)-1]+"/"+imageListBox.get(nowIndex)
            originFile=open(path+"/"+imageListBox.get(nowIndex),'rb')
            copyFile=open(folderListText[int(event.keysym)-1]+"/"+imageListBox.get(nowIndex),'wb')

            for i in originFile:
                copyFile.write(i)

            originFile.close()
            copyFile.close()
            imageListBox.select_clear(nowIndex,nowIndex)
            imageListBox.select_set(nowIndex+1)
            pass
        event.widget.destroy()
        pass

    else:
        print "folder no exist!!!"


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
    global app
    global flag

    nowIndex=int(imageListBox.curselection()[0])

    for i in xrange(nowIndex,imageListBox.size(),1):

        if flag:
            flag=False
            break

        print path+"/"+imageListBox.get(nowIndex)
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

        Tkinter.Label(folderNameSelectWindow,text='create folder = \'c\'').pack()

        number=1
        for i in folderListBox.get(0,'end'):
            Tkinter.Label(folderNameSelectWindow,text=i).pack()
            number+=1

        folderNameSelectWindow.bind('<Key>',folderSelectCallback)

        app.wait_window(folderNameSelectWindow)





extension = ['jpg', 'gif', 'jpeg','png']
folderListText=[]
path=''
flag=False

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
#folderRenameButton.grid(row=baseRow+2,column=baseColumn+3)


imageListBox.bind('<<ListboxSelect>>',imageListClick)

app.mainloop()