import csv
from utils import Text
from utils import Call

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# destruction in python - similarly in javascript
first_text = Text(texts[0])
print("First record of texts, <incoming_number> texts <answering_number> at time <time>"
      .replace("<incoming_number>", first_text.incoming)
      .replace("<answering_number>", first_text.answering)
      .replace("<time>", first_text.time))

last_call = Call(calls[len(calls)-1])
print("Last record of calls, <incoming_number> calls <answering_number> at time <time>, lasting <during> seconds"
      .replace("<incoming_number>", last_call.incoming)
      .replace("<answering_number>", last_call.answering)
      .replace("<time>", last_call.time)
      .replace("<during>", last_call.during))
