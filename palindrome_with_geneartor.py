

def is_pallindrome(num):

    if num % 10 ==0:
        return False
    
    temp = num
    reversed_n = 0

    while temp != 0:
        reversed_n = (temp % 10) + (reversed_n * 10)
        temp = temp // 10
    print(reversed_n)
    if reversed_n == num :
        return True
    return False


print(is_pallindrome(1001))

def my_pallindrome_sequence_generator(n):

    for i in range(10,n+1):
        if is_pallindrome(i):
            print(i)


x = my_pallindrome_sequence_generator(100)

print(next(x))
print(next(x))

print(next(x))

print(next(x))

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))




