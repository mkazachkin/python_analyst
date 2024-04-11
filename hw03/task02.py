import re
import pandas


PATTERN = re.compile(r"[^\wА-Яа-яЁё]+")

LARGE_STRING = """
История
Проект iXBT.com берёт начало в 1997 году, когда он начал развиваться, как самостоятельное
направление в холдинге Rambler. По оценкам экспертов стартовый объём инвестиций в проект iXBT
составил около $80-100 тыс. Одним из стратегических партнёров,который вывел iXBT в лидеры
российского рынка интернет рекламы, стало агентство 2sun («Двасолнца»). К 2000 году iXBT
становится одним из лидеров рынка интернет рекламы. В 2002 году между партнёрами произошёл
разрыв, iXBT прекратил сотрудничество с 2sun и начал работать совместно с компанией Mediastars.
Это был один из громких скандалов в российской IT-индустрии, закончившийся судебными исками[1]
[2]

Сайт iXBT.com существует с 7 января 1997 года. Официальной датой открытия сайта является 1
октября 1997 года. За прошедшее время сайт постоянно развивался, появились новые разделы, новые
авторы и новые темы. Несколько раз менялся внешний вид сайта.

Reactor Critical
Reactor Critical (www.reactor.ru) — известное в прошлом российское онлайн-издание, посвящённое
компьютерным платформам[прояснить] и их тестированию. После своего открытия в 1997 году долгое
время оставалось достаточно авторитетным изданием о компьютерных технологиях в России[3].
Просуществовал с 16 января 1997 по 21 июня 2003, затем все права на публикации сайта были
переданы изданию iXBT[4], а сам проект закрыт.

Владельцы и современное состояние
Сайт принадлежит компании «Бёрдз Рисёч энд Паблишинг» (англ. Byrds Research and Publishing, Ltd),
которая имеет свидетельство о регистрации средства массовой информации iXBT.com (Ай-Экс-Би-Ти Дот
Ком) за номером: ЭЛ № ФС77-22565 от 20 декабря 2005. На все материалы, опубликованные на сайте
iXBT.com, распространяются нормы законодательства о СМИ РФ. Авторские статьи (содержащие имя и
фамилию автора), опубликованные на сайте iXBT.com, являются собственностью iXBT.com. Все
опубликованные статьи пишутся либо штатными авторами сайта iXBT.com, либо по заказу сайта, либо
предлагаются для публикации в готовом виде. Авторское право на статьи, опубликованные на сайте
iXBT.com, всегда принадлежит авторам статей. В случае, если статья, опубликованная на iXBT.com,
не подписана, эта статья подготовлена коллективом авторов сайта iXBT.com и является собственностью
сайта.

В 2007 году среднесуточная аудитория в конкретный месяц года достигала 30 тыс. посещений. В мае же
2011 года на сайт в среднем приходило 150 тыс. человек в сутки[5]. По внутренней открытой
статистике проекта на основе Webalizer в январе 2016 зафиксирована средняя дневная посещаемость
534 000 визитов в сутки, среднее количество просмотров страниц составило более 2,9 млн[6].
"""

tmp_str = re.sub(PATTERN, ' ', LARGE_STRING.lower())
words = tmp_str.split()
word_dict = {}

for word in words:
    try:
        word_dict[word] += 1
    except KeyError:
        word_dict[word] = 1

counter_list = list(word_dict.values())
counter_list.sort()
minimum = counter_list[-10:][0]

for key, value in word_dict.items():
    if value >= minimum:
        print(f'Слово "{key}" встречается {value} раз.')

# Альтернативное решение с использованием сторонней библиотеки

from collections import Counter

result = Counter(x for x in re.findall(r"[\wА-Яа-яЁё]+", LARGE_STRING.lower()))
print(result.most_common(10))