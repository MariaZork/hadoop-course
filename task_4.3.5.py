"""
Реализуйте reducer второй mapreduce задачи для расчета TF-IDF с помощью Hadoop Streaming.
Входные данные: ключ - слово, значение - тройка: номер документа, tf слова в документе и 1 (разделены ';').

Выходные данные: ключ - пара: слово, номер документа (разделены '#'), значение - пара: tf слова в документе,
n - количество документов с данным словом (разделены табуляцией).

Sample Input:

aut	1;4;1
aut	2;2;1
bene	2;1;1
de	2;1;1
mortuis	2;1;1
nihil	1;1;1
nihil	2;1;1
Caesar	1;1;1

Sample Output:

aut#1	4	2
aut#2	2	2
bene#2	1	1
de#2	1	1
mortuis#2	1	1
nihil#1	1	2
nihil#2	1	2
Caesar#1	1	1

Программирование — Напишите программу. Тестируется через stdin → stdout
"""
import sys
import collections

d = collections.defaultdict(int)
lastword = ''
num_tf = list()

for line in sys.stdin:
    word, triple = line.strip().split("\t")
    num_sentence, tf = triple.strip().split(";")[:-1]
    d[word] += 1
    num_tf.append((num_sentence, tf))

tmp = 0
for k, v in d.items():
    tmp += v
    for j in range(tmp - v, tmp):
        print(k + '#' + num_tf[j][0] + '\t' + num_tf[j][1] + '\t' + str(v))

