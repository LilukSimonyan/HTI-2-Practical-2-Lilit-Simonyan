def segment_length(n):
    # էս լուծումով կարող ենք ցանկացած n-անկյան համար հաշվել, ստուգել եմ 4,5,6-անկյունների դեպքում
    # բոլոր կողմերի հաշվարկը Պյութագորասի թեորեմով, a**2 + b**2 = c**2
    # հայտարարում ենք p, որը (x1, y1) և (xn, yn) կողմն է կազմում, (xn, yn) n-անկյան վերջին կետն է
    p = pow(((n[len(n) - 1] - n[1]) ** 2) + ((n[len(n) - 2] - n[0]) ** 2), 0.5)
    print(p)
    for i in range(0, len(n), 2):
        while i < len(n)//2 + len(n)//4:
            a = pow(((n[i + 3] - n[i + 1]) ** 2) + ((n[i + 2] - n[i]) ** 2), 0.5)
            print(a)  # որպեսզի կողմերի երկարություններն էլ վերադարձնի
            p = p + a
            break
    return p

n = [float(num) for num in input('Enter a number list: ').split()]
print("P =", segment_length(n))
