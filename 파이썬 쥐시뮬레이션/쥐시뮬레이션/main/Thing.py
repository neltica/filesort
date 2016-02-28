__author__ = 'Nelician'


class Thing():
    def __init__(self):
        self.symbol='.'  # 오브젝트를 표현할 심벌을 정한한다. 디폴트는 .이다
        self.pos=[-1,-1]  # 오브젝트의 위치로 디폴트는 -1,-1 이다.
        self.age=0  # 마찬가지로 오브젝트의 나이로 디폴트는 0이다.
        pass

    def __del__(self):
        pass

    def performAction(self):
        pass
