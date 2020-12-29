s = input('Enter your ticket number or exit to finish: ')

while str(s) != 'exit':
    while int(s) < 10 or int(s) > 99999999 or len(s) % 2 != 0:
        print('Please, enter correct number!')
        s = input('Enter your ticket number or exit to finish: ')
    else:
        if len(s) == 2:
            if s[0] != s[1]:
                print('HO-HO-HO, YOU LOST!')
                print('If you have another ticket enter it, else enter exit to finish')
            else:
                print('CONGRATULATIONS, YOU WON!!!')
                print('If you have another ticket enter it, else enter exit to finish')
        else:
            a = int(s[0])
            for i in range(len(s)//2 - 1):
                b = int(s[len(s)//2])
                for j in range(len(s)//2 + 1, len(s)):
                    sum2 = b + int(s[j])
                    b = sum2
                sum1 = a + int(s[i + 1])
                a = sum1
            if sum1 != sum2:
                print('HO-HO-HO, YOU LOST!')
                print('If you have another ticket enter it, else enter exit to finish')
            else:
                print('CONGRATULATIONS, YOU WON!!!')
                print('If you have another ticket enter it, else enter exit to finish')
    s = input('Enter your ticket number or exit to finish: ')