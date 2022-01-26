# Task_5_a
from random import uniform


def transfer_list_in_str(list_in: list) -> str:

    str_out = ''
    for i in my_list:
        num = str(i)[0:2]
        coin = str(i)[3:5]
        if 0 < int(coin) < 10 and int(coin) // 10 == 0:
            coin = '{}0'.format(coin)[0:2]
            # print(new_coin)
        str_out += f'{num} руб {coin} коп, '
    return str_out[:-2]


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)


# Task_5_b
print('\n\n')

def sort_prices(list_in: list) -> list:
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
    my_list_2.sort()
    return my_list_2

my_list_2 = [round(uniform(10, 100), 2) for _ in range(1, 16)]
print(f'Исходный список: {my_list_2}')
# print(my_list_2)
result_2 = sort_prices(my_list)
print(id(result_2[0]))
print(id(my_list_2[0]))
# зафиксируйте здесь доказательство, что результат result_2 остался тем же объектом
print(result_2)

# Task_5_c
print('\n\n')


def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""
    list_out = []
    for i in my_list_2:
        list_out.append(i)
    list_out.reverse()
    # пишите реализацию здесь
    return list_out


result_3 = sort_price_adv(my_list)
print(result_3)


# Task_5_d
print('\n\n')

def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    list_out = []
    my_list_4.sort()
    list_out.extend(my_list_4[-5:])
    return list_out

my_list_4 = [56.79, 19.16, 58.41, 81.29, 83.77, 33.28, 82.06, 34.04, 94.17, 22.63, 25.06, 64.51, 18.31, 73.32, 27.19]

result_4 = check_five_max_elements(my_list)
print(result_4)