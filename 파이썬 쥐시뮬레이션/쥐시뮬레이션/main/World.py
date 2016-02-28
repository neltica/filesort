__author__ = 'Nelician'
import Creature
import Plant


class World():


    def __init__(self,mapWidth=79,mapHeight=24):
        self.mapWidth=mapWidth    # mapwidth 맵 width 사이즈
        self.mapHeight=mapHeight  # mapheight 맵 height 사이즈
        self.mouses=[]            # 쥐들정보 저장해놓는 변수
        self.plants=[]            # 콘정보 저장해놓는 변수
        self.sprinfCount=0        # springCount은 offSpringCycle인지 체크하는 카운트 변수
        self.worldMap=[]          #월드맵 배열

        self.makeWorldMap()    #실제 월드맵을 채우는 함수
        pass

    def __del__(self):
        pass

    def makeWorldMap(self):   # 월드맵을 채우는 함수
        for i in range(0,self.mapHeight,1):
            self.worldMap.append([])
            for j in range(0,self.mapWidth,1):
                self.worldMap[i].append('.')

    def setMousePlant(self,_mouse,_plant):   # Createure클래스와 Plants클래스에서 쥐와 식물들을 가져온다.
        self.mouses=_mouse
        self.plants=_plant

    def computeLifeCycle(self):

        for i in self.mouses: #쥐들
            existFlag=[False,False,False,False]   # 4방향으로 먹을수 있는게 있는지 체크하는 플래그

            for j in range(1,5,1): #북쪽으로 1~4칸까지 콘이 있는지 체크하는 작업
                if self.getPos(i)[0]-j>=0:    # 북쪽으로 j만큼 이동해서
                    if self.worldMap[self.getPos(i)[0]-j][self.getPos(i)[1]].symbol=='Y':  #콘이 있으면
                        existFlag[0]=True   # 플래그를  true로 바꾼다.

                if self.getPos(i)[0]+j<self.mapHeight:   # 남쪽으로 j만큼 이동해서
                    if self.worldMap[self.getPos(i)[0]+j][self.getPos(i)[1]].symbol=='Y':   # 콘이 있으면
                        existFlag[1]=True # 플래그를 TRue로 바꾼다.

                if self.getPos(i)[1]-j>=0:  # 서쪽으로 j만큼 가서
                    if self.worldMap[self.getPos(i)[0]][self.getPos(i)[1]-j].symbol=='Y':  # 마찬가지
                        existFlag[2]=True

                if self.getPos(i)[1]+j<self.mapWidth:  # 동쪽으로 j만큼 가서
                    if self.worldMap[self.getPos(i)[0]][self.getPos(i)[1]+j].symbol=='Y':
                        existFlag[3]=True

            for k in existFlag:  # existFlag에 들어있는 변수들이 하나라도 True이면 계속 진행한다.
                if k==True:

                    import random  #랜덤모듈을 읽어온다.
                    while True:
                        azimuth=random.randrange(0,4)  # 랜덤방향은 동서남북 4방향이므로 0~3까지 값을 이용해 진행할 방향을 판단한다.
                        if existFlag[azimuth]==True:  # 랜덤으로 얻어온 방향값에 있는 exitFlag값이 True이면 월드맵에 현재 쥐가 있는 위치에 쥐를 지워버린다.
                            for j in self.plants:  # 현재 쥐가 있는 위치에 있는 식물의 정보를 얻어와서
                                if j.pos==i.pos:
                                    j.symbol='.'  # 식물은 먹힌걸로 처리하고 (쥐가 먹고 이동했으니까)
                                    j.seedCycle=0  #식물이 자라나는 사이클인 seedCYcle을 다시 0으로 초기화시킨다.
                                    self.worldMap[j.pos[0]][j.pos[1]]=j  #식물을 월드맵에 배치시킨다.
                                    break


                            #방향값에 따라서 분기점이 선택된다.
                            # azimuth 0~3까지는 azimuth==0의 내용과 동일하고 방향만 달라진다.


                            if azimuth==0:

                                for j in range(1,5,1): # 쥐가 현재 있는 위치에서 1~4칸만큼을 채크한다.
                                    if self.getPos(i)[0]-j>=0: #월드맵 밖으로 벗어나면 안되니까 월드맵 범위를 벗어나는지 체크한다. 벗어나지 않으면
                                        if self.worldMap[self.getPos(i)[0]-j][self.getPos(i)[1]].symbol=='Y':   # 그 위치에 식물이 있는지 체크한다.
                                            self.worldMap[self.getPos(i)[0]-j][self.getPos(i)[1]]=i   # 월드맵에 그위치에 위치할 쥐를 배치한다.
                                            i.pos=[self.getPos(i)[0]-j,self.getPos(i)[1]]   # 쥐의 위치를 변경해준다.
                                            i.starving=0   #먹었으므로 생존카운터인 startving을 다시 0으로 초기화한다.
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

                    i.performAction()  # 쥐 자체의 행동  ( starving시간에 따른 쥐의 변화-> starving이 +1 되고 offSpring이 오면 age가 +1 되는 등의 작업_ 을 한번 진행한다.
                    break


        i=0
        deadFlagExist=False   # 쥐가 죽었는지 체크한다.
        while True:
            if i<len(self.mouses):
                if self.mouses[i].deadFlag==True:  # 만약 쥐 배열에 있는 쥐가 죽었다면
                    for j in self.plants:  # 그자리에 위치할 식물을 가져와서
                        if j.pos==self.mouses[i].pos:
                            self.worldMap[self.mouses[i].pos[0]][self.mouses[i].pos[1]]=j  #월드맵에 배치시키고
                    del self.mouses[i]   # 쥐들의 정보가 담긴 self.mouse배열에서 해당 쥐의 정보를 삭제시킨다.
                    i=0
                else:
                    i+=1
            else:
                break


        self.sprinfCount+=1  # 월드맵의 springCount를 +1 시킨다.
        if self.sprinfCount==12: #offSpringCount가 오면 쥐들의 나이가 +1된다.
            self.sprinfCount=0
            for i in self.plants:
                i.symbol='Y'  # 식물들은 다시 다 자라난다.
                i.seedCycle=0

        else:
            for i in self.plants:   # 식물들도 자기자신의 동작을 한다.  (먹히면 seedCycle이
                i.performAction()
            pass


    def printMap(self):   # 월드맵을 화면에 출력한다.
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

    def getPos(self,_thing): # 쥐배열에서 쥐를 넘겨주면 쥐의 현재 위치가 리턴된다.
        return _thing.pos

    def move(self,this,pos):
        pass




