# Load libraries
import pandas as pd
import numpy as np
import codecademylib3
import matplotlib.pyplot as plt
import seaborn as sns

# Define a function to calculate statistics for a given column
def calculate_statistics(column):
    print(f'The average is {column.mean():.2f}')
    print(f'The median is {column.median():.2f}')
    print(f'The mode is {column.mode()}')
    print(f'The range is {column.max() - column.min():.2f}')
    print(f'The standard deviation is {column.std():.2f}')
    print(f'The mean absolute deviation is {column.mad():.2f}')

# Import data
students = pd.read_csv('students.csv')

# Print first few rows of data
print(students.head())

# Print summary statistics for all columns
print(students.describe(include='all'))
# More students live in urban locations

# Calculate multiple statistics using agg()
math_stats = students.math_grade.agg(['mean', 'median'])
mode_value = students.math_grade.mode()
print(f"The average grade is {math_stats['mean']:.2f}")
print(f"The median grade is {math_stats['median']:.2f}")
print(f"The modal grades are {mode_value}")

# Calculate range
print(f'The range of the grade is {students.math_grade.max() - students.math_grade.min():.2f}')

# Calculate standard deviation
print(f'The standard deviation of the grade is {students.math_grade.std():.2f}')

# Calculate MAD
print(f'The mean absolute deviation of the grade is {students.math_grade.mad():.2f}')

# Create a histogram of math grades
sns.histplot(x='math_grade', data=students)

plt.show()
plt.clf()

# Create a box plot of math grades
sns.boxplot(x='math_grade', data=students)

plt.show()
plt.clf()

# Calculate number of students with mothers in each job category
print(students.Mjob.value_counts())
# The most common job type is 'other', followed by 'services'.

# Calculate proportion of students with mothers in each job category
print(students.Mjob.value_counts(normalize=True))
# The proportion of moms who work at healt is about 8.6%

# Create bar chart of Mjob
sns.countplot(x='Mjob', data=students)

plt.show()
plt.clf()

# Create pie chart of Mjob
students.Mjob.value_counts().plot.pie()

plt.show()
plt.clf()
# Calculating statistics for address
print(students.address.value_counts(normalize=True))


# Calculate statistics for absences
calculate_statistics(students.absences)

print(students.Fjob.value_counts())
print(students.Fjob.value_counts(normalize=True))

# Create a histogram of number of absences
sns.histplot(x='absences', data=students)

plt.show()
plt.clf()

# Create a box plot of number of absences
sns.boxplot(x='absences', data=students)

plt.show()
plt.clf()
