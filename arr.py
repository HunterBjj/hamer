num = 2564

def sorted(num):
    maxnum = []
    while num > 0:
        res = num % 10
        num //= 10
        maxnum.append(res)
    for i in range(1, len(maxnum), 1):
        for g in range(0, len(maxnum), 1):
            if maxnum[i] > maxnum[g]:
                maxnum[i], maxnum[g] = maxnum[g], maxnum[i]  # swap
    number = int(''.join(map(str, maxnum)))
    return number

def square_digits(num):
    numcut = []
    while num > 0:
        cut = (num % 10) ** 2
        num //= 10
        numcut.append(cut)
    res = int(''.join(map(str, numcut)))
    return res

res = square_digits(num)
print(res)
