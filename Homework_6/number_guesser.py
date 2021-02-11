def number_guesser(num):
    start = 0
    end = 1000
    i = 0
    while num != 0:
        if num == 1:
            start = (start + end) // 2
        elif num == -1:
            end = (start + end) // 2
        if start == (start + end) // 2:
            return 'I couldn’t guess in 10 steps! This means you cheated!'
        i += 1
        num = int(input(f'My guess number {i}: {(start + end) // 2}\nInput: '))
    return f'Your number is {(start + end) // 2}, I guessed it in {i} steps!'

first_num = input(f'Think of a number between 1 and 999. Input 0 once you’re ready to play.\nInput: ')
print(number_guesser(first_num))