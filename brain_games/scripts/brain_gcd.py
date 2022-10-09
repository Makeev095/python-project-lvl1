#!/usr/bin/env python

from brain_games.games import gcd
from brain_games import engine_games


def main():
    engine_games.run(gcd)


if __name__ == '__main__':
    main()
