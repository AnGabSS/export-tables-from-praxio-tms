from datetime import datetime

from src.utils.SubtractMonths import subtract_months


def GetDate6MonthsAgo():
    current_date = datetime.now()
    date_six_months_ago = subtract_months(current_date, 6)
    formatted_date = date_six_months_ago.strftime('%d/%m/%Y')
    return formatted_date