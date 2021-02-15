def divisor(number):
    for i in range(1, number + 1):
        if number % i == 0:
                yield i
    yield None



three = divisor(3)
print(next(three))
print(next(three))
print(next(three))