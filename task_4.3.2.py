"""
Реализуйте mapper первой mapreduce задачи для расчета TF-IDF с помощью Hadoop Streaming.

Формат входных данных следующий: каждая строка содержит номер документа и строку из него,
разделенные ":". Ключ выходных данных является составным: он содержит слово документа и его номер, разделенные "#".

Слово в документе - последовательность символов (букв или цифр), не содержащая пробельных символов и знаков пунктуации.

Sample Input:

1:aut Caesar aut nihil
1:aut aut
2:de mortuis aut bene aut nihil

Sample Output:

aut#1	1
Caesar#1	1
aut#1	1
nihil#1	1
aut#1	1
aut#1	1
de#2	1
mortuis#2	1
aut#2	1
bene#2	1
aut#2	1
nihil#2	1

Программирование — Напишите программу. Тестируется через stdin → stdout
"""
import sys
import re

for line in sys.stdin:
    info = line.strip().split(":", maxsplit=1)
    result = re.sub(r'[:;!?,.()[\]{}@#%\-"\t]', ' ', info[1])
    for t in result.split():
        print(str(t) + '#' + info[0] + '\t' + '1')



