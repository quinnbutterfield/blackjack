# Blackjack

### Introduction
This is a simple command line implementation of the game of blackjack.
By default, there are two players including the dealer. This can be changed along with a few other settings in the constants.py file.

Players can bet before the cards are dealt, and interact with the command line interface by typing in numbers for bet amounts or commands.

### Stack
I chose to use Python for this project as its syntax is simple and works well for an object oriented application. 

### Installation
1. Clone the repository
2. Ensure python 3.10 is installed. (This is necessary as I am using a couple of features not available in versions less than 3.10)
```
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.10
```
Verify the installation:
		python3.10 --version
3. To run the program, use the following command in the folder the repo has been cloned in:
		python3.10 main.py

### Playing the Game
To play the game, run main.py with python 3.10, and you'll be greeted by a welcome screen. Players are able to place their bets, then the 6 decks (also alterable via the constants file) are shuffled together and dealt to the players

The following commands can be used:
- hit
- stand
- quit
- hand (show your hand)
- cash (show your available money)

Note that in the betting phase, the dealer wants to lock in the bets quickly so only decimal and integer input will be accepted and other commands will be momentarily disabled.

The current implementation runs only one round of the game, and starting cash is reset every time the program is run. A potential extension of this could involve having players cash deposits written and read from a file.