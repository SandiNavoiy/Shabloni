import time
from functools import wraps


def decor_time(func):
    """Декоратор функции для измерения времени"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        """внутряння функция декоратора"""
        # начальное время
        time_start = time.time()
        # просто мост выполнения
        f = func(*args, **kwargs)
        # конечное ремя
        time_end = time.time()
        # расчет времени
        print(
            f"Время выполнения функции составило {round(time_end -time_start, 10)} секунд"
        )
        # вывод

        return f

    # вывод внешней
    return wrapper
