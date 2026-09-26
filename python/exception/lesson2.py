number = input("정수 입력> ")

if number.isdigit():
    int_number = int(number)
    print(f"원의 반지름: {number}")
    print(f"원의 둘레: {number * 2 * 3.14}")
    print(f"원의 넓이: {number ** 2 * 3.14}")
else:
    print("정수를 입력하지 않았습니다.")