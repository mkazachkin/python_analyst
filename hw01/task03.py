from random import randint


class NumGame:
    """
    Класс игры в "Угадай число"
    """
    LOWER_LIMIT = 0
    UPPER_LIMIT = 1_001
    ATTEMPTS_LIMIT = 10

    def __init__(self):
        """
        Подготовка игры в "Угадай число"
        """
        self.num = randint(self.LOWER_LIMIT, self.UPPER_LIMIT)
        self.attempts = self.ATTEMPTS_LIMIT

    def run(self):
        """
        Запуск игры "Угадай число"
        """
        print(
            f'Я загадал число от 0 до 1000. Отгадай его. У тебя {self.ATTEMPTS_LIMIT} попыток.')
        win_flag = False
        while not win_flag and self.attempts > 0:
            correct_input_flag = False
            user_num = 0
            while not correct_input_flag:
                print(f'Попытка № {self.ATTEMPTS_LIMIT - self.attempts + 1}')
                try:
                    user_num = int(input('Введи число\n>>'))
                    correct_input_flag = True
                except ValueError:
                    print('Ошибка ввода. Попробуй еще раз.')
            if self.num > user_num:
                print('Загаданное число больше')
            elif self.num < user_num:
                print('Загаданное число меньше')
            else:
                win_flag = True
            self.attempts -= 1
        if win_flag:
            print(f'Ты победил! Я загадал число {self.num}')
        else:
            print(f'Ты проиграл! Я загадал число {self.num}')


game = NumGame()
game.run()
