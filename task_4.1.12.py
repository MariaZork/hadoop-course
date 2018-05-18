"""
Реализуйте reducer из задачи Distinct Values v2.
Reducer принимает на вход строки, каждая из которых состоит из разделенных табуляцией значения и названия группы.

Sample Input:

1	a
1	b
1	b
2	a
2	d
2	e
3	a
3	b

Sample Output:

a	3
d	1
b	2
e	1
"""
import sys
import collections

tmp_list = []
counter = collections.Counter()
previous_number = ''

for line in sys.stdin:
    (number, category) = line.strip().split("\t")

    if not previous_number:
        previous_number = number
        tmp_list.append(category)
        counter[category] += 1
    elif number == previous_number:
        if category not in tmp_list:
            tmp_list.append(category)
            counter[category] += 1
    else:
        previous_number = number
        tmp_list = [category]
        counter[category] += 1

for key, value in counter.items():
    print(key + '\t' + str(value))

