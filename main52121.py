def check_division(func):
    def hol(a, b):
        if b == 0:
            return("На ноль делить нельзя")
        return func(a, b)
    return hol

@check_division
def plus(a, b):
    return a + b
def minus(a, b):
    return a - b
def umn(a, b):
    return a * b
def delit(a, b):
    return a / b

print(plus(52, 2))
print(minus(52, 2))
print(umn(52, 2))
print(delit(52, 2))


