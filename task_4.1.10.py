"""
Реализуйте reducer из фазы 1 задачи Distinct Values v1.
Reducer принимает на вход данные, созданные mapper из предыдущей шага.

Sample Input:

1,a	1
1,b	1
1,b	1
2,a	1
2,d	1
2,e	1
3,a	1
3,b	1

Sample Output:

1,a
1,b
2,a
2,d
2,e
3,a
3,b

Программирование — Напишите программу. Тестируется через stdin → stdout
"""
import sys

last_value = None

for line in sys.stdin:
    value = line.strip().split("\t")[0]
    if value != last_value:
        print(value)
    last_value = value

