a = float(input("Input first day result (km):"))

b = float(input("Input target result (km):"))

day_res = a

day_count = 1

print(day_count, day_res)

while day_res < b:
    day_res *= 1.1
    day_count += 1
    print(day_count, day_res)

print("Result reached at", day_count, "training day")
