import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Sample Data Creation
# Creating a DataFrame of students' scores in various subjects
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Math': [85, 78, 92, 65, 89],
    'Science': [88, 75, 95, 60, 82],
    'English': [90, 82, 85, 70, 88],
    'History': [80, 85, 78, 72, 84]
}

df = pd.DataFrame(data)

# Step 2: Data Analysis - Calculating Average Score for Each Student
df['Average'] = df[['Math', 'Science', 'English', 'History']].mean(axis=1)

# Step 3: Plotting Bar Graph
# Plot average scores of students
plt.figure(figsize=(10, 6))
plt.bar(df['Student'], df['Average'], color='skyblue')
plt.xlabel('Student')
plt.ylabel('Average Score')
plt.title('Average Scores of Students in Different Subjects')
plt.show()

# Step 4: Plot Scores by Subject for Each Student
df.set_index('Student')[['Math', 'Science', 'English', 'History']].plot(kind='bar', figsize=(10, 6))
plt.title('Scores of Students by Subject')
plt.xlabel('Student')
plt.ylabel('Scores')
plt.legend(title='Subjects')
plt.show()