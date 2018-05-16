from com.inheritance1.FParent import FParent


class FChild(FParent):

    def ___init___(self):
        print("child")

    def chd(self):
        print("junglee")

obj = FChild("llll")
obj.pm()
obj.chd()