"""Functions for tracking poker hands and assorted card tasks."""



def get_rounds(number):
    x=number
    y=x+1
    z=y+1
    return [x,y,z]

def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    if number in rounds:
        return True
    else:
        return False


def card_average(hand):
    x=sum(hand)
    y=len(hand)
    return x/y
    
  


def approx_average_is_average(hand):
    x=hand[0]
    y=hand[-1]
    z=x+y
    if z/2==sum(hand)/len(hand) or sum(hand)/len(hand)== hand[1] or sum(hand)/len(hand)==hand[2] :
        return True
    else:
        return False

def average_even_is_average_odd(hand):
    x=hand[::2]
    y=hand[1::2]
    z=sum(x)/len(x)
    a=sum(y)/len(y)
    if z==a:
        return True
    else:
        return False

def maybe_double_last(hand):
    if hand[-1]==11:
        result=hand.pop(-1)
        hand.append(result*2)
        return hand
    else :
        return hand