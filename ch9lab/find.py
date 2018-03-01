def find(the_list,b):
    current = -1
    for i in the_list:
        current = current + 1
        if i == b:
            print('Found', i, 'at position', current)




my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]
find(my_list, 12)
find(my_list, 91)
find(my_list, 80)
