text = input()
import pandas as pd

def txtgistogramm(text):
    elements = {}
    maxsymcount = 0
    for i in text:
        if i not in elements:
            elements[i] = 0
        elements[i] += 1
        maxsymcount = max(maxsymcount, elements[i])
    sorteduniqsyms = sorted(elements.keys())
    for row in range(maxsymcount, 0, -1):
        for sym in sorteduniqsyms:
            if elements[sym] >= row:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    print(''.join(sorteduniqsyms))



result = txtgistogramm(text)
print(result)
