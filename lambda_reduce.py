from functools import reduce
nums = [3,2,6,8,4,6,2,9]
evens = list(filter(lambda n:n%2 ==0,nums))
print(evens)
doubls = list(map(lambda n:n*2,evens))
print(doubls)
sum = reduce(lambda a,b: a+b, doubls)
print(sum)