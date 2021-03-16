import tkinter as tk
import csv

master = tk.Tk()
master.geometry('300x300')


class Computers:
    def __init__(self, brand, model, cpu, ram, storage, os=None, os_version=None):
        self.brand = brand
        self.model = model
        self.cpu = cpu
        self._ram = None
        self.ram = ram
        self.storage = storage
        self.os = os
        self.os_version = os_version

    @property
    def full_name(self):
        return f'Brand: {self.brand} Model: {self.model}'


    @property
    def ram(self):
        return self._ram

    @ram.setter
    def ram(self, value):
        value = int(value[:-2])
        self._ram = value


class Laptops(Computers):
    def __init__(self, brand, model, cpu, ram, storage, category, screen_size,
                 screen, gpu, weight, price, os=None, os_version=None):
        super().__init__(brand, model, cpu, ram, storage, os, os_version)
        self.category = category
        self.screen_size = float(screen_size[:-1])
        self.screen = screen
        self.gpu = gpu
        self._weight = None
        self.weight = weight
        self._price = None
        self.price = price

    @property
    def full_name_5_expensive_cheap(self):
        return f'Brand: {self.brand} Model: {self.model} Price: {self.price}'

    @property
    def full_name_5_heavy(self):
        return f'Brand: {self.brand} Model: {self.model} Weight: {self.weight}'

    @property
    def full_name_5_powerful(self):
        return f'Brand: {self.brand} Model: {self.model} RAM: {self.ram}'

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for letter in alphabet:
            value = value.replace(letter, '')
        self._weight = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        bad_char = ','
        value = float(value.replace(bad_char, '.'))
        self._price = value


def laptops():
    with open('/Users/Liluk/Desktop/laptops.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            yield Laptops(
                brand=row['Manufacturer'],
                model=row['Model Name'],
                category=row['Category'],
                screen_size=row['Screen Size'],
                screen=row['Screen'],
                cpu=row['CPU'],
                ram=row['RAM'],
                storage=row['Storage'],
                gpu=row['GPU'],
                os=row['Operating System'],
                os_version=row['Operating System Version'],
                weight=row['Weight'],
                price=row['Price (Euros)'],
            )


# 5 MOST EXPENSIVE LAPTOPS
data_price = {}
for lt in laptops():
    if lt._price in data_price:
        data_price[lt._price].append(lt.full_name_5_expensive_cheap)
    else:
        data_price[lt._price] = [lt.full_name_5_expensive_cheap]


def print_5_most_expensive():
    result_expensive = sorted(data_price.items(), key=lambda x: x[0], reverse=True)[:5]
    print()
    l_expensive = []
    for i in range(len(result_expensive)):
        for j in range(len(result_expensive[i][1])):
            l_expensive.append(result_expensive[i][1][j])
    print('5 MOST EXPENSIVE LAPTOPS')
    for i in range(5):
        print(l_expensive[i])


# 5 CHEAPEST LAPTOPS
def print_5_cheapest():
    result_cheap = sorted(data_price.items(), key=lambda x: x[0], reverse=False)[:5]
    print()
    l_cheap = []
    for i in range(len(result_cheap)):
        for j in range(len(result_cheap[i][1])):
            l_cheap.append(result_cheap[i][1][j])
    print('5 CHEAPEST LAPTOPS')
    for i in range(5):
        print(l_cheap[i])


# OPERATION SYSTEMS COUNT
op_sys = {}
for lt in laptops():
    if lt.os in op_sys:
        op_sys[lt.os] += 1
    else:
        op_sys[lt.os] = 1


def print_operation_sys():
    result_os = {k: v for k, v in sorted(op_sys.items(), key=lambda x: x[1], reverse=False)}
    print()
    print('OPERATION SYSTEMS COUNT')
    for k, v in result_os.items():
        print('{}: {}'.format(k, v), end=', ')
    print()


# 5 HEAVIEST LAPTOPS
data_weight = {}
for lt in laptops():
    if lt._weight in data_weight:
        data_weight[lt._weight].append(lt.full_name_5_heavy)
    else:
        data_weight[lt._weight] = [lt.full_name_5_heavy]


def print_weight():
    result_heavy = sorted(data_weight.items(), key=lambda x: x[0], reverse=True)[:5]
    l_weight = []
    for i in range(len(result_heavy)):
        for j in range(len(result_heavy[i][1])):
            l_weight.append(result_heavy[i][1][j])
    print()
    print('5 HEAVIEST LAPTOPS')
    for i in range(5):
        print(f'{l_weight[i]}kg')
    print()


# 5 MOST POWERFUL LAPTOPS
data_ram = {}
for lt in laptops():
    if lt._ram in data_ram:
        data_ram[lt._ram].append(lt.full_name_5_powerful)
    else:
        data_ram[lt._ram] = [lt.full_name_5_powerful]


def print_power():
    result_ram = sorted(data_ram.items(), key=lambda x: x[0], reverse=True)[:5]
    l_powerful = []
    for i in range(len(result_ram)):
        for j in range(len(result_ram[i][1])):
            l_powerful.append(result_ram[i][1][j])
    print()
    print('5 MOST POWERFUL LAPTOPS')
    for i in range(5):
        print(f'{l_powerful[i]}GB')


# ALL SIZE RAM COUNTS
ram_count = {}
for lt in laptops():
    if lt._ram in ram_count:
        ram_count[lt._ram] += 1
    else:
        ram_count[lt._ram] = 1


def print_ram_counts():
    result_ram_count = sorted(ram_count.items(), key=lambda x: x[0], reverse=True)
    print()
    print('ALL SIZE RAM COUNTS')
    for k, v in result_ram_count:
        print(f'{k}GB: {v}', end=', ')
    print()


# SCREEN SIZE COUNTS
screen_count = {'10" and less': 0, '10" - 13"': 0, '13" - 15"': 0, '15" and more': 0}
for lt in laptops():
    if lt.screen_size <= 10:
        screen_count['10" and less'] += 1
    elif 10 < lt.screen_size <= 13:
        screen_count['10" - 13"'] += 1
    elif 13 < lt.screen_size <= 15:
        screen_count['13" - 15"'] += 1
    else:
        screen_count['15" and more'] += 1


def print_screen_count():
    print()
    print('SCREEN SIZE COUNTS')
    for k, v in screen_count.items():
        print('{}: {} //'.format(k, v), end=' ')
    print()


# ALL BRANDS COUNTS
brand_count = {}
for lt in laptops():
    if lt.brand in brand_count:
        brand_count[lt.brand] += 1
    else:
        brand_count[lt.brand] = 1


def print_brand_count():
    result_brand_count = {k: v for k, v in sorted(brand_count.items(), key=lambda x: x[0], reverse=False)}
    print()
    print('ALL BRANDS COUNTS')
    for k, v in result_brand_count.items():
        print('{}: {}'.format(k, v), end=', ')
    print()


tk.Button(master, command=print_5_most_expensive, text='5 MOST EXPENSIVE LAPTOPS', bd=5, bg='indigo', width=40).pack()
tk.Button(master, command=print_5_cheapest, text='5 CHEAPEST LAPTOPS', bd=5, bg='darkviolet', width=40).pack()
tk.Button(master, command=print_operation_sys, text='OPERATION SYSTEMS COUNT', bd=5, bg='darkorchid', width=40).pack()
tk.Button(master, command=print_weight, text='5 HEAVIEST LAPTOPS', bd=5, bg='mediumorchid', width=40).pack()
tk.Button(master, command=print_power, text='5 MOST POWERFUL LAPTOPS', bd=5, bg='orchid', width=40).pack()
tk.Button(master, command=print_ram_counts, text='ALL SIZE RAM COUNTS', bd=5, bg='violet', width=40).pack()
tk.Button(master, command=print_screen_count, text='SCREEN SIZE COUNTS', bd=5, bg='plum', width=40).pack()
tk.Button(master, command=print_brand_count, text='ALL BRANDS COUNTS', bd=5, bg='pink', width=40).pack()
exit_button = tk.Button(master, command=master.destroy, text='THANKS FOR KNOWLEDGE GIVEN US!!!\nEXIT',
                        bd=5, bg='lightpink', width=40).pack()


master.mainloop()
