#这个不是创建函数最简单的方式
def print_two(*args):
    arg1,arg2=args
    print("arg1:%r,arg2:%r"%(arg1,arg2))
#直接使用（）里边的名字作为变量名
def print_two_again(arg1,arg2):
    print("ard1:%r,arg2:%r"%(arg1,arg2 ))
#接受单个参数
def print_one(arg1):
    print("arg1:%r"%arg1)
#不接收任何参数
def print_none():
    print("i got nothing")

print_two("zed","shaw")
print_two_again("zed","shaw")
print_one("first!")
print_none()