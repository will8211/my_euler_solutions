#!/usr/bin/env python3

'''
Poker hands
Problem 54

In the card game poker, a hand consists of five cards and are ranked, from 
lowest to highest, in the following way:

High Card:       Highest value card.
One Pair:        Two cards of the same value.
Two Pairs:       Two different pairs.
Three of a Kind: Three cards of the same value.
Straight:        All cards are consecutive values.
Flush:           All cards of the same suit.
Full House:      Three of a kind and a pair.
Four of a Kind:  Four cards of the same value.
Straight Flush:  All cards are consecutive values of same suit.
Royal Flush:     Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest 
value wins; for example, a pair of eights beats a pair of fives (see example 1 
below). But if two ranks tie, for example, both players have a pair of queens, 
then highest cards in each hand are compared (see example 4 below); if the 
highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

   Player 1	                         Player 2                             Winner
1  5H 5C 6S 7S KD  Pair of Fives     2C 3S 8S 8D TD  Pair of Eights       P2

2  5D 8C 9S JS AC  Highest card Ace  2C 5C 7D 8S QH  Highest card Queen   P1

3  2D 9C AS AH AC  Three Aces        3D 6D 7D TD QD  Flush with Diamonds  P2

4  4D 6S 9H QH QC  Pair of Queens    3D 6D 7H QD QS  Pair of Queens       P1
                    Highest card Nine                 Highest card Seven
5  2H 2D 4C 4D 4S  Full House        3C 3D 3S 9S 9D  Full House           P1 
                    with Three Fours                  with Three Threes 

The file, poker.txt, contains one-thousand random hands dealt to two players. 
Each line of the file contains ten cards (separated by a single space): the 
first five are Player 1's cards and the last five are Player 2's cards. You 
can assume that all hands are valid (no invalid characters or repeated cards), 
each player's hand is in no specific order, and in each hand there is a clear 
winner.

How many hands does Player 1 win?
'''

class Card:
    def __init__(self, card_string):
        self.value = card_string[0]
        self.suit = card_string[1]
        self.raw = card_string
        
        if self.value == 'T':
            self.numeric_value = 10
        elif self.value == 'J':
            self.numeric_value = 11
        elif self.value == 'Q':
            self.numeric_value = 12
        elif self.value == 'K':
            self.numeric_value = 13
        elif self.value == 'A':
            self.numeric_value = 14
        else:
            self.numeric_value = int(self.value)

class Hand:
    def __init__(self, cards):
        c = cards
        self.cards = (Card(c[0]), Card(c[1]), Card(c[2]), Card(c[3]), 
                      Card(c[4]))    
        self.values = [x.numeric_value for x in self.cards]
        self.suits = [x.suit for x in self.cards]


def most_common(lst):
    """
    returns a tuple containing the most common numeric value and it's 
    occurence.
    """
    commonest = max(set(lst), key=lst.count)
    return (commonest, lst.count(commonest))

def remove_all(lst, val):
    """
    returns lst with all instances of val removed.
    """
    return [x for x in lst if x != val]

def calc_value(hand):
    """
    Returns a list of values showing strength of hand.
    """
    straight = False
    sm = min(hand.values) #smallest value in hand
    mc = most_common(hand.values) #most common value in hand
    val = [0, 0, 0, 0, 0, 0] #hand, rank, kicker1 rank, kicker2 rank, etc...

    flush = all(s == hand.suits[0] for s in hand.suits)
    
    straight =  (all(x in hand.values for x in [sm+1, sm+2, sm+3, sm+4])
                 or sorted(hand.values) == [2, 3, 4, 5, 14])

    # 9 pts --> Royal Flush; 8 pts --> Straight Flussh
    if flush:
        if sorted(hand.values) == [10, 11, 12, 13, 14]:
            val[0] = 9
            return val, 'Royal Flush'
        if straight:
            val[0] = 8
            val[1] = min(hand.values)
            return val, 'Straight Flush'
        
    # 7 pts --> Four of a Kind
    if mc[1] == 4:
        val[0] = 7
        val[1] = mc[0]
        val[2] = max(remove_all(hand.values, mc[0]))
        return val, 'Four of a Kind'

    # 6 pts --> Full House
    if mc[1] == 3:
        leftover = remove_all(hand.values, mc[0])
        if leftover[0] == leftover[1]:
            val[0] = 6
            val[1] = mc[0]
            val[2] = leftover[0]
            return val, 'Full House'
        
    # 5 pts --> Flush
    if flush:
        val[0] = 5
        val[1] = sorted(hand.values)[4]
        val[2] = sorted(hand.values)[3]
        val[3] = sorted(hand.values)[2]
        val[4] = sorted(hand.values)[1]
        val[5] = sorted(hand.values)[0]
        return val, 'Flush'

    # 4 pts --> Straight
    if straight:
        val[0] = 4
        val[1] = min(hand.values)
        return val, 'Straight'

    # 3 pts --> Three of a Kind
    if mc[1] == 3:
        leftover1 = remove_all(hand.values, mc[0])
        leftover2 = remove_all(hand.values, max(leftover1))
        val[0] = 3
        val[1] = mc[0]
        val[2] = max(leftover1)
        val[3] = max(leftover2)
        return val, 'Three of a Kind'
        
    # 2 pts --> Two Pairs; 1 pt --> One Pair
    if mc[1] == 2:
        leftover1 = remove_all(hand.values, mc[0])
        mc2 = most_common(leftover1)
        if mc2[1] == 2:
            leftover2 = remove_all(leftover1, mc2[0])
            val[0] = 2
            val[1] = mc[0] 
            val[2] = mc2[0] 
            val[3] = leftover2[0]
            return val, 'Two Pairs'

        else:
            val[0] = 1
            val[1] = mc[0] 
            val[2] = sorted(leftover1)[2]
            val[3] = sorted(leftover1)[1]
            val[4] = sorted(leftover1)[0]
            return val, 'One Pair'

    # 0 pts --> High Card
    else:
        val[0] = 0
        val[1] = sorted(hand.values)[4]
        val[2] = sorted(hand.values)[3]
        val[3] = sorted(hand.values)[2]
        val[4] = sorted(hand.values)[1]
        val[5] = sorted(hand.values)[0]
        return val, 'High Card'

rounds = []
with open('p054_poker.txt') as f:
    for l in f:
        line = l.split()
        rounds.append((line[:5], line[5:]))

p1_wins = 0
p2_wins = 0

for i, r in enumerate(rounds):
    p1 = Hand(r[0])
    p2 = Hand(r[1])

    results = calc_value(p1), calc_value(p2)
    print('\nRound', i+1)
    print('P1:', [y.raw for y in [x for x in p1.cards]],
          results[0][1], tuple(results[0][0]))
    print('P2:', [y.raw for y in [x for x in p2.cards]],
          results[1][1], tuple(results[1][0]))

    for sub in range(6):
        if results[0] > results[1]:
            p1_wins += 1
            print('P1 wins!')
            break
        elif results[1] > results[0]:
            p2_wins += 1
            print('P1 wins!')
            break

print('\nPlayer 1:', p1_wins, 'wins')
print('Player 2:', p2_wins, 'wins')
