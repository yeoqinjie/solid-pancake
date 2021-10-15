num = 0
try:
    num = input("Please input a positive number: ")
    num = int(num)
    if num < 0:
        raise TypeError
    result = 10 / num
except ValueError:
    pass
except TypeError:
    num = num * -1
    result = 10 / num
except ZeroDivisionError:
    result = 1000000

