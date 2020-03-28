import csv
from utils import Text
from utils import Call
from utils import print_nums

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def find_telemarkers(calls, texts):
    outgoing = set({})
    non_tele = set({})
    for call in calls:
        call = Call(call)
        outgoing.add(call.incoming)
        non_tele.add(call.answering)
    for text in texts:
        text = Text(text)
        non_tele.add(text.incoming)
        non_tele.add(text.answering)
    possible_tele = list(outgoing - non_tele)
    possible_tele.sort()
    return possible_tele


# Print telemarkers
print_nums(find_telemarkers(calls, texts))
