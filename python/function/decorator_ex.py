def out_decorator(number):
    def decorator(function):
        print("미리 어떤 처리를 진행합니다.", number)
        return function
    return decorator

@out_decorator(number = 100)
def test():
    print("안녕하세요")

test()