# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

import argparse
import datetime


class DateCheck:
    """
    Класс проверки даты на валидность
    """
    __slots__ = ['ok_status', 'date', 'in_date_str']

    def __init__(self, *args, **kwargs):
        try:
            self.in_date_str = args[0]
        except Exception as err:
            self.in_date_str = kwargs.get('date', None)
        if not self.in_date_str:
            terminal_args = argparse.ArgumentParser()
            terminal_args.add_argument(
                'date',
                help='Дата в формате DD.MM.YYYY на проверку валидности'
            )
            self.in_date_str = terminal_args.parse_args().date
        self.ok_status = False
        try:
            self.date = datetime.datetime.strptime(
                self.in_date_str, "%d.%m.%Y"
            ).date()
            self.ok_status = True
        except Exception as err:
            self.date = None

    def __str__(self):
        if self.ok_status:
            return f'Дата {self.in_date_str} прошла проверку.'
        return f'Дата {self.in_date_str} не прошла проверку.'


app = DateCheck()
print(app)
