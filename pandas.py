import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp =int( time.strftime('%H'))
print(timestamp)
timestamp =int( time.strftime('%M'))
print(timestamp)
timestamp =int( time.strftime('%S'))
print(timestamp)

if(timestamp>=6 and timestamp<=9):
  print("Gud morning")
elif(timestamp>9 and timestamp<=13):
  print("Gud afternoon")
elif(timestamp>13 and timestamp<=18):
  print("Gud Evening")
elif(timestamp>18 and timestamp<=24):
  print("Gud night")
