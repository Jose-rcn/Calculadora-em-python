import re

NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')
def is_num_or_dot(string:str):
    return bool(NUM_OR_DOT_REGEX.search(string))
def is_empty(string:str):
    return len(string) == 0

def is_valid_number(string:str):
    try:
        float(string)
        return True
    except ValueError:
        return False