__author__ = 'Nelician'

import Thing


class Plant(Thing.Thing):
    def __init__(self,_seedCycle=6):
        Thing.Thing.__init__(self)
        self.symbol='Y'  # 식물의 기본 적인 심벌은 Y이다.
        self.seedCycle=0 # 식물이 자라나는 사이클이다. 0이 기본값이다.
        self.maxSeedCycle=_seedCycle  # 식물이 자라나는 분기점을 지정한다. 디폴트는 6으로 지정되어있다. 생성자를 통해서 변경가능
        pass

    def __del__(self):
        pass

    def performAction(self):
        if self.symbol=='.':   # 식물 심벌이 쥐한테 뜯어먹혀서 .이미되면 동작하도록 한다.
            self.seedCycle+=1  # seedCycle을 +1시킨다.
            if self.seedCycle==self.maxSeedCycle-1:   #seedCycle이 maxSeedCycle과 같아시면 y로 다시 바꾼다.
                self.symbol='Y'
        pass