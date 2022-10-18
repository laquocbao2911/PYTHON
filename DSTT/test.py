import re

email = "chAothadasdasdao3001@gmail.com"
check = re.search('^[a-z0-9]+\w+@[a-z]+\.+[a-z]{2,4}$',email)

if check:
  print("YES! We have a match!")
else:
  print("No match")
