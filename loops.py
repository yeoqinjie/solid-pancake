# list = [1, 2, 3, 4, 5]
#
# for x in list:
#     x = x * 2  # x *= 2
#     print(x)

# dict = {'a': 1, 'b': 2, 'c': 3}
#
# for a, b in dict.items():
#     print(a, b)

# table = [[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9]]
#
# for x in range(3): # 2
#     for y in range(3): # 0
#         print(x, y, table[x][y])

a = 5
counter = 0
while a > 0:
    a -= 0.03213
    counter += 1

print(counter)
