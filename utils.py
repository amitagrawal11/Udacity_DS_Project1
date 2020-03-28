class Text:
    def __init__(self, text):
        incoming, answering, time = text
        self.incoming = incoming
        self.answering = answering
        self.time = time


class Call:
    def __init__(self, call):
        incoming, answering, time, during = call
        self.incoming = incoming
        self.answering = answering
        self.time = time
        self.during = during


def is_space(num):
    if ' ' in num:
        return True
    return False


def is_parantheses(num):
    if '(' in num or ')' in num:
        return True
    return False


def is_enclosed_parantheses(num):
    if '(' in num and ')' in num:
        return True
    return False


def is_mob(num):
    if (num.startswith('7') or num.startswith('8') or num.startswith('9')) and is_space(num) and not is_parantheses(num):
        return True
    return False


def is_fixed_line(num):
    if num.startswith('(0') and is_enclosed_parantheses(num):
        return True
    return False


def is_bangalore_num(num):
    if is_fixed_line(num) and num.startswith('(080)'):
        return True
    return False


def is_telemarketer_num(num):
    if num.startswith('140') and not is_parantheses(num) and not is_space(num):
        return True
    return False


def print_nums(nums):
    for num in nums:
        print(num)
