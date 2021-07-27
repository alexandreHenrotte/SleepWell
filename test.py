import datetime
from datetime import datetime, timedelta

complete_time = "%s:%s:00" % ("10", "00")

time_1 = {
    "nb_cycles" : "6",
    "sleep_time" : str(datetime.strptime(complete_time, "%H:%M:%S") - datetime.strptime("09:15:00", "%H:%M:%S"))
}

time_2 = {
    "nb_cycles" : "5",
    "sleep_time" : str(datetime.strptime(complete_time, "%H:%M:%S") - datetime.strptime("07:45:00", "%H:%M:%S"))
}
    
time_3 = {
    "nb_cycles" : "4",
    "sleep_time" : str(datetime.strptime(complete_time, "%H:%M:%S") - datetime.strptime("06:15:00", "%H:%M:%S"))
}
    
time_4 = {
    "nb_cycles" : "3",
    "sleep_time" : str(datetime.strptime(complete_time, "%H:%M:%S") - datetime.strptime("04:45:00", "%H:%M:%S"))
}

raw_time_list = [time_1, time_2, time_3, time_4]
for time in raw_time_list:
    # Remove unecessary information
    time["sleep_time"].replace("-1 day, ", "") 

    # Add leading zero if necessary
    if len(time["sleep_time"].split(":")[0]) == 1:
        time["sleep_time"] = "0" + time["sleep_time"]

print(raw_time_list)