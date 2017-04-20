#! python2
# coding:utf-8


class Card():
    def __init__(self, suit_id, rank_id):
        self.suit_id = suit_id
        self.rank_id = rank_id

        if 2 <= self.rank_id <= 10:
            self.rank = str(self.rank_id)
            self.value = self.rank_id
        elif self.rank_id == 1:
            self.rank = 'Ace'
            self.value = 1
        elif self.rank_id == 11:
            self.rank = 'Jack'
            self.value = 10
        elif self.rank_id == 12:
            self.rank = 'Queen'
            self.value = 10
        elif self.rank_id == 13:
            self.rank = 'King'
            self.value = 10
        else:
            self.rank = 'RankError'
            self.value = -1

        if suit_id == 1:
            self.suit = 'Diamonds'  # 方块
        elif suit_id == 2:
            self.suit = 'Hearts'    # 红心
        elif suit_id == 3:
            self.suit = 'Spades'    # 黑桃
        elif suit_id == 4:
            self.suit = 'Clubs'     # 梅花
        else:
            self.suit = 'SuitError'

        self.short_name = self.rank[0] + self.suit[0]
        if self.rank == 10:
            self.short_name = self.rank + self.suit[0]
        self.long_name = self.rank + ' of ' + self.suit