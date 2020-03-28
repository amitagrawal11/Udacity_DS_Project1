import csv
from utils import Text
from utils import Call

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

dic = {}
for call in calls:
    record = Call(call)
    dic[record.incoming] = 1
    dic[record.answering] = 1

print("There are <count> different telephone numbers in the records."
      .replace("<count>", str(len(dic))))
