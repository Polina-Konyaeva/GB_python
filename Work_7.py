import json

new_st = []
new_dict = {}
profit_average = {}
all_net_profit = 0
kol = 0

with open('file_task_7.txt', 'r', encoding='utf-8') as file_7:
    for i in file_7:
        title, form, receive, damages = i.split()
        net_profit = int(receive) - int(damages) #чистая прибыль
        if net_profit >= 0:
            all_net_profit += net_profit #прибыль фирм (суммирование)
            kol += 1
        new_dict[title] = net_profit
    new_st.append(new_dict)
    if kol != 0:
        profit_average['Average profit of firms'] = round(all_net_profit / kol)
        new_st.append(profit_average)
    else:
        print('Фирмы работают в убыток, поэтому средней прибыли нет.')
    print(new_st)

with open('7_task.json', 'w', encoding='utf-8') as file_7_json:
    json.dump(new_st, file_7_json)

