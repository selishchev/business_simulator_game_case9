import random

start = {'bitcoins': 10000, 'staff': 100, 'territory': 150, 'gigabytes': 10000, 'working conditions': 95, 'quarter': 0}


def selling():
    """Information about selling"""
    price1 = random.randint(20, 35)
    buyers = 'Люди готовы купить 1 Гб информации за', price1, 'биткойнов. Сколько Гб продать?'
    print(*buyers)
    amount1 = int(input())
    _max1 = start.get('gigabytes', [])
    update2 = {'bitcoins': start.get('bitcoins', []) + amount1 * price1,
               'gigabytes': start.get('gigabytes', []) - amount1}
    update3 = {'bitcoins': start.get('bitcoins', []) + _max1 * price1,
               'gigabytes': start.get('gigabytes', []) - _max1}
    if amount1 < start.get('gigabytes', []):
        start.update(update2)
    else:
        print('Вы не можете столько продать, максимум:', _max1)
        start.update(update3)


def buying():
    """Information about buying"""
    price = random.randint(20, 35)
    sellers = 'На сегодняшний день 1 Гб хранилища на флешках продается за', price, 'биткойнов. Сколько Гб купить?'
    print(*sellers)
    amount = int(input())
    _max = start.get('bitcoins', []) // price
    update = {'bitcoins': start.get('bitcoins', []) - amount * price, 'gigabytes': start.get('gigabytes', []) + amount}
    update1 = {'bitcoins': start.get('bitcoins', []) - _max * price, 'gigabytes': start.get('gigabytes', []) + _max}
    if amount * price < start.get('gigabytes', []):
        start.update(update)
    else:
        print('Вы не можете столько купить, максимум:', _max)
        start.update(update1)


def investments():
    """Investments in new technologies"""
    inv = 'Сколько Гб вы хотите инвестировать в разработку новых технологий?'
    print(inv)
    gb = int(input())
    _max2 = start.get('gigabytes', [])
    update4 = {'gigabytes': start.get('gigabytes', []) - gb}
    update5 = {'gigabytes': 0}
    if gb < _max2:
        start.update(update4)
    else:
        print('Вы не можете столько инвестировать, максимум:', _max2)
        start.update(update5)


def salaries():
    """Information about salaries"""
    question = 'Сколько биткойнов выделить на зарплату рабочим?'
    print(question)
    sal = int(input())
    _max3 = start.get('bitcoins', [])
    update6 = {'bitcoins': start.get('bitcoins', []) - sal}
    update7 = {'bitcoins': 0}
    if sal < _max3:
        start.update(update6)
    else:
        print('Вы не можете столько заплатить, максимум:', _max3)
        start.update(update7)


print(start)
selling()
print(start)
buying()
print(start)
investments()
print(start)
salaries()
print(start)
