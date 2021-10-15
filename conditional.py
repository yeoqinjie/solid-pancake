var_a = True
var_b = 5
var_c = "Hello"
var_d = "hello"

result = var_a and var_b < 10
result2 = var_c == var_d

result3 = result or result2
result4 = (var_a and var_b < 10) or (var_c == var_d)

print(result4)

if var_b > 0:
    print('Positive')
else:
    print('Negative')

print('Positive') if var_b > 0 else print('Negative')