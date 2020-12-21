a1 = int(input('Enter a year "YYYY": '))
x = a1/100
y = a1//100
while a1 > 0:                 # եթե մուտքագրված տարեթիվը դրական թիվ է
    if x - y > 0:
        print('CE ', y + 1)   # Մ.Թ.
        break
    else:
        print('CE ', y)       # Մ.Թ.
        break
else:                         # եթե մուտքագրված տարեթիվը բացասական թիվ է
    if x - y < 0:
        print('BCE ', 1-y)    # Մ.Թ.Ա.
    else:
        print('BCE ', -y)     # Մ.Թ.Ա.