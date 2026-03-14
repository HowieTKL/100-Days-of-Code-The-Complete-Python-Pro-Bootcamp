def add(*args):
    result = 0
    for n in args:
        result += n
    return result

print(add(1,2,3,4,5))


def calc(n, **kwargs):
    print(n, kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calc(2, add=5, multiply=3)