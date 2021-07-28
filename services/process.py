from time import sleep
from datetime import date, datetime, timedelta


def calculate(selected_mode, hour, minutes):
    if selected_mode == "mode1":
        return mode1(hour, minutes)
    elif selected_mode == "mode2":
        return mode2()


def mode1(hour, minutes):
    complete_time = "%s:%s:00" % (hour, minutes)

    time_1 = {
        "level" : "Très bien",
        "nb_cycles" : 6,
        "time" : str(datetime.strptime(complete_time, "%H:%M:%S") - datetime.strptime("09:15:00", "%H:%M:%S"))
    }
    
    time_2 = {
        "level" : "Bien",
        "nb_cycles" : 5,
        "time" : str(datetime.strptime(complete_time, "%H:%M:%S") - datetime.strptime("07:45:00", "%H:%M:%S"))
    }
        
    time_3 = {
        "level" : "Minimum",
        "nb_cycles" : 4,
        "time" : str(datetime.strptime(complete_time, "%H:%M:%S") - datetime.strptime("06:15:00", "%H:%M:%S"))
    }
        
    time_4 = {
        "level" : "Risqué",
        "nb_cycles" : 3,
        "time" : str(datetime.strptime(complete_time, "%H:%M:%S") - datetime.strptime("04:45:00", "%H:%M:%S"))
    }

    raw_time_list = [time_1, time_2, time_3, time_4]
    return formatTimeForTemplates(raw_time_list)


def mode2():
    time_1 = {
        "level" : "Risqué",
        "nb_cycles" : 3,
        "time" : datetime.today() + timedelta(hours=4, minutes=45)
    }
    time_2 = {
        "level" : "Minimum",
        "nb_cycles" : 4,
        "time" : datetime.today() + timedelta(hours=6, minutes=15)
    }
    time_3 = {
        "level" : "Bien",
        "nb_cycles" : 5,
        "time" : datetime.today() + timedelta(hours=7, minutes=45)
    }
    time_4 = {
        "level" : "Très bien",
        "nb_cycles" : 6,
        "time" : datetime.today() + timedelta(hours=9, minutes=15)
    }

    raw_time_list = [time_1, time_2, time_3, time_4]
    return formatTimeForTemplates(raw_time_list)


def formatTimeForTemplates(raw_time_list):
    formatted_time_list = []
    for time in raw_time_list:
        # Mode 2 result
        if type(time["time"]) is datetime:
            time["time"] = time["time"].strftime("%H:%M")
        # Mode 1 result
        else:
            # Remove unecessary information in the output
            time["time"] = time["time"].replace("-1 day, ", "") 

            # Add leading zero if necessary
            if len(time["time"].split(":")[0]) == 1:
                time["time"] = "0" + time["time"]

        # Separate for templates
        time_split = time["time"].split(":")
        formatted_time_list.append({
            "level": time["level"],
            "nb_cycles": time["nb_cycles"],
            "time_duration": convertCyclesToTime(time["nb_cycles"]),
            "hour": time_split[0],
            "minutes": time_split[1]
        })

    return formatted_time_list


def convertCyclesToTime(nb_cycles):
    # Conversion
    full_hours = nb_cycles * (90 / 60) # Ex : 1.5
    hour = int(full_hours // 1) # Ex : 1
    minutes = int((full_hours % 1) * 60) # Ex : 30
    
    # String formatting (add leading zero if necessary)
    hour = ("0" + str(hour)) if (hour < 10) else str(hour)
    minutes = ("0" + str(minutes)) if (minutes < 10) else str(minutes)
    
    return hour + ":" + minutes