"""
Реализуйте reducer в задаче подсчета среднего времени, проведенного пользователем на странице.

Mapper передает в reducer данные в виде key / value, где key - адрес страницы, value - число секунд,
проведенных пользователем на данной странице.

Среднее время на выходе приведите к целому числу.

Sample Input:

www.facebook.com	100
www.google.com	10
www.google.com	5
www.google.com	15
www.stepic.org	60
www.stepic.org	100

Sample Output:

www.facebook.com	100
www.google.com	10
www.stepic.org	80

Программирование — Напишите программу. Тестируется через stdin → stdout
"""
import sys

summa, counter = 0, 0
lastKey = None

for pair in sys.stdin:
    (pagename, time) = pair.strip().split("\t")
    if lastKey and lastKey != pagename:
        print(lastKey + '\t' + str(int(summa/counter)))
        counter = 0
        (lastKey, summa) = (pagename, int(time))
    else:
        (lastKey, summa) = (pagename, summa + int(time))
    counter += 1
if lastKey:
    print(lastKey + '\t' + str(int(summa/counter)))
