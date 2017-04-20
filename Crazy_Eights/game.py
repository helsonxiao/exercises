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
print('The display card is ' + display.long_name)
print('...')

for card in hand:
    if card.suit == display.suit or card.rank == display.rank:
        show_card(hand)
        print('You have ' + card.short_name)
        decision = raw_input('Play or not? Please enter Y/N: ')
        judge(decision)
    elif card.rank == 8:
        show_card(hand)
        print('You have a magic 8!')
        decision = raw_input('Play or not? Please enter Y/N: ')
        judge(decision)
        suit_id = new_suit_id()
    else:
        print('Bad luck, no match. Card appended.')
        append_card(hand)

