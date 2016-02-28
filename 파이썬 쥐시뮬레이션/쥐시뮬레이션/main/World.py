__author__ = 'Nelician'
import Creature
import Plant


class World():


    def __init__(self,mapWidth=79,mapHeight=24):
        self.mapWidth=mapWidth    # mapwidth �� width ������
        self.mapHeight=mapHeight  # mapheight �� height ������
        self.mouses=[]            # ������� �����س��� ����
        self.plants=[]            # ������ �����س��� ����
        self.sprinfCount=0        # springCount�� offSpringCycle���� üũ�ϴ� ī��Ʈ ����
        self.worldMap=[]          #����� �迭

        self.makeWorldMap()    #���� ������� ä��� �Լ�
        pass

    def __del__(self):
        pass

    def makeWorldMap(self):   # ������� ä��� �Լ�
        for i in range(0,self.mapHeight,1):
            self.worldMap.append([])
            for j in range(0,self.mapWidth,1):
                self.worldMap[i].append('.')

    def setMousePlant(self,_mouse,_plant):   # CreateureŬ������ PlantsŬ�������� ��� �Ĺ����� �����´�.
        self.mouses=_mouse
        self.plants=_plant

    def computeLifeCycle(self):

        for i in self.mouses: #���
            existFlag=[False,False,False,False]   # 4�������� ������ �ִ°� �ִ��� üũ�ϴ� �÷���

            for j in range(1,5,1): #�������� 1~4ĭ���� ���� �ִ��� üũ�ϴ� �۾�
                if self.getPos(i)[0]-j>=0:    # �������� j��ŭ �̵��ؼ�
                    if self.worldMap[self.getPos(i)[0]-j][self.getPos(i)[1]].symbol=='Y':  #���� ������
                        existFlag[0]=True   # �÷��׸�  true�� �ٲ۴�.

                if self.getPos(i)[0]+j<self.mapHeight:   # �������� j��ŭ �̵��ؼ�
                    if self.worldMap[self.getPos(i)[0]+j][self.getPos(i)[1]].symbol=='Y':   # ���� ������
                        existFlag[1]=True # �÷��׸� TRue�� �ٲ۴�.

                if self.getPos(i)[1]-j>=0:  # �������� j��ŭ ����
                    if self.worldMap[self.getPos(i)[0]][self.getPos(i)[1]-j].symbol=='Y':  # ��������
                        existFlag[2]=True

                if self.getPos(i)[1]+j<self.mapWidth:  # �������� j��ŭ ����
                    if self.worldMap[self.getPos(i)[0]][self.getPos(i)[1]+j].symbol=='Y':
                        existFlag[3]=True

            for k in existFlag:  # existFlag�� ����ִ� �������� �ϳ��� True�̸� ��� �����Ѵ�.
                if k==True:

                    import random  #��������� �о�´�.
                    while True:
                        azimuth=random.randrange(0,4)  # ���������� �������� 4�����̹Ƿ� 0~3���� ���� �̿��� ������ ������ �Ǵ��Ѵ�.
                        if existFlag[azimuth]==True:  # �������� ���� ���Ⱚ�� �ִ� exitFlag���� True�̸� ����ʿ� ���� �㰡 �ִ� ��ġ�� �㸦 ����������.
                            for j in self.plants:  # ���� �㰡 �ִ� ��ġ�� �ִ� �Ĺ��� ������ ���ͼ�
                                if j.pos==i.pos:
                                    j.symbol='.'  # �Ĺ��� �����ɷ� ó���ϰ� (�㰡 �԰� �̵������ϱ�)
                                    j.seedCycle=0  #�Ĺ��� �ڶ󳪴� ����Ŭ�� seedCYcle�� �ٽ� 0���� �ʱ�ȭ��Ų��.
                                    self.worldMap[j.pos[0]][j.pos[1]]=j  #�Ĺ��� ����ʿ� ��ġ��Ų��.
                                    break


                            #���Ⱚ�� ���� �б����� ���õȴ�.
                            # azimuth 0~3������ azimuth==0�� ����� �����ϰ� ���⸸ �޶�����.


                            if azimuth==0:

                                for j in range(1,5,1): # �㰡 ���� �ִ� ��ġ���� 1~4ĭ��ŭ�� äũ�Ѵ�.
                                    if self.getPos(i)[0]-j>=0: #����� ������ ����� �ȵǴϱ� ����� ������ ������� üũ�Ѵ�. ����� ������
                                        if self.worldMap[self.getPos(i)[0]-j][self.getPos(i)[1]].symbol=='Y':   # �� ��ġ�� �Ĺ��� �ִ��� üũ�Ѵ�.
                                            self.worldMap[self.getPos(i)[0]-j][self.getPos(i)[1]]=i   # ����ʿ� ����ġ�� ��ġ�� �㸦 ��ġ�Ѵ�.
                                            i.pos=[self.getPos(i)[0]-j,self.getPos(i)[1]]   # ���� ��ġ�� �������ش�.
                                            i.starving=0   #�Ծ����Ƿ� ����ī������ startving�� �ٽ� 0���� �ʱ�ȭ�Ѵ�.
                                            break
                                break
                                pass
                            elif azimuth==1:

                                for j in range(1,5,1):
                                    if self.getPos(i)[0]+j<self.mapHeight:
                                        if self.worldMap[self.getPos(i)[0]+j][self.getPos(i)[1]].symbol=='Y':
                                            self.worldMap[self.getPos(i)[0]+j][self.getPos(i)[1]]=i
                                            i.pos=[self.getPos(i)[0]+j,self.getPos(i)[1]]
                                            i.starving=0
                                            break
                                break
                                pass
                            elif azimuth==2:

                                for j in range(1,5,1):
                                    if self.getPos(i)[1]-j>=0:
                                        if self.worldMap[self.getPos(i)[0]][self.getPos(i)[1]-j].symbol=='Y':
                                            self.worldMap[self.getPos(i)[0]][self.getPos(i)[1]-j]=i
                                            i.pos=[self.getPos(i)[0],self.getPos(i)[1]-j]
                                            i.starving=0
                                            break
                                break
                                pass
                            elif azimuth==3:

                                for j in range(1,5,1):
                                    if self.getPos(i)[1]+j<self.mapWidth:
                                        if self.worldMap[self.getPos(i)[0]][self.getPos(i)[1]+j].symbol=='Y':
                                            self.worldMap[self.getPos(i)[0]][self.getPos(i)[1]+j]=i
                                            i.pos=[self.getPos(i)[0],self.getPos(i)[1]+j]
                                            i.starving=0
                                            break
                                break
                                pass

                    i.performAction()  # �� ��ü�� �ൿ  ( starving�ð��� ���� ���� ��ȭ-> starving�� +1 �ǰ� offSpring�� ���� age�� +1 �Ǵ� ���� �۾�_ �� �ѹ� �����Ѵ�.
                    break


        i=0
        deadFlagExist=False   # �㰡 �׾����� üũ�Ѵ�.
        while True:
            if i<len(self.mouses):
                if self.mouses[i].deadFlag==True:  # ���� �� �迭�� �ִ� �㰡 �׾��ٸ�
                    for j in self.plants:  # ���ڸ��� ��ġ�� �Ĺ��� �����ͼ�
                        if j.pos==self.mouses[i].pos:
                            self.worldMap[self.mouses[i].pos[0]][self.mouses[i].pos[1]]=j  #����ʿ� ��ġ��Ű��
                    del self.mouses[i]   # ����� ������ ��� self.mouse�迭���� �ش� ���� ������ ������Ų��.
                    i=0
                else:
                    i+=1
            else:
                break


        self.sprinfCount+=1  # ������� springCount�� +1 ��Ų��.
        if self.sprinfCount==12: #offSpringCount�� ���� ����� ���̰� +1�ȴ�.
            self.sprinfCount=0
            for i in self.plants:
                i.symbol='Y'  # �Ĺ����� �ٽ� �� �ڶ󳭴�.
                i.seedCycle=0

        else:
            for i in self.plants:   # �Ĺ��鵵 �ڱ��ڽ��� ������ �Ѵ�.  (������ seedCycle��
                i.performAction()
            pass


    def printMap(self):   # ������� ȭ�鿡 ����Ѵ�.
        import os
        os.system('cls')
        mCount=0
        mpos=[]
        for i in range(0,self.mapHeight,1):
            for j in range(0,self.mapWidth,1):
                if self.worldMap[i][j].symbol=='M':
                    mCount+=1
                    mpos.append([i,j])
                print self.worldMap[i][j].symbol,
            print

        print "mouse count:"+str(mCount)
        pass

    def getPos(self,_thing): # ��迭���� �㸦 �Ѱ��ָ� ���� ���� ��ġ�� ���ϵȴ�.
        return _thing.pos

    def move(self,this,pos):
        pass




