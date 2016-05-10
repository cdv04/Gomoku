# Gomoku

Follow the progress on [Trello](https://trello.com/b/e5nu9jE7)!

## The project's objectives

The project is an implementation of the game Gomoku Ninuki with artificial intelligence (AI) capable of winning.

It is divided into 3 part:

- The referee, comprising all the rules. He will be able to determine if a shot is valid, what are the consequences, declare victory ... In other words, it is the engine of the game.
- The GUI, should allow a human to play, but also to observe the various statistics of the game.
- Artificial intelligence, must be able to implement a winning strategy. It must be relevant and timely.

The structure allows the easy and quick change of each of these components.

In addition, there are two game modes:

- Player VS Player: game mode allows a human to play against another human. You will need to provide a customized set of aid for each player offering a coup considered interesting.
- Player VS CPU: The most interesting game mode, in which the human player plays against artificial intelligence.

## Install script

Use:

```bash
./install.sh
```

to run the script.

```bash
[I]nstall dependencies/[S]etup/[E]xit?
```

- `Setup` will perform the configuration of virtualenv and put you in the good environment.
- `Install dependencies` Will install all dependencies for `python3` `pip3` and `pygames`
- `Exit` obviously exit the script.

## Run the game

Use:

```bash
./gomoku
```
