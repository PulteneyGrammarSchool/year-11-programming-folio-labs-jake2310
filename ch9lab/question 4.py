import random
import numpy as np
def my_list(a):
    lists = []
    for i in range(a):
        lists.append(int(random.randint(1,6)))
    return lists
print(my_list(5))

def count_list(a,b):
    count = 0
    for i in a:
        if i == b:
            count = count + 1
    return count
print(count_list([1,2,3,3,3,4,2,1],5))

def average_list(a):
    return int(np.mean(a))
print(average_list([1,2,3]))
