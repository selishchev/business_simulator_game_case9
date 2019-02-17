import random

start = {'bitcoins': 10000, 'staff': 100, 'territory': 150, 'gigabytes': 10000, 'working conditions': 5, 'quarter': 0}


def buying():
    """Information about buying"""
    price = random.randint(20, 35)
    seller = 'На сегодняшний день 1 Гб информации на черном рынке продается за', price, 'биткойнов. Сколько гб купить?'
    print(*seller)
    amount = int(input())
    _max = start.get('gigabytes', []) // price
    update = {'bitcoins': start.get('bitcoins', []) - amount * price, 'gigabytes': start.get('gigabytes', []) + amount}
    update1 = {'bitcoins': start.get('bitcoins', []) - _max * price, 'gigabytes': start.get('gigabytes', []) + _max}
    if amount * price < start.get('gigabytes', []):
        start.update(update)
    else:
        print('Вы не можете купить столько, максимум:', _max)
        start.update(update1)





buying()
print(start)