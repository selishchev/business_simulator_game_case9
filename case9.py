import random

start = {'bitcoins': 10000, 'staff': 100, 'shops': 5, 'gigabytes': 10000, 'working conditions': 5, 'quarter': 1}


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
    sellers = 'На сегодняшний день 1 Гб информации на флешках продается за', price, 'биткойнов. Сколько Гб купить?'
    print(*sellers)
    amount = int(input())
    _max = start.get('gigabytes', []) // price
    update = {'bitcoins': start.get('bitcoins', []) - amount * price, 'gigabytes': start.get('gigabytes', []) + amount}
    update1 = {'bitcoins': start.get('bitcoins', []) - _max * price, 'gigabytes': start.get('gigabytes', []) + _max}
    if amount * price < start.get('gigabytes', []):
        start.update(update)
    else:
        print('Вы не можете столько купить, максимум:', _max)
        start.update(update1)
print('{0:^12} {1:^12} {2:^12} {3:^12} {4:^12} {5:^12}'.format('Бетховены','Сотрудники','Магазины','Гигабайты',
                                                               'Условия работы','Квартал'))
print('{0:^12} {1:^12} {2:^12} {3:^12} {4:^12} {5:^12}'
      .format(start.get('bitcoins'),start.get('staff'),start.get('shops'),start.get('gigabytes'),
                                 start.get('working conditions'), start.get('quarter')))
selling()
buying()
