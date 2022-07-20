#PARSER

import time
import datetime
import re
from datetime import datetime
from datetime import time
from datetime import date
MESSAGE = {'Status': 'Success',"Date":{"Day":None}, "Params":{"Repeat_always":None, "Day_of_week":None}}
text_i = input('ENTER YOUR STRING: ')
n = text_i.split()
def main():

    text_i = input('ENTER YOUR STRING: ')
    n = text_i.split()
    Time = re.findall(r"[0-2]\d:[0-5]\d", text_i)
    mes = re.sub('[0-2]\d:[0-5]\d', '', text_i)
    STRING = re.sub('\d{2}.\d{2}.\d{4}', '', mes)

    match = re.search(r'\d{2}.\d{2}.\d{4}', text_i)
    print(match)
    date = datetime.strptime(match.group(), '%d.%m.%Y').date()
    day_month_year = str(date)
    year = day_month_year[:4]
    month = day_month_year[5:7]
    day = day_month_year[-2:]

    Year = int(year)
    Month = int(month)
    Day = int(day)

    time1 = str(Time)
    hour = time1[2:4]
    minute = time1[5:7]

    Hour = int(hour)
    Minute = int(minute)
    try:
        current_date = datetime.now().replace(second=0, microsecond=0)
        text_date = datetime(Year, Month, Day, Hour, Minute)
        delta = text_date - current_date
        sec = delta.total_seconds()

        seconds = int(sec)
        time.sleep(seconds)
    except OverflowError:
        print('Неправильный ввод даты')

    else:
        print(STRING)

    try:

        for i in range(len(my_list)):

            if my_list[i] == 'Через' or my_list[i] == 'через':
                if 0 < int(my_list[i + 1]) < 60 and (
                        my_list[i + 2] == 'минуту' or my_list[i + 2] == 'минуты' or my_list[i + 2] == 'минут'):
                    find_delayed_minute = my_list[i + 1]
                    find_delayed_hour = 0 # определяем минуты

            if 0 < int(my_list[i + 1]) < 24 and (
                    my_list[i + 2] == 'час' or my_list[i + 2] == 'часа' or my_list[i + 2] == 'часов'):
                find_delayed_minute = 0
                find_delayed_hour = my_list[i + 1] # определяем часы

            if 0 < int(my_list[i + 1]) < 24 and (
                    my_list[i + 2] == 'час' or my_list[i + 2] == 'часа' or my_list[i + 2] == 'часов') and \
                    0 < int(my_list[i + 3]) < 60 and (
                    my_list[i + 4] == 'минуту' or my_list[i + 4] == 'минуты' or my_list[i + 4] == 'минут'):
                find_delayed_hour = my_list[i + 1] # определяем часы
                find_delayed_minute = my_list[i + 3] # орпеделяем минуты

    except IndexError:

        print(
            'Необходимо ввести в формате: Через (число) часов (число) минут ИЛИ Через (число) часов ИЛИ Через (число) минут')

if ('завтра'in n) or ('tomorrow'in n):
    from datetime import date, timedelta, datetime
    tomorrow = str((date.today() + timedelta(days=1)))
    print(tomorrow)
    tomorrow = tomorrow.split('-')
    print(tomorrow)
    MESSAGE['Date']['Year'] = tomorrow[0]
    MESSAGE['Date']['Month'] = tomorrow[1]
    MESSAGE['Date']['Day'] =  tomorrow[2]
    print(MESSAGE)

elif ('послезавтра'in n) or ('aftertomorrow' in n):
    from datetime import date, timedelta, datetime

    aftertomorrow = str((date.today() + timedelta(days=2)))
    print(aftertomorrow)
    aftertomorrow = aftertomorrow.split('-')
    print(aftertomorrow)
    MESSAGE['Date']['Year'] = aftertomorrow[0]
    MESSAGE['Date']['Month'] = aftertomorrow[1]
    MESSAGE['Date']['Day'] = aftertomorrow[2]
    print(MESSAGE)