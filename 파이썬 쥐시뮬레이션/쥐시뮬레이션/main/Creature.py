__author__ = 'Nelician'

import Thing

class Creature(Thing.Thing):

    def __init__(self,_starving=0,_maxAge=2,_maxStarving=7,_offspringCycle=12):
        #super(self.__class__,self).__init__()
        Thing.Thing.__init__(self)
        self.symbol='M' # ���ǽɹ��� "M"�� �Ѵ�.
        self.offsprintCycle=_offspringCycle   # ���� �ٽ� ���� ī��Ʈ�� �����Ѵ�.
        self.starving=_starving  # starving �� maxStarving
        self.maxStarving=_maxStarving  # maxStarving ���� �ִ� ������� �����Ѵ�.
        self.maxAge=_maxAge  #���� �ִ� ���̸� �����Ѵ�.
        self.azimuth=[]  # �Ⱦ���.
        self.nowSpringCycle=0  # ���� spingCycle�� �����Ѵ�.
        self.deadFlag=False # �׾����� üũ�ϴ� �÷���
        pass

    def __del__(self):
        pass

    def performAction(self):
        self.nowSpringCycle+=1  # ���� ������� üũ�ϴ� nowSpingCycle
        if self.nowSpringCycle==self.offsprintCycle:  # offSpingCYcle�� ��������
            self.nowSpringCycle=0  # �ٽ� 0���� �ʱ�ȭ�ϰ�
            self.age+=1  # ���̸� �ѻ� �Դ´�.
            return 1
        if self.age==self.maxAge-1 or self.starving==self.maxStarving:  # ���̰� �����ų� �ƹ��͵� ���������¿��� �������� �ٴ��� ����
            self.deadFlag=True  # ���������� �÷��׸� True�� �ٲ۴�.
            return 0
        pass

if __name__=="__main__":
    c=Creature()
    c.performAction()
    print c.pos