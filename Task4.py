import csv
from utils import Text
from utils import Call

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def find_telemarkers(calls):
    callers = {}
    for call in calls:
        call = Call(call)
        if call.incoming.startswith('140'):
            callers[call.incoming] = 1
    telemarketers = {}
    for marketer in callers:
        for text in texts:
            text = Text(text)
            if text.incoming != marketer or text.answering != marketer:
                telemarketers[marketer] = 1
    telemarketers = [k for k in telemarketers]
    telemarketers.sort()

    print("These numbers could be telemarketers: ")
    for marketer in telemarketers:
        print(marketer)
    return


# Print telemarkers
find_telemarkers(calls)
