import numpy as np


data = np.array([10, 20, 30, 40, 50])

# 1. Random number chahiye → rand()
'''print(np.random.rand())''' # 0 aur 1 ke beech koi random decimal number.

# If i want 5 num
'''print(np.random.rand(5))'''

# 2. Random integer chahiye → randint()
'''rand_int = np.random.randint(1, 11)
print(rand_int)

  # If i want 5 num
aa = np.random.randint(1,11,5)
print(aa)'''

# 3. Existing data me se random value chahiye → choice()
'''data = np.array([10, 20, 30, 40, 50])
np.random.choice(data)
#  3 value
bb = np.random.choice(data, 3)
print(bb)'''


# 4. Array ko random order mein karna → shuffle()
'''data = np.array([10, 20, 30, 40, 50])
np.random.shuffle(data)
print(data)   #Original data change ho gaya.'''

# 5. Shuffle karna but original safe rakhna → permutation()
'''data = np.array([10, 20, 30, 40, 50])

new_data = np.random.permutation(data)
print(new_data)'''


# 6. Same random result chahiye → seed()np.random.seed(10)
'''import numpy as np

np.random.seed(10)
print(np.random.randint(1, 10, 5))

np.random.seed(10)
print(np.random.randint(1, 10, 5))'''

# seed() → random result ko reproducible banata hai

# 7. random() kya hai?

'''Ye bhi rand() jaisa hai.
randn() — abhi sirf basic idea

Ye normal distribution se random numbers deta hai.
np.random.randn(5)
Ex- [-0.52  1.13 -0.24  0.71 -1.02]  negative values bhi aa sakti hain'''

# DISTRIBUTIONS
# 9. Uniform Distribution
"""In a uniform distribution, values have roughly equal probability within a specified range."""
data = np.random.uniform(10, 20, 5)

# print(data)

# 10. Normal Distribution

'''Normal distribution is also called a bell-shaped distribution.'''
data = np.random.normal(50, 10, 5)
'''50 → Mean
10 → Standard deviation
5  → Number of values
eal-world examples:

Student marks
Heights
Measurement errors
Exam scores'''
# print(data)

# 11. Binomial Distribution

'''Binomial distribution is used for experiments with two possible outcomes, such as:

Success / Failure
Yes / No
Buy / Don't Buy
Head / Tail
Open / Not Open'''

# Syntax: np.random.binomial(n, p, size)
'''n    → Number of trials
p    → Probability of success
size → Number of experiments'''
# result = np.random.binomial(10, 0.5, 5)
# print(result)
'''10 trials
50% probability of success
5 experiments
Possible output:

[6 4 5 7 3]

For example:

Experiment 1 → 6 successes
Experiment 2 → 4 successes
Experiment 3 → 5 successes
...'''


# NUMPY RANDOM MODULE — PRACTICE QUESTIONS
# ========================================

# LEVEL 1 — BASIC
# ----------------

import numpy as np
'''# Q1. Random Decimal
# Generate one random decimal number between 0 and 1.
print(np.random.rand())

# Q2. Multiple Random Decimals
# Generate 5 random decimal numbers between 0 and 1.
print(np.random.rand(5))

# Q3. Random Integer
# Generate one random integer between 1 and 10.
print(np.random.randint(1,10))

# Q4. Multiple Random Integers
# Generate 5 random integers between 1 and 100.
print(np.random.randint(1,100,5))

# Q5. Random Selection
# Given:

data = np.array([10, 20, 30, 40, 50])
# Randomly select one value from the array.
print(np.random.choice(data))

# Q6. Multiple Random Selection
# Given:

data = np.array([10, 20, 30, 40, 50])
# Randomly select 3 values from the array.
print(np.random.choice(data,3))

# Q7. Shuffle an Array
# Given:
data = np.array([10, 20, 30, 40, 50])
# Randomly rearrange the elements of the array.
np.random.shuffle(data)
# Check whether the original array is changed or not.

print(data)
# Q8. Keep Original Array Safe
# Given:
data = np.array([10, 20, 30, 40, 50])

# Create a randomly rearranged version of the array.
tand =np.random.permutation(data)
print("Rearange",tand)
# Check whether the original array remains unchanged.

print(data)

# Q9. Reproducible Random Values
# Set a fixed starting value for the random generator.
np.random.seed(1)
# Generate 5 random integers between 1 and 10.
a = np.random.randint(1,10,5)
# Again set the same starting value and generate 5 random integers.
np.random.seed(1)
b = np.random.randint(1,10,5)
# Check whether both results are exactly the same.
print(a,b)

# Q10. Negative Random Values
# Generate 10 random values where both positive and negative values are possible.
value = np.random.randn(10)
val = np.round(value,2)             #after value two digit value
# Observe the generated values.
print(val)'''

# LEVEL 2 — INTERMEDIATE
# ----------------------

# Q11. Random Sales
# Generate 10 random sales values between ₹1,000 and ₹10,000.
value = np.random.randint(1000,10001,10)
print(value)

# Q12. Random Student Marks
# Generate marks for 100 students.
# Each mark should be an integer between 0 and 100.
marks = np.random.randint(0,101,100)
print(marks)

# Q13. Random 2D Data
# Generate a 5 × 3 array containing random integers between 1 and 100.
matrix = np.random.randint(1,101,(5,3))
print(matrix)

# Q14. Random Matrix
# Generate a 3 × 4 matrix containing random decimal values between 0 and 1.
matrix = np.random.rand(3,4)
print(matrix)

# Q15. Selection Without Repetition
# Given:

students = np.array(["A", "B", "C", "D", "E"])
# Randomly select 3 students.


# The same student should not appear more than once.
select = np.random.choice(students,3,replace=False)
print(select) 

# Q16. Selection With Repetition
# Given:

students = np.array(["A", "B", "C", "D", "E"])
# Randomly select 10 students.
# A student is allowed to appear multiple times.
select =np.random.choice(students,10,replace=True)
print(select)


# Q17. Random Values in a Range
# Generate 10 random decimal values between 10 and 50.
value =np.random.uniform(10,50,10)
print(value)

# Q18. Student Score Simulation
# Generate 20 random exam scores around an average of 70.

# Use a standard deviation of 10.
score = np.random.normal(70,10,20)
# Observe the generated values.
print(score)

# Q19. Coin Toss Simulation
# A coin is tossed 10 times.

# The probability of getting Heads is 0.5.
# Repeat this complete experiment 5 times.
# For every experiment, record the number of Heads.
toss = np.random.binomial(10,0.5,5)
print(toss)

# Q20. Reproducible Sales Dataset
# Create 10 random sales values between 1,000 and 5,000.

# Use a fixed random starting value.
np.random.seed(1)
# Run the same code again with the same starting value.

# Check whether the generated sales are identical.
sales = np.random.randint(1000,5000,10)
print(sales)


np.random.seed(1)
sales = np.random.randint(1000,5000,10)
print(sales)


# LEVEL 3 — ADVANCED
# -------------------

# Q21. Employee Salary Dataset
# Generate salaries for 100 employees.

# Salary range:

# ₹20,000 to ₹1,00,000

# Then calculate:

# 1. Maximum salary
# 2. Minimum salary
# 3. Average salary


# Q22. Student Performance Dataset
# There are 50 students and 5 subjects.

# Generate a 50 × 5 marks dataset.

# Marks should be between 0 and 100.

# Calculate:

# 1. Total marks of every student
# 2. Highest total
# 3. Lowest total
# 4. Class average


# Q23. Monthly Product Sales
# There are 12 months and 4 products.

# Generate a 12 × 4 sales dataset.

# Sales should be between 1,000 and 10,000.

# Calculate:

# 1. Total sales
# 2. Average sales
# 3. Highest sale
# 4. Lowest sale


# Q24. Compare Two Random Rearrangements
# Given:

# data = np.array([10, 20, 30, 40, 50])

# Randomly rearrange the array in two different ways.

# For the first method, check whether the original array changes.

# For the second method, check whether the original array changes.

# Identify the difference between the two approaches.


# Q25. Product Purchase Simulation
# Given:

# products = np.array([
#     "Laptop",
#     "Mobile",
#     "Tablet",
#     "Headphones",
#     "Keyboard"
# ])

# Simulate 100 random customer purchases.

# Then calculate how many times each product was purchased.


# Q26. Marketing Campaign Simulation
# A company contacts customers.

# Each experiment has:

# 10 customers

# Probability of purchase = 0.3

# Run the experiment 20 times.

# Find:

# 1. Purchases in every experiment
# 2. Maximum purchases
# 3. Minimum purchases
# 4. Average purchases


# Q27. Exam Score Distribution
# Generate 1,000 student exam scores.

# Average score should be around 70.

# Standard deviation should be 10.

# Calculate:

# 1. Mean
# 2. Minimum
# 3. Maximum
# 4. Standard deviation


# Q28. Complete Reproducibility Test
# Set a fixed random starting value.

# Generate:

# 1. 10 random integers
# 2. 5 random decimal values
# 3. 5 normally distributed values

# Reset the same starting value.

# Generate everything again.

# Check whether all three results are identical.


# Q29. Employee Sampling
# Given:

# employees = np.arange(1, 101)

# Randomly select 10 employees from the 100 employees.

# No employee should be selected more than once.

# Print the selected employee IDs.


# Q30. MINI PROJECT — RANDOM SALES SIMULATION 🔥
# ----------------------------------------------

# Create a random sales dataset for:

# 12 months
# 5 products

# Generate realistic random sales data.

# Then calculate:

# 1. Total Sales
# 2. Average Sales
# 3. Highest Sales
# 4. Lowest Sales
# 5. Best Performing Product
# 6. Worst Performing Product
# 7. Best Performing Month
# 8. Worst Performing Month

# Also make the result reproducible so that running the program again produces the same dataset.