"""
Реализуйте mapper из фазы 1 задачи Distinct Values v1.
Mapper принимает на вход строку, содержащую значение и через табуляцию список групп, разделенных запятой.

Sample Input:

1	a,b
2	a,d,e
1	b
3	a,b

Sample Output:

1,a	1
1,b	1
2,a	1
2,d	1
2,e	1
1,b	1
3,a	1
3,b	1

Программирование — Напишите программу. Тестируется через stdin → stdout
"""
import sys

for line in sys.stdin:
    (value, groups) = line.strip().split("\t")
    for category in groups.split(","):
        print(value + ',' + category + '\t' + '1')
