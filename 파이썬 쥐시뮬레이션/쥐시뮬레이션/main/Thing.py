__author__ = 'Nelician'


class Thing():
    def __init__(self):
        self.symbol='.'  # ������Ʈ�� ǥ���� �ɹ��� �����Ѵ�. ����Ʈ�� .�̴�
        self.pos=[-1,-1]  # ������Ʈ�� ��ġ�� ����Ʈ�� -1,-1 �̴�.
        self.age=0  # ���������� ������Ʈ�� ���̷� ����Ʈ�� 0�̴�.
        pass

    def __del__(self):
        pass

    def performAction(self):
        pass
