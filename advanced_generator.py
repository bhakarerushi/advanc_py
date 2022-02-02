

# Advanced generators with .send(), .threw(), .close()


from operator import ge


def demo_generator(num):

    for i in range(num):
        yield i

gen = demo_generator(10)

for i in gen:
    print(i)
    if i == 400:
        gen.throw(ValueError("lazy generator"))    # to throw exception in generator sequence

    gen.send(5)                                    # send will return back the given value to generator \
                                                    # and started excution from that given value.
    if i == 20:
        print("20 reach")
        gen.close()                                   # can close generator sequence at certain condition.