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

Create a basic implementation of the card game known as War. If you have never played, a [standard deck of 52 cards](https://upload.wikimedia.org/wikipedia/commons/0/02/Piatnikcards.jpg) is distributed evenly between two players, each player plays the card on the top of their deck. Typically, the game is played with ace high (it is worth the most points). The player with the higher card value wins and takes the losing player's card. If there is a tie, each player will place a predetermined amount of cards face down and then play another card face up.

We will bend the rules slightly to simplify our script. We will only track the outcome of the card flip between two players for one round of play. Cards will not be reassigned, and a tie will simply be noted (no other cards flipped).

Handout code is provided in [war.py](war.py).

Complete the `create_deck`, `deal`, and `battle` functions as described in their docstrings so that the included assertions pass. Then, complete the program so that it will simulate a game of our version of War between two players. Here's an example output from the completed program:

```
Player 1 draws Ace of Clubs
Player 2 draws 3 of Diamonds
Player 1 wins!
Player 1 draws 6 of Spades
Player 2 draws Queen of Hearts
Player 2 wins!
Player 1 draws Queen of Clubs
Player 2 draws 3 of Hearts
Player 1 wins!
Player 1 draws Ace of Spades
Player 2 draws Ace of Diamonds
It's a tie!
Player 1 draws 8 of Clubs
Player 2 draws 8 of Spades
It's a tie!
Player 1 draws 3 of Spades
Player 2 draws 2 of Clubs
Player 1 wins!
Player 1 draws 3 of Clubs
Player 2 draws 5 of Hearts
Player 2 wins!
Player 1 draws 4 of Clubs
Player 2 draws Queen of Diamonds
Player 2 wins!
Player 1 draws 5 of Clubs
Player 2 draws 7 of Hearts
Player 2 wins!
Player 1 draws Queen of Spades
Player 2 draws Jack of Spades
Player 1 wins!
Player 1 draws 9 of Clubs
Player 2 draws Jack of Diamonds
Player 2 wins!
Player 1 draws 4 of Diamonds
Player 2 draws 2 of Hearts
Player 1 wins!
Player 1 draws 2 of Diamonds
Player 2 draws 9 of Spades
Player 2 wins!
Player 1 draws 4 of Spades
Player 2 draws King of Hearts
Player 2 wins!
Player 1 draws 2 of Spades
Player 2 draws 9 of Diamonds
Player 2 wins!
Player 1 draws King of Clubs
Player 2 draws 9 of Hearts
Player 1 wins!
Player 1 draws 6 of Clubs
Player 2 draws Jack of Hearts
Player 2 wins!
Player 1 draws 8 of Hearts
Player 2 draws 10 of Clubs
Player 2 wins!
Player 1 draws 8 of Diamonds
Player 2 draws King of Diamonds
Player 2 wins!
Player 1 draws King of Spades
Player 2 draws 6 of Diamonds
Player 1 wins!
Player 1 draws 10 of Hearts
Player 2 draws Ace of Hearts
Player 2 wins!
Player 1 draws 10 of Diamonds
Player 2 draws 5 of Diamonds
Player 1 wins!
Player 1 draws 6 of Hearts
Player 2 draws 7 of Spades
Player 2 wins!
Player 1 draws 7 of Clubs
Player 2 draws 5 of Spades
Player 1 wins!
Player 1 draws Jack of Clubs
Player 2 draws 4 of Hearts
Player 1 wins!
Player 1 draws 10 of Spades
Player 2 draws 7 of Diamonds
Player 1 wins!

Game summary
Player 1    Win: 11 Loss: 13 Tie: 2
Player 2    Win: 13 Loss: 11 Tie: 2
```