def roman_to_integer(roman):
    l = []
    for i in range(len(roman)):
        l = l + [roman[i], ]

    for i in range(len(l)):
        try:
            if l[i] == 'I':
                if l[i + 1] == 'V' or l[i + 1] == 'X':
                    l[i] = -1
                else:
                    l[i] = 1
        except IndexError:
            l[i] = 1
        try:
            if l[i] == 'X':
                if l[i + 1] == 'L' or l[i + 1] == 'C':
                    l[i] = -10
                else:
                    l[i] = 10
        except IndexError:
            l[i] = 10
        try:
            if l[i] == 'C':
                if l[i + 1] == 'D' or l[i + 1] == 'M':
                    l[i] = -100
                else:
                    l[i] = 100
        except IndexError:
            l[i] = 100

        if l[i] == 'V':
            l[i] = 5
        if l[i] == 'L':
            l[i] = 50
        if l[i] == 'D':
            l[i] = 500
        if l[i] == 'M':
            l[i] = 1000

    def sum_of_elements(l):
        if not l:
            return 0
        return l[0] + sum_of_elements(l[1:])

    return sum_of_elements(l)

text = input('Enter a text: ')
print(roman_to_integer(text))