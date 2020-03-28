import csv
from utils import Text
from utils import Call

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# NOTE Set: to persist distinct values
# - Methods: add(), update(), discard(), remove(), clear(), pop()
# - discard() - does not throw error even if elem is not present in set.
# - remove() - does not throw error when element does not exists in set.
# - Ref link - https://www.programiz.com/python-programming/set


def find_unique_tele_numbers(texts, calls):
    uniq_tele_nums = set({})     # using set instead of dict
    for call in calls:
        call = Call(call)
        uniq_tele_nums.add(call.incoming)
        uniq_tele_nums.add(call.answering)

    for text in texts:
        text = Text(text)
        uniq_tele_nums.add(text.incoming)
        uniq_tele_nums.add(text.answering)
    return len(uniq_tele_nums)


print("There are {0} different telephone numbers in the records.".format(
    find_unique_tele_numbers(texts, calls)))
