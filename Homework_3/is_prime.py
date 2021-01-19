def prime(n):
    is_prime = True

    if n == 1:
        is_prime = False
    elif n % 2 == 0 and n > 2:
        is_prime = False
    for i in range(1, n - 2):
        if n % (i + 1) == 0:
            is_prime = False
            break
    if is_prime:
        return 'Yes'
    if not is_prime:
        return 'No'

n = int(input("Enter a number: "))
print(prime(n))
