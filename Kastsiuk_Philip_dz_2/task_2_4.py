def convert_name_extract(list_in: list) -> list:

    list_out = []
    for i in range(len(my_list)):
        name_num = my_list[i]
        name_list = name_num.split()
        name_latter = name_list[-1]
        name_cap = name_latter.capitalize()
        str_in_list = [f'Привет, {name_cap}!']
        list_out.extend(str_in_list)
    return list_out


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)
