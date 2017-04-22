#! python2
# coding:utf-8

from cards import Card
import random


def show_card(obj):
    print('Now you have these cards:')
    for card in obj:
        print(card.long_name)
    print('...')


def append_card(obj):
    global cards
    card = random.choice(cards)
    obj.append(card)
    cards.remove(card)

def judge(deci):
    if deci == 'Y' or deci == 'y':
        print("Brilliant! Let's move on.")
        print('...')
        hand.remove(card)
        show_card(hand)
    elif deci == 'N' or deci == 'n':
        print("You're a nice person. Good luck!")
        print('...')
        append_card(hand)
        print('Card appended.')
        show_card(hand)
    else:
        deci = raw_input("Error! Please enter Y/N:")
        judge(deci)


def new_suit_id():
    print('Please choose a new suit:')
    print('1 - Diamonds')
    print('2 - Hearts')
    print('3 - Spades')
    print('4 - Clubs')
    new_one = raw_input('Enter your number: ')
    if new_one in range(1,5):
        return new_one
    else:
        print('InputError!')
        new_suit_id()


cards = []
for suit_id in range(1,5):
    for rank_id in range(1, 14):
        new_card = Card(suit_id, rank_id)
        if rank_id == 8:
            new_card.value = 50
        cards.append(new_card)

hand = []
for i in range(5):
    card = random.choice(cards)
    hand.append(card)
    cards.remove(card)
show_card(hand)

computer = []
for i in range(5):
    card = random.choice(cards)
    computer.append(card)
    cards.remove(card)

display = random.choice(cards)
cards.remove(display)
print('The display card is ' + display.long_name)
print('...')

score = 0 # 玩家积分
c_score = 0 # 电脑积分

done = False
while not done:
    weapons = []    # 玩家的武器
    for card in hand:
        if card.suit == display.suit or \
                        card.rank == display.rank or card.rank == 8:
            # print('You have ' + card.short_name)
            weapons.append(card)
            # decision = raw_input('Play or not? Please enter Y/N: ')
            # judge(decision)
        # 这里存在一个逻辑性的 BUG
        # elif card.rank == 8:
        #     show_card(hand)
        #     print('You have magic 8!')
        #     decision = raw_input('Play or not? Please enter Y/N: ')
        #     judge(decision)
        #     suit_id = new_suit_id()
    if not weapons:
        print('Bad luck, no match was found.'
              'Append a card to you.')
        append_card(hand)
    elif weapons:   # 出招吧！ todo
        pass        # 玩家若出8，可以指定新的花色。若出对应牌则重新抽取展示牌。

    if not hand:    # 玩家手牌消耗完毕，根据电脑手牌记分，然后重新发牌 todo
        pass

    c_weapons = []  # 电脑的武器
    for card in computer:
        if card.suit == display.suit or \
                        card.rank == display.rank or card.rank == 8:
            c_weapons.append(card)
    if not c_weapons:
        print("Good luck! Computer also doesn't have match card."
              "Append a card to computer")
        append_card(hand)
    elif c_weapons: # 电脑随机出牌
        c_choice = random.choice(c_weapons)
        print('Computer shows its %s' % c_choice.short_name)
        c_weapons.remove(c_choice)
        if c_choice.value == 8: # 若电脑出8，随机改变花色。若出对应牌则重新选取展示牌。
            c_suit = random.choice(['Diamonds', 'Hearts', 'Spades', 'Clubs'])
            print('Computer chose a new suit - %s' % c_suit)
            # todo

    if not computer:    # 电脑手牌消耗完毕，根据玩家手牌记分，然后重新发牌 todo
        pass

    if not cards:   # 卡牌消耗完毕，根绝双方的手牌分别记分，重新发牌 todo
        pass

    if score >= 200 or c_score >= 200: # 率先达到200分的人取得胜利 todo
        done = True