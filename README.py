import calendar
try:
  a = int(input("Choose year for calendar: "))
  print(calendar.calendar(a))
except:
  print("Valid year")
