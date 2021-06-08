import json

firm_dict = {}
av_profit = 0
n_ind = 0

with open('05_07_text.txt', 'r', encoding='utf-8') as text_file:
    for line in text_file:
        firm = line.split()
        n_ind += 1
        print(f'Название фирмы - {firm[0]}\n',
              f'Форма собственности - {firm[1]}\n',
              f'Выручка фирмы: {firm[2]} у.е\n',
              f'Издержки фирмы: {firm[3]} у.е')
        firm_dict[firm[0]] = int(firm[2]) - int(firm[3])
        if int(firm[2]) - int(firm[3]) > 0:
            print(f'Прибыль компании составила {int(firm[2]) - int(firm[3])} у.е')
            av_profit += (int(firm[2]) - int(firm[3]))
        elif int(firm[2]) - int(firm[3]) < 0:
            print(f'Убыток компании составил {abs(int(firm[2]) - int(firm[3]))} у.е')
        else:
            print('Выручка фирмы равна издержкам')
    print(f'Средняя прибыль фирм составила {round(av_profit / n_ind, 1)}')
    av_profit_dict = {'средняя прибыль': f'{round(av_profit / n_ind, 1)}'}
    firm_list = [firm_dict, av_profit_dict]
    print(firm_list) # Чтобы показать как список реализовался

with open("05_07_jfile.json", "w", encoding='utf-8') as write_f:
    json.dump(firm_list, write_f)
