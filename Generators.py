

# python generators.


from calendar import c
import sys

def simple_generator():

    yield 1
    yield 5
    yield 10


x = simple_generator()




print(next(x))
print(next(x))
print(next(x))
