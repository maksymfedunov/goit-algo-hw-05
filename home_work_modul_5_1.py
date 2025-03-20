def caching_fibonacci():
    cache = {} #Создаём словарь для кэширования результатов

    def fibonacci(n): # Функция числа Фибоначчи
        if n <= 0: # Если число меньше или равно 0, возвращаем 0
            return 0
        if n == 1: #Если число равно 1, возвращаем 1
            return 1
        if n in cache: #Если результат уже существует в кэше, извлекаем его
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2) #Вычисляем результат рекурсивно
        return cache[n] #Возвращаем результат, и сохраняем в кэше

    return fibonacci #Возвращаем функцию



