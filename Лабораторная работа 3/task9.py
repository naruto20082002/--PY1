salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
need_money = spend - salary
for i in range(1, months ):
    trat = spend * ((1 + increase) ** i)
    need_money += trat - salary


# TODO Оформить решение
print(round(need_money))
