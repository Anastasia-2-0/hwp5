# с человеком
from random import randint as ri

all_sweet = 2021
take_sweet = 0
first_sweets = 0
second_sweets = 0

first_name = input('Введите имя:')
second_name = input('Введите имя:')

def who_is_first():
    print('Началась игра с конфетками!')
    random_number = ri(1,2)
    if random_number == 1:
        print(random_number)
        first_turn()
    else:
        second_turn()

def first_turn():
    global all_sweet
    global first_sweets
    global first_name
    print(f'Ход игрока {first_name}')
    take_sweet = int(input("Сколько конфет вы хотите взять? "))
    while take_sweet > 28 or take_sweet < 0 or take_sweet > all_sweet:
        take_sweet=int(input("Очень много конфет, так много есть нельзя, возьмите меньше: "))
    all_sweet -= take_sweet
    if all_sweet > 0:
        second_turn()
    else: print("Вы победили")

def second_turn():
    global all_sweet
    global first_sweets
    global second_name
    print(f'Ход игрока {second_name}')
    take_sweet = int(input("Сколько конфет вы хотите взять? "))
    while take_sweet > 28 or take_sweet < 0 or take_sweet > all_sweet:
        take_sweet=int(input("Очень много конфет, так много есть нельзя, возьмите меньше: "))
    all_sweet -= take_sweet
    if all_sweet > 0:
        first_turn()
    else: print("Вы победили")

who_is_first()