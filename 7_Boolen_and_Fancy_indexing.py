# ============================================================
# LEVEL 1 — BASIC BOOLEAN INDEXING
# ============================================================

import numpy as np
# 1. Create a NumPy array:
'''arr =np.array([10, 20, 30, 40, 50])
#    Print all values greater than 30.
value = arr > 30
print(value)
print(arr[value])'''

# 2. Create an array:
'''arr =np.array([5, 12, 18, 25, 32, 40])
#    Print all values less than 20.
value = arr < 20
print(arr[value])'''

# 3. Create an array:
'''arr = np.array([10, 20, 30, 40, 50])

#    Print all values greater than or equal to 30.
value = arr >= 30 
print(arr[value])'''

# 4. Create an array:
'''arr = np.array([10, 15, 20, 25, 30, 35])
#    Print all even numbers.
value = arr % 2 == 0
print(arr[value])'''

# 5. Create an array:
'''arr = np.array([10, 15, 20, 25, 30, 35])
#    Print all odd numbers.
value = arr % 2 != 0
print(arr[value])'''


# 6. Create an array:
arr= np.array([5, 10, 15, 20, 25, 30])
#    Print all values that are equal to 20.

# 7. Create an array:
#    [10, 20, 30, 40, 50]

#    Print all values that are NOT equal to 30.


# ============================================================6
# LEVEL 2 — BOOLEAN FILTERING
# ============================================================

# 8. Create:
'''marks = np.array([35, 45, 67, 78, 89, 32, 91])
#    Print all marks greater than or equal to 50.
value = marks >= 50
print(marks[value])

# 9. Using the same marks array, print all marks between
#    40 and 80.
con = (marks >= 40) & (marks <= 80)
print(marks[con])

# 10. Create:
salary = np.array([25000, 35000, 45000, 55000, 65000, 80000])

#     Print salaries greater than 50000.
print(salary[salary >50000])

# 11. Using the salary array, print salaries between
#     30000 and 60000.
print(salary[(salary >= 30000) & (salary <= 60000)])

# 12. Create:
sales = np.array([100, 250, 400, 150, 600, 750, 300])
#     Print sales values greater than 300.
print(sales[sales >300])

# 13. Using the sales array, print values less than or equal to 300.
print(sales[sales <= 300])

# 14. Create:
temperatures = np.array([15, 22, 30, 18, 35, 25, 40])
#     Print temperatures greater than 25.
print(temperatures[temperatures >25])'''

# ============================================================
# LEVEL 3 — MULTIPLE CONDITIONS
# ============================================================

# 15. Create:
'''arr = np.array([10, 20, 30, 40, 50, 60, 70])
#     Print values greater than 20 AND less than 60.
value = (arr > 20) & (arr < 60)
print(arr[value])

# 16. Create:
marks = np.array([35, 45, 55, 65, 75, 85, 95])
#     Print marks less than 50 OR greater than 80.
print(marks[(marks < 50) | (marks > 80)])

# 17. Create:
salary = np.array([20000, 30000, 40000, 50000, 80000, 70000])
#     Print salaries greater than 30000 AND less than 70000.

print(salary[(salary > 30000) & (salary < 70000)])

# 18. Create:
sales = np.array([100, 200, 300, 400, 500, 600])
#     Print values less than 200 OR greater than 500.
print(sales[(sales < 200) | (sales > 500)])

# 19. Create:
arr = np.array([5, 10, 15, 20, 25, 30, 35])
#     Print values that are NOT greater than 20.
print(arr[~(arr < 20)])'''

# 20. Create:
'''marks = np.array([30, 45, 55, 65, 75, 85, 95])
#     Print marks that are:

#     - greater than 40
#     - AND less than 90
#     - AND not equal to 65
print(marks[(marks > 40) & (marks < 90) & (marks != 65)])'''


# ============================================================
# LEVEL 4 — FANCY INDEXING
# ============================================================

# 21. Create:
'''arr = np.array([10, 20, 30, 40, 50, 60])

#     Using fancy indexing, print elements at indexes:
#     0, 2, and 5.
print(arr[[0,2,5]])'''

# 22. Using the same array, print elements at indexes:
#     1, 3, and 4.
'''print(arr[[1,3,4]])

# 23. Create:
arr = np.array([100, 200, 300, 400, 500, 600, 700])
#     Using fancy indexing, print elements at indexes:
#     6, 3, and 0.
print(arr[[6,3,0]])

# 24. Create the following 2D array:
arr = np.array([
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90],
        [100, 110, 120]
    ])
#     Select rows 0, 2, and 3 using fancy indexing.
print(arr[[0,2,3]])

# 25. Using the same 2D array, select columns 0 and 2.
print(arr[:,[0,2]])

# 26. Using the same 2D array, select rows 1 and 3.
print(arr[[1,3]])

# 27. Using the same 2D array, select columns 1 and 2.
print(arr[:,[1,2]])'''

# ============================================================
# LEVEL 5 — ADVANCED / DATA ANALYTICS
# ============================================================

# 28. Create:

sales = np.array([
        [100, 200, 300],
        [150, 250, 350],
        [200, 300, 400],
        [250, 350, 450]
    ])
#     Using fancy indexing:
#     - Select rows 0 and 3.
print(sales[[0,3]])
#     - Select columns 0 and 2.
print(sales[:,[0,2]])

# 29. Create:

marks = np.array([
        [45, 67, 89, 76],
        [55, 72, 91, 60],
        [35, 48, 70, 82],
        [90, 88, 95, 92]
    ])
 
#     Using Boolean indexing:
#     - Find all marks greater than 80.
print("G.T",marks[marks >= 80])
#     - Find all marks between 50 and 90.
print(marks[(marks >= 50) & (marks <= 90)])

# 30. FINAL MASTER CHALLENGE

#     Create:

sales = np.array([
        [120, 250, 180, 400],
        [300, 150, 500, 220],
        [450, 350, 200, 600],
        [100, 700, 320, 250],
        [550, 280, 450, 800]
    ])
#     Perform the following:

#     a. Find all sales values greater than 400.
print(sales[sales > 400])
#     b. Find all sales values between 200 and 600.
print(sales[(sales >= 200) & (sales <= 600)])

#     c. Find all sales values less than 200 OR greater than 700.
print(sales[(sales < 200) | (sales > 700)])
#     d. Select rows 0, 2, and 4 using fancy indexing.
print(sales[[0,2,4]])
#     e. Select columns 1 and 3 using fancy indexing.
print(sales[:,[1,3]])
#     f. Select rows 1 and 3 AND columns 0 and 2.
print(sales[[1,3],[0,2]])
print(sales[np.ix_([1,3], [0,2])])

#     g. Find all values greater than the average sales value.
avg = sales.mean()
print(sales[sales > avg])
#     h. Find all values that are NOT greater than 300.
print(sales[~(sales > 300)])