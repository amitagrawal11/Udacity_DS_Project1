import csv
from utils import Text
from utils import Call

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def find_area_codes(call_records):
    total_calls_made = 0
    area_codes = {}
    sorted_codes = []
    for record in call_records:
        call = Call(record)
        if '(080)' in call.answering and '140' not in call.incoming:
            total_calls_made += 1
            area_code = ''
            if '(' in call.incoming:
                idx = call.incoming.index(")")
                area_code = call.incoming[:idx+1]
            else:
                area_code = call.incoming[:4]
            area_codes[area_code] = 1
    for code in area_codes:
        sorted_codes.append(str(code))
    sorted_codes.sort()
    return sorted_codes, total_calls_made


# Soluction: Part A
print("The numbers called by people in Bangalore have codes:")
codes, total_calls = find_area_codes(calls)
for code in codes:
    print(code)


def find_fixed_lines_calls(calls):
    total_fixed_line_calls = 0
    for call in calls:
        call = Call(call)
        if '(080)' in call.incoming and '(080)' in call.answering:
            total_fixed_line_calls += 1
    return total_fixed_line_calls


fixed_line_calls_percentage = round(((
    find_fixed_lines_calls(calls) * 100) / total_calls), 2)

print(str(fixed_line_calls_percentage) +
      " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
