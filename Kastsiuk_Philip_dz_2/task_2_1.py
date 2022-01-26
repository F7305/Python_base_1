num_1 = 15 * 3
num_2 = 15 / 3
num_3 = 15 // 2
num_4 = 15 ** 2

print(type(num_1))

print(type(num_2) == float)

if isinstance(num_3, int):
    print('num_3 - тип int')

if not isinstance(num_4, float):
    print('num_4 - тип не float')
