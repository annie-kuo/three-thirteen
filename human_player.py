# Annie Kuo

from card2 import *

# define functions

def draw(hand, top_discard_card):
    """ (list, int) -> str
    
    The function takes a list of the cards in the player's hand as argument,
    and the card at the top of the discard pile.
    The function returns either 'stock' or 'discard' depending on the user's input.
    
    >>> location = draw([4, 17, 29, 31], 6)
    Draw location: stock
    >>> print(location)
    'stock'
    >>> draw([4, 50, 15, 21], None)
    Draw location: discard
    'discard'
    >>> draw([24, 30, 51], 3)
    Draw location: stock
    'stock'
    
    """
    # ask for user's input
    action = input("Draw location: ")
    
    # determine which string to return depending on the random_int and on the top_discard_card
    return action
    
    
    
def discard(hand):
    """ (list) -> int
    
    The function takes a list of the cards in the player’s hand as argument,
    prints out each card and its index in the list.
    The function returns the card at the index from the user's input.
    
    >>> card_to_discard = discard([4, 50, 15, 21])
    0       TWO of SPADES
    1       ACE of DIAMONDS
    2       FIVE of CLUBS
    3       SEVEN of HEARTS
    Choice: 2
    >>> print(card_to_discard)
    15
    >>> discard([45, 1, 33, 21, 12])
    0       KING of HEARTS
    1       TWO of HEARTS
    2       TEN of HEARTS
    3       SEVEN of HEARTS
    4       FOUR of SPADES
    Choice: 4
    12
    >>> discard([2, 5, 52, 51, 29, 38, 23, 27])
    0       TWO of DIAMONDS
    1       THREE of HEARTS
    2       ACE of SPADES
    3       ACE of CLUBS
    4       NINE of HEARTS
    5       JACK of DIAMONDS
    6       SEVEN of CLUBS
    7       EIGHT of CLUBS
    Choice: 5
    38

    """
    # print each card and its index in the list
    for index in range(len(hand)):
        card_name = str(card_to_string(hand[index]))
        print(str(index) + "\t\t" + card_name)
    
    # ask for user's input
    choice = int(input("Choice: "))
    
    # determine which card is discarded
    card_to_discard = hand[choice]
    return card_to_discard
