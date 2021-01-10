s = [int(num) for num in input('Enter a number list: ').split()]
product = s[0] * s[1]
for i in range(1, len(s)):
    a = s[i - 1]
    b = s[i]
    c = a * b
    if c > product:
        product = c
print(product)





