# Annie Kuo

# Cards
# This program contains functions to retrieve the suit and the rank of a card in a deck of 52 cards,
# and to compare the suits and ranks of two cards.

#Define global variables

#Suits
HEARTS= 0
DIAMONDS= 1
CLUBS= 2
SPADES= 3

#Ranks
TWO= 0
THREE= 1
FOUR= 2
FIVE= 3
SIX= 4
SEVEN= 5
EIGHT= 6
NINE= 7
TEN= 8
JACK= 9
QUEEN= 10
KING= 11
ACE= 12

#Define functions
def get_suit(card):
    """ (int) -> int
    This function returns the card's suit as an integer between 0 and 3.
    >>> get_suit(7)
    2
    >>> get_suit(18)
    1
    >>> get_suit(36)
    3
    >>> get_suit(9)
    0
    """
    suit= (card%4)-1
    if suit == -1: # we want {0,1,2,3} to be cyclic, so that 0-1= 3
        suit = SPADES
    return suit
    
def get_rank(card):
    """ (int) -> int
    This function returns the card's rank as an integer between 0 and 12.
    >>> get_rank(4)
    0
    >>> get_rank(7)
    1
    >>> get_rank(41)
    10
    >>> get_rank(48)
    11
    >>> get_rank(39)
    9
    """
    rank= (card-1)//4
    return rank
    
def same_rank(card1, card2):
    """ (int, int) -> bool
    This function returns True if the two cards are both of the same rank, False otherwise.
    >>> same_rank(1,3)
    True
    >>> same_rank(40,41)
    False
    >>> same_rank(37,40)
    True
    """
    # retrieve each card's rank
    card1_rank= get_rank(card1)
    card2_rank= get_rank(card2)
    # compare the ranks
    return card1_rank == card2_rank

def same_suit(card1, card2):
    """ (int, int) -> bool
    This function returns True if the two cards are both of the same suit, False otherwise.
    >>> same_suit(7, 15)
    True
    >>> same_suit(29, 33)
    True
    >>> same_suit(33, 34)
    False
    >>> same_suit(37, 23)
    False
    """
    # retrieve each card's suit
    card1_suit= get_suit(card1)
    card2_suit= get_suit(card2)
    # compare the suits
    return card1_suit == card2_suit
    
def same_color_suit(card1, card2):
    """ (int, int) -> bool
    This function returns True if the two cards are both of the same color of suit, False otherwise.
    >>> same_color_suit(5, 6)
    True
    >>> same_color_suit(34, 39)
    False
    >>> same_color_suit(43, 44)
    True
    >>> same_color_suit(49, 48)
    False
    """
    # retrieve each card's suit
    card1_suit= get_suit(card1)
    card2_suit= get_suit(card2)
    # compare the color of the suits by comparing the suits' integer
    if (card1_suit==DIAMONDS and card2_suit==CLUBS) or (card2_suit==CLUBS and card1_suit==DIAMONDS):
        return False
    else:
        return abs(card1_suit - card2_suit) <= 1