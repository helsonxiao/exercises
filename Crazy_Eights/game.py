#! python2
# coding:utf-8
from cards import Card
import random


def show_card(card_list):
    print('Your cards:')
    for card in card_list:
        print(card.long_name)
    print('...')


def show_weapon(card_list):
    print('Weapon List:')
    for card in card_list:
        print card.short_name,
    print


def append_card(card_list):
    global a_card
    a_card = random.choice(cards)
    card_list.append(a_card)
    cards.remove(a_card)
    cards_test()

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
#         deci = raw_input("Error! Please enter Y/N:")
#         judge(deci)


def new_suit_id():
    while True:
        print('Please choose a new suit:')
        print('0 - Diamonds')
        print('1 - Hearts')
        print('2 - Spades')
        print('3 - Clubs')
        new_one = int(raw_input('Enter your number:'))
        if new_one in range(0,4):
            break
        elif new_one not in range(0, 4):
            print('Out of range!')
    return new_one


def cards_test():
    global score, c_score
    if not cards:   # 卡牌消耗完毕，根绝双方的手牌分别记分，重新发牌
        score += calculate_score(computer)
        c_score += calculate_score(hand)
        print('No more card. Shuffling.')
        print('========================')
        GAME_START()


def calculate_score(card_list):
    s = 0
    for card in card_list:
        s += card.value
    return s


def GAME_START():
    global cards, hand, computer, display
    cards = []  # 生成牌堆，52张牌
    for suit_id in range(1, 5):
        for rank_id in range(1, 14):
            new_card = Card(suit_id, rank_id)
            if rank_id == 8:
                new_card.value = 50
            cards.append(new_card)

    hand = []   # 清空玩家的初始手牌
    for i in range(5):
        append_card(hand)

    computer = []   # 清空电脑的初始手牌
    for i in range(5):
        append_card(computer)

    display = random.choice(cards)  # 抽取展示牌
    cards.remove(display)
    cards_test()
    print('The display card is ' + display.long_name)
    print('...')


# Let's Go!
suits =['Diamonds', 'Hearts', 'Spades', 'Clubs']    # 生成花色列表
score = 0  # 玩家积分
c_score = 0  # 电脑积分
print("Let's go!")
print('...')
GAME_START()
done = False
while not done:
    show_card(hand)
    weapons = []    # 生成玩家的武器列表
    for card in hand:
        if card.suit == display.suit or card.rank == display.rank or card.rank == '8':
            weapons.append(card)

    if not weapons:  # 没有对应武器，增加手牌
        print('Bad luck, no match was found.')
        append_card(hand)
        print('Appended {:s} to you.').format(a_card.long_name)
        print('...')
    elif weapons:   # 拥有武器，选择出牌或者不出牌 todo
        show_weapon(weapons)
        valid_input = False
        weapon_index = 0    # 根据答案粗糙地修改了下获取输入的方法，不然要大改，太麻烦了。
        while not valid_input:
            input_name = raw_input("Which one do you want to use? Enter card's short name: ")
            # py2 中的input只能输入数字
            for card in weapons:
                if input_name == card.short_name:
                    valid_input = True
                    break
                weapon_index += 1
            if not valid_input:
                print('Input is invalid!')
        print('...')
        weapon = weapons[weapon_index]
        hand.remove(weapon) # 出牌后，手牌列表发生变化
        if not hand:    # 玩家手牌消耗完毕，根据电脑手牌记分，然后重新开始
            score += calculate_score(computer)
            GAME_START()
            print('You got one.')
            print("Your score is {0:d}, computer's score is {1:d}.").format(score, c_score)
            print('=====================================')
        if weapon.rank == '8':   # 若出8，玩家可以指定花色让电脑出牌。抹去rank属性。
            suit_id = new_suit_id()
            display.suit = suits[suit_id]
            display.rank = 0
            print('Now, computer should show card matching suit - %s' % display.suit)
            print('...')
        elif weapon.suit == display.suit or weapon.rank == display.rank: # 若出对应牌，重新抽取展示牌。
            display = random.choice(cards)
            print('New display card is %s' % display.long_name)
            print('...')
            cards.remove(display)   # 抽出展示牌后，牌堆列表发生变化
            cards_test()

    c_weapons = []  # 电脑的武器
    for card in computer:
        if card.suit == display.suit or card.rank == display.rank or card.rank == '8':
            c_weapons.append(card)
    if not c_weapons:
        print("Good luck! Computer failed to match card.")
        append_card(computer)
        print('Appended a card to computer.')
        print('...')
    elif c_weapons:  # 电脑随机出牌
        c_choice = random.choice(c_weapons)
        print('Computer shows its %s' % c_choice.short_name)
        print('...')
        computer.remove(c_choice)
        if not computer:    # 电脑手牌消耗完毕，根据玩家手牌记分，然后重新发牌
            c_score += calculate_score(hand)
            GAME_START()
            print('Computer got one.')
            print("Your score is {0:d}, computer's score is {1:d}.").format(score, c_score)
            print('=====================================')
        if c_choice.rank == '8':  # 若电脑出8，随机改变花色。若出对应牌则重新选取展示牌。
            c_suit = random.choice(suits)
            print('Computer chose a new suit - %s' % c_suit)
            print('...')
            display.suit = c_suit
            display.rank = 0
        elif c_choice.suit == display.suit or c_choice.rank == display.rank:  # 若电脑出对应牌，重新抽取展示牌。
            display = random.choice(cards)
            print('New display card is %s' % display.long_name)
            print('...')
            cards.remove(display)   # 抽出展示牌后，牌堆列表发生变化
            cards_test()

    if score >= 60:  # 率先达到60分的人取得胜利，保存分数至文档 todo
        print('Congratulations! You are the winner!')
        print("Your score is {0:d}, computer's score is {1:d}.").format(score, c_score)
        done = True
    elif c_score >= 60:
        print('Sorry, you lose.')
        print("Your score is {0:d}, computer's score is {1:d}.").format(score, c_score)
        done = True