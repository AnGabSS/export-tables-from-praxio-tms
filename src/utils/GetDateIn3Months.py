from datetime import datetime

from src.utils.AddMonths import add_months


def GetDateInThreeMonths():
    current_date = datetime.now()
    date_three_months_ago = add_months(current_date, 3)
    formatted_date = date_three_months_ago.strftime('%d/%m/%Y')
    return formatted_date