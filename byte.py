def add(x, y):
    return x + y

print(list(add.__code__.co_code))


import dis


dis.dis(add)