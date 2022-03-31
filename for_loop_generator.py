# rushikesh bhakare 

def range_func(n):
    for i in range(n):
        yield i

x = range_func(10)
print(next(x))
print(next(x))

print(next(x))

print(next(x))

print(next(x))
