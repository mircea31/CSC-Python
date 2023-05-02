######1!!!

# def f1(a):
#     return a*10

# list1 = list(range(10))
# print(list1)

# map1 = map(f1, list1)
# print(list(map1))

# map2 = map(lambda a: a*10, list1)
# print(list(map2))
#############################
# iteme = [1, 2, 3, 4, 5]
# patrat = []
# for i in iteme:
#     patrat.append(i**2)

# iteme = [1, 2, 3, 4, 5]
# patrat = list(map(lambda x: x**2, iteme))
# print(patrat)

#````````````
# def multiply(x):
#     return (x*x)
# def add(x):
#     return (x+x)

# funcs = [multiply, add]
# for i in range(5):
#     value = list(map(lambda x: x(i), funcs))
#     print(value)

######filter!!!!
####ex1
# ages = [5, 12, 17, 18, 24, 32]

# def myFunc(x):
#   if x < 18:
#     return False
#   else:
#     return True

# adults = filter(myFunc, ages)

# for x in adults:
#   print(x)

######ex2
# number_list = range(-5, 5)
# less_than_zero = list(filter(lambda x: x < 0, number_list))
# print(less_than_zero)


####REDUCE

# from functools import reduce
# reduce(lambda a,b: a*b, [1,2,3,4,5])

# print(reduce(lambda a,b: a+" "+b, "pyyython"))