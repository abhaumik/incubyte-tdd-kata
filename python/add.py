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

    if numbers and numbers.startswith("//"):
        delimiter, input_str = numbers[2:].split("\n", 1)

    number_list = list(map(convertToInt, re.split(delimiter, input_str)))

    return sum(number_list)
