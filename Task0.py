import csv
from utils import Text
from utils import Call

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# Notes: for my understanding
# - Negative index works in python to traverse in reverse
# - Use Format method on string to put dymanic values
print("First record of texts, {0} texts {1} at time {2}".format(*texts[0]))
print("Last record of calls, {0} calls {1} at time {2}, lasting {3} seconds".format(
    *calls[-1]))
