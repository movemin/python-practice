def custom_filter(data, func):
    output = []
    for num in data:
        if func(num):
            output.append(num)
    return output
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print(custom_filter(numbers, lambda item: item % 2 == 0))