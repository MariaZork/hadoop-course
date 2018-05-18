"""
Напишите программу, которая реализует mapper для задачи WordCount в Hadoop Streaming.

Sample Input:

Vivere est cogitare
Vivere militate est
Scientia potentia est

Sample Output:

Vivere	1
est	1
cogitare	1
Vivere	1
militate	1
est	1
Scientia	1
potentia	1
est	1
Программирование — Напишите программу. Тестируется через stdin → stdout

$ cat test.txt | countMap.py | sort | countReduce.py
"""
import sys

for line in sys.stdin:
    for word in line.strip().split(" "):
        if word: print(word + '\t' + '1')