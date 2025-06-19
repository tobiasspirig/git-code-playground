squared = lambda num : num * num

print(squared(2))

addtwo = lambda num : num + 2

print(addtwo(12))

sum_total = lambda a, b: a + b
print(sum_total(10,5))

##########################

def funcbuilder(x):
    return lambda num : num + x

addten = funcbuilder(10)
addtwenty = funcbuilder(20)

print(addten(80))

##########################



numbers = [3,7,12,18,20,21]

squarednumbers = map(lambda num : num + num, numbers)
print(list(squarednumbers))


##########################



odd_nums = filter(lambda num : num % 2 != 0, numbers)

print(list(odd_nums))

##########################

from functools import reduce


numbers = [1,2,3,4,5,1]

total = reduce(lambda acc, curr : acc + curr, numbers, 10)

print(total)
print(sum(numbers, 10))

