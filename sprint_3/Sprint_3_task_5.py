def logger(func):
    def wrapper(*args, **kwargs):
        vals = ""
        for a in args:
            vals += str(a) + ', '
        for k in kwargs.values():
            vals += str(k) + ', '
        x = func(*args, **kwargs)
        print(f"Executing of function {func.__name__} with arguments {vals[:-2]}...")

        return x
    return wrapper


@logger
def concat(*args, **kwargs):
    val = ''
    for a in args:
        val += str(a)
    for k in kwargs.values():
        val += str(k)
    return val

@logger
def sum(*args, **kwargs):
    s = 0
    for a in args:
        s += a
    for k in kwargs.values():
        s += k
    return s
@logger
def print_arg(arg):
    print(arg)


print(concat(1))
print(sum(2,3))
print_arg(2)

