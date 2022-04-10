for n in range(10000):
    output = ""#Sets the output to an empty string
    if (n % 5 == 00):#Checks to see if the moudle returns 0 for the iteration and 5
        output = output + "Fizz"#Appends "Fizz" to the output string
    if (n %  3 == 00):#Checks to see if the moudle returns 0 for the iteration and 3
        output = output +  "Buzz"#Appends "Buzz" to the output string
    else:
        output = n#"Sets the output to the itteration if nothing no test was passed"
    print(output)#Outputs the variable output