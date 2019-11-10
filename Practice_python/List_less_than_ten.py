import random
randList = random.sample(range(0, 40), 20)
print(randList)
lists = [i for i in randList if i <= 6]
lists.sort()
print(lists)
