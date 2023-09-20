def run():
    count = 0
    balance = 0.00
    while True:
        show_menu(balance)
        try:
            change = int(input())
        except ValueError:
            print('Ошибка. Введите число!')
            continue

        if change == 1:
            balance = replenish(balance, input_sum('Сумма должна быть кратной 50 \nКакую сумму хотите внести: '),
                                count)
            count += 1
        if change == 2:
            balance = take_off(balance, input_sum('Сумма должна быть кратной 50 \nКакую сумму хотите снять: '),
                               count)
            count += 1
        if change == 3:
            return


# Показать меню
def show_menu(balance: float):
    balance = round(balance, 2)
    print(f'Баланс: {balance}')
    print('1. Пополнить')
    print('2. Снять')
    print('3. Выйти')


# Ввод суммы и обработка исключения если ввели не числовое значение
def input_sum(msg: str) -> float:
    while True:
        try:
            amount = float(input(msg))
            return amount
        except ValueError:
            print('Ошибка. Введите число!')


# Пополнить баланс
def replenish(balance: float, how_many: float, count: int) -> float:
    if how_many <= 0:
        print('Сумма должна быть больше нуля и кратная 50. Попробуйте снова.')
        return check_limit(balance)
    if how_many % 50 != 0:
        print('Вы ввели некорректную сумму, сумма должна быть кратной 50. \nПопробуйте снова.')
        return check_limit(balance)
    else:
        return check_limit(balance) + (how_many * check_count_rep(count))


# Снять с баланса
def take_off(balance: float, how_many: float, count: int) -> float:
    commission = how_many * 0.015
    min_commission = 30
    max_commission = 600
    if how_many <= 0:
        print('Сумма должна быть больше нуля и кратная 50. Попробуйте снова.')

        return check_limit(balance)
    if balance < 50 or how_many > balance:
        print('На счете недостаточно средств.')
        return check_limit(balance)
    if how_many % 50 != 0:
        print('Вы ввели некорректную сумму, сумма должна быть кратной 50. \nПопробуйте снова.')
        return check_limit(balance)
    else:
        if commission < min_commission:
            return check_limit(balance) - (how_many + (how_many * check_count_take(count))) - min_commission
        elif commission > max_commission:
            return check_limit(balance) - (how_many + (how_many * check_count_take(count))) - max_commission
        else:
            return check_limit(balance) - (how_many + (how_many * check_count_take(count))) - commission


# Проверить баланс на сумму 5млн, если больше, то возвращаем сумму с учетом налога на богатство
def check_limit(balance: float) -> float:
    if balance > 5_000_000:
        return balance * 0.9
    else:
        return balance


# Проверяем счетчик операций пополнения (если 3 и больше, то возвращаем значение для удержании комиссии 3%)
def check_count_rep(count: int) -> int | float:
    if count >= 3:
        return 0.97
    else:
        return 1


# Проверяем счетчик операций списания (если 3 и больше, то возвращаем значение для удержании комиссии 3%)
def check_count_take(count: int) -> int | float:
    if count >= 3:
        return 0.03
    else:
        return 0


run()
