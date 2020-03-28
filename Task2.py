import csv
from utils import Text
from utils import Call

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def find_max_time_spent_phone_no(calls):
    phone_dict = {}
    for call in calls:
        call = Call(call)
        # Adding answering numbers to dictionary with call duration
        if call.answering not in phone_dict:
            phone_dict[call.answering] = int(call.during)
        else:
            phone_dict[call.answering] += int(call.during)

        # adding incoming numbers to dictionary with their call duration
        if call.incoming not in phone_dict:
            phone_dict[call.incoming] = int(call.during)
        else:
            phone_dict[call.incoming] += int(call.during)

    # finding out max time spent phone no in records
    phone_no = max(phone_dict, key=lambda k: phone_dict[k])

    # returning phone_no and time spent
    return phone_no, phone_dict[phone_no]


print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(
    *find_max_time_spent_phone_no(calls)))

# Test Sample
# test_calls = [
#     ["95266 42732", "(080)45291968", "02-09-2016 06:56:36", 2329],
#     ["(080)45291968", "95266 42732", "03-09-2016 14:15:24", 201],
#     ["(080)45291968", "90365 06212", "01-09-2016 06:30:36", 9],
#     ["90192 87313", "(080)33251027", "01-09-2016 07:28:01", 110],
#     ["(044)30727085", "92414 22596", "01-09-2016 07:39:09", 725]
# ]

# test(test_calls)      # Test Output: (080)45291968
