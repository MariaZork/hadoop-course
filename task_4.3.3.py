"""
Реализуйте reducer первой mapreduce задачи для расчета TF-IDF с помощью Hadoop Streaming.
Ключ входных данных составной: он содержит слово и номер документа через "#".
Ключом в выходных данных является слово, а значение состоит из двух элементов, разделенных табуляцией:
номер документа и tf (сколько раз данное слово встретилось в данном документе).

Sample Input:

aut#1	1
aut#1	1
aut#1	1
aut#1	1
aut#2	1
aut#2	1
bene#2	1
de#2	1
mortuis#2	1
nihil#1	1
nihil#2	1
Caesar#1	1

Sample Output:

aut	1	4
aut	2	2
bene	2	1
de	2	1
mortuis	2	1
nihil	1	1
nihil	2	1
Caesar	1	1

Программирование — Напишите программу. Тестируется через stdin → stdout
"""
import sys
import collections

d, counter = dict(), collections.Counter()
lastkey = ''
for line in sys.stdin:
    word, num_sentence = line.strip().split("\t")[0].split('#')
    if not lastkey:
        lastkey = num_sentence
        counter[word] = counter[word] + 1
        d[num_sentence] = {word: counter[word]}
    elif num_sentence not in d.keys():
        for key in d.keys():
            for subkey in d[key]:
                print(subkey + '\t' + key + '\t' + str(d[key][subkey]))
        counter.clear()
        d.clear()
        lastkey = num_sentence
        counter[word] = counter[word] + 1
        d[num_sentence] = {word: counter[word]}
    else:
        counter[word] = counter[word] + 1
        d[num_sentence][word] = counter[word]

if d is not None:
    for key in d.keys():
        for subkey in d[key]:
            print(subkey + '\t' + key + '\t' + str(d[key][subkey]))



