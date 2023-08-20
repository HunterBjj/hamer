"""
Дана последовательность чисел длинной N(N > 1)
Найти максимальное число в последовательности и второе по величине число
(такое, которое будет максимальным, если вычеркнуть из полседовательности
одно число)

"""


def findmax2(num):
    max1 = max(num[0], num[1])
    max2 = min(num[0], num[1])
    for i in range(2, len(num)):
        if num[i] > max1:
            max1 = num[i]
            max2 = max1
        elif num[i] > max2:
            max2 = num[i]
    return (max1, max2)