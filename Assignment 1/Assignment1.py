#Problem 1 
name = input("What is your name? ") #Asks for user input for name
print("Hello " + name + "!") #Prints out the name

address = input("What is your address? ") #Asks for user input for address
print("Your address is " + address) #Prints out the address

major = input("What is your major? ") #Asks for user input for major
print("Your major is " + major) #Prints out the major

favorite_color = input("What is your favorite color? ") #Asks for user input for favorite color
print("Your favorite color is " + favorite_color) #Prints out the


#problem 2
print("Blah " * 10) 

#problem 3
full_name = input("What is your full name? ") #Asks for user input for full name

#prints the number of characters in the full name excluding spaces

print("your name has:", len(full_name.replace(" ", "")),"letters" )

#problem 4
def total_inches(feet, inches):
    return (feet * 12) + inches

feet = int(input("Enter the number of feet: "))
inches = int(input("Enter the number of inches: "))
print("The total number of inches is: ", total_inches(feet, inches))

