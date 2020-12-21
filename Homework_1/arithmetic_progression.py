a1 = float(input('Enter first member of progression: '))
a2 = float(input('Enter second member of progression: '))
n = int(input('Enter N: '))
an = float(a1 + (n - 1) * (a2 - a1))
bn = int(a1 + (n - 1) * (a2 - a1))
if an - bn > 0:
    print('[', n, '] = ', an, sep='')
else:
    print('[', n, '] = ', bn, sep='')
