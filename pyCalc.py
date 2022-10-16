# defines addition function, adds two float variables together and returns result to op_val function
def addition():
    print("\nI would like to add two float values.\n\nEnter the first value:")
    num1 = float(input())
    print("\nEnter the second value to be added:")
    num2 = float(input())

    result = num1 + num2
    return(result)

# defines subtraction function, subtracts one float variable from another and returns result to op_val function
def subtraction():
    print("\nI would like to subtract one float value from another.\n\nEnter the first value:")
    num1 = float(input())
    print("\nEnter the value to be subtracted:")
    num2 = float(input())

    result = num1 - num2
    return(result)

# defines multiplication function, multiplies two float variables together and
#  rounds after the fifth decimal place then returns result to op_val function
def multiplication():
    print("\nI would like to multiply two float values.\n\nEnter the first value:")
    num1 = float(input())
    print("\nEnter the second value to be multiplied by:")
    num2 = float(input())

    result = round((num1 * num2), 5)
    return(result) 

# defines division function, divides one float variable from another and
#  rounds after the fifth decimal place then returns result to op_val function
def division():
    print("\nI would like to divide one float value from another.\n\nEnter the first value:")
    num1 = float(input())
    print("\nEnter the value to divide by:")
    num2 = float(input())

    result = round((num1 / num2), 5)
    return(result)

# defines the op_val function (or operation validation function), this validates the
#  user input so that a valid value is always passed into the function. First it
#  truncates the user input to the first letter then compares that letter to the letters
#  that correspond with an available operation. Second, it calls that operation which
#  then returns a final value all the way back to the main function. If the user input
#  does not correspond with an available operation, the function returns an error message
def op_val(operand):
    result = operand[0]

    if(result == "a"):
        return(addition())

    elif(result == "s"):
        return(subtraction())

    elif(result == "m"):
        return(multiplication())

    elif(result == "d"):
        return(division())

    else:
        return("\nNot a valid operation. Please enter one of the available operations.")

# main function
#  1. Prints the available operations
#  2. Gets user input, forces this value to be a string to prevent issues within the functions
#  3. Forces the previous user input to a lowercase string, then passes it to the op_val function
print("\nAvailable operations:\n\na\tAddition\ns\tSubtraction\nm\tMultiplication\nd\tDivision\n")
operand = str(input("Which operation would you like to do? "))
print("\nResult: " + str(op_val(operand.lower())) + "\n")