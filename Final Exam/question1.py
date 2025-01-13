debt = 31.55 
debtRate = 0.092 


for z in range(2023, 2036):
    totaldebt = debt + (debt * debtRate) # calculate the debt for the next year

    debt = totaldebt # update the debt for the next year

    print("The year is:", z)
    print("the debt for that year is: {:0.2f} trillion".format(debt))
    print()
