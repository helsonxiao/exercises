#! python2
# coding:utf-8

import random

def loadTxt(filename):
    text = open(filename, 'r')
    contents = text.readline().split(', ')
    text.close()
    return contents

adj = loadTxt('adjectives.txt')
adv = loadTxt('adverbial_phrases.txt')
nouns = loadTxt('nouns.txt')
verbs = loadTxt('verbal_phrases.txt')

print('The '+ random.choice(adj) + ' ' + random.choice(nouns) + ' ' + random.choice(verbs) + ' ' + random.choice(adv) +'.')