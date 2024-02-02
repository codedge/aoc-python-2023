import operator
from os import path, getcwd
from typing import List
from functools import reduce

"""
Advent of Code 2023
Day 2: https://adventofcode.com/2023/day/2
"""

limits = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def get_game_info(item: str):
    game_name, *games_string = item.split(':')
    game_id: int = int(game_name.rsplit(' ', 1)[1])
    games: List[str] = games_string[0].split(';')

    return game_id, games


def game(part: int) -> int:
    if part not in [1, 2]:
        raise Exception("Part must be either 1 or 2.")

    sum_game_ids = 0

    with open(path.join(getcwd(), 'd2/input.txt')) as f:
        for item in f:
            gid, games = get_game_info(item)

            if part == 1:
                res = validate_game_p1(gid, games)
            else:
                res = validate_game_p2(games)

            sum_game_ids += res

    return sum_game_ids


def validate_game_p1(game_id: int, games: List[str]) -> int:
    game_cnt = 0
    combination_valid = True

    for cubes_str in games:
        combinations = cubes_str.split(',')

        for cube in combinations:
            cube = cube.strip()
            amount, *color = cube.split()
            if int(amount) > limits[color[0]]:
                combination_valid = False

    if combination_valid is True:
        game_cnt += game_id

    return game_cnt


def validate_game_p2(games: List[str]) -> int:
    results = {}

    for cubes_str in games:
        combinations = cubes_str.split(',')

        for cube in combinations:
            cube = cube.strip()
            amount, *color = cube.split()
            amount = int(amount)

            # Add new entries, if color does not exist
            if color[0] not in results.keys():
                results[color[0]] = amount

            # If the entry has a lower amount, update with current one
            if color[0] in results.keys() and results[color[0]] < amount:
                results[color[0]] = amount

    return reduce(operator.mul, results.values())
