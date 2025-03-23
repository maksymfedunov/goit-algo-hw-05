import re
from typing import Callable


def generator_numbers(text: str):
    pattern = r"\b-?\d+\.\d+?\b" #создаем регулярное выражение для поиска целых чисел
    matches = re.findall(pattern, text) #находим нужные нам числа в тексте
    for match in matches: #преобразовываем все числа в float
        yield float(match)
       
def sum_profit(text: str, func: Callable):
    total = sum(func(text)) #вычисляем сумму чисел из генератора
    return total
       


    