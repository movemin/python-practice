def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return f(n - 1) + f(n - 2)

# revise
memo = {1: 2, 2: 1}
def f(n):
    if n in memo:
        return memo[n] 
    else:
        temp = f(n - 1) + f(n - 2)
        memo[n] = temp
        return temp
print(f(10))