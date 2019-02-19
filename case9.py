import ru_local
import random
import sys

start = {'bitcoins': 10000, 'staff': 100, 'shops': 5, 'gigabytes': 10000, 'working conditions': 95, 'quarter': 0}
tech = 0

print()
print('{}'.format(ru_local.WELCOME))
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
    buyers = '{}'.format(ru_local.PEOPLE_READY), price1, '{}'.format(ru_local.SELL)
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
            if amount1 <= start.get('gigabytes', []):
                start.update(update2)
            else:
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
            _max = start.get('bitcoins', []) // price
            update = {'bitcoins': start.get('bitcoins', []) - amount * price,
                      'gigabytes': start.get('gigabytes', []) + amount}
            update1 = {'bitcoins': start.get('bitcoins', []) - _max * price,
                       'gigabytes': start.get('gigabytes', []) + _max}
            if amount * price < start.get('bitcoins', []):
                start.update(update)
            else:
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
            if gb <= _max2:
                start.update(update4)
                global tech
                tech += gb
            else:
                print('{}'.format(ru_local.CANT_INVEST), _max2)
                start.update(update5)
                tech += _max2
        except ValueError:
            check = False
            print('{}'.format(ru_local.PRINT_NUM))


def salaries():
    """Information about salaries"""
    question = '{}'.format(ru_local.PAYMENT)
    print(question)
    rand0 = random.randint(50, 100)
    rand1 = random.randint(0, 30)
    rand2 = random.randint(30, 50)
    check = False
    while not check:
        try:
            sal = int(input())
            check = True
            start1 = start.copy()
            _max3 = start.get('bitcoins', [])
            update6 = {'bitcoins': start.get('bitcoins', []) - sal}
            update7 = {'bitcoins': 0}
            update8 = {'working conditions': start.get('working conditions', []) - rand0}
            update9 = {'working conditions': start.get('working conditions', []) - rand1}
            update10 = {'working conditions': start.get('working conditions', []) + rand1}
            update11 = {'working conditions': start.get('working conditions', []) + rand2}
            update12 = {'working conditions': 100}
            if sal <= _max3:
                start.update(update6)
            else:
                print('{}'.format(ru_local.ERR_PAYMENT), _max3)
                start.update(update7)
            checking = start1.get('bitcoins', []) - start.get('bitcoins', [])
            if 0 <= checking <= 1000:
                start.update(update8)
            elif 1001 <= checking <= 5000:
                start.update(update9)
            elif 5001 <= checking <= 10000:
                start.update(update10)
            elif checking >= 10001:
                start.update(update11)
            if start.get('working conditions', []) > 100:
                start.update(update12)
        except ValueError:
            check = False
            print('{}'.format(ru_local.PRINT_NUM))


def chance_of_act():
    """Appearance of random acts"""
    rand = random.randint(1, 3)
    if rand >= 2:
        random_acts()


def staff():
    """Changing of staff"""
    rand = random.randint(30, 80)
    rand1 = random.randint(1, 30)
    update = {'staff': start.get('staff', []) - rand}
    update1 = {'staff': start.get('staff', []) - rand1}
    update2 = {'staff': start.get('staff', []) + rand}
    if start.get('working conditions', []) <= 40:
        start.update(update)
    elif 41 <= start.get('working conditions', []) <= 80:
        start.update(update1)
    elif 100 <= start.get('working conditions', []):
        start.update(update2)


def random_inv():
    """Success of investments"""
    rand = random.randint(1, 2)
    rand1 = random.randint(2, 3)
    global tech
    update = {'gigabytes': start.get('gigabytes', []) + tech * rand1}
    if rand == 1:
        print('{}'.format(ru_local.GOOD_INFORM_INVEST))
        start.update(update)
        tech = 0
    else:
        print('{}'.format(ru_local.BAD_INFORM_INVEST))
        tech = 0


def gbs():
    rand = random.randint(50, 100)
    rand1 = random.randint(1, 5)
    update = {'gigabytes': 0}
    update1 = {'staff': start.get('staff') - rand, 'shops': start.get('shops') - rand1,
               'working conditions': start.get('working conditions') - 50}
    if start.get('gigabytes', []) < 0:
        start.update(update)
    if start.get('gigabytes', []) == 0:
        print('{}'.format(ru_local.NO_GIGS))
        start.update(update1)


def loss():
    """Checking of conditions of loss"""
    if start.get('working conditions', []) <= 0:
        print('{}'.format(ru_local.NO_PEOPLE))
        menu()
        sys.exit()
    if start.get('shops', []) <= 0:
        print('{}'.format(ru_local.NO_SHOPS))
        menu()
        sys.exit()
    if start.get('staff', []) <= 0:
        print('{}'.format(ru_local.NO_STAFF))
        menu()
        sys.exit()


def counter():
    """Counting quarters"""
    update = {'quarter': start.get('quarter', []) + 1}
    start.update(update)


def random_1():
    situation = '{}'.format(ru_local.MVD)
    print(situation)
    check = False
    while not check:
        try:
            money = int(input())
            check = True
            _max3 = start.get('bitcoins', [])
            update6 = {'bitcoins': start.get('bitcoins', []) - money}
            update7 = {'bitcoins': 0}
            minimum = start.get('bitcoins', []) * 0.1
            if money < _max3:
                start.update(update6)
                if money < int(minimum):
                    close = start.get('shops', []) * 0.25 + 1
                    update = {'shops': start.get('shops', []) - int(close)}
                    start.update(update)
            else:
                print('{}'.format(ru_local.CANT_INVEST), _max3)
                start.update(update7)
        except ValueError:
            check = False
            print('{}'.format(ru_local.PRINT_NUM))


def random_2():
    gb = random.randint(100, 500)
    low_cond = random.randint(5, 10)
    print('{} {} {}'.format('{}'.format(ru_local.YOU_HAVE), gb,
                            '{}'.format(ru_local.UN_USE)))
    check = False
    while not check:
        answer = input().lower()
        check = True
        if answer == '{}'.format(ru_local.YES):
            cond = {'working conditions': start.get('working conditions', []) + low_cond}
            print('{}'.format(ru_local.HAPPY))
            start.update(cond)
        elif answer == '{}'.format(ru_local.NO):
            new_gb = {'gigabytes': start.get('gigabytes') + gb}
            start.update(new_gb)
            cond1 = {'working conditions': start.get('working conditions', []) - low_cond}
            print('{}'.format(ru_local.THEY_KNOW))
            start.update(cond1)
        else:
            check = False
            print('{}'.format(ru_local.YES_OR_NO))


def random_3():
    gb = random.randint(1000, 2000)
    print('{} {} {}'.format('{}'.format(ru_local.OH_NO), gb, '{}'.format(ru_local.GIG)))
    check = False
    while not check:
        b = input('{}'.format(ru_local.POLICE)).lower()
        check = True
        stolen = {'gigabytes': start.get('gigabytes') - gb}
        start.update(stolen)
        if b == '{}'.format(ru_local.YES):
            print('{}'.format(ru_local.DET))
            print('{}'.format(ru_local.BORYA))
            print('{}'.format(ru_local.LENIA))
            print('{}'.format(ru_local.NIK))
            check = False
            while not check:
                try:
                    c = int(input('{}'.format(ru_local.NUM_DET)))
                    check = True
                    if c == 1:
                        cost1 = {'bitcoins': start.get('bitcoins', []) - 15000}
                        start.update(cost1)
                        d = random.randint(1, 6)
                        if d == 6:
                            print('{}'.format(ru_local.IN_JAIL))
                        else:
                            back = {'gigabytes': start.get('gigabytes') + gb}
                            start.update(back)
                            print('{}'.format(ru_local.MAF))
                    elif c == 2:
                        cost2 = {'bitcoins': start.get('bitcoins', []) - 5000}
                        start.update(cost2)
                        e = random.randint(1, 6)
                        if e >= 5:
                            back2 = {'gigabytes': start.get('gigabytes') + 40}
                            start.update(back2)
                            print('{}'.format(ru_local.HATE))
                        elif e == 4:
                            back3 = {'gigabytes': start.get('gigabytes') + gb / 2}
                            start.update(back3)
                            print('{}'.format(ru_local.YOU_ARE_LATE))
                        else:
                            back4 = {'gigabytes': start.get('gigabytes') + gb}
                            start.update(back4)
                            print('{}'.format(ru_local.YOU_ARE_LATE))
                    elif c == 3:
                        cost3 = {'bitcoins': start.get('bitcoins', []) - 202}
                        start.update(cost3)
                        f = random.randint(1, 6)
                        if f >= 3:
                            bn = {'bitcoins': start.get('bitcoins', []) + 200}
                            start.update(bn)
                            print('{}'.format(ru_local.CATCHED))
                        elif f == 2:
                            print('{}'.format(ru_local.MEXICO))
                        else:
                            print('{}'.format(ru_local.WHAT))
                    elif c > 3 or c < 1:
                        check = False
                        print('{}'.format(ru_local.ERR_NUMB))
                except ValueError:
                    check = False
                    print('{}'.format(ru_local.ERR_NUMB))
        elif b == 'нет':
            print('{}'.format(ru_local.SAY_BYE))
        else:
            check = False
            print('{}'.format(ru_local.YES_OR_NO))


def random_4():
    gb = random.randint(1000, 8000)
    loose = {'gigabytes': start.get('gigabytes') - gb}
    start.update(loose)
    print('{} {} {}'.format('{}'.format(ru_local.LOOSE), gb, '{}'.format(ru_local.GIG)))


def random_5():
    gb = random.randint(500, 1000)
    loose = {'gigabytes': start.get('gigabytes') - gb}
    start.update(loose)
    print('{} {} {}'.format('{}'.format(ru_local.BAD), gb, '{}'.format(ru_local.GIG)))


def random_6():
    take = {'gigabytes': start.get('gigabytes') + 1000}
    start.update(take)
    print('{}'.format(ru_local.SURPRISE))


def random_7():
    bit = random.randrange(5000, 35000, 100)
    print('{} {} {}'.format('{}'.format(ru_local.NEWS), bit, '{}'.format(ru_local.BTC)))
    check = False
    while not check:
        b = input('{}'.format(ru_local.DO)).lower()
        check = True
        if b == '{}'.format(ru_local.YES):
            take = {'bitcoins': start.get('bitcoins', []) - bit, 'shops': start.get('shops', []) + 1}
            start.update(take)
            print('{}'.format(ru_local.CONG))
        elif b == '{}'.format(ru_local.NO):
            print('{}'.format(ru_local.YES_OR_NO))
        else:
            check = False
            print()


def random_8():
    print('{}'.format(ru_local.ONE_SHOP))
    b = {'shops': start.get('shops', []) - 1}
    start.update(b)


def random_9():
    print('{}'.format(ru_local.DEAD))
    bill = {'bitcoins': start.get('bitcoins') + 10000}
    start.update(bill)


def random_10():
    cost = random.randrange(10000, 30000, 100)
    print('{}'.format(ru_local.LAW))
    print('{}'.format(ru_local.COST), cost)
    check = False
    while not check:
        answ = input('{}'.format(ru_local.DO_IT)).lower()
        check = True
        if answ == '{}'.format(ru_local.YES):
            if start.get('bitcoins') >= cost:
                chance = random.randint(1, 6)
                pay = {'bitcoins': start.get('bitcoins') - cost}
                start.update(pay)
                if chance >= 4:
                    print('{}'.format(ru_local.WIN))
                    rand = random.randint(50, 100)
                    rand1 = random.randint(1, 5)
                    updat = {'staff': start.get('staff') - rand, 'shops': start.get('shops') - rand1,
                             'working conditions': start.get('working conditions') - 50}
                    start.update(updat)
                else:
                    print('{}'.format(ru_local.WIN))
            else:
                print('{}'.format(ru_local.NO_BTC))
                check_1 = False
                while not check_1:
                    b = input('{}'.format(ru_local.ALL)).lower()
                    check_1 = True
                    if b == '{}'.format(ru_local.YES):
                        pay1 = {'bitcoins': start.get('bitcoins') - start.get('bitcoins')}
                        start.update(pay1)
                        ch = random.randint(1, 6)
                        if ch >= 4:
                            print('{}'.format(ru_local.NO_WIN))
                            ra = random.randint(50, 100)
                            ra1 = random.randint(1, 5)
                            update1 = {'staff': start.get('staff') - ra, 'shops': start.get('shops') - ra1,
                                       'working conditions': start.get('working conditions') - 50}
                            start.update(update1)
                        else:
                            print('{}'.format(ru_local.WIN))
                    elif b == '{}'.format(ru_local.NO):
                        print('{}'.format(ru_local.NO_WIN))
                        ran = random.randint(50, 100)
                        ran1 = random.randint(1, 5)
                        up = {'staff': start.get('staff') - ran, 'shops': start.get('shops') - ran1,
                              'working conditions': start.get('working conditions') - 50}
                        start.update(up)
                    else:
                        check_1 = False
                        print('{}'.format(ru_local.YES_OR_NO))
        elif answ == '{}'.format(ru_local.NO):
            print('{}'.format(ru_local.NO_WIN))
            ranty = random.randint(50, 100)
            ranty1 = random.randint(1, 5)
            upty = {'staff': start.get('staff') - ranty, 'shops': start.get('shops') - ranty1,
                    'working conditions': start.get('working conditions') - 50}
            start.update(upty)
        else:
            check = False


def random_acts():
    rand = random.randint(1, 10)
    if rand == 1:
        random_1()
    elif rand == 2:
        random_2()
    elif rand == 3:
        random_3()
    elif rand == 4:
        random_4()
    elif rand == 5:
        random_5()
    elif rand == 6:
        random_6()
    elif rand == 7:
        random_7()
    elif rand == 8:
        random_8()
    elif rand == 9:
        random_9()
    elif rand == 10:
        random_10()


def menu():
    print('|{0:^12} | {1:^12} | {2:^12} | {3:^12} | {4:^12} | {5:^12}|'.format(
          '{}'.format(ru_local.BI), '{}'.format(ru_local.ST), '{}'.format(ru_local.SH),
          '{}'.format(ru_local.GIGS), '{}'.format(ru_local.WC),
          '{}'.format(ru_local.QR)))
    print('|{0:^12} | {1:^12} | {2:^12} | {3:^12} | {4:^14} | {5:^12}|'
          .format(start.get('bitcoins'), start.get('staff'), start.get('shops'), start.get('gigabytes'),
                  start.get('working conditions'), start.get('quarter')))


def main():
    menu()
    while True:
        selling()
        menu()
        buying()
        menu()
        investments()
        menu()
        salaries()
        menu()
        chance_of_act()
        random_inv()
        staff()
        gbs()
        loss()
        counter()
        menu()


if __name__ == '__main__':
    main()
