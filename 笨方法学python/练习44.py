#继承就是一个类的大部分或者全部功能都是从一个父类中获得的
#隐式继承
class parent(object):
    def implicit(self):
        print("PARENT implicit()")
class Child(parent):
    pass

dad=parent()
son=Child()

dad.implicit()
son.implicit()

#显式覆盖
class parent(object):

    def override(self):
        print("parent override()")

class child(parent):

    def override(self):
        print("child override()")

dad=parent()
son=child()

dad.override()
son.override()

#在运行钱或者运行后替换
class parent(object):

    def altered(self):
        print("parent altered()")
class child(parent):
    def altered(self):
        print("child,before parent altered()")
        super(child, self).altered()
        print("child,after parent altered()")

dad=parent()
son=child()

dad.altered()
son.altered()



#组合
class parent(object):

    def override(self):
        print("parent override()")

    def implicit(self):
        print("parent implicit()")

    def altered(self):
        print("parent altered()")
class child(parent):
    def override(self):
        print("child override")
    def altered(self):
        print("child,before parent altered()")
        super(child, self).altered()
        print("child,after parent altered()")

dad=parent()
son=child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

