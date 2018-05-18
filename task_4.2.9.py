"""
Напишите reducer, реализующий объединение двух файлов (Join) по id пользователя.
Первый файл содержит 2 поля через табуляцию: id пользователя и запрос в поисковой системе.
Второй файл содержит id пользователя и URL, на который перешел пользователь в поисковой системе.

Mapper передает данные в reducer в виде key / value, где key - id пользователя, value состоит из 2 частей:
маркер файла-источника (query или url) и запрос или URL.

Каждая строка на выходе reducer должна содержать 3 поля, разделенных табуляцией: id пользователя, запрос, URL.

Sample Input:

user1	query:гугл
user1	url:google.ru
user2	query:стэпик
user2	query:стэпик курсы
user2	url:stepic.org
user2	url:stepic.org/explore/courses
user3	query:вконтакте

Sample Output:

user1	гугл	google.ru
user2	стэпик	stepic.org
user2	стэпик	stepic.org/explore/courses
user2	стэпик курсы	stepic.org
user2	стэпик курсы	stepic.org/explore/courses

Программирование — Напишите программу. Тестируется через stdin → stdout
"""
import sys

query, url = list(), list()

for line in sys.stdin:
    in_line = line.strip().split("\t")
    if in_line[1].startswith('query'):
        query.append((in_line[0], in_line[1].split(':')[1]))
    else:
        url.append((in_line[0], in_line[1].split(':')[1]))

for i in range(len(query)):
    for j in range(len(url)):
        if query[i][0] == url[j][0]:
            print(query[i][0] + '\t' + query[i][1] + '\t' + url[j][1])

