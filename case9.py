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

    check = False
    while not check:
        try:
            amount1 = int(input())
            check = True
            _max1 = start.get('gigabytes', [])
            update2 = {'bitcoins': start.get('bitcoins', []) + amount1 * price1,
                       'gigabytes': start.get('gigabytes', []) - amount1}
            update3 = {'bitcoins': start.get('bitcoins', []) + _max1 * price1,
                       'gigabytes': start.get('gigabytes', []) - _max1}
            if amount1 < start.get('gigabytes', []):
                start.update(update2)
            else:
                check = False
                print('{}'.format(ru_local.YOU_CANT), _max1)
                start.update(update3)
        except ValueError:
            check = False
            print('{}'.format(ru_local.PRINT_NUM))


def buying():
    """Information about buying"""
    price = random.randint(20, 35)
    sellers = '{}'.format(ru_local.TODAY), price, '{}'.format(ru_local.BTC_BUY)
    print(*sellers)

    check = False
    while not check:
        try:
            amount = int(input())
            check = True
            _max = start.get('gigabytes', []) // price
            update = {'bitcoins': start.get('bitcoins', []) - amount * price, 'gigabytes': start.get('gigabytes', []) + amount}
            update1 = {'bitcoins': start.get('bitcoins', []) - _max * price, 'gigabytes': start.get('gigabytes', []) + _max}
            if amount * price < start.get('gigabytes', []):
                start.update(update)
            else:
                check = False
                print('{}'.format(ru_local.CANT_BUY), _max)
                start.update(update1)
        except ValueError:
            check = False
            print('{}'.format(ru_local.PRINT_NUM))


def investments():
    """Investments in new technologies"""
    inv = '{}'.format(ru_local.HOW_MANY)
    print(inv)
    check = False
    while not check:
        try:
            gb = int(input())
            check = True
            _max2 = start.get('gigabytes', [])
            update4 = {'gigabytes': start.get('gigabytes', []) - gb}
            update5 = {'gigabytes': 0}
            if gb < _max2:
                start.update(update4)
            else:
                check = False
                print('{}'.format(ru_local.CANT_INVEST), _max2)
                start.update(update5)
        except ValueError:
            check = False
            print('{}'.format(ru_local.PRINT_NUM))


def salaries():
    """Information about salaries"""
    question = '{}'.format(ru_local.PAYMENT)
    print(question)
    check = False
    while not check:
        try:
            sal = int(input())
            check = True
            _max3 = start.get('bitcoins', [])
            update6 = {'bitcoins': start.get('bitcoins', []) - sal}
            update7 = {'bitcoins': 0}
            if sal < _max3:
                start.update(update6)
            else:
                check = False
                print('{}'.format(ru_local.ERR_PAYMENT), _max3)
                start.update(update7)
        except ValueError:
            check = False
            print('{}'.format(ru_local.PRINT_NUM))


print(start)
selling()
print(start)
buying()
print(start)
investments()
print(start)
salaries()
print(start)
