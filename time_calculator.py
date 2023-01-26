def add_time(start, duration, day_of_week = False):
    
    days_of_the_week_index = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}

    days_of_the_week_array = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    #For the start split the hour and minute string by partition(:)
    duration_tuple = duration.partition(":")
    duration_hours = int(duration_tuple[0])
    duration_minutes = int(duration_tuple[2])

    #Split between the start hours and minutes with AM/PM by (:)
    start_tuple = start.partition(":")

    #Split between the minutes and AM/PM by space (" ")
    start_minutes_tuple = start_tuple[2].partition(" ")

    #For hours would be the first index [0]
    start_hours = int(start_tuple[0])

    #For minutes would be the first index [0] after spliting the minutes and AM/PM
    start_minutes = int(start_minutes_tuple[0])

    #For AM/PM would be the second value of the minutes_tuple
    am_or_pm = start_minutes_tuple[2]

    #AM and PM flip dictionary
    am_and_pm_flip = {"AM": "PM", "PM": "AM"}

    #Put in the amount_of_days and set it to be an integer
    amount_of_days = int(duration_hours / 24)

    #Set conditions for the returnTime (hours, minutes and AM/PM flip)
    end_minutes = start_minutes + duration_minutes
    if (end_minutes >= 60):
      start_hours += 1
      end_minutes = end_minutes % 60
    amount_of_am_or_pm_flips = int((start_hours + duration_hours) / 12)
    end_hours = (start_hours + duration_hours) % 12

    end_minutes = end_minutes if end_minutes > 9 else "0" + str(end_minutes)
    end_hours = end_hours = 12 if end_hours == 0 else end_hours

    #Set the returnTime for AM/PM for the amount_of_days
    if (am_or_pm == "PM" and start_hours + (duration_hours % 12) >= 12):
      amount_of_days += 1

    #This will flip the AM & PM object. If the amount_of_am_or_pm adds up to be more than (has remainder), it will flip the AM/PM. Else without remainder/even, it will return the current AM/PM
    am_or_pm = am_and_pm_flip[am_or_pm] if amount_of_am_or_pm_flips % 2 == 1 else am_or_pm

    returnTime = str(end_hours) + ":" + str(end_minutes) + " " + am_or_pm
    if(day_of_week):
      day_of_week = day_of_week.lower()
      index = int((days_of_the_week_index[day_of_week]) + amount_of_days) % 7
      new_day = days_of_the_week_array[index]
      returnTime += ", " + new_day
      
    ##Set up the returnTime (next day or 2 days later)
    if (amount_of_days == 1):
      return returnTime + " " + "(next day)"
    elif (amount_of_days > 1):
      return returnTime + " (" + str(amount_of_days) + " days later)"
      
    return returnTime
