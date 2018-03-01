def min3(a,b,c):
    as_list = [a,b,c]
    as_list.sort()
    return as_list[0]

print(min3(4, 7, 5))
print(min3(4, 5, 5))
print(min3(4, 4, 4))
print(min3(-2, -6, -100))
print(min3("Z", "B", "A"))


#num1 = input('number 1: ')
#num2 = input('number 2: ')
#num3 = input('number 3: ')
#print(min3(num1, num2, num3))
