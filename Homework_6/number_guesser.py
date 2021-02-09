def number_guesser(num):
    start = 0
    end = 1000
    n = (start + end)//2
    print(f'My guess number 1: {n}')
    num = int(input())
    while num != 0:
        if num == 1:
            start = n
            n = (start + end) // 2
            if n == start:
                return 'I couldn’t guess in 10 steps! This means you cheated!'
            print(f'My guess number 1: {n}')
            num = int(input())
        elif num == -1:
            end = n
            n = (start + end) // 2
            if n // 2 == start:
                return 'I couldn’t guess in 10 steps! This means you cheated!'
            print(f'My guess number 1: {n}')
            num = int(input())
    return f'Your number is {n}', 'I guessed it in 10 steps!'

print('Think of a number between 1 and 999. Input 0 once you’re ready to play.')
first_num = input()
print(number_guesser(first_num))