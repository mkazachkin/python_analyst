# Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.

class AtmMachine:
    """
    Класс банкомата
    """
    MIN_NOMINATION = 50
    COMMISSION = 0.015
    MIN_COMMISSION = 30
    MAX_COMMISSION = 600
    DIVIDENDS = 0.03
    DIVIDENDS_COUNTER = 3
    TAX = 0.1
    TAX_LIMIT = 5_000_000
    SUCCESS_ADD = 'Деньги внесены.'
    FAILED_ADD = 'Не могу принять деньги. Внесение возможно суммами, ' \
                 f'кратными {MIN_NOMINATION} у. е.'
    SUCCESS_WITHDRAWAL = 'Деньги выданы.'
    FAILED_WITHDRAWAL = 'Не могу выдать деньги. Выведение возможно суммами, ' \
                        f'кратными {MIN_NOMINATION} у. е.'
    NO_CASH = f'Снятие невозможно. Недостаточно средств с учетом комиссии.'

    def __init__(self):
        self.cash = 0
        self.counter = 0

    def cash_info(self):
        """
        Выводит остаток на счете
        """
        print(f'Остаток на карте: {self.cash}')

    def check_nomination(self, cash):
        """
        Проверяет кратность внесения суммы
        :param cash: сумма
        :return: True, если сумма кратно заданной, иначе False
        """
        return cash % self.MIN_NOMINATION == 0

    def check_dividends(self):
        """
        Проверяет условия начисления дивидендов и начисляет их,
        если условие выполняется
        """
        self.counter += 1
        if self.counter % self.DIVIDENDS_COUNTER == 0:
            self.cash += self.cash * self.DIVIDENDS

    def check_wealth(self):
        """
        Изымает налог на богатство
        """
        if self.cash > self.TAX_LIMIT:
            self.cash -= self.cash * self.TAX

    def get_commission(self, cash):
        """
        Рассчитывает сумму комиссионных
        :param cash: сумма операции
        :return: сумма комиссии
        """
        tmp = cash * self.COMMISSION
        if tmp < self.MIN_COMMISSION:
            tmp = self.MIN_COMMISSION
        elif tmp > self.MAX_COMMISSION:
            tmp = self.MAX_COMMISSION
        return tmp

    def add(self):
        """
        Производит внесение средств на банковский счёт
        """
        cash = self.get_int('Введите сумму пополнения >>')
        self.check_wealth()
        if self.check_nomination(cash):
            self.cash += cash
            self.check_dividends()
            print(self.SUCCESS_ADD)
        else:
            print(self.FAILED_ADD)
        self.cash_info()

    def withdraw(self):
        """
        Снимает сумму со счета
        """
        cash = self.get_int('Введите сумму снятия >>')
        self.check_wealth()
        if self.check_nomination(cash):
            operation_sum = self.get_commission(cash) + cash
            if operation_sum > self.cash:
                self.cash -= operation_sum
                self.check_dividends()
                print(self.SUCCESS_WITHDRAWAL)
            else:
                print(self.NO_CASH)
        self.cash_info()

    @classmethod
    def get_int(cls, message):
        """
        Выводит запрос на ввод и возвращает целое число
        :param message: запрос на ввод
        :return: целое число
        """
        while True:
            try:
                return int(input(message))
            except Exception:
                # Стоим до последнего, все исключения игнорируем
                pass

    def run(self):
        operations = '''
Выберите операцию:
1 - внесение
2 - снятие
3 - выход        
        '''
        flag = False
        while not flag:
            operation = self.get_int(operations)
            if operation == 1:
                self.add()
            elif operation == 2:
                self.withdraw()
            elif operation == 3:
                flag = True


app = AtmMachine()
app.run()
