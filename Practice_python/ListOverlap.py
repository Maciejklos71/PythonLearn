import random
list_one = random.sample(range(0, 20), 30)
list_two = random.sample(range(0, 20), 25)
list_three = list(set([el for el in list_one if el in list_two]))
print(list_three)


#import random
#print([list(set([el for el in random.sample(range(0, 29), 16) if el in random.sample(range(0, 20), 15)]))])
