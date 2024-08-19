import re

numOrDotRegex = re.compile(r'^[0-9.]$')

def isNumOrDotRegex(string: str):
    return bool(numOrDotRegex.search(string))

def isEmpty(string: str):
    return len(string) == 0