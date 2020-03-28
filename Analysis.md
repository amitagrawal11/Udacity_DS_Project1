# Worst Case Big O Notation - (https://wiki.python.org/moin/TimeComplexity)

## Task 0 - Prints first text and last call

```
print("First record of texts, {0} texts {1} at time {2}".format(*texts[0]))     # O(1)
print("Last record of calls, {0} calls {1} at time {2}, lasting {3} seconds".format(    #(1)
    *calls[-1]))

```

**Complexity** : O(1) + O(1)  => O(1)

## Task 1 - Prints number of distinct telephone numbers in the dataset.

```
def find_unique_tele_numbers(texts, calls):
    uniq_tele_nums = set({})     
    for call in calls:           # O(n) - where n is the number of calls           
        call = Call(call)
        uniq_tele_nums.add(call.incoming)
        uniq_tele_nums.add(call.answering)

    for text in texts:          # O(m) - where m is the number of texts 
        text = Text(text)
        uniq_tele_nums.add(text.incoming)
        uniq_tele_nums.add(text.answering)
    return len(uniq_tele_nums)      # O(1)

```

**Complexity** : O(n) + O(m) + O(1)  => O(n)

## Task 2 - Prints the telephone number that spent the longest time on the phone and the total time in seconds they spend on phone call.

```
def find_max_time_spent_phone_no(calls):
    phone_dict = {}
    for call in calls:                                              # O(n) - where n is the number of calls
        call = Call(call)
        if call.answering not in phone_dict:                        # O(n)
            phone_dict[call.answering] = int(call.during)
        else:
            phone_dict[call.answering] += int(call.during)

        if call.incoming not in phone_dict:                         # O(n)
            phone_dict[call.incoming] = int(call.during)
        else:
            phone_dict[call.incoming] += int(call.during)

    # finding out max time spent phone no in records
    phone_no = max(phone_dict, key=lambda k: phone_dict[k])         # O(k) - where k is the phone number of keys

    # returning phone_no and time spent
    return phone_no, phone_dict[phone_no]

```

**Complexity** : O(n) + O(k)  => O(n)

## Task 3 - Prints the telephone codes called by fixed-line numbers in Bangalore and the percentage of calls from fixed lines in Bangalore that are to fixed lines in Bangalore.

```
def find_area_codes(calls):
    total_calls_made = 0
    area_codes = set({})  
    for call in calls:                              # O(n) - where n is the number of calls      
        call = Call(call)
        if is_bangalore_num(call.incoming):
            total_calls_made += 1
            area_code = ''
            if '(0' in call.answering:              # O(n)
                idx = call.answering.index(")")
                area_code = call.answering[1:idx]
            else:
                area_code = call.answering[:4]
            area_codes.add(area_code)               # O(1) 
    return sorted(area_codes), total_calls_made     # O(n log n) - where n is the number of elements in area_codes


# Solution: Part A
codes, total_calls = find_area_codes(calls)
print("The numbers called by people in Bangalore have codes:")
print_nums(codes)       # O(n)  -- printing each code

```
**Part A: Complexity** : O(n) + O(n) + O(1) + O(n log n) + O(n) => O(n log n)


```
def find_fixed_lines_calls(calls):
    total_fixed_line_calls = 0
    for call in calls:                              # O(n)
        call = Call(call)
        if is_bangalore_num(call.incoming) and is_bangalore_num(call.answering):
            total_fixed_line_calls += 1
    return total_fixed_line_calls

```
**Part B: Complexity** : O(n)

## Task 4 - Prints the list of numbers that could be telemarketers.

```
def find_telemarkers(calls, texts):
    outgoing = set({})
    non_tele = set({})
    for call in calls:      # O(n) where n is no of calls
        call = Call(call)
        outgoing.add(call.incoming)
        non_tele.add(call.answering)
    for text in texts:     # O(m) - where m is the no of texts
        text = Text(text)
        non_tele.add(text.incoming)
        non_tele.add(text.answering)
    possible_tele = list(outgoing - non_tele)       # O(len(set)) -> O(x) - where x is no of elements in set
    possible_tele.sort()                    # O(n log n) - as per documentation 
    return possible_tele

```
**Complexity** : O(n) + O(m) + O(x) + O(n log n) => O(n log n)


