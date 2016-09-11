import copy
# copy模块
class Animal:
    def __init__(self, species, number_of_legs, color):
        self.species = species
        self.number_of_legs = number_of_legs
        self.color = color

harry = Animal('hippogriff', 6, 'pink')

miyi = copy.copy(harry)

import keyword
print(keyword.iskeyword('if'))
print(keyword.iskeyword('true'))
print(keyword.kwlist)

import random
print(random.randint(1,100))
print(random.randint(1,1000))

import random
family=['me','bro','dogs','mom']
print(random.choice(family))

import sys
sys.exit()

import sys
print(sys.version)

import time
print(time(time))

import copy
class Car:
    pass
car1=Car()
car1.wheels=4
car2=car1
car2.wheels=3
print(car1,wheels)