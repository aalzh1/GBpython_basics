n = int(input("Input number from 1 to 9:"))

if n > 9 or n < 1:
    print("Inputted number is out of predefined range")
else:
    m = n * 10 + n
    k = n * 100 + n * 10 + n
    print("Result:", n + m + k)
