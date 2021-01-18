def intermediate(n): #78996
    root_str = str(n)
    sum = 0

    for i in range(len(root_str)):
        sum = sum + int(root_str[i])
    return sum
def root(n):
    while intermediate(n) > 10:
        n = intermediate(n)
        sum = 0
        intermediate(n)
    else:
        print(intermediate(n))


root(78996)
root(10)
root(8)
root(37100005)
