__author__ = 'Nelician'

import Plant
import World
import Creature



def main():
    maxWidth=79 # 맵 최대 너비를 지정한다.
    maxHeight=24  # 맵 최대 높이를 지정한다.

    world=World.World(maxWidth,maxHeight)  # 월드맵을 생성한다.
    mouses=[]  #쥐들을 담을 배열을 만든다.
    plants=[]  #콘들을 담을 배열을 만든다.
    for i in range(0,maxHeight,1):
        for j in range(0,maxWidth,1):
            plants.append(Plant.Plant()) # 콘를 생성해서 배열에 담는다.
            world.worldMap[i][j]=plants[len(plants)-1]  #콘을 월드맵에 채운다.
            plants[len(plants)-1].pos=[i,j]  #월드맵에 위치한 위치정보를 다시 콘의 위치정보에 대입해준다.


    for i in range(0,20,1):
        mouses.append(Creature.Creature())  # 쥐를 만든다.
        import random  # 랜덤모듈을 불러온다.
        while True:
            height=random.randrange(0,maxHeight)   # 쥐의 높이를 랜덤으로 정한다.
            width=random.randrange(0,maxWidth)   #쥐의 너비를 랜덤으로 정한다.
            if world.worldMap[height][width].symbol!='M':   # 월드맵위치에 이미 쥐가 위치한게 아니라면
                world.worldMap[height][width]=mouses[len(mouses)-1]  # 생성한 쥐를 월드맵에 위치시킨다.
                mouses[len(mouses)-1].pos=[height,width]  # 위의 위치를 월드맵에 위치한 정보로 바꿔준다.

                break

    world.setMousePlant(mouses,plants)  # 월드맵에 쥐들이 담긴 배열과 콘들이 담긴 배열을 넘겨준다.
    count=0
    while True:
        world.printMap()  # 월드맵을 출력한다/
        print count  # 입력을 몇번했는지 출력한다.
        count+=1
        mouseCount=0
        for i in world.mouses:
            print "mouse"+str(mouseCount+1)+" age:"+str(i.age+1)+" month:"+str(i.nowSpringCycle+1)  #쥐들의 나이와 계절을 표현한다.
            mouseCount+=1
        #명령어들에 관한 설명을 담아놓은 배열
        text=["<\'h\' for help>", "<\'Enter\' for next cycle>","<\'i1\' for insert mouse pos(y=0,x=15)>", "<\'i2\' for insert mouse pos(y=9,x=15)>","<\'.\' for print object(y=0,x=15)>", "<\'N\' for print object(y=0,x=15) North>","<\'D\' for delete object(y=9,x=15)>"]
        for i in text:
            print i
        command=raw_input("Enter Command:")   # 명령어를 입력한다.

        world.computeLifeCycle() #월드맵에 식물과 쥐들이 동작할 값을 계산한다.

        if command=='':
            pass
        elif command=='h':

            print "help"*20
            raw_input("Enter")
            pass
        elif command=='i1':
            if world.worldMap[0][15].symbol != 'M':
                world.worldMap[0][15]=Creature.Creature()
                mouses.append(world.worldMap[0][15])
                world.mouses.append(world.worldMap[0][15])
            pass
        elif command=='i2':
            if world.worldMap[9][15].symbol != 'M':
                world.worldMap[9][15]=Creature.Creature()
                mouses.append(world.worldMap[9][15])
                world.mouses.append(world.worldMap[9][15])
            pass
        elif command=='.':
            print world.worldMap[0][15].symbol
            raw_input("Enter")
            pass
        elif command=='N':
            print "worldmap[0-1][15]==worldmap[-1][15]"
            raw_input("Enter")
            pass
        elif command=='D':
            if world.worldMap[9][15]=='M':
                del mouses[mouses.index([9,15])]
                del world.mouses[mouses.index([9,15])]
                for i in world.plants:
                    if i.pos==[9,15]:
                        world.worldMap[9][15]=i
            else:
                for i in world.plants:
                    if i.pos==[9,15]:
                        i.symbol='.'
                        world.worldMap[9][15]=i
            pass

if __name__=="__main__":

    main()
