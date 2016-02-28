
from cs1graphics import *
import time

"""
window setting value
"""
windowX=800
windowY=800
windowBgColor='white'
windowTitle="cowMove"



"""
cow move setting value
"""
cowSpeed=80
cowMoveMininumX=0
cowMoveMaxinumX=800



"""
cow Image setting
"""
cowFrameImage=[Image('cow1.gif'),Image('cow2.gif'),Image('cow3.gif'),Image('cow4.gif')]
cowFrameReverseImage=[Image('reverseCow1.gif'),Image('reverseCow2.gif'),Image('reverseCow3.gif'),Image('reverseCow4.gif')]



def show(layerList,rlayerList):

    global canvas   #main window canvas
    global cowSpeed
    global cowMoveMininumX
    global cowMoveMaxinumX

    cowX=300   #cow move horizon x-axis value
    cowY=400   #cow move vertical y-axis value

    flag=True
    i=0

    canvas.add(layerList[i])
    layerList[i].moveTo(cowX,cowY)   # image move to (cowX,cowY)
    while True:

        if cowX>cowMoveMaxinumX:
            flag=False
            canvas.remove(layerList[i%4])
            canvas.add(rlayerList[i])
            rlayerList[i].moveTo(cowX,cowY)
        elif cowX<cowMoveMininumX:
            flag=True
            canvas.remove(rlayerList[i%4])
            canvas.add(layerList[i])
            layerList[i].moveTo(cowX,cowY)


        if flag:
            canvas.remove(layerList[i%4])
            canvas.add(layerList[(i+1)%4])
            layerList[(i+1)%4].moveTo(cowX,cowY)
            time.sleep(0.1)
            cowX+=cowSpeed

            pass
        else:
            canvas.remove(rlayerList[i%4])
            canvas.add(rlayerList[(i+1)%4])
            rlayerList[(i+1)%4].moveTo(cowX,cowY)
            time.sleep(0.1)
            cowX-=cowSpeed
            pass

        i+=1
        i%=4

    pass

def draw(layerList,imageList):
    for i in imageList:
        layerList.append(Layer())
        layerList[len(layerList)-1].add(i)
    pass


canvas = Canvas(windowX,windowY,windowBgColor,windowTitle)


cowLayerList=[]
rcowLayerList=[]
imageList=[]
imageList.append(cowFrameImage)
imageList.append(cowFrameReverseImage)

draw(cowLayerList,imageList[0])
draw(rcowLayerList,imageList[1])

show(cowLayerList,rcowLayerList)

