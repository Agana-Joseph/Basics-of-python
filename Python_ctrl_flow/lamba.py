#print(list(filter((lambda x: x % 2 == 0), range(1, 11))))
numbers = [-1, -3, -4, 5, 6, 7, 8]
print(list(filter((lambda n: n > 0, numbers), range(-1, -11))))
