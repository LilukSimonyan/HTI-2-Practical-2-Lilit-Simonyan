def prime(n):
    is_prime = True

    if n == 1:
        is_prime = False
    if n % 2 == 0 and n > 2:
        is_prime = False
    for i in range(1, n - 2):
        if n % (i + 1) == 0:
            is_prime = False
    if is_prime:
        return 'Yes'
    if not is_prime:
        return 'No'

print(prime(13))
print(prime(11))
print(prime(9))
print(prime(4))
print(prime(1))
print(prime(2))