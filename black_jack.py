"""Functions to help play and score a game of blackjack."""


def value_of_card(card):
    if card=="J" or card=="Q" or card=="K":
        return 10
    elif card=="A":
        return 1
    elif card in ("2", "3", "4", "5", "6", "7", "8", "9", "10"):
        return int(card)
   
    
    


def higher_card(card_one, card_two):
    x=value_of_card(card_one)
    y=value_of_card(card_two)
    if x>y:
        return card_one
    elif x<y:
        return card_two
    else:
        return card_one,card_two
    


def value_of_ace(card_one, card_two):
    x=value_of_card(card_one)
    y=value_of_card(card_two)
    z=x+y
    if z+11>21:
        return 1
    elif card_one=="A" or card_two=="A":
        return 1
    else:
        return 11





def is_blackjack(card_one, card_two):
    if card_one in ("A") and card_two in ("10","J","Q","K"):
        return True
    elif card_one in ("10","J","Q","K")and card_two in ("A"):
        return True
    else:
        return False
    


def can_split_pairs(card_one, card_two):
    x=value_of_card(card_one)
    y=value_of_card(card_two)
    if int(x)==int(y):
        return True
    else: 
        return False

def can_double_down(card_one, card_two):
    x=value_of_card(card_one)
    y=value_of_card(card_two)
    z=int(x)+int(y)
    if 9<=z<=11:
        return True
    else:
        return False
  