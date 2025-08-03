import pandas as pd

# Step 1: Create a DataFrame with 3 students
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [20, 22, 19],
    'grade': [85, 45, 70]
}

df = pd.DataFrame(data)

# Step 2: Add a "Passed" column where grade > 50 = True
df['Passed'] = df['grade'] > 50

# Step 3: Filter and display only students who passed
passed_students = df[df['Passed']]

# Display the result
print(passed_students)