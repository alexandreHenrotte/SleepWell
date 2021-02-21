import os
import subprocess
import re
from time import sleep
from datetime import datetime, timedelta


def mode1(hour, minutes):
    complete_time = "%s:%s:00" % (hour, minutes)

    sleep_time_1 = str(datetime.strptime(
        complete_time, "%H:%M:%S") - datetime.strptime("09:15:00", "%H:%M:%S"))
    sleep_time_2 = str(datetime.strptime(
        complete_time, "%H:%M:%S") - datetime.strptime("07:45:00", "%H:%M:%S"))
    sleep_time_3 = str(datetime.strptime(
        complete_time, "%H:%M:%S") - datetime.strptime("06:15:00", "%H:%M:%S"))
    sleep_time_4 = str(datetime.strptime(
        complete_time, "%H:%M:%S") - datetime.strptime("04:45:00", "%H:%M:%S"))

    liste = [sleep_time_1, sleep_time_2, sleep_time_3, sleep_time_4]

    result = "Voici les heures ou vous devriez allez vous coucher :"
    for i in liste:
        i = re.sub("-1 day, ", "", i)
        result += "\r\n--->" + i + ""

    return result


def mode2():
    wakeup_time_1 = datetime.today() + timedelta(hours=4, minutes=45)
    wakeup_time_2 = datetime.today() + timedelta(hours=6, minutes=15)
    wakeup_time_3 = datetime.today() + timedelta(hours=7, minutes=45)
    wakeup_time_4 = datetime.today() + timedelta(hours=9, minutes=15)

    liste = [wakeup_time_1, wakeup_time_2, wakeup_time_3, wakeup_time_4]

    result = "Voici les heures ou vous devriez vous réveiller :"
    for i in liste:
        i = i.strftime("%H h %M")
        result += "\r\n--->" + i + ""

    return result


def calculate(selected_mode, hour, minutes):
    if selected_mode == "mode1":
        return mode1(hour, minutes)
    elif selected_mode == "mode2":
        return mode2()
    else:
        return "Ce mode n'existe pas !"
