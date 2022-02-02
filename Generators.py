

# python generators.


def simple_generator():

    yield 1
    yield 5
    yield 10


x = simple_generator()

print(next(x))
print(next(x))
print(next(x))
