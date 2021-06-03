from sys import argv

script_name, hours, wage_hours, award = argv
hours = int(hours)
wage_hours = int(wage_hours)
award = int(award)
overall_pay = (hours * wage_hours) + award
print('Общая выплата составила {} рублей'.format(overall_pay))
