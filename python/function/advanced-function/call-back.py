def call_10_times(call_back_func):
    for i in range(10):
        call_back_func(i)

def print_hello(parameter):
    print("hello", parameter)

call_10_times(print_hello)