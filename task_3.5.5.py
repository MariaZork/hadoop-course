"""
Напишите программу, которая реализует reducer для задачи WordCount в Hadoop Streaming.

Sample Input:

cogitare	1
est	1
est	1
est	1
militate	1
potentia	1
Scientia	1
Vivere	1
Vivere	1

Sample Output:

cogitare	1
est	3
militate	1
potentia	1
Scientia	1
Vivere	2

Программирование — Напишите программу. Тестируется через stdin → stdout
"""
import sys

(lastKey, summa)=(None, 0)

for line in sys.stdin:
    (key, value) = line.strip().split("\t")
    if lastKey and lastKey != key:
       print(lastKey + '\t' + str(summa))
       (lastKey, summa) = (key, int(value))
    else:
       (lastKey, summa) = (key, summa + int(value))
if lastKey:
    print(lastKey + '\t' + str(summa))
