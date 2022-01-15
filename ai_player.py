# Annie Kuo

# IMPORT MODULES
from card import *
from arrangement import *
 
# DEFINITIONS
# Complete group/sequence: 3+ cards
# Partial group/sequence: 2 cards
# Deadwood card: 1 random out of place card 
 
# DEFINE HELPER FUNCTIONS
def list_to_tuple(list_to_convert):
    """ (list) -> tuple
 
    The function converts either a 1D or a 2D list into a tuple.
    
    >>> list_to_tuple([[1, 2], [4, 5, 6], [7, 8]])
    ((1, 2), (4, 5, 6), (7, 8))
    >>> list_to_tuple([[45, 97, 3]])
    ((45, 97, 3),)
    >>> list_to_tuple([["hello", "cat"], ["dog"]])
    (('hello', 'cat'), ('dog',))
    >>> list_to_tuple([])
    ()
    >>> list_to_tuple([1,2,3,4,5])
    (1, 2, 3, 4, 5)
    >>> list_to_tuple([1,3,[4,5],7])
    (1, 3, (4, 5), 7)
    >>> list_to_tuple([3.0, 6.8, 10, [3]])
    (3.0, 6.8, 10, (3,))
    """
    # If 2D, convert each sublist into a tuple
    for i in range(len(list_to_convert)):
        if type(list_to_convert[i]) == list:
            list_to_convert[i] = tuple(list_to_convert[i])
        else:
            continue
 
    # Convert the list into a tuple
    return tuple(list_to_convert)
 
 
 
def test_card(hand, card_to_test, wildcard_rank, test_for_partial):
    """ (list, int, int, bool) -> bool
 
    The function returns True if the hand can form an arrangement
    (and/or a partial arrangement if test_for_partial is True)
    with the card_to_test, returns false otherwise.
    The function returns false if a partial arrangement can be made, but that it won't
    benefit the hand too much point-wise.
    
    >>> test_card([10,11,12,20,24,28,32,45,46,52,1], 47, 8, True)
    True
    >>> test_card([10,11,12,20,24,28,32,45,46,52,1], 2, 9, True)
    False
    >>> test_card([1, 10, 20, 30], 51, 3, True)
    False
    >>> test_card([1, 10, 20, 30], 52, 7, False)
    False
    >>> test_card([1, 10, 20, 30], 9, 7, False)
    True
    >>> test_card([1, 20, 30], 9, 2, False)
    False
    >>> test_card([], 34, 7, True)
    False
    """
    # Get the arrangement for if we were to add the card to the hand
    hypothetical_hand = hand + [card_to_test]
    hyp_arrangement = get_arrangement(list_to_tuple(hypothetical_hand), wildcard_rank)
    
    # Check if the added card is part of an arrangement
    deadwood_cards = hypothetical_hand[:]
    for arrangement in hyp_arrangement:
        for arranged_card in arrangement: 
            if arranged_card == card_to_test:
                return True
            # remove arranged cards to isolate deadwood cards
            deadwood_cards.remove(arranged_card)
    
    # If test_for_partial is True,
    # check if the added card can form a partial arrangement
    # by adding a wildcard into the deadwood cards
    if test_for_partial:
        deadwood_cards += [get_card(HEARTS, wildcard_rank)]
        partial_arrangement = get_arrangement(list_to_tuple(deadwood_cards), wildcard_rank)
        
        # In case there are no arrangement possible
        if (partial_arrangement != ()) or (partial_arrangement != []): 
          return False
 
        # In case the card to test is part of an arrangement
        for arrangement in partial_arrangement:
            for arranged_card in arrangement:
                if arranged_card == card_to_test:
                    return True
    return False
 
 
 
def is_almost_group(list_unarranged_cards):
    """ (list) -> list
 
    The function checks if the deadwood cards in a hand can almost form a group.
    It returns a 2D list of partial groups.
    If there are no cards that are almost a group, it returns an empty list
 
    >>> list_unarranged_cards = [1, 3, 5, 7]
    >>> is_almost_group(list_unarranged_cards)
    [[1, 3], [5, 7]]
    >>> list_unarranged_cards = [3, 13 , 33]
    >>> is_almost_group(list_unarranged_cards)
    []
    >>> list_unarranged_cards = [7, 51, 49, 3]
    >>> is_almost_group(list_unarranged_cards)
    [[51, 49]]
    >>> list_unarranged_cards = []
    >>> is_almost_group(list_unarranged_cards)
    []
    """
    # Create a dictionary for which the keys correspond to ranks
    rank_dictionary = dict.fromkeys(range(13),[])
        
    # Iterate through the elements of the list of deadwood cards
    for i in range(len(list_unarranged_cards)):
        # Add the card to the value with key corresponding to its rank
        card_rank = get_rank(list_unarranged_cards[i])
        rank_dictionary[card_rank] =  rank_dictionary[card_rank] + [list_unarranged_cards[i]]
                            
    # Initialize a list that will contain the almost group card
    cards_almost_group = []
                    
    # Iterate through the dictionary
    for key in rank_dictionary:
        # Check if there is more than one card of a certain rank 
        if len(rank_dictionary[key]) > 1:
            cards_almost_group += [rank_dictionary[key]]
                
    return cards_almost_group
 
 
 
def is_almost_seq(list_unarranged_cards):
    """ (list) -> list
 
    The function checks if the deadwood cards in a hand can almost form a sequence.
    It returns a 2D list of partial sequences.
    If there are no cards that are almost a sequence, it returns an empty list
 
    >>> list_unarranged_cards = [1, 5, 32, 7]
    >>> is_almost_seq(list_unarranged_cards)
    [[1, 5]]
    >>> list_unarranged_cards = [3, 13, 33]
    >>> is_almost_seq(list_unarranged_cards)
    []
    >>> list_unarranged_cards = [7, 52, 11, 48]
    >>> is_almost_seq(list_unarranged_cards)
    [[7, 11], [48, 52]]
    >>> list_unarranged_cards = []
    >>> is_almost_seq(list_unarranged_cards)
    []
    """
    # Create a dictionary for which the keys correspond to suits
    suit_dictionary = dict.fromkeys(range(4),[])
        
    # Iterate through the elements of the list of deadwood cards
    for i in range(len(list_unarranged_cards)):
        # Add the card to the value with key corresponding to its suit
        card_suit = get_suit(list_unarranged_cards[i])
        suit_dictionary[card_suit] =  suit_dictionary[card_suit] + [list_unarranged_cards[i]]
    
    # Sort the values
    for key in suit_dictionary:
        suit_dictionary[key].sort()
        
    # Initialize a list that will contain the almost group card
    cards_almost_seq = []
                    
    # Iterate through the dictionary
    for key in suit_dictionary:
        # Check if there are two cards of consecutive rank 
        if len(suit_dictionary[key]) > 1:
            for i in range(len(suit_dictionary[key])-1):
                same_suit= suit_dictionary[key]
                if same_suit[i] == (same_suit[i+1] - 4):
                    cards_almost_seq.append([same_suit[i], same_suit[i+1]])
                    i += 1
                
    return cards_almost_seq
 
 
 
def num_cards_same_rank(picked_up_discard_cards, rank):
    """ (list, int) -> int
    
    This function takes for input the nested list of the picked cards and the rank of which
    we want to know how often it has already appeared in the discard pile.
    It returns the number of time cards of that rank has appeared. 
 
    >>> discard_cards = [[12, 51, 39],[2, 17, 26],[10, 13, 32],[33, 44, 1]]
    >>> num_cards_same_rank(discard_cards, 10)
    1
    >>> discard_cards = [[12, 51, 16],[2, 17, 29],[10, 13, 32],[10, 44, 1],[29, 48, 24]]
    >>> num_cards_same_rank(discard_cards, 7)
    3
    >>> discard_cards = [[36, 51, 39, 4, 7],[2, 34, 26, 30, 21],[10, 13, 32, 43, 5],[33, 44, 1, 51, 33],[17, 25, 35, 45, 52],[13, 27, 28, 36, 9]]
    >>> num_cards_same_rank(discard_cards, 8)
    6
    >>> discard_cards = [[],[]]
    >>> num_cards_same_rank(discard_cards, 5)
    0
    """
    # Initialize a counter variable
    counter_rank = 0
        
    # Iterate through the picked_up_discard_cards list
    for sublist in picked_up_discard_cards:
        for discard_card in sublist:
            # The card is of the rank inputed 
            if get_rank(discard_card) == rank:
                # Add one to the counter
                counter_rank += 1
                    
    return counter_rank
 
 
 
 
# DEFINE MAIN FUNCTIONS
def draw(hand, top_discard, last_turn, picked_up_discard_cards, player_index, wildcard_rank, num_turns_this_round):
    """
    (list, int, bool, list, int, int, int) -> str
 
    The function decides from where to pick up a card.
    It returns either "stock" or "discard".
    If top_discard is None, it returns "stock".
 
    >>> draw([1,2,3,4,15,19,23], 27, False, [[],[],[]], 1, 5, 4)
    'discard'
    >>> draw([32,36,3,19,2], 15, False, [[],[],[23]], 0, 3, 14)
    'discard'
    >>> draw([1,2,3,4,5,1,2,3,4,5], 52, False, [[],[],[2,22,34,21]], 2, 3, 3)
    'stock'
    >>> draw([34,23,22], 4, False, [[1,2,3],[34,22],[2],[4,32,51,3],[]], 1, 5, 10)
    'discard'
    >>> draw([], 1, True, [[],[],[2]], 0, 4, 39)
    'stock'
    """
    # Checking if discard pile is empty
    if top_discard == None:
        return "stock"
 
    # Checking if top card in discard pile is a wildcard
    elif get_rank(top_discard) == wildcard_rank:
        return "discard"
 
    # Checking if the top card can be added to, or form,
    # an arrangement or a partial arrangement
    elif test_card(hand, top_discard, wildcard_rank, True):
        return "discard"
                
    # On the last turn, check if top card is useless and 
    # has a lower rank than other penalties cards in the hand
    elif last_turn:
        hand_arrangement = get_arrangement(list_to_tuple(hand), wildcard_rank)
        deadwood_cards = hand[:]
 
        # Remove each card in arrangements from deadwood_cards
        for arrangement in hand_arrangement:
            for arranged_card in arrangement:
                deadwood_cards.remove(arranged_card)
 
        # Check if the wildcard has the lowest rank within the deadwood cards
        for card in deadwood_cards:
            if get_rank(card) < get_rank(top_discard):
              return "stock"
            
    # Checking if other players have any partial groups/sequences to
    # determine if we want to draw from the discard pile
    for player in range(len(picked_up_discard_cards)):
        if player == player_index:
            continue
 
        else:
            # Checking if they are about to form an arrangement
            # from the picked up discard cards that we know
            player_picked_up = picked_up_discard_cards[player]
            almost_group = is_almost_group(player_picked_up)
            almost_seq = is_almost_seq(player_picked_up)
            
            if almost_group != []:
                for group in almost_group:
                    if is_valid_group(tuple(group+[top_discard]), wildcard_rank):
                        return "discard"
 
            if almost_seq != []:
                for seq in almost_seq:
                    if is_valid_sequence(tuple(seq+[top_discard]), wildcard_rank):
                        return "discard"
            
    # If all strategies have been inconclusive, draw from the stock pile
    return "stock"
        
 
 
def discard(hand, last_turn, picked_up_discard_cards, player_index, wildcard_rank, num_turns_this_round):
    """
    (list, int, bool, list, int, int, int) -> int
 
    The function decides and returns which card to discard from hand.
 
    >>> discard([5,6,7,9], False, [[5,6],[4],[1,2,3]], 1, 10, 34)
    9
    >>> discard([5,6,7,9,52], True, [[5,6],[7],[1,2,3],[],[34,12,56]], 0, 10, 34)
    52
    >>> discard([5], False, [[],[],[]], 0, 6, 1)
    5
    >>> discard([6,10,14], False, [[],[],[]], 0, 3, 7)
    6
    >>> discard([1,2,3,24,28,32,10,25], True, [[],[],[1,2,3]], 1, 2, 7)
    25
    """
    # Create a deep copy of the player's hand 
    # Remove from this list the cards that we want to keep
    copy_of_hand = hand[:]
 
    # Discard a card that is not in any arrangement nor almost in one
    # Create a variable that stores the arrangements in the player's hand
    cards_in_arrangement = get_arrangement(list_to_tuple(copy_of_hand), wildcard_rank)
 
    # Check if the player has any arrangement in their hand
    if cards_in_arrangement != [] and cards_in_arrangement != ():
        # Iterate through the different sublist of the tuple obtained by calling get_arrangement
        for sublist in cards_in_arrangement:
            # Iterate through each element of the sublists
            for element in sublist:
                # Removing the elements that are contained in cards_in_arrangement 
                # from the copy we made of the player's hand
                copy_of_hand.remove(element)
            
    # On the last turn, return the card with the highest value
    if last_turn and copy_of_hand != []:
        return max(copy_of_hand)
 
    # Check if the cards that aren't already in an arrangement are almost in an arrangement
    # Create a wildcard that will be added to the unarranged cards
    wildcard = get_card(HEARTS, wildcard_rank)
    
    # The deadwood cards can almost create an arrangement
    if test_card(copy_of_hand, wildcard, wildcard_rank, False):
        # Create a variable that contains the possible arrangement obtained 
        # by calling get_arrangement on the deadwood cards
        possible_arrangement = get_arrangement(list_to_tuple(copy_of_hand), wildcard_rank)
        
        # Remove cards that are in partial arrangements from the list of potential cards to discard
        for arrangement in possible_arrangement:
            for card in arrangement:
                copy_of_hand.remove(card)
                
    # If a rank appeared too often
    possible_groups = is_almost_group(copy_of_hand)
    if possible_groups != []:
        for sublist in possible_groups:
            for element in sublist:
                rank1 = get_rank(element)
                if num_cards_same_rank(picked_up_discard_cards, rank1) > 5:
                    copy_of_hand.append(element)
    
    # Keep track of the card in the next player's hand 
    # so don't discard a card needed by the next player
 
    # Empty list 
    picked_up_copy = []
    
    # Deep copy of picked_up_discard_cards
    for sublist in picked_up_discard_cards:
        nested = []
        for card in sublist:
            nested.append(card)
        picked_up_copy.append(nested)
   
    # If there's only two players
    if len(picked_up_discard_cards) < 3:
        
        # Remove the picked up discarded card of ai_player
        # Keep a list of dicarded cards of the next player
        if player_index == 1:
            next_player_cards = picked_up_copy.pop(0)
        else:
            next_player_cards = picked_up_copy.pop(1)
        
        # Copy of the next player's cards
        cards_left = next_player_cards[:]
 
        # Remove the next player's cards that are
        # Picked by the ai_player
        for card in picked_up_discard_cards[player_index]:
            if card in next_player_cards:
                cards_left.remove(card)
 
    # if there's more than two players 
    else:
        cards_left = []
 
        # if the player is the last to play then the next
        # player is at index 0 and remove card picked by
        # the next next player
        if player_index == len(picked_up_discard_cards) - 1:
            for card in picked_up_discard_cards[0]:
                if card not in picked_up_discard_cards[1]:
                    cards_left.append(card)
                    
        # if the player is second last to play then the
        # next next player is at index 0 and remove its
        # cards from the next player's hand
        elif player_index == len(picked_up_discard_cards) - 2:
            for card in picked_up_discard_cards[-1]:
                if card not in picked_up_discard_cards[0]:
                    cards_left.append(card)
                    
        # if the player is first to second to last       
        else:
            for card in picked_up_discard_cards[player_index + 1]:
                if card not in picked_up_discard_cards[player_index + 2]:
                    cards_left.append(card)
            
    # add the possible cards to discard to the next player's hand 
    for card in copy_of_hand:
        cards_left.append(card)
    
    # check if the next player's hand can form an arrangement
    nxt_play_arrgnmt = get_arrangement(list_to_tuple(cards_left), wildcard_rank)
 
    # if the hand can form an arrangement, remove
    # the card in arrangement from possible cards to discard
    if nxt_play_arrgnmt != [] and nxt_play_arrgnmt != ():
        for arrangement in nxt_play_arrgnmt:
            for card in arrangement:
                if card in copy_of_hand:
                    copy_of_hand.remove(card)
 
 
    # Check if the highest value card is not a wildcard
    if copy_of_hand == []:
        return min(hand)
 
    elif get_rank(max(copy_of_hand)) != wildcard_rank:
      # Evaluate the card with the highest rank from the deadwood cards and return it
      return max(copy_of_hand)
 
    else:
      # Remove the wildcard from the deadwood cards
      copy_of_hand.remove(max(copy_of_hand))
      return max(copy_of_hand)