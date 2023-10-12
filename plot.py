import collections

import matplotlib.pyplot as plt

a1 = bin(42)
b2 = bin(101)

a, b = 42, 101 # Создание двух переменных.
print(a, b)

a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)  # Значения поменялись местами.
z = ['aaa', 2, 3]
for i, j in enumerate(z):
    print(i, j)
arg = {1: 2}
arg.get('cats', 0),
animals = ['cat', 'dog', 'moose']
for i, animal in enumerate(animals):
    print(i, animal)
while not a1.isdigit():
   a1 = input('Введите ЧИСЛО ')
scores = collections.defaultdict(int)
print(scores['a'])
#numberOfPets.setdefault('cats', 0) # Ничего не делать, если 'cats' существует.

rectanglePerimeter = lambda rect: (rect[0] * 2) + (rect[1] * 2)
rectanglePerimeter([4, 10])
mapObj = map(lambda n: str(n), [8, 16, 18, 19, 12, 1, 6, 7])
list(mapObj)
['8', '16', '18', '19', '12', '1', '6', '7']

filterObj = filter(lambda n: n % 2 == 0, [8, 16, 18, 19, 12, 1, 6, 7])
list(filterObj)
[8, 16, 18, 12, 6]

[str(n) for n in [8, 16, 18, 19, 12, 1, 6, 7]]

from typing import List, Union
catNames: List[str] = ['Zophie', 'Simon', 'Pooka', 'Theodore']
numbers: List[Union[int, float]] = [42, 3.14, 99.9, 86]


import time, cProfile


def addUpNumbers():
    total = 0
    for i in range(1, 1000001):
         total += i
cProfile.run('addUpNumbers()')