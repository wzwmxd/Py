# 此文件实现了一个树的类，2016/7/5


class Tree:
    def __init__(self, li):
        self.a, self.l, self.r = li

    def printf(self):
        print(self.a)
        if self.l != 0:
            self.l.printf()
        if self.r != 0:
            self.r.printf()


l = Tree([1, 0, 0])
r = Tree([2, 0, 0])
t1 = Tree([3, l, r])

l = Tree([4, 0, 0])
r = Tree([5, 0, 0])
t2 = Tree([6, l, r])

t = Tree([7, t1, t2])

t.printf()
