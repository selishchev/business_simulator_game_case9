import random

start = {'bitcoins': 10000, 'staff': 100, 'shops': 5, 'gigabytes': 10000, 'working conditions': 95, 'quarter': 0}


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

def random_1():
    situation = 'К вам с проверкой пришли из МВД,  и непрозрачно намекают на взятку. Сколько биткоинов им дать?'
    print(situation)
    money = int(input())
    _max3 = start.get('bitcoins', [])
    update6 = {'bitcoins': start.get('bitcoins', []) - sal}
    update7 = {'bitcoins': 0}
    minimum = start.get('bitcoins', []) * 0.1
    if money < _max3:
        start.update(update6)
        if money < int(minimum):
            close = start.get('shops', []) * 0.25 + 1
            update = {'shops': start.get('shops', []) - int(close)}
            start.update(update)
        else:
            update1 = {'bitcoins': start.get('bitcoins', []) - money}
            start.update(update1)
    else:
        print('Вы не можете столько инвестировать, максимум:', _max3)
        start.update(update7)

def random_2():
    gb = random.randint(100,500)
    low_cond = random.randint(5,10)
    print('{}{}{}'.format('У вас на складе скопилось', gb, 'неиспользованных гигабайт. Раздать рабочим?(напишите да или нет'))
    answer = input()
    if answer == 'да':
        cond = {'working conditions': start.get('working conditions', []) + low_cond}
        print('Сотрудники вам благодарны!')
        start.update(cond)
    else:
        new_gb = {'gigabytes': start.get('gigabytes') + gb}
        start.update(new_gb)
        cond1 = {'working conditions': start.get('working conditions', []) - low_cond}
        print('Сотрудники узнали, что вы жмот!')
        start.update(cond1)

def random_3():
    gb = random.randint(700,2000)
    print(print('{} {} {}'.format('О нет! Склад с вашими флешками ограбили! Вы потеряли', gb, 'гигабайт!')))
    b = input('Полиция не очень охотно расследует дело. Вы можете нанять частого детектива (да/нет)')
    stolen = {'gigabytes': start.get('gigabytes') - gb}
    start.update(stolen)
    if b == 'да':
        print('Вам предлагается выбор из 3ёх детективов.')
        print('1. Борис Грачевский. Профессионал своего дела, выгнали из участка из-за излишней профессиональности. '
              'Гроза преступного мира, известный как "Бетмен за лупой". Цена за услуги 4000 бетховенов.')
        print('2. Леонид Перевалов. Бывший морпех, агрессивный, не всегда устойчив психикой, но если дело его '
              'заинтересует можете быть уверенны в его выполнении. Имеет судимость по статье о продаже наркотиков.'
              'Сам Леонид отрицает решение суда о признании его виновным. Цена за услуги 2000 бетховенов.')
        print('3. Никита Скоробей. Студент факультета естественных наук, оставивший предложение на YouDo. Участник шоу'
              '"Битва экстрасенсов". В университете Никиту считают странным. В детстве увлекался дедукцией и вполне '
              'успешно расследовал преступления по заказу местных пивнушек. Цена за услуги 200 бетховенов и '
              'полторы бутылочки пива.')
        c = int(input('Напишите номер выбранного детектива:'))
        if c == 1:
            cost1 = {'bitcoins': start.get('bitcoins', []) - 4000}
            start.update(cost1)
            d = random.randint(1,6)
            if d == 6:
                print('К сожалению Борис Грачевский посадил в тюрьму слишком серьёзных людей. На него было совершено '
                      'покушение и он скончался в больнице. Ваше дело он не закончил.')
            else:
                back = {'gigabytes': start.get('gigabytes') + gb}
                start.update(back)
                print('Борис Грачевский за 9 минут раскрыл ваше дело и вышел на мафиозного авторитета. Все ваши '
                      'гигабайты вернулись')
        elif c == 2:
            cost2 = {'bitcoins': start.get('bitcoins', []) - 2000}
            start.update(cost2)
            e = random.randint(1,6)
            if e >= 5:
                back2 = {'gigabytes': start.get('gigabytes') + 40}
                start.update(back2)
                print('Леонид оказался ярым ненавистником интернета, но за дело взялся. Однако пока он боролся'
                      'со своим нежеланием работать на благо мировой паутины, злоумышленники успели сбыть весь товар и '
                      'на их базе было найдено только 4 флешки.')
            elif e == 4:
                back3 = {'gigabytes': start.get('gigabytes') + gb/2}
                start.update(back3)
                print('Дело раскрыли слишком поздно и половину ваших флешек успели сбыть.')
            else:
                back4 = {'gigabytes': start.get('gigabytes') + gb}
                start.update(back4)
                print('Леонид расскрыл дело. Преступниками оказалась конкурирующая компания.')
        else:
            cost3 = {'bitcoins': start.get('bitcoins', []) - 202}
            start.update(cost3)
            f = random.randint(1,6)
            if f >= 3:
                bn = {'bitcoins': start.get('bitcoins', []) + 200}
                start.update(bn)
                print('Как ни странно Никита вышел на преступную организацию, но к сожалению они взяли его в плен и '
                      'жестоко пытали. После того как его отпустили, Никита отказывался говорить под страхом снова там '
                      'оказаться. Он вернул вам деньги, но не за пиво.')
            elif f == 2:
                print('Никита оказывается главой преступной организации, которая обокрала вас. Он пропал навсегда. По '
                      'слухам уехал в Мексику')
            else:
                print('ЧТО? Никита Скоробей справился с заданием. Его детективный ум прославился на всю страну и его '
                      'наняло на работу агенство Бориса Грачевского')
    else:
        print('Попрощайтесь с флешками!')

def random_4():
    gb = random.randint(1000, 8000)
    loose = {'gigabytes': start.get('gigabytes') + gb}
    start.update(loose)
    print('{}{}{}'.format('Ваша система подверглась заражению! Вы потеряли', gb, 'гигабайт!'))

def menu():
    print('|{0:^12} | {1:^12} | {2:^12} | {3:^12} | {4:^12} | {5:^12}|'.format('Бетховены', 'Сотрудники', 'Магазины',
                                                                              'Гигабайты','Условия работы', 'Квартал'))
    print('|{0:^12} | {1:^12} | {2:^12} | {3:^12} | {4:^12} | {5:^12}|'
          .format(start.get('bitcoins'), start.get('staff'), start.get('shops'), start.get('gigabytes'),
                  start.get('working conditions'), start.get('quarter')))


menu()
selling()

menu()
buying()

menu()
investments()

menu()
salaries()

menu()
