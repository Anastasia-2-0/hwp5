# с ботом
from random import randint as ri

all_sweet = 2021
take_sweet = 0
users_sweets = 0
bots_sweets = 0


def who_is_first():
    print('Началась игра с конфетками!')
    random_number = ri(1,2)
    if random_number == 1:
        print(random_number)
        player_turn()
    else:
        bot_turn()

def player_turn():
    global all_sweet
    global users_sweets
    print("Ваш ход")
    take_sweet = int(input("Сколько конфет вы хотите взять? "))
    while take_sweet > 28 or take_sweet < 0 or take_sweet > all_sweet:
        take_sweet=int(input("Очень много конфет, так много есть нельзя, возьмите меньше: "))
    all_sweet -= take_sweet
    if all_sweet > 0:
        bot_turn()
    else: print("Вы победили")

def bot_turn():
    global all_sweet
    global users_sweets
    global bots_sweets
    take_sweet = all_sweet % 28 if all_sweet % 28 !=0 else ri(1,28)
    all_sweet -= take_sweet
    print(f'бот взял - {take_sweet}')
    if all_sweet > 0:
        player_turn()
    else:
        print("Бот выиграил!!")

who_is_first()