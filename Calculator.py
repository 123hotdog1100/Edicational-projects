n1 = int(input("Please enter your first number: "))#Asks user for a first number and limits the response to numbers only
n2 = int(input("Please enter your second number: "))#Asks user for the second number and limits the response to numbers only
op = str(input("What operation do you wish to perform? "))#Asks user for the operation to perform and sets the response to a string
if op == "x" or "*":#Checks to see if the user wants to multiply
    answer = n1 * n2
elif op == "+":#Checks to see if the user wants to add
    answer = n1 + n2
elif op == "/":#Checks to see if the user wants to divide
    answer = n1 / n2
elif op == "-":#Checks to see if the user wants to subtract
    answer = n1 - n2
print(f"The result is {answer}")