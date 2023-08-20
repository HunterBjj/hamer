"""
Релизация множество
"""

setsize = 10
myset = [[] for _ in range(setsize)] # создаём множество из двумерных список _- это имя переменной от 0 до 9

def add(x):
    if not find(x):
        myset[x % setsize].append(x)

def find(x):
    for now in myset[x % setsize]:
        if now == x:
            return True
        return False

def delete(x):
    xlist = myset[x % setsize] # определяем номер списка
    for i in range(len(xlist)):
        if xlist[i] == x:
            xlist[i] = xlist[len(xlist) - 1]
            xlist.pop()
            return