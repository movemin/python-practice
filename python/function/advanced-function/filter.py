def is_even_number(number):
    if number % 2 == 0:
        return True
    return False

A_list = [num for num in range(1, 6)]

iterator = filter(is_even_number, A_list)

print(list(iterator))