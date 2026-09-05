# ============================================================
# DAY 12: MISSING VALUES + SPECIAL VALUES
# Practice Questions — Basic to Advanced
# ============================================================

import numpy as np


# =========================
# REQUIRED ARRAYS
# =========================

data = np.array([100, 200, np.nan, 400, 500, np.inf, 700, np.nan, 900, -np.inf])

sales = np.array([
    [100, 200, np.nan, 400],
    [500, np.inf, 700, 800],
    [np.nan, 1000, 1100, -np.inf]
])

marks = np.array([85, 90, np.nan, 72, 68, np.nan, 95, 80, np.inf, 88])

profit = np.array([
    [100, 200, 300],
    [np.nan, 500, 600],
    [700, np.inf, 900]
])


# ============================================================
# BASIC QUESTIONS — Q1 to Q7
# ============================================================

# Q1. From 'data', check which values are NaN.
import numpy as np

data = np.array([100, 200, np.nan, 400, 500, np.inf, 700, np.nan, 900, -np.inf])
print(np.isnan(data))

# Q2. From 'data', check which values are Infinity.
print(np.isinf(data))

# Q3. From 'data', check which values are finite.
print(np.isfinite(data))

# Q4. Find and print only the NaN values from 'data'.
print(data[np.isnan(data)])

# Q5. Find and print only the Infinity values from 'data'.
infinite = data[np.isinf(data)]
print(infinite)

# Q6. Count how many NaN values are present in 'data'.
countt = np.sum(np.isnan(data))
print(countt)

# Q7. Count how many Infinity values are present in 'data'.
inf = np.sum(np.isinf(data))
print(inf)


# ============================================================
# INTERMEDIATE QUESTIONS — Q8 to Q14
# ============================================================


marks = np.array([85, 90, np.nan, 72, 68, np.nan, 95, 80, 88])
# Q8. Find the mean of 'marks' while ignoring NaN.
print("Mean:",np.nanmean(marks))

# Q9. Find the total of 'marks' while ignoring NaN.
print("Total:",np.nansum(marks))

# Q10. Find the minimum value in 'marks' while ignoring NaN.
print("Min_Value:",np.nanmin(marks))

# Q11. Find the maximum value in 'marks' while ignoring NaN.
print("Max_Value:",np.nanmax(marks))

# Q12. Find the average sales from 'sales' while ignoring NaN.
print("Average:",np.nanmean(sales))

# Q13. Find the total sales from 'sales' while ignoring NaN.
print("Total Sales:",np.nansum(sales))

# Q14. Find the minimum and maximum sales from 'sales'
#      while ignoring NaN.
print("Max:",np.nanmax(sales))
print("Min:",np.nanmin(sales))

# ============================================================
# ADVANCED QUESTIONS — Q15 to Q20
# ============================================================

# Q15. Find the positions (indexes) of all NaN values in 'data'.
data = np.array([100, 200, np.nan, 400, 500, np.inf, 700, np.nan, 900, -np.inf])
nan_Position=  np.where(np.isnan(data))
print(nan_Position)

# Q16. Find the positions of all Infinity values in 'data'.
print(np.where(np.isinf(data)))

# Q17. Using 'sales', find the positions (row, column)
#      where NaN values exist.
sales = np.array([
    [100, 200, np.nan, 400],
    [500, np.inf, 700, 800],
    [np.nan, 1000, 1100, -np.inf]
])
print(np.where(np.isnan(sales)))

# Q18. Using 'profit', find the positions (row, column)
#      where Infinity values exist.
profit = np.array([
    [100, 200, 300],
    [np.nan, 500, 600],
    [700, np.inf, 900]
])
print(np.where(np.isinf(profit)))

# Q19. Using 'sales', calculate the mean of only finite values.
#      Do not include NaN or Infinity.
sales = np.array([
    [100, 200, np.nan, 400],
    [500, np.inf, 700, 800],
    [np.nan, 1000, 1100, -np.inf]
])
value=sales[np.isfinite(sales)]
print("value:",value)
mean = np.mean(value)
print("Mean:", mean)

# Q20. FINAL CHALLENGE 🔥
#
# Using 'profit':
#
profit = np.array([
    [100, 200, 300],
    [np.nan, 500, 600],
    [700, np.inf, 900]
])
# 1. Find all NaN values.uy
print(np.isnan(profit))
# 2. Find all Infinity values.
print(np.isinf(profit))
# 3. Count total NaN values. 
print(np.sum(np.isnan(profit)))

# 4. Count total Infinity values.
print(np.sum(np.isinf(profit)))
# 5. Find the minimum finite value.
finite_value = profit[np.isfinite(profit)]
print("Min:",np.min(finite_value))
# 6. Find the maximum finite value.
print("Max:",np.max(finite_value))
# 7. Calculate the mean of finite values.
print("Mean:",np.mean(finite_value))
# Rule:
# NaN, +Infinity and -Infinity should NOT be included
# in the finite-value calculations.