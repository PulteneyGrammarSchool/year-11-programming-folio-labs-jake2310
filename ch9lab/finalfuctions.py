import random
import numpy as np
def my_list(a):
    lists = []
    for i in range(a):
        lists.append(int(random.randint(1,6)))
    return lists
nextlist = my_list(10000)
print(my_list(10000))

def count_list(a,b):
    count = 0
    for i in a:
        if i == b:
            count = count + 1
    return count
for i in range(6):
    print((i+1), count_list(nextlist,(i+1)))
def average_list(a):
    return int(np.mean(a))

print(average_list(nextlist))
