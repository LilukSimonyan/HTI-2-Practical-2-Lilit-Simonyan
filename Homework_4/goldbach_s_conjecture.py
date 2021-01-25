def is_prime(n):
    if n == 1:
        return False
    if n > 2 and n % 2 == 0:
        return False
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True

def goldbach_s_conjecture(num):
    while num <= 2 or num >= 10000 or num % 2 != 0:
        print('Please, enter an even number between 2 and 10000: ')
        num = int(input('Enter a number: '))
    else:
        if num == 4:
            return 2, 2
        else:
            prime_num = 3
            for i in range(2, num//2 + 1):
                if not is_prime(prime_num) or not is_prime(num - prime_num):
                    prime_num = prime_num + 2
                else:
                    return prime_num, num - prime_num

num = int(input('Enter a number: '))
print(goldbach_s_conjecture(num))