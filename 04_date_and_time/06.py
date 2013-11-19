now = datetime.now()

year = now.year
month = now.month
day = now.day

mmddyyyy = str(month) + "/" + str(day) + "/" + str(year)
hhmmss = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)

print mmddyyyy + " " + hhmmss
