year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))
if year < 1800 or year > 2025:
  print("Invalid year")
elif month < 1 or month > 12:
  print("Invalid month")
elif day < 1 or day > 31:
  print("Invalid day")
else:
  if month == 12 and day == 31:
    year += 1
    month = 1
    day = 1
  elif day == 31:
    month += 1
    day = 1
  elif month in [4, 6, 9, 11] and day == 30:
    month += 1
    day = 1
  elif month == 2 and day == 28:
    month += 1
    day = 1
  else:
    day += 1
  print("Next date:", day , "/", month, "/" , year)
