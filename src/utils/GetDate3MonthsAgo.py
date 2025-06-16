from datetime import datetime

from src.utils.SubtractMonths import subtract_months


def GetDate3MonthsAgo():
    current_date = datetime.now()
    date_three_months_ago = subtract_months(current_date, 3)
    formatted_date = date_three_months_ago.strftime('%d/%m/%Y')
    return formatted_date