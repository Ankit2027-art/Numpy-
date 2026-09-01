# ============================================================
# LEVEL 1 — BASIC
# ============================================================
import numpy as np

# 1. Create a NumPy array:
arr = np.array([10, 20, 30, 40, 50])

# Find the positions of all values greater than 25.
'''print(np.where(arr > 25))'''

# 2. Create:
arr = np.array([5, 10, 15, 20, 25, 30])
#    Find the positions of all values less than 20.
'''print("Position:",np.where(arr < 20))
print("Value:",arr[np.where(arr < 20)])'''

# 3. Create:
arr = np.array([10, 0, 20, 0, 30, 40, 0])
#    Find the positions of all non-zero values.
'''print(np.nonzero(arr))'''

# 4. Create:
'''arr = np.array([0, 15, 0, 25, 35, 0, 45])
#    Find the positions of all zero values.
print(np.where(arr == 0))'''

# 5. Create:
arr = np.array([50, 20, 80, 10, 60, 30])
#    Find the position of the maximum value.
'''print(np.argmax(arr))

# 6. Using the same array, find the position of the minimum value.
print(np.argmin(arr))'''

# 7. Create:
'''arr = np.array([40, 10, 70, 20, 90, 30])
#    Sort the values in ascending order.
print("ASC:",np.sort(arr))
print("DESC:",np.sort(arr)[::-1])

# 8. Using the same array, find the order of indexes that would
#    arrange the values in ascending order.
print(np.argsort(arr))'''

# ============================================================
# LEVEL 2 — SEARCHING & SORTING
# ============================================================

# 9. Create:
marks = np.array([45, 67, 32, 89, 76, 91, 55])
#    Find the positions of students who scored more than 70.
print(np.where(marks > 70))

# 10. Using the same marks array, find the positions of students
#     who scored between 50 and 80.
print(np.where((marks > 50) & (marks < 80)))

# 11. Create:
sales = np.array([1200, 800, 1500, 600, 2000, 950])
#     Find the positions where sales are greater than 1000.
print(np.where(sales > 1000))

# 12. Using the same sales array, find the position of the
#     highest sales value.
print(np.argmax(sales))

# 13. Find the position of the lowest sales value.

print(np.argmin(sales))

# 14. Sort the sales values from lowest to highest.
print(np.sort(sales))

# 15. Find the index order required to arrange the sales from
#     highest to lowest.
sales = np.array([1200, 800, 1500, 600, 2000, 950])
print(np.argsort(sales)[::-1])

# print(np.argsort(sort))

# 16. Create:
salary = np.array([35000, 55000, 25000, 75000, 45000, 90000])
#     Find the positions of employees whose salary is greater
#     than 50000.
print(np.where(salary > 50000))

# 17. Sort the salary values in ascending order.
print(np.sort(salary))

# 18. Find the position of the employee with the highest salary.
print(np.argmax(salary))

# ============================================================
# LEVEL 3 — 2D ARRAYS
# ============================================================

# 19. Create:
data = np.array([
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ])

#     Find the positions of all values greater than 50.
print(np.argwhere(data >50))

# 20. Using the same array, find the positions of all values
#     less than 40.
print(np.argwhere(data < 40))

# 21. Create:

data = np.array([
        [0, 10, 20],
        [30, 0, 40],
        [50, 60, 0]
    ])

#     Find the positions of all non-zero elements.
print(np.nonzero(data))

# 22. Create:
import numpy as np
marks = np.array([
        [45, 67, 89],
        [55, 32, 91],
        [78, 88, 60]
    ])

#     Find the positions of all marks greater than 80.
print(np.argwhere(marks > 80))

# 23. Using the same marks array, find the position of the
#     highest mark.

max_value = np.max(marks)
print("Max:",np.argwhere(marks == max_value))

# 24. Find the position of the lowest mark.
Min_value = np.min(marks)
print("Min:",np.argwhere(marks == Min_value))

# 25. Sort every row of the following array:

data = np.array([
        [30, 10, 20],
        [60, 40, 50],
        [90, 70, 80]
    ])

print(np.sort(data))
# ============================================================
# LEVEL 4 — DATA ANALYTICS
# ============================================================

# 26. An IPL team records runs scored by players:

runs = np.array([45, 78, 102, 34, 89, 12, 67, 95])

#     Perform the following:

#     a. Find the highest score.
max_value = np.max(runs)
print("Highest Run:",max_value)
#     b. Find the lowest score.
Min_value = np.min(runs)
print("Lowest Run:",Min_value)
#     c. Find the position of the highest score.
print("Position of Highest Run:",np.where(runs == max))
#     d. Find the position of the lowest score.
print("Position of Lowest Run:",np.where(runs == min))
#     e. Find the positions of players who scored more than 70.
print(np.where(runs > 70))

# 27. A company records monthly sales:

sales = np.array([
        120000, 95000, 150000, 80000,
        175000, 110000, 200000, 130000
    ])
#     Perform the following:

#     a. Find the highest monthly sales.
max_value = np.max(sales)
print("Highest Monthly Sales:",max_value)
#     b. Find the lowest monthly sales.
Min_value = np.min(sales)
print("Lowest Monthly Sales:",Min_value)
#     c. Find the position of the highest sales.
print(np.argwhere(sales == max_value))
#     d. Sort the sales values in ascending order.
print(np.sort(sales))
#     e. Find the order of indexes for the sales from highest
#        to lowest.
print(np.argsort(sales)[::-1])

# 28. A company records employee salaries:

salary = np.array([
        28000, 45000, 62000, 35000,
        75000, 52000, 90000, 40000
    ])

#     Perform the following:

#     a. Find the positions of employees earning more than 50000.
print(np.where(salary > 50000))
#     b. Find the positions of employees earning less than 40000.
print(np.where(salary < 40000))
#     c. Find the highest salary.
max_value =np.max(salary)
print("Maximum Salary:",max_value)
#     d. Find the lowest salary.
print("Lowest Salary:",np.min(salary))
#     e. Find the position of the highest salary.
print(np.where(salary == max_value))

# ============================================================
# LEVEL 5 — ADVANCED
# ============================================================

# 29. An IPL team records runs scored by players in 3 matches:
runs = np.array([
        [45, 78, 102, 34],
        [67, 89, 23, 110],
        [56, 95, 76, 42]
    ])

#     Perform the following:

#     a. Find all positions where runs are greater than 80.
print(np.where(runs > 80))
#     b. Find all positions where runs are less than 50.
print(np.where(runs < 50))
#     c. Find the position of the highest run.
max_value =np.max(runs)
print(np.where(runs == max_value))
#     d. Find the position of the lowest run.
Min_value =np.min(runs)
print(np.where(runs == Min_value))
#     e. Sort the values in each row.
print(np.sort(runs))

# 30. FINAL MASTER CHALLENGE

#     A company has the following monthly sales data:

sales = np.array([
        [120, 450, 230, 600],
        [300, 150, 700, 250],
        [500, 350, 180, 800],
        [220, 650, 400, 100],
        [750, 280, 550, 320]
    ])

#     Perform the following:

#     a. Find all positions where sales are greater than 500.

print(np.argwhere(sales > 500))
#     b. Find all positions where sales are less than 200.
print(np.argwhere(sales < 200))
#     c. Find all non-zero positions.

print("Non Zero Position:",np.nonzero(sales))

#     d. Find the highest sales value.
max_value =np.max(sales)
print("Highest Sales:",max_value)

#     e. Find the lowest sales value.
Min_value =np.min(sales)
print("Lowest:",Min_value)

#     f. Find the position of the highest sales value.
print(np.argwhere(sales == max_value))

#     g. Find the position of the lowest sales value.
print(np.argwhere(sales == Min_value))

#     h. Sort every row in ascending order.
print(np.sort(sales,axis =1))

# #     i. Find the index order of the values in each row.
print(np.argsort(sales,axis=1))
# #     j. Arrange all sales values into ascending order.
print(np.sort(sales,axis = None))
# #     k. Arrange all sales values into descending order.
print(np.sort(sales,axis = None)[::-1])
# #     l. Find the positions of sales values between 250 and 600.
print(np.argwhere((sales >250)&(sales<600)))
