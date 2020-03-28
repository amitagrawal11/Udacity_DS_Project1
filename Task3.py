import csv
from utils import Text
from utils import Call
from utils import is_mob
from utils import is_bangalore_num
from utils import print_nums

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def find_area_codes(calls):
    total_calls_made = 0
    area_codes = set({})  # e.g. { area_code1, area_code2 }
    for call in calls:
        call = Call(call)
        if is_bangalore_num(call.incoming) or is_mob(call.incoming):
            total_calls_made += 1
            area_code = ''
            if '(0' in call.incoming:
                idx = call.incoming.index(")")
                area_code = call.incoming[1:idx]
            else:
                area_code = call.incoming[:4]
            area_codes.add(area_code)
    return sorted(area_codes), total_calls_made


# Solution: Part A
codes, total_calls = find_area_codes(calls)
print("The numbers called by people in Bangalore have codes:")
print_nums(codes)


def find_fixed_lines_calls(calls):
    total_fixed_line_calls = 0
    for call in calls:
        call = Call(call)
        if is_bangalore_num(call.incoming) and is_bangalore_num(call.answering):
            total_fixed_line_calls += 1
    return total_fixed_line_calls


fixed_line_calls_percentage = round(((
    find_fixed_lines_calls(calls) * 100) / total_calls), 2)

print(str(fixed_line_calls_percentage) +
      " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
