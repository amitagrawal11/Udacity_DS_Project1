import csv
from utils import Text
from utils import Call

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def find_max_duration_call(calls):
    all_call = {}          # calls with time spent on call { tel_no: time_spent }
    for call in calls:
        call = Call(call)
        # combining keys to make one key
        # OPTIMIZATION: remove all duplicate entry since both incoming & answering make two distinct keys and values
        # e.g. time spent on incoming::answering is the same as answering::incoming
        tele_key = (call.incoming + ':' + call.answering) + \
            '::' + (call.answering + ':' + call.incoming)
        if tele_key not in all_call:
            all_call[tele_key] = call.during
        else:
            all_call[tele_key] += call.during

    # getting telephone which has spent max time
    tele_no_key = max(all_call, key=lambda k: all_call[k])

    # extracting incoming call number
    tele_no = tele_no_key\
        .split('::')[0]\
        .split(":")[0]

    return tele_no, all_call[tele_no_key]


# TODO: Need to ask which telephone number do I need to display since spent time is between incoming vs answering phone numbers
print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(
    *find_max_duration_call(calls)))
