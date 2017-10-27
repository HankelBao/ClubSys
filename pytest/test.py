def tt(obj):
    pass

class A:
    @staticmethod
    def func1():
        tt(B)

class B:
    @staticmethod
    def func1():
        tt(A)
