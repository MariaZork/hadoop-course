"""
Реализуйте mapper ﻿второй mapreduce задачи для расчета TF-IDF с помощью Hadoop Streaming.
Во входных данных ключом является слово, а значение состоит из номера документа и tf, разделенных табуляцией.
Значение в выходных данных - это тройка: номер документа, tf и единица, разделенные ";".

Sample Input:

aut	1	4
aut	2	2
bene	2	1
de	2	1
mortuis	2	1
nihil	1	1
nihil	2	1
Caesar	1	1

Sample Output:

aut	1;4;1
aut	2;2;1
bene	2;1;1
de	2;1;1
mortuis	2;1;1
nihil	1;1;1
nihil	2;1;1
Caesar	1;1;1

Программирование — Напишите программу. Тестируется через stdin → stdout
"""
import sys

for line in sys.stdin:
    word, num_sentence, tf = line.strip().split("\t")
    print("{}\t{};{};{}".format(word, num_sentence, tf, '1'))