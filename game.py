# Annie Kuo

from card1 import *
from card2 import *

# define functions

def calculate_winner(points):
    """ (list) -> list

    The function takes a list of integers as argument,
    and returns a list containing the indices of the list corresponding to the lowest int of the list
    
    >>> calculate_winner([100, 5, 20, 42])
    [1]
    >>> calculate_winner([34, 1, 29, 53, 4])
    [1]
    >>> calculate_winner([5, 5, 75])
    [0, 1]
    >>> calculate_winner([3, 5, 3, 3])
    [0, 2, 3]

    """
    # find the lowest interger of the list
    lowest_int = min(points)
    
    # find indices with the lowest_int as value
    indices = []
    for i in range(len(points)):
        if points[i] == lowest_int:
            indices.append(i)
    
    # return list of indices
    return indices



def calculate_round_points(hand):
    """ (list) -> int

    The function takes a player's hand as argument, and returns the point value of that hand.
    
    >>> calculate_round_points([1, 2, 3, 4])
    8
    >>> calculate_round_points([3, 34, 51, 45])
    23
    >>> calculate_round_points([2, 5, 24, 32])
    21
    >>> calculate_round_points([13, 13])
    10
    >>> calculate_round_points([3, 50, 51, 52, 51])
    6
    
    """
    round_points = 0
    
    # add the number of points alloted by each card to the sum
    for card in hand:
        rank = get_rank(card)
        
        if rank == ACE:
            round_points += 1
        elif rank in [JACK, QUEEN, KING]:
            round_points += 10
        else:
            round_points += (rank+2)
        
    return round_points



def is_valid_group(cards):
    """ (list) -> bool

    The function takes a list of integers as argument,
    and returns True if the cards form a valid group, and False otherwise
    
    >>> is_valid_group([1, 2, 3])
    True
    >>> is_valid_group([3, 7, 28, 42])
    False
    >>> is_valid_group([8, 6])
    False
    >>> is_valid_group([35, 28, 33, 31])
    False
    
    """
    # check if the group is a set of three or more cards
    if len(cards) < 3:
        return False
    
    # check if all cards are of the same rank
    return all_same_rank(cards)



def is_valid_sequence(cards):
    """ (list) -> bool

    The function takes a list of integers as argument,
    and returns True if the cards form a valid sequence, and False otherwise
    
    >>> is_valid_sequence([1, 5, 9])
    True
    >>> is_valid_sequence([3, 17, 24])
    False
    >>> is_valid_sequence([3, 52])
    False
    >>> is_valid_sequence([46, 42, 38, 50])
    True
    
    """
    # check if the group is a set of three or more cards
    if len(cards) < 3:
        return False
    
    # check if all cards are of the same suit
    if not all_same_suit(cards):
        return False
    
    # check if all cards are of consecutive rank
    cards.sort()
    for i in range(len(cards)-1):
        if not (get_rank(cards[i]) == get_rank(cards[i+1]) -1):
            return False
    return True
