#! python2
# coding:utf-8
from cards import Card
import random

def show_card(obj):
    print('Now you have these cards:')
    i = 0
    for card in obj:
        print(str(i) + ' - ' + card.long_name)
        i += 1
    print('...')

def show_weapon(obj):
    print('Weapon List:')
    i = 0
    for card in obj:
        print(str(i) + ' - ' + card.long_name)
        i += 1
    print('...')

def append_card(obj):
    global cards
    card = random.choice(cards)
    obj.append(card)
    cards.remove(card)

# def judge(deci):
#     if deci == 'Y' or deci == 'y':
#         print("Brilliant! Let's move on.")
#         print('...')
#         hand.remove(card)
#         show_card(hand)
#     elif deci == 'N' or deci == 'n':
#         print("You're a nice person. Good luck!")
#         print('...')
#         append_card(hand)
#         print('Card appended.')
#         show_card(hand)
#     else:
#         deci = input("Error! Please enter Y/N:")
#         judge(deci)

def new_suit_id():
    print('Please choose a new suit:')
    print('0 - Diamonds')
    print('1 - Hearts')
    print('2 - Spades')
    print('3 - Clubs')
    new_one = input('Enter your number: ')
    if new_one in range(0,4):
        return new_one
    else:
        print('InputError!')
        new_suit_id()

# Go!

suits =['Diamonds', 'Hearts', 'Spades', 'Clubs']    # 生成花色列表
cards = []  # 生成牌堆，52张牌
for suit_id in range(1, 5):
    for rank_id in range(1, 14):
        new_card = Card(suit_id, rank_id)
        if rank_id == 8:
            new_card.value = 50
        cards.append(new_card)

hand = []   # 发放玩家的初始手牌
for i in range(5):
    append_card(hand)
show_card(hand) # 展示玩家手牌

computer = []   # 发放电脑的初始手牌
for i in range(5):
    append_card(computer)

display = random.choice(cards)  #　抽取首张展示牌
cards.remove(display)
print('The display card is ' + display.long_name)
print('...')

score = 0 # 玩家积分
c_score = 0 # 电脑积分

done = False
while not done:
    weapons = []    # 生成玩家的武器列表
    for card in hand:
        if card.suit == display.suit or \
                        card.rank == display.rank or card.rank == 8:
            weapons.append(card)

    if not weapons: # 没有对应武器，增加手牌
        print('Bad luck, no match was found.\nAppend a card to you.')
        print('...')
        append_card(hand)

    elif weapons:   # 拥有武器，选择出牌或者不出牌 todo
        show_weapon(weapons)
        weapon_index = input('Which one do you want to use? ')
        while not isinstance(weapon_index, int) or (weapon_index not in range(0, len(weapons))):
            print('InputError!')
            weapon_index = input('Please choose one:')
        weapon = weapons[weapon_index]
        hand.remove(weapon) # 出牌后，手牌列表发生变化
        if weapon.rank == '8':   # 若出8，可改变展示牌花色。同时抹去rank属性。
            suit_id = new_suit_id()
            display.suit = suits[suit_id]
            display.rank = '0'
            print('Now, computer should show card matching suit - %s' % display.suit)
        elif weapon.suit == display.suit or weapon.rank == display.rank: # 若出对应牌，重新抽取展示牌。
            display = random.choice(cards)
            print('New display card is %s' % display.long_name)
            print('...')
            cards.remove(display)   # 抽出展示牌后，牌堆列表发生变化

    if not hand:    # 玩家手牌消耗完毕，根据电脑手牌记分，然后重新发牌 todo
        done = True
        pass

    c_weapons = []  # 电脑的武器
    for card in computer:
        if card.suit == display.suit or \
                        card.rank == display.rank or card.rank == 8:
            c_weapons.append(card)
    if not c_weapons:
        print("Good luck! Computer doesn't have match card.\nAppend a card to computer.")
        append_card(computer)
    elif c_weapons: # 电脑随机出牌, 2种情况
        c_choice = random.choice(c_weapons)
        print('Computer shows its %s' % c_choice.short_name)
        print('...')
        computer.remove(c_choice)
        if c_choice.rank == '8': # 若电脑出8，随机改变花色。若出对应牌则重新选取展示牌。
            c_suit = random.choice(suits)
            print('Computer chose a new suit - %s' % c_suit)
            display.suit = c_suit
            display.rank = '0'
        elif c_choice.suit == display.suit or c_choice.rank == display.rank: # 若出对应牌，重新抽取展示牌。
            display = random.choice(cards)
            print('New display card is %s' % display.long_name)
            print('...')
            cards.remove(display)   # 抽出展示牌后，牌堆列表发生变化

    if not computer:    # 电脑手牌消耗完毕，根据玩家手牌记分，然后重新发牌 todo
        done = True
        pass

    if not cards:   # 卡牌消耗完毕，根绝双方的手牌分别记分，重新发牌 todo
        done = True
        pass

    if score >= 200 or c_score >= 200: # 率先达到200分的人取得胜利 todo
        done = True