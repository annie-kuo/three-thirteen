# Annie Kuo

import random

# define functions

def draw(hand, top_discard_card):
    """ (list, int) -> str
    
    The function takes a list of the cards in the player's hand as argument,
    and the card at the top of the discard pile.
    The function returns either 'stock' or 'discard' at random,
    unless there are no card at the top of the discard pile, it returns 'stock'.
    
    >>> random.seed(5)
    >>> draw([4, 17, 29, 31], 6) # random_int == 2
    'discard'
    >>> draw([4, 50, 15, 21], None) # random_int == 2
    'stock'
    >>> draw([24, 30, 51], 3) # random_int == 1
    'stock'
    
    """
    # generate a random int
    random_int = random.randint(1,2)
    
    # determine which string to return depending on the random_int and on the top_discard_card
    if random_int == 1 or top_discard_card == None:
        return 'stock'
    else:
        return 'discard'
    
    
    
def discard(hand):
    """ (list) -> int
    
    The function takes a list of the cards in the player’s hand as argument,
    and returns a random card in the hand
    
    >>> random.seed(5)
    >>> discard([4, 50, 15, 21]) # random_int == 2
    15
    >>> discard([12, 34, 52, 34, 43, 23]) # random_int == 5
    23
    >>> discard([37, 38, 39]) # random_int == 1
    38
    
    """
    # generate a random int
    random_int = random.randint(0,len(hand)-1)
    
    # determine which card is discarded
    card_to_discard = hand[random_int]
    return card_to_discard
