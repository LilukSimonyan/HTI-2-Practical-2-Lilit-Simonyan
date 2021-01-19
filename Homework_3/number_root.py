def intermediate(n):
    root_str = str(n)
    sum = 0

    for i in range(len(root_str)):
        sum = sum + int(root_str[i])
    return sum
def root(n):
    while intermediate(n) >= 10:
        n = intermediate(n)
        sum = 0
        intermediate(n)
    else:
        return intermediate(n)

n = int(input("Let's find a root of number: "))
print(root(n))
