#创建列表
hair=['brown','red','blond']
#用for循环循环列表
the_count=['1','2','3','4','5']
fruits=['apples','oranges','pears','apricots']
change=['1','pennies','2','dimes','3','quarters']
for number in the_count:
    print("this is count %r"%(number))
for fruit in fruits:
    print("a fruit of type:%s"%fruit)
for i in change:
    print("i got %r"%i)
for i in range(0,6):
    print("adding %d to the list"%i)
for i in range(0,6):
    print("element was %d"%i)