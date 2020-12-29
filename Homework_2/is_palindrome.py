s = input('Enter the word: ')

if len(s) == 1:
    print('Yes')
elif len(s) == 2:
    if s[0] != s[1]:
        print('No')
    else:
        print('Yes')
else:
    first = 0
    last = len(s) - 1
    while first < last:
        if s[first] == s[last]:
            first = first + 1
            last = last - 1
            print('Yes')
            break
        else:
            print('No')
            break

