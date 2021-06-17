class DayErr(Exception):
    pass


class MonthErr(Exception):
    pass


class YearErr(Exception):
    pass


class Data:
    def __init__(self, day, month, year):
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)

    @classmethod
    def date_output(cls, data):
        day, month, year = data.split('-')
        return cls(day, month, year)

    @staticmethod
    def validation(self):
        try:
            month = self.month
            day = self.day
            if day <= 0 or day > 31:
                raise DayErr('Вы ввели неверно информацию о дне. Повторите процедуру')
            elif month > 12 or month < 1:
                raise MonthErr('Вы ввели неверно информацию о месяце. Повторите процедуру')
            elif len(str(self.year)) != 4:
                raise YearErr('Вы ввели неверно информацию о годе. Повторите процедуру')
        except DayErr as err:
            print(err)
        except MonthErr as err:
            print(err)
        except YearErr as err:
            print(err)
        else:
            print('Все данные введены верно!')


data_1 = Data.date_output('10-12-2001')
print(data_1.day)
data_1.validation(data_1)
