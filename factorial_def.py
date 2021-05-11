
def factorial(x):
    pr = 1
    for i in range(1, x + 1):
        pr *= i
    return pr

print(factorial(10))