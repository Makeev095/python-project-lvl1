#!/usr/bin/env python

from brain_games.games import calc
from brain_games import engine_games


def main():
    engine_games.run(calc)


if __name__ == '__main__':
    main()
