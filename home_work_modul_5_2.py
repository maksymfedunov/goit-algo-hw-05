import re
from typing import Callable


def generator_numbers(text: str):
    pattern = r" \-?\d+\.\d+? " #создаем регулярное выражение для поиска целых чисел
    matches = re.findall(pattern, text) #находим нужные нам числа в тексте
    for match in matches: #преобразовываем все числа в float
        yield float(match)
       
def sum_profit(text: str, func: Callable):
    total = sum(func(text)) #вычисляем сумму чисел из генератора
    return total
       
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")


    