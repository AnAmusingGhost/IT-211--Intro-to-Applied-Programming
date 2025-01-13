1. At the end of 2022, the national debt in the US is projected to be 31.55 trillion dollars. In theory, the debt will rise by 9.2% every year. Write a program showing what the debt will be each year to 2035. You can use a string stating your figures are in the trillions and must use 2 decimal points. The output in the Shell should be every year from 2022 to 2035 with a result. Don't give me results that are only for 2023 and 2035.


2. For the following dictionary, 
roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5, 'X': 10, 'L': 50} 

Write a program that does the following: 

Create a list of its keys.
Create a list of its values. 
Create a list of its items. 

The lists you created in the program must display in the Shell once the program runs.

3. A leap year is when a year has 366 days: An extra day, February 29. Write a program when entering a year & it should say if that year is a leap year or not. You must have the following requirements:
a. Must use if, elif, and else statements in your program.
b. The year must be divisible by 4.
c. If the year is a century year (1700, 1800, etc.), the year must be evenly divisible by 400.

4. Write a program that takes a 10-digit phone number and adds a hyphen in the correct location. Using an input field for the user to enter the information. Also, use a string for instructions on how to enter the phone in the input field.

Ex: 
3125551212
 
Output
312-555-1212
You may not use a regular expression in this program. If you do, you will receive a zero for this problem.

5. Create a class named Car. Do the following:
a. Define an instance method with a parameter that automatically refers to the instance being created, along with 3 other parameters: make, year, and color. This method will take in these parameters and assign them to attributes associated with items made from this class. For example, when we make a new Car instance, we'll need to specify a make, year, and color for our instance.


b. Create a 2nd method that puts a car's make, year, and color into one string describing the car. This way, you don't need to print each attribute's value individually.
c. Create a variable named new_car that creates a new Car instance with values using the attributes.

d. Have a print statement that calls the 2nd method that describes the car you have.


Find and Correct Errors. There are 5 errors combined in both programs (3 errors in one and 2 in the other), with 5 points for each solved correctly. Don't add or erase from the code given; only correct the errors. If you do either two, there will be a deduction in points. Identify the mistakes by using comments in your code and correct them. Failure to do so points will be deducted. Correctly fixed all the errors, so the code runs perfectly in the Shell.


1. Once all the errors are fixed, your problem should run correctly.

def celsius_to_kelvin(value_celsius):

  value_kelvin = 0.0

  value_kelvin = value_cel + 273.15

return value_kelvin

def kelvin_to_celsius(value_kelvin):

  value_celsius = 0.0

  value_celsius = value_kelvin - 273.15

  return value_celsius

value_c = 0.0

value_k = 0.0
value_c = 10.0

print(value_c, 'C is', celsius_2_kelvin(value_c), 'K')

value_k = 283.15

print(value_k, 'is', kelvin_to_celsius(value_k), 'C')

7. Once all the errors are fixed, you will be able to answer the prompts given:
user_input = ''

while user_input != 'q':

    weight = int(input('Enter weight (in pounds): '))

    if weight < 0:

        print('Invalid weight.')

    :

        height = int(input('Enter height (in inches): '))

        if height <= 0:

            print('Invalid height')
if (weight < 0) or (height <= 0):

        print('Can not compute info.')

    else:

        bmi = (float(weight) / float(height * height)) * 703

        print('BMI:', bmi)

        print('(CDC: 18.6-24.9 normal)\n') 



    user_input = ("Enter any key ('q' to quit): ")
