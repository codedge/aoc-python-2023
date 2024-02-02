import re
from os import path, getcwd

"""
Advent of Code 2023
Day 1: https://adventofcode.com/2023/day/1
"""


def calibrate_p1() -> int:
    calibration_code = 0

    with open(path.join(getcwd(), 'd1/input.txt')) as f:
        for item in f:
            first_number = re.search("\d{1}", item).group()
            last_number = re.search("(\d{1})(?!.*\d)", item).group()

            tmp_sum = int(first_number + last_number)
            print("f: " + first_number + " - l: " + last_number)

            calibration_code += tmp_sum
            print("code: " + str(calibration_code))

    return calibration_code


def calibrate_p2() -> int:
    calibration_code = 0
    number_word = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        '\d{1}': '10'
    }

    with open(path.join(getcwd(), 'd1/input.txt')) as f:
        for line in f:
            matches = re.findall(r"(?=(" + '|'.join(str(x) for x in number_word.keys()) + r"))", line)
            first_match = matches[0]
            last_match = matches[-1]

            if first_match in number_word.keys():
                first_match = number_word[first_match]
            if last_match in number_word.keys():
                last_match = number_word[last_match]

            tmp_sum = int(first_match + last_match)
            print("f: " + first_match + " - l: " + last_match)

            calibration_code += tmp_sum
            print("code: " + str(calibration_code))

    return calibration_code
