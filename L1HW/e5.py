revenue = int(input("Input revenue:"))

cogs = int(input("Input COGS:"))

prof = False

if revenue != cogs:
    if revenue > cogs:
        print("The company is profitable")
        prof = True
    elif revenue < cogs:
        print("The company is unprofitable")
elif revenue == cogs:
    print("The company operates at break-even point")

if prof:
    profit = revenue - cogs
    ror = revenue / profit
    print("Return on revenue ratio: %.3f" % ror)
    employees_num = int(input("Input number of employees:"))
    print("Profit per employee: %.3f" % (profit / employees_num))
