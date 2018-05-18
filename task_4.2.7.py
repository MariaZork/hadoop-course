"""
Напишите reducer, который реализует симметричную разность множеств A и B
(т.е. оставляет только те элементы, которые есть только в одном из множеств).
На вход в reducer приходят пары key / value, где key - элемент множества, value - маркер множества (A или B)

Sample Input:

1	A
2	A
2	B
3	B

Sample Output:

1
3

"""
import sys

A, B = set(), set()

for line in sys.stdin:
    key = line.strip().split("\t")
    if key[1] == 'A':
        A.add(key[0])
    else:
        B.add(key[0])

print('\n'.join(sorted(A.symmetric_difference(B))))
