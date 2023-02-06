def add_time(start, duration, optional=False):
  days_array = [
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
    "Sunday"
  ]
  days_index = {
    "monday": 0,
    "tuesday": 1,
    "wednesday": 2,
    "thursday": 3,
    "friday": 4,
    "saturday": 5,
    "sunday": 6
  }
  durationTuple = duration.partition(":")
  durationHours = int(durationTuple[0])
  durationMinutes = int(durationTuple[2])

  startTuple = start.partition(":")
  startMinutesTemp = startTuple[2].partition(" ")
  startHours = int(startTuple[0])
  startMinutes = int(startMinutesTemp[0])
  hour_am_pm = startMinutesTemp[2]
  hour_flip = {"AM": "PM", "PM": "AM"}
  amountOfdays = int(durationHours / 24)

  endMinutes = durationMinutes + startMinutes
  if (endMinutes >= 60):
    startHours += 1
    endMinutes %= 60
  amount_hour_flip = int((startHours + durationHours) / 12)
  endHours = (startHours + durationHours) % 12

  endMinutes = endMinutes if endMinutes > 9 else "0" + str(endMinutes)
  endHours = endHours = 12 if endHours == 0 else endHours
  if (hour_am_pm) == "PM" and startHours + (durationHours % 12) >= 12:
    amountOfdays += 1

  hour_am_pm = hour_flip[
    hour_am_pm] if amount_hour_flip % 2 == 1 else hour_am_pm

  new_time = str(endHours) + ":" + str(endMinutes) + " " + hour_am_pm
  if (optional):
    optional = optional.lower()
    index = int((days_index[optional]) + amountOfdays) % 7
    newDay = days_array[index]
    new_time += ", " + newDay

  if (amountOfdays == 1):
    return new_time + " " + "(next day)"
  elif (amountOfdays > 1):
    return new_time + " (" + str(amountOfdays) + " days later)"

  return new_time
