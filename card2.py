# Annie Kuo

from card1 import *

# define additional global variables

SUITS = [HEARTS, DIAMONDS, CLUBS, SPADES]
RANKS = [TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING, ACE]
SUITS_STR = ['HEARTS', 'DIAMONDS','CLUBS','SPADES']
RANKS_STR = ['TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING', 'ACE']

# define functions

def get_card(suit, rank):
    """ (int, int) -> int

    The function takes two integers as arguments (one for the suit between 0 and 3, and the other for a rank between 0 and 12).
    The function returns the integer representation of the card with that suit and rank.
    
    >>> get_card(SPADES, NINE)
    32
    >>> get_card(DIAMONDS, JACK)
    38
    >>> get_card(3, 12)
    52
    >>> get_card(3, 3)
    16
    >>> get_card(CLUBS, 4)
    19

    """
    # iterate between all 52 cards until it finds the one with correct suit and rank
    for card in range(1,53):
        if (get_suit(card) == suit) and (get_rank(card) == rank):
            return card
    
    
    
def card_to_string(card):
    """ (int) -> str

    The function takes an integer as argument for a card between 1 and 52.
    The function returns a string for that card's name in the form RANK of SUIT.
    
    >>> card_to_string(1)
    'TWO of HEARTS'
    >>> card_to_string(15)
    'FIVE of CLUBS'
    >>> card_to_string(42)
    'QUEEN of DIAMONDS'

    """
    # retrieve the card's suit and rank
    suit_int = get_suit(card)
    suit_str = SUITS_STR[suit_int]
    
    rank_int = get_rank(card)
    rank_str= RANKS_STR[rank_int]
    
    # return concatenated name
    name = rank_str + " of " + suit_str
    return name
    
    

def hand_to_string(hand):
    """ (list) -> str

    The function takes a list of cards between 1 and 52 as argument.
    The function returns a string containing the names of all the cards.
    
    >>> hand_to_string([1, 2, 3, 4])
    'TWO of HEARTS, TWO of DIAMONDS, TWO of CLUBS, TWO of SPADES'
    >>> hand_to_string([35])
    'TEN of CLUBS'
    >>> hand_to_string([3, 8, 26, 34, 48])
    'TWO of CLUBS, THREE of SPADES, EIGHT of DIAMONDS, TEN of DIAMONDS, KING of SPADES'
    >>> hand_to_string([9])
    'FOUR of HEARTS'
    
    """
    # create string with the name of the first card
    str_card_names= card_to_string(hand[0])
    
    # for every remaining card in the list, concatenante its name with the string
    for index in range(1, len(hand)):
        card_name = card_to_string(hand[index])
        str_card_names += ", " + card_name
    
    # return the string with all the cards' names
    return str_card_names



def get_deck():
    """ () -> list
    
    The function returns a list of integers containing the 52 cards in a deck of playing cards.
    
    >>> len(get_deck())
    52
    >>> type(get_deck())
    <class 'list'>
    >>> max(get_deck())
    52
    >>> min(get_deck())
    1

    """
    # create a list
    deck = []
    
    # add every card integer into the deck list
    for suit in SUITS:
        for rank in RANKS:
            card = get_card(suit, rank)
            deck.append(card)
            
    # return list
    return deck



def all_same_suit(cards):
    """ (list) -> bool

    The function takes a list of integers between 1 and 52 as argument.
    The function returns True if all cards in the list are of the same suit, and False otherwise.
    
    >>> all_same_suit([5, 53])
    True
    >>> all_same_suit([1, 2, 3, 4])
    False
    >>> all_same_suit([2, 6, 10, 14, 18, 22, 25])
    False
    >>> all_same_suit([1, 1])
    True
    >>> all_same_suit([1])
    True
    
    """
    # check if the suit is the same for all cards in the list
    for i in range(len(cards)-1):
        if not same_suit(cards[i], cards[i+1]):
            return False
    return True


       
def all_same_rank(cards):
    """ (list) -> True

    The function takes a list of integers between 1 and 52 as argument.
    The function returns True if all cards in the list are of the same rank, and False otherwise.

    >>> all_same_rank([5, 53])
    False
    >>> all_same_rank([1, 2, 3, 4])
    True
    >>> all_same_rank([2, 6, 10, 14, 18, 22, 25])
    False
    >>> all_same_rank([1, 1])
    True
    >>> all_same_rank([1])
    True
    
    """
    # check if the suit is the same for all cards in the list
    for i in range(len(cards)-1):
        if not same_rank(cards[i], cards[i+1]):
            return False
    return True
