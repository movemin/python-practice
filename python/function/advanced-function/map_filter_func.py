# map()
def my_map(func: function, lst: list):
    output = []
    for item in lst:
        output.append(func(item))
    return output

# filter()
def my_filter(func: function, lst: list):
    output = []
    for item in lst:
        if func(item):
            output.append(item)
    return output

# my_list
my_list = [num for num in range(1, 6)]

# power
def power(num: int):
    return num ** 2

print(my_map(power, my_list))

def is_even(num: int):
    if num % 2 == 0:
        return True
    return False

print(my_filter(is_even, my_list))