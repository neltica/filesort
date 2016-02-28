__author__ = 'Nelician'

import Thing


class Plant(Thing.Thing):
    def __init__(self,_seedCycle=6):
        Thing.Thing.__init__(self)
        self.symbol='Y'  # �Ĺ��� �⺻ ���� �ɹ��� Y�̴�.
        self.seedCycle=0 # �Ĺ��� �ڶ󳪴� ����Ŭ�̴�. 0�� �⺻���̴�.
        self.maxSeedCycle=_seedCycle  # �Ĺ��� �ڶ󳪴� �б����� �����Ѵ�. ����Ʈ�� 6���� �����Ǿ��ִ�. �����ڸ� ���ؼ� ���氡��
        pass

    def __del__(self):
        pass

    def performAction(self):
        if self.symbol=='.':   # �Ĺ� �ɹ��� ������ �������� .�̵̹Ǹ� �����ϵ��� �Ѵ�.
            self.seedCycle+=1  # seedCycle�� +1��Ų��.
            if self.seedCycle==self.maxSeedCycle-1:   #seedCycle�� maxSeedCycle�� ���ƽø� y�� �ٽ� �ٲ۴�.
                self.symbol='Y'
        pass