sec = int(input('Input time in seconds:'))

hours = sec // 3600

minleft = sec % 3600

minutes = minleft // 60

seconds = minleft % 60

print(f"Inputted time in full time format: {hours:02}:{minutes:02}:{seconds:02}")

# print("Inputed time in full format: %s:%s:%s" % (sec // 3600, sec % 3600 // 60, sec % 3600 % 60))
