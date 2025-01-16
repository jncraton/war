from random import shuffle

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]


def create_deck():
    """Return a list of 52 unique cards

    Each list item should be a dictionary of the form:

    {
        "rank": "2",
        "suit": "Hearts",
    }
    """


assert len(create_deck()) == 52
assert create_deck()[0]["rank"] in ranks
assert create_deck()[13]["suit"] in suits
assert len(set(map(str, create_deck()))) == 52
assert create_deck() is not create_deck()


def deal(deck):
    """Return a tuple containing a list of cards for each player

    Cards are given to players one at a time from the front of the list

    For example, assuming `deck` is a list of 6 cards, the function should
    return a tuple contain two lists of three cards each. The cards in each
    list should be "drawn" in order from the front of the `deck`.
    """


assert deal([2, 3]) == ([2], [3])
assert deal([2, 3, 4, 5]) == ([2, 4], [3, 5])
assert len(deal(create_deck())[0]) == 26
assert len(deal(create_deck())[1]) == 26


def battle(player_card, opponent_card):
    """
    Return result of a battle between two cards

    If the `player_card` rank is higher, return "win"
    If the `player_card` rank is lower, return "loss"
    If the `player_card` rank is equal, return "tie"
    """


assert battle({"rank": "Queen"}, {"rank": "Queen"}) == "tie"
assert battle({"rank": "King"}, {"rank": "Queen"}) == "win"
assert battle({"rank": "Jack"}, {"rank": "Queen"}) == "loss"
assert battle({"rank": "Ace"}, {"rank": "Queen"}) == "win"
assert battle({"rank": "3"}, {"rank": "2"}) == "win"

# Complete the program so that it will simulate a game of our version of War between two players
# See readme.md for more details
