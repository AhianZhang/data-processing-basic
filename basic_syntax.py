# get data form console and print
# data = input("please input: ")
# print(data)


# print
print('a', 'b')  # a b
print('a', 'b', sep='.')  # a.b
print('a', 'b', end=',')  # a b,c
print('c')

# list combine
a = ['a', 'b']
b = [1, 2]
c = a + b  # combine
d = a * 3  # repeat 3 times
print(c)
print(d)
# list delete elements by index
arr = [1, 2, 3]
print("before delete:", arr)
del arr[0]
print("after delete:", arr)
# find element
arr = [1, 2, 3]
print(1 in arr)
print(4 in arr)

# fast value assignment
arr = [1, 2, 3]
first, second, third = arr
print(first, second, third, sep=',')

# list add method: append(), insert()
arr = [1, 2, 3]
arr.append(4)
print(arr)  # [1, 2, 3, 4]
arr.insert(0, 0)  # insert an element where index is 0
print(arr)  # [0, 1, 2, 3, 4]

# list remove method: remove(val)
arr = [1, 2, 3, 2]
arr.remove(2)
print(arr)  # [1, 3, 2]

# list sort
arr = [1, 2, 3, 2]
arr.sort()
print(arr)  # [1, 2, 2, 3]
arr.sort(reverse=True)
print(arr)  # [3, 2, 2, 1]
arr = ["a", "A", "a", "B", "b"]
arr.sort()  # ascii ordered
print(arr)
arr = ["a", "A", "a", "B", "b"]
arr.sort(key=str.lower)  # dictionary ordered
print(arr)

# string isX()
str = "abc"
print(str.islower())
print(str.isupper())
print(str.isalpha())
print(str.isnumeric())
# startwith endwith
print("abc".startswith('a'))
print("abc".endswith('c'))
# join split
print(','.join("abc"))  # a,b,c
print('a b c'.split())  # ['a', 'b', 'c']

# text align  rjust() ljust() center()
print('abc'.rjust(5))
print('abc'.ljust(5))
print('abc'.center(5))
print('abc'.center(10, '*'))
# trim str
print(' abc '.strip())
print(' abc '.lstrip())
print(' abc '.rstrip())

