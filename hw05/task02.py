# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str,
# ставка int, премия str с указанием процентов вида “10.25%”. В результате получаем словарь с именем в качестве
# ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии

names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10.25%", "5.5%", "15.3%"]

print ({names[i]: salary[i]*float(bonus[i].strip()[:-1])/100 for i in range (len(names))})
