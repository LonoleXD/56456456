
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




