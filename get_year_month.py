from datetime import datetime


def get_previos_month_and_year():
    testando = datetime.today()
    if testando.month ==  1:
        previous_month = 1 #12
        year = testando.year #- 1
    else:
        previous_month = testando.month #- 1
        year = testando.year
    return previous_month,year


