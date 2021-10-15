a = input('Please key in a number from 1 - 10: ')

a = int(a)
b = input('Please key in another number from 1 - 10: ')
b = int(b)

add = a + b
minus = a - b
multiply = a * b
divide = a / b
modulus = a % b

print(add)
print(minus)
print(multiply)
print(divide)
print(modulus)

list_a = [1, 2, 3, 4]

for x in list_a:
    x = x + 2
    print(x)


def add_2_nums():
    add2 = 1 + 2
    print(add2)
