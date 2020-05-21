# CS61A Projects
## Project 1: The Game of Hog (hog)
A simulator with different strategies and rules for 2 players in the dice game Hog.
### Rules
In Hog, two players alternate turns trying to be the first to end a turn with at least 100 total points. On each turn, the current player chooses some number of dice to roll, up to 10. That player's score for the turn is the sum of the dice outcomes.

To spice up the game, we will play with some special rules:

- __Pig Out__. If any of the dice outcomes is a 1, the current player's score for the turn is 1.
- __Free Bacon__. A player who chooses to roll zero dice scores points equal to ten minus the minimum of of the ones and tens digit of the opponent's score.
- __Swine Swap__. After points for the turn are added to the current player's score, if the first (leftmost) digit of the current player's score and the last (rightmost) digit of the opponent player's score are equal, then the two scores are swapped.


## Project 2: CS 61A Autocorrected Typing Software (cats)
A program that measures typing speed and features autocorrect
### Features
- Calculate correctness (%) of words in typed paragraph compared to reference paragraph
- Calculate words per minute (wpm) and elapsed time
- Autocorrect attempts to correct the spelling of a word after an user types it


## Project 3: Ants Vs.SomeBees (ants)
A [tower defense](https://en.wikipedia.org/wiki/Tower_defense) game called Ants Vs. SomeBees. As the ant queen, you populate your colony with the bravest ants you can muster. Your ants must protect their queen from the evil bees that invade your territory. Irritate the bees enough by throwing leaves at them, and they will be vanquished. Fail to pester the airborne intruders adequately, and your queen will succumb to the bees' wrath. This game is inspired by PopCap Games' [Plants Vs. Zombies](https://en.wikipedia.org/wiki/Tower_defense)

More details can be found in [ants](https://github.com/nam-m/CS61A-Projects/tree/master/ants) folder
