def add_time(start, duration, starting_day=0):

    def get_keys(dic, value):

        return [key for key, val in dic.items() if val == value]

    count_am_pm = 0
    count_days = 0

    week = {"Monday": 1, "Tuesday": 2, "Wednesday": 3,
     "Thursday": 4, "Friday": 5, "Saturday": 6, "Sunday": 7}

    #Split and get each value of the input
    start_time = start.split(":")
    start_time[1] = start_time[1].split()

    start_hrs = int(start_time[0])
    start_mins = int(start_time[1][0])

    duration_time = duration.split(":")

    duration_hrs = int(duration_time[0])
    duration_mins = int(duration_time[1])

    start_am_pm = start_time[1][1]
    am_pm = start_am_pm

    #add the duration
    minutes = start_mins + duration_mins
    hours = start_hrs + duration_hrs

    if minutes >= 60:
        minutes -= 60
        hours += 1

    while hours > 12:
        hours -= 12
        count_am_pm += 1

    if hours == 12:
        count_am_pm +=1

    #set the AM/PM value
    if start_am_pm == "AM" and count_am_pm % 2 != 0:
        am_pm = "PM"
    elif start_am_pm == "PM" and count_am_pm  % 2 != 0:
        am_pm = "AM"

    while count_am_pm >= 2:
        count_am_pm -= 2
        count_days += 1

    if count_am_pm > 0 and start_am_pm == "PM":
        count_days += 1

    if starting_day != 0:
        day = week[starting_day.capitalize()] + count_days
        if day > 7:
            day -= 7

    new_time = f'{hours}:{minutes:{0}>{2}} {am_pm}'

    if starting_day != 0:
        new_time += f', {"".join(get_keys(week, day))}'

    if count_days > 0:
        if count_days == 1:
            new_time += f' (next day)'
        else:
            new_time += f' ({count_days} days later)'
        
    return new_time

print(add_time("11:43 PM", "24:20", "tueSday"))