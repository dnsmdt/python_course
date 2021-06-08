working_dict = {}
below_salary_list = []
salary_value = 0

with open('05_03_text.txt', 'r') as working_file_text:
    for line in working_file_text:
        working_dict[line.split(' - ')[0]] = '{}'.format(line.split(' - ')[1].replace('\n', ''))
    for el in working_dict.items():
        if int(el[1]) < 20000:
            below_salary_list.append(el[0])
    for v_el in working_dict.values():
        salary_value += int(v_el)
    print('Средняя величина зарплаты сотрудников равна {}'.format(salary_value / len(working_dict)))
    print('Данные сотрудники имеют зарплату ниже 20000 у.е:')
    for an_el in below_salary_list:
        print('{}'.format(an_el))
