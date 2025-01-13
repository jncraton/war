War (card game)
===============

A Python lab to implement a simplified version of [War](https://en.wikipedia.org/wiki/War_(card_game)).

![cards](https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Wojna_gra_karciana.jpg/800px-Wojna_gra_karciana.jpg)

Learning Outcomes
-----------------

After completing this lab, students will be able to:

- Use assert() to confirm program correctness
- Create working functions
- Use lists and dictionaries to store data

Task
----

Create a basic implementation of the card game known as War. If you have never played, a standard deck of 52 cards is distributed evenly between two players, each player plays the card on the top of their deck. Typically, the game is played with ace high (it is worth the most points). The player with the higher card value wins and takes the losing player's card. If there is a tie, each player will place a predetermined amount of cards face down and then play another card face up.

We will bend the rules slightly to simplify our script. We will only track the outcome of the card flip between two players for one round of play. Cards will not be reassigned, and a tie will simply be noted (no other cards flipped).

Handout code is provided in [war.py](war.py).
