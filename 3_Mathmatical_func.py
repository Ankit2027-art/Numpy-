# NUMPY MATHEMATICAL FUNCTIONS
# 20 PRACTICE QUESTIONS
# BASIC → ADVANCED
# ============================================

# Use NumPy for all questions.

import numpy as np
# LEVEL 1 — BASIC
# ============================================

# 1. A dataset contains the following values:
a = np.array( [4, 9, 16, 25, 36] )
#    Calculate the mathematical square-root transformation
#    for every value.
print(np.sqrt(a))

# 2. A dataset contains:
a=np.array([2, 4, 6, 8, 10])

#    Calculate the square of every value.
print("Square:",np.square(a))

# 3. A company's monthly profit changes are:
a =np.array([-500, 200, -150, 800, -300])

#    Convert all values into their corresponding absolute values.
print(np.abs(a))

# 4. A dataset contains:
aa= np.array([2, 3, 4, 5])

#    Calculate the third power of every value.
print(np.power(aa,3))

# 5. Calculate the exponential transformation of:
#    [0, 1, 2, 3].
print(np.exp(aa))

# LEVEL 2 — LOGARITHMIC & ROUNDING
# ============================================

# 6. A dataset contains:
aa = np.array([1, 10, 100, 1000, 10000])
#    Calculate the logarithmic transformation commonly used
#    for base-10 scaled data.
print(np.log10(aa))


# 7. A dataset contains:
a =np.array( [1, 2.7182818, 7.389056])

#    Calculate their natural logarithmic values.
print(np.log(a))

# 8. A sensor produces the following measurements:
a =np.array( [12.34, 15.67, 18.92, 21.45, 25.89])

#    Round each value to the nearest integer.
print(np.round(a))

# 9. A company records delivery times:
a = np.array([2.1, 3.4, 4.8, 5.2, 6.9])

#    Find the next integer value for each measurement.
print(np.ceil(a))

# 10. A dataset contains:
a= np.array([2.9, 3.8, 4.1, 5.7, 6.2])

#     Find the previous integer value for each measurement.
print(np.floor(a))

# LEVEL 3 — DATA ANALYTICS
# ============================================

# 11. A company records the following profit/loss values:

profit = np.array([-1200, 800, -450, 1500, -300, 2200])
#     Perform an absolute-value transformation on the dataset.
print(np.abs(profit))

# 12. A dataset contains monthly sales:

sales = np.array([100, 400, 900, 1600, 2500])

#     Apply a square-root transformation to reduce the scale
#     of the values.
print(np.sqrt(sales))

# 13. A dataset contains customer transaction amounts:

transactions = np.array([10, 100, 1000, 10000, 100000])

#     Apply a logarithmic transformation suitable for
#     highly skewed financial data.
print(np.log10(transactions))

# 14. A machine-learning dataset contains:

values = np.array([2, 4, 8, 16, 32])

#     Calculate the exponential transformation of each value.
print(np.exp(values))

# 15. A dataset contains:

scores = np.array([45.67, 78.23, 91.89, 66.45, 82.51])

#     Create a version of the dataset where every value is
#     rounded to the nearest integer.
print(np.round(scores))

# LEVEL 4 — MIXED ANALYTICAL PROBLEMS
# ============================================

# 16. A company's profit data is:

profit = np.array([-450.7, 820.4, -120.9, 1500.8, -300.5])

#     Perform the following transformations:

#     a. Convert all values to positive magnitudes.
print("Postive:",np.abs(profit))
#     b. Calculate the square of each magnitude.
print("Square:",np.square(profit))
#     c. Calculate the square root of each magnitude.
print("Square root:",np.sqrt(profit))

# 17. A dataset contains:

data = np.array([1.25, 2.49, 3.51, 4.99, 5.01])

#     Create three transformed versions:

#     a. Nearest integer values
print(np.round(data))
#     b. Values rounded upward
print(np.ceil(data))
#     c. Values rounded downward
print(np.floor(data))


# 18. A sales dataset contains:

sales = np.array([100, 250, 500, 1000, 2500, 5000])

#     Perform:

#     a. Square-root transformation
print(np.sqrt(sales))
#     b. Square transformation
print("Square",np.square(sales))
#     c. Base-10 logarithmic transformation
print(np.log10(sales))

# Compare the resulting scales.


# LEVEL 5 — ADVANCED DATA ANALYTICS
# ============================================

# 19. A dataset contains:

data = np.array([
        [-4.5, 9.2, -16.7],
        [25.4, -36.8, 49.9]
    ])

#     Create transformed versions of this dataset:

#     a. Absolute values
absulte = np.abs(data)
print(absulte)

#     b. Squared values
square = np.square(absulte)
print(square)

#     c. Square-root values of the absolute data
sqrt = np.sqrt(absulte)

#     d. Rounded values
print(np.round(absulte))
#     e. Values rounded upward
print(np.ceil(absulte))
#     f. Values rounded downward
print(np.floor(absulte))


# 20. FINAL MASTER QUESTION

#     A data analyst receives the following transaction dataset:

transactions = np.array([
        [-125.6, 250.4, 625.8],
        [1000.2, -2500.7, 5000.9],
        [10000.5, -25000.3, 50000.8]
    ])

#     Perform the following analytical transformations:

#     a. Convert negative transaction values into their
#        positive magnitudes.
abs = np.abs(transactions)
print(abs)
#     b. Calculate the square of every magnitude.
print(np.square(abs))

#     c. Calculate the square-root transformation of the
#        magnitudes.
print(np.sqrt(abs))

#     d. Apply a base-10 logarithmic transformation to
#        appropriate positive values.
print(np.log10(abs))
#     e. Round the original transaction values to the
#        nearest integer.
print(np.round(abs))
#     f. Create an upward-rounded version.
print(np.ceil(abs))
#     g. Create a downward-rounded version.
print(np.floor(abs))
#     h. Apply an exponential transformation to a separate
#        array containing [0, 1, 2].
print(np.exp([0,1,2]))