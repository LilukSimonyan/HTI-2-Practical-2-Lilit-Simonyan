def intermediate(n):
    root_str = str(n)
    sum = 0

    for i in range(len(root_str)):
        sum = sum + int(root_str[i])
    while sum >= 10:
        return intermediate(sum)
    else:
        return sum

n = int(input("Let's find a root of number: "))
print(intermediate(n))
