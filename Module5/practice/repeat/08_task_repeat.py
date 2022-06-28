# Вы решили сделать вклад в банк некоторой суммы на n лет.
# Банк вам предложил x% годовых с расчетом по простым процентам или
# y% годовых по сложным % с периодом капитализации 1 месяц.
# При заданных процентных ставках, определите какой из вкладов вам выгоднее на 5 лет.
# Примечание: формулы расчета простых и сложных процентов ищите на гуглодиске в папке с материалами.

def deposit_hard(cash, percent, years):
    for i in range(years * 12):
        cash += cash / 100 * (percent / 12)
    return cash


def deposit_simple(cash, percent, years):
    return cash + cash / 100 * (percent * years)


cash = int(input("Введите сумму вклада: "))
years = int(input("Введите срок вклада: "))
percent_h = int(input("Введите ставку сложных процентов: "))
percent_s = int(input("Введите ставку простых процентов: "))

if deposit_hard(cash, percent_h, years) > deposit_simple(cash, percent_s, years):
    print("Рекомендуем вклад со сложными процентами. Итоговая сумма: ", round(deposit_hard(cash, percent_h, years)))
else:
    print("Рекомендуем вклад с простыми процентами. Итоговая сумма: ", round(deposit_simple(cash, percent_s, years)))
    
