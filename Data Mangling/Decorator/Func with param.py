def div_decorator(func):
    def innerfun(x, y):
        if y == 0:
            return 'Provide a non zero denominator'
        else:
            return func(x, y)

    return innerfun

@div_decorator
def div(a, b):
    return a / b


res = div_decorator(div)
print(res(10, 2))
print(res(10, 0))
