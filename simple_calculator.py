def add(num1, num2): # So in thee first line the function is defined as add, it takes 2 arguments, "num1 and num2" and will return the sum of this number.
    # No value has been assigned to num1 and num2 as we will try and get this from the user.
    return num1 + num2

def subtract(num1, num2): #similar to above but instead function defined as subtract.
    return num1 - num2

def multiply(num1, num2): #similar to above but instead function defined as multiply.
    return num1 * num2

def divide(num1, num2): #similar to above but instead function defined as divide.
    return num1 / num2

num1 = float(input("Enter the first number in the calculator: ")) #Now I am asking for user input which is being stored as a variable to be called on later.
num2 = float(input("Enter the second number in the calculator: ")) # Also I am converting the input to a float incase the user would like to use decimal numbers.

print("Please select what you would like the calculator to do. Please choose a NUMBER. ")
print("1.Add") # User needs to select what they would like to be done with the numbers selected.
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = int(input("Please select a NUMBER (1/2/3/4): ")) # Then users input is converted from a string to and integer and stored as a variable called 'choice'

if choice == 1: # Now we check what the users choice(mathmatical function) is equavalent to. For example if they chose 1 we add and 2 we substract etc.
    result = add(num1, num2)
elif choice == 2: # Then depending on what option was chosen the if/elif statement will call upon the function it is assigned to. So 2 will call upon the subtract function and subtract those 2 numbers.
    result = subtract(num1, num2)
elif choice == 3:
    result = multiply(num1, num2)
elif choice == 4:
    result = divide(num1, num2)
else:
    result = "Please enter a valid input."

print(result)
