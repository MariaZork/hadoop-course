"""
Напишите reducer, который делает вычитание элементов множества B из множества A.
На вход в reducer приходят пары key / value, где key - элемент множества, value - маркер множества (A или B)

Sample Input:

1	A
2	A
2	B
3	B

Sample Output:

1

"""

import sys

A, B = set(), set()

for line in sys.stdin:
    key = line.strip().split("\t")
    if key[1] == 'A':
        A.add(key[0])
    else:
        B.add(key[0])

print('\n'.join(sorted(A.difference(B))))