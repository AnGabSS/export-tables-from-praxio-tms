from calendar import monthrange
from datetime import datetime


def subtract_months(date, months):
    new_month = date.month - months
    new_year = date.year

    if new_month <= 0:
        new_year -= 1
        new_month += 12

    # Ajusta o dia se o mês resultante tiver menos dias que o original
    last_day_of_new_month = monthrange(new_year, new_month)[1]
    new_day = min(date.day, last_day_of_new_month)

    return datetime(new_year, new_month, new_day)