date = input("Введите дату: Cегодня ")
print("Cегодня",date)
tasks = input("Введите задачу: Сделать все дела ")
print("Cегодня Сделать все дела ",tasks)


#Задание 1
# Напишите программу, которая последовательно запрашивает у пользователя Дату и Описание задачи, а затем выводит их через пробел.

# Введите дату: Сегодня
# Введите задачу: Сделать все дела
# Сегодня Сделать все дела

date = input("Введите дату: Cегодня ")
tasks = input("Введите задачу: Выучить Python ")
date2 = input("Введите дату: Завтра ")
tasks2 = input("Введите задачу: Разработать TODO-приложение ")
date3 = input("Введите дату: Послезавтра ")
tasks3 = input("Введите задачу: Разработать Telegram-бота ")
print(date, tasks("Выучить Python"))
print(date2, tasks2("Разработать TODO-приложение"))
print(date3, tasks3("Разработать Telegram-бота"))



# Задание 2
# Модифицируйте программу из задания 1 таким образом, чтобы запрос даты и задачи выполнялся трижды и после этого результаты выводились на экран построчно в формате: на одной строчке дата и задача через пробел.

# Введите дату: Сегодня
# Введите задачу: Выучить Python
# Введите дату: Завтра
# Введите задачу: Разработать TODO-приложение
# Введите дату: Послезавтра
# Введите задачу: Разработать Telegram-бота
# Сегодня Выучить Python
# Завтра Разработать TODO-приложение
# Послезавтра Разработать Telegram-бота

tasks_dict = {}

date = input("Введите дату: Сегодня ")
tasks = input("Введите задачу: Выучить Python ")
tasks_dict[date] = tasks

date2 = input("Введите дату: Завтра ")
tasks2 = input("Введите задачу: Разработать TODO-приложение ")
tasks_dict[date2] = tasks2

date3 = input("Введите дату: Послезавтра ")
tasks3 = input("Введите задачу: Разработать Telegram-бота ")
tasks_dict[date3] = tasks3

print("Данные успешно сохранены в словарь.")












# Задание 3
# Модифицируйте программу из задания 2 таким образом, чтобы данные не выводились на экран, а сохранялись в словарь. Ключами в этом словаре должны быть даты, а значениями - соответствующие им задачи.

# Введите дату: Сегодня
# Введите задачу: Выучить Python
# Введите дату: Завтра
# Введите задачу: Разработать TODO-приложение
# Введите дату: Послезавтра
# Введите задачу: Разработать Telegram-бота