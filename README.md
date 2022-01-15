# three-thirteen
This program allows the user to play Three Thirteen (rummy game variant) with 4 players or more.

## Features
- Allows user to check if a group of cards form a valid group (same rank).
- Allows user to check if a group of cards form a valid sequence (same suit with consecutive ranks).
- Allows user to play a game of Three Thirteen with a combination of human players, automated players, and random players.

## How the Game Works
This game uses 104 playing cards (two decks of cards). In the first round, each player receives three cards. For each remaining rounds, the number of cards dealt increases by one (i.e. in round 2, four cards are dealt each; in round 3, five cards are dealt each; and so on). Undealt cards are placed face-down in a *stock* pile and its first card is put face-up into a *discard* pile.

The goal of the game is to arrange cards in your hand into valid combinations. A combination is considered valid if it is one the following:
- a *group* of three or more cards of the same rank;
- a *sequence* of three or more cards of the same suit with consecutive rank.

Each card can only be part of one combination. Each combination can be extended if it does not disrupt the combination's pattern. 

Cards of a certain rank are considered wildcards and can used in place for any other card. For each round, the number of cards dealt determines the wildcard rank.

Players take turn drawing the first card of the stock pile or the discard pile. The player must then discard a card from their hand. 

A round ends when a player can arrange all of their cards into combinations, after which each player who has yet to play in that round is given one more turn.

The game ends after eleven rounds.

## Determining the Winner
At the end of each round, each hand is attributed a score as such: Any card that cannot be included in a combination is counted as penalty points. An Ace is worth 1 point; Twos through Tens are worth their numeric values; Face cards are worth 10 points.

The scores are accumulated from round to round. Whichever player has the lowest score wins the game.
