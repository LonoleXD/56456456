"""n = int(input())
a = 1
for i in range(a, n + 1):
    print(i)"""
from wheel.macosx_libfile import calculate_macosx_platform_tag

"""class bober:
    def __init__(self, f):
        self.max = f
        self.cnt = -2
    def __iter__(self):
        return self
    def __next__(self):
        self.cnt += 2
        if(self.cnt > self.max):
            raise StopIteration
        else:
            return self.cnt
f = bober(51)
for num in f:
    print(num)"""

"""def generator(f):
    for i in range(1, f+1):
        yield(i * i)

f = int(input())
counter = generator(f)
for num in counter:
    print(num)"""
def calculate(expression):
    def hol(a, b):
        return expression(a, b)
    return hol

@calculate
def divide(a, b):
    if(b != 0):
        yield a + b
        yield a - b
        yield a * b
        yield a / b
    else:
        yield a + b
        yield a - b
        yield a * b
        yield "На ноль делить нельзя"
print(divide(52, 2))




