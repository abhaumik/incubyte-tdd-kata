import re


def convertToInt(input_str):
    try:
        return int(input_str)
    except:
        return 0


def add(numbers: str = None) -> int:
    delimiter = r'[,\n]'
    input_str = numbers

    if numbers == None:
        return 0

    number_list = list(map(convertToInt, re.split(delimiter, input_str)))

    return sum(number_list)
