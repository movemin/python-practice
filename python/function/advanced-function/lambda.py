def power(number):
    return number ** 2
print(power(10))

power = lambda number: number ** 2
print(power(10))

def is_odd(number):
    return number % 2 == 0
print(is_odd(10))

is_odd = lambda number: number % 2 == 0
print(is_odd(10))

my_list = [num for num in range(1, 6)]
iterater = map(lambda number: number ** 2, my_list)
print(list(iterater))

iterater = filter(lambda number: number % 2 == 0, my_list)
print(list(iterater))