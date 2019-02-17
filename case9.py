import ru_local
import random

start = {'bitcoins': 10000, 'staff': 100, 'shops': 5, 'gigabytes': 10000, 'working conditions': 5, 'quarter': 1}
print()
print('{}'.format(ru_local.WELLCOME))
print('{}'.format(ru_local.SEAS))
print('{}'.format(ru_local.TAX))
print('{}'.format(ru_local.INTERNET))
print('{}'.format(ru_local.POOR))
print()
print('{}'.format(ru_local.YOU_ARE))
print('{}'.format(ru_local.YOU_ARE_1))
print('{}'.format(ru_local.YOU_ARE_2))
print('{}'.format(ru_local.YOU_ARE_3))
print()

def selling():
    """Information about selling"""
    price1 = random.randint(20, 35)
    buyers = '{}'.format(ru_local.PEOP_READY), price1, '{}'.format(ru_local.SELL)
    print(*buyers)
    chek = False
    while not chek:
        try:
            amount1 = int(input())
            chek = True
            _max1 = start.get('gigabytes', [])
            update2 = {'bitcoins': start.get('bitcoins', []) + amount1 * price1,
                       'gigabytes': start.get('gigabytes', []) - amount1}
            update3 = {'bitcoins': start.get('bitcoins', []) + _max1 * price1,
                       'gigabytes': start.get('gigabytes', []) - _max1}
            if amount1 < start.get('gigabytes', []):
                start.update(update2)
            else:
                print('{}'.format(ru_local.YOU_CANT), _max1)
                start.update(update3)
        except ValueError:
            chek = False
            print('{}'.format(ru_local.PRINT_NUM))
def buying():
    """Information about buying"""
    price = random.randint(20, 35)
    sellers = '{}'.format(ru_local.TODAY), price, '{}'.format(ru_local.BTC_BUY)
    print(*sellers)
    chek = False
    while not chek:
        try:
            amount = int(input())
            chek = True
            _max = start.get('gigabytes', []) // price
            update = {'bitcoins': start.get('bitcoins', []) - amount * price, 'gigabytes': start.get('gigabytes', []) + amount}
            update1 = {'bitcoins': start.get('bitcoins', []) - _max * price, 'gigabytes': start.get('gigabytes', []) + _max}
            if amount * price < start.get('gigabytes', []):
                start.update(update)
            else:
                print('{}'.format(ru_local.CANT_BUY), _max)
                start.update(update1)
        except ValueError:
            chek = False
            print('{}'.format(ru_local.PRINT_NUM))


selling()
buying()
print(start)
