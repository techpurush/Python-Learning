class A:
    def __init__(self):
        print("inside a init")

    def feature1(self):
        print("feature 1-a")
    def feature2(self):
        print("feature 2")


class B:

    def __init__(self):
        print("inside b init")

    def feature1(self):
        print("feature 1-b")

    def feature4(self):
        print("feature 4")


class C(B,A):

    def __init__(self):
        super().__init__()
        print("inside c init")

    def feature5(self):
        print("feature 5")


c1=C()
c1.feature1()

# C.feature5()

