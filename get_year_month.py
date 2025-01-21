from datetime import datetime


def get_previos_month_and_year():
    today = datetime.today()
    if today.month ==  1:
        previous_month = 12
        year = today.year - 1
    else:
        previous_month = today.month - 1
        year = today.year
    return previous_month,year