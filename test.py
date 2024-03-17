class A():
    def __init__(self):
        print("hello")


class B(A):
    def __init__(self,name):
        name = name
        print(name)
o = B("gd")