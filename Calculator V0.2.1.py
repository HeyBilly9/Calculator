#import random module
import random
#Set lastResult to NA if the user has not done any operations yet
lastResult = "NA"
#Function to get number to simplify and shorten the code
def getNumber(prompt):
    while True:
        userInput = input(prompt)
        if userInput.lower() == "pre":
            #Return the last result if the user inputs "pre"
            if lastResult != "NA":
                return lastResult
        try:
            #Return user's input if it is valid
            return float(userInput)
        except ValueError:
            if userInput.lower() == "pre":
                print("You have not done any operations yet.")
            else:
                #Return error if not valid with a random example of a valid input
                print("That is not a valid quantity. Please enter a valid quantity, such as " + str(round(random.uniform(-100, 100), 2)) + ".")

#Welcome user :D
print("Welcome to Calculator V2.1!")
print("""This version adds the ability to enter "pre" to use the result of your last equation.""")
print("This is the latest version.")
#Different wording for first operation, not case sensitive
request = input("What operation would you like to perform? ").lower()
while True:
    match request:
        case "add" | "addition" | "adding" | "plus" | "combine" | "total" | "sum" | "increase"| "a":
            #Addition
            NumOne = getNumber("What is the first number you would like to add? ")
            NumTwo = getNumber("What is the second number you would like to add to " + str(NumOne) + "? ")
            lastResult = NumOne + NumTwo
            print("The sum of " + str(NumOne) + " and " + str(NumTwo) + " is " + str(lastResult) + ".")
        case "subtract" | "subtracting" | "minus" | "difference" | "take away" | "remove" | "deduct" | "decrease" | "s":
            #Subtraction
            NumOne = getNumber("What is the first number you would like to be subtracted? ")
            NumTwo = getNumber("What is the second number you would like to subtract from " + str(NumOne) + "? ")
            lastResult = NumOne - NumTwo
            print("The difference between " + str(NumOne) + " and " + str(NumTwo) + " is " + str(lastResult) + ".")
        case "multiply" | "multiplying" | "multiplication" | "times" | "product" | "scale" | "expand" | "m":
            #Multiplication
            NumOne = getNumber("What is the first number you would like to multiply? ")
            NumTwo = getNumber("What is the second number you would like to multiply " + str(NumOne) + " by? ")
            lastResult = NumOne * NumTwo
            print("The product of " + str(NumOne) + " and " + str(NumTwo) + " is " + str(lastResult) + ".")
        case "division" | "divide" | "quotient" | "split" | "fraction" | "ratio" | "halve" | "half" | "d":
            #Division
            NumOne = getNumber("What is the first number you would like to be divided? ")
            while True:
                #Prevent a ZeroDivisionError if the user enters a zero.
                NumTwo = getNumber("What is the second number you would like to divide " + str(NumOne) + " by? ")
                if NumTwo == 0:
                    print("You can not divide by zero. Please enter a nonzero number.")
                else:
                    break
            lastResult = NumOne / NumTwo
            print("The quotient of " + str(NumOne) + " and " + str(NumTwo) + " is " + str(lastResult) + ".")
        case _:
            print(request.capitalize() + " is an invalid operation. Please input a valid operation, such as addition, subtraction, multiplication, or division.")
    #Loop for another input, not case sensitive
    request = input("""What is another operation you would like to perform? You can type "pre" to use the result of your last equation as the number. """).lower()