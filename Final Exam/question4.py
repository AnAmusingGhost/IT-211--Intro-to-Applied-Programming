n = input("Enter your phone number: ")

if len(n) == 10:
    x = n[0:3]
    y = n[3:6]
    z = n[6:]
    print(x + "-" + y + "-" + z)
else:
    print("The phone number you entered is not valid.")
    
