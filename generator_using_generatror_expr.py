

# Generator using Genrator Expression.
import sys

num_array1 = [n*2 for n in range(1000)]

num_array2 = (n*2 for n in range(1000))


print("list compression",num_array1)

print("generator expression",num_array2)

print("size of list compr",sys.getsizeof(num_array1))

print("size of geneatoir",sys.getsizeof(num_array2))