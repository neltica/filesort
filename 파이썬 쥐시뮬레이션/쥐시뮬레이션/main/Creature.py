__author__ = 'Nelician'

import Thing

class Creature(Thing.Thing):

    def __init__(self,_starving=0,_maxAge=2,_maxStarving=7,_offspringCycle=12):
        #super(self.__class__,self).__init__()
        Thing.Thing.__init__(self)
        self.symbol='M' # 쥐의심벌은 "M"로 한다.
        self.offsprintCycle=_offspringCycle   # 봄이 다시 오는 카운트를 지정한다.
        self.starving=_starving  # starving 이 maxStarving
        self.maxStarving=_maxStarving  # maxStarving 쥐의 최대 생명력을 지정한다.
        self.maxAge=_maxAge  #쥐의 최대 나이를 지정한다.
        self.azimuth=[]  # 안쓴다.
        self.nowSpringCycle=0  # 현재 spingCycle을 지정한다.
        self.deadFlag=False # 죽었는지 체크하는 플래그
        pass

    def __del__(self):
        pass

    def performAction(self):
        self.nowSpringCycle+=1  # 현재 몇월인지 체크하는 nowSpingCycle
        if self.nowSpringCycle==self.offsprintCycle:  # offSpingCYcle과 같아지면
            self.nowSpringCycle=0  # 다시 0으로 초기화하고
            self.age+=1  # 나이를 한살 먹는다.
            return 1
        if self.age==self.maxAge-1 or self.starving==self.maxStarving:  # 나이가 꽉차거나 아무것도 못먹은상태에서 생존력이 바닥이 나면
            self.deadFlag=True  # 죽은것으로 플래그를 True로 바꾼다.
            return 0
        pass

if __name__=="__main__":
    c=Creature()
    c.performAction()
    print c.pos