#Create an array with numbers 10 to 50.
#Find the maximum and minimum values.
#Multiply all elements by 3.

import numpy as np

#Create array
myArray = []

for num in range(10, 51):
    myArray.append(num)
    
    
# Convert to NumPy array
myArray = np.array(myArray)

# Step 2: Find max and min
max_value = np.max(myArray)
min_value = np.min(myArray)

print("Min:", min_value)
print("Max:", max_value)

# Step 3: Multiply all elements by 3
myArray_multiplied = myArray * 3

print("First few elements after multiplying by 3:", myArray_multiplied[:5])    
     
