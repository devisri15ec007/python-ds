year = 2005
if (year % 4) == 0:
  if (year % 100) == 0:
    if (year % 400) == 0:
      print("The given year is a Leap year")
    else:
        print("The given year is not a Leap year")
  else:
    print("The given year is not a Leap year")
else:
  print("The given year is not a Leap year")
       
