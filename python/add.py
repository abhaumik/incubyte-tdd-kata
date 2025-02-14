import re

delimiter_regex = r'\[[^\]]+?\]'


def convertToInt(input_str):
    try:
        return int(input_str)
    except:
        return 0


def extract_delimiter(match):
    return match.group()[1:-1]


def escape_delimiter(delimiter):
    escaped_characters = ['\\' + charachter for charachter in delimiter]
    return ''.join(escaped_characters)


def add(numbers: str = None) -> int:
    delimiter = r'[,\n]'
    input_str = numbers

    if numbers == None:
        return 0

    if numbers and numbers.startswith("//"):
        delimiter, input_str = numbers[2:].split("\n", 1)

    if isinstance(delimiter, str):
        if re.search(delimiter_regex, delimiter):
            matched_delimiters = re.finditer(delimiter_regex, delimiter)
            delimiter_list = map(extract_delimiter, matched_delimiters)
            escaped_delimiters = map(escape_delimiter, delimiter_list)
            delimiter = f"[({'|'.join(escaped_delimiters)})]"

    number_list = list(map(convertToInt, re.split(delimiter, input_str)))

    for n in number_list:
        if n < 0:
            raise ValueError(f"negative numbers not allowed {n}")

    return sum(current for current in number_list if current < 1000)
