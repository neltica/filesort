__author__ = 'Nelician'

class A:
    def __init__(self):
        self.pos=1
        print 'A'

class B(A):
    def __init__(self):
        A.__init__(self)
        print 'B'

    def print1(self):
        print self.pos

b=B()
b.print1()