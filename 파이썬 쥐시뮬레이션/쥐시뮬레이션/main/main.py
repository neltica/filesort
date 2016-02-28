__author__ = 'Nelician'

import Plant
import World
import Creature



def main():
    maxWidth=79 # �� �ִ� �ʺ� �����Ѵ�.
    maxHeight=24  # �� �ִ� ���̸� �����Ѵ�.

    world=World.World(maxWidth,maxHeight)  # ������� �����Ѵ�.
    mouses=[]  #����� ���� �迭�� �����.
    plants=[]  #�ܵ��� ���� �迭�� �����.
    for i in range(0,maxHeight,1):
        for j in range(0,maxWidth,1):
            plants.append(Plant.Plant()) # �ܸ� �����ؼ� �迭�� ��´�.
            world.worldMap[i][j]=plants[len(plants)-1]  #���� ����ʿ� ä���.
            plants[len(plants)-1].pos=[i,j]  #����ʿ� ��ġ�� ��ġ������ �ٽ� ���� ��ġ������ �������ش�.


    for i in range(0,20,1):
        mouses.append(Creature.Creature())  # �㸦 �����.
        import random  # ��������� �ҷ��´�.
        while True:
            height=random.randrange(0,maxHeight)   # ���� ���̸� �������� ���Ѵ�.
            width=random.randrange(0,maxWidth)   #���� �ʺ� �������� ���Ѵ�.
            if world.worldMap[height][width].symbol!='M':   # �������ġ�� �̹� �㰡 ��ġ�Ѱ� �ƴ϶��
                world.worldMap[height][width]=mouses[len(mouses)-1]  # ������ �㸦 ����ʿ� ��ġ��Ų��.
                mouses[len(mouses)-1].pos=[height,width]  # ���� ��ġ�� ����ʿ� ��ġ�� ������ �ٲ��ش�.

                break

    world.setMousePlant(mouses,plants)  # ����ʿ� ����� ��� �迭�� �ܵ��� ��� �迭�� �Ѱ��ش�.
    count=0
    while True:
        world.printMap()  # ������� ����Ѵ�/
        print count  # �Է��� ����ߴ��� ����Ѵ�.
        count+=1
        mouseCount=0
        for i in world.mouses:
            print "mouse"+str(mouseCount+1)+" age:"+str(i.age+1)+" month:"+str(i.nowSpringCycle+1)  #����� ���̿� ������ ǥ���Ѵ�.
            mouseCount+=1
        #��ɾ�鿡 ���� ������ ��Ƴ��� �迭
        text=["<\'h\' for help>", "<\'Enter\' for next cycle>","<\'i1\' for insert mouse pos(y=0,x=15)>", "<\'i2\' for insert mouse pos(y=9,x=15)>","<\'.\' for print object(y=0,x=15)>", "<\'N\' for print object(y=0,x=15) North>","<\'D\' for delete object(y=9,x=15)>"]
        for i in text:
            print i
        command=raw_input("Enter Command:")   # ��ɾ �Է��Ѵ�.

        world.computeLifeCycle() #����ʿ� �Ĺ��� ����� ������ ���� ����Ѵ�.

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
