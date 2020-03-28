import csv
from utils import Text
from utils import Call

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def find_max_time_call(calls):
    max_time = 0
    max_time_call = {}
    for call_record in calls:
        call = Call(call_record)
        if max_time < int(call.during):
            max_time = int(call.during)
            max_time_call = call
    return max_time_call


max_time_call = find_max_time_call(calls)
print("<telephone number> spent the longest time, <total time> seconds, on the phone during September 2016."
      .replace("<telephone number>", max_time_call.incoming)
      .replace("<total time>", max_time_call.during))
