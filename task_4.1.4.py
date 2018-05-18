"""
Напишите программу, которая реализует In-mapper combining v.1 для задачи WordCount в Hadoop Streaming.

Sample Input:

aut Caesar aut nihil
aut aut
de mortuis aut bene aut nihil

Sample Output:

nihil	1
aut	2
Caesar	1
aut	2
nihil	1
aut	2
de	1
bene	1
mortuis	1

"""
import sys

words = dict()
for line in sys.stdin:
    for word in line.strip().split(" "):
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
    for key, value in words.items():
        print(key + '\t' + str(value))
    words.clear()

