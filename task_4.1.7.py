"""
Реализуйте Combiner в задаче подсчета среднего времени, проведенного пользователем на странице.

Mapper пишет данные в виде key / value, где key - адрес страницы, value - пара чисел, разделенных ";".
Первое - число секунд, проведенных пользователем на данной странице, второе равно 1.

Sample Input:

www.facebook.com	100;1
www.google.com	10;1
www.google.com	5;1
www.google.com	15;1
stepic.org	60;1
stepic.org	100;1

Sample Output:

www.facebook.com	100;1
www.google.com	30;3
stepic.org	160;2

Программирование — Напишите программу. Тестируется через stdin → stdout
"""
import sys

summa, counter, counter_new = 0, 0, 0
lastKey = None

for pair in sys.stdin:
    (pagename, time) = pair.strip().split("\t")
    (time, counter) = time.split(";")
    if lastKey and lastKey != pagename:
        print(lastKey + '\t' + str(summa) + ';' + str(counter_new))
        counter_new = 0
        (lastKey, summa) = (pagename, int(time))
    else:
        (lastKey, summa) = (pagename, summa + int(time))
    counter_new += int(counter)
if lastKey:
    print(lastKey + '\t' + str(summa) + ';' + str(counter_new))
