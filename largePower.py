#Create a method that tests whether the result of taking the power of one number to another number provides an answer which is greater than 5000.
#We will use a conditional statement to return True if the result is greater than 5000 or return False if it is not
#In order to accomplish this, we will need the following steps:

#1.Define the function to accept two input parameters called base and exponent
#2.Calculate the result of base to the power of exponent
#3.Use an if statement to test if the result is greater than 5000. If it is then return True. Otherwise, return False

#Instance
#4² (4(Base) to the power of 2(Exponent), or 4 squared) = 4 * 4 = 16

print("We'll be doing exponents and returning...\n True if condition met is above 5000 and False if below")
#Validation for User base input for expression
while True:
    try:
        base = int(input("Give me the Base i.e 4 in expression (4²):\n"))
        break #Exit loop if invalid
    except ValueError:
        print("Invalid input.Please enter a valid digits not in words!")
 
while True:
    try:
        exponent = float(input("Give me the exponent i.e 2 in expression (4²):\n"))
        break #Exit loop if invalid
    except ValueError:
        print("Invalid input.Please enter a valid digits not in words!")

#fn
result = base ** exponent
rounded_result = round(result, 2)

def exponent_math(base,exponent):
    #Calc 
    result = base ** exponent
    # Round to 2 decimal places to avoid floating point issues
    rounded_result = round(result, 2)
    
    if rounded_result >=5000: 
        return True
    else:
        return False  

#Calling the fn   
results = exponent_math(base,exponent)
    
print(f"The expression {base} to the power of {exponent} = {rounded_result} which is {results}.")      