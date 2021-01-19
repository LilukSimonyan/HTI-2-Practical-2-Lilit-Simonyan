def factorial(n):
    f = 1
    for i in range(n):
        f = f * (i + 1)
    return f

n = int(input("Enter a number: "))
print(factorial(n))