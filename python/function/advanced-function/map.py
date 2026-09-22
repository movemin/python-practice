def power(number):
    return number ** 2

A_list = [num for num in range(1, 5)]

iterator = map(power, A_list)

print(list(iterator))
print(iterator)
