num_pets = 2
size_household = 2
total = (num_pets + size_household)
print("Pets and household addition: ")
print(total)

def add(x, y, z):
    return(x + y + z)
    
sum1 = add(3, 3, 10)
print("Practice Sum 1:")
print(sum1)
sum2 = add(sum1, 2, 2)
print("Practice Sum 2:")
print(sum2)


def pi_party(x):
    pi = 3.14159
    return((x ** 2) * pi)


def num_get(y):
    num = y
    while num < 10:
        if num % 2 == 0:
            num = num + 1
        else:
            num = num + 1
    return num



area = pi_party(6)
print("Example 1 - Pi Area:")
print(area)
my_num = num_get(7)
print("Example 2 - Number Iterate:")
print(my_num)


   
