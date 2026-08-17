# NUMPY INDEXING & SLICING
# 30 PRACTICE QUESTIONS
# BASIC → ADVANCED
# ================================

# Use: 
import numpy as np


# LEVEL 1 — BASIC INDEXING
# ================================

# 1. Create a NumPy array:
a =   np.array([10, 20, 30, 40, 50])
print(a)
#    Print the element at index 2.
'''print(a[1])'''

# 2. Using negative indexing, print the last element and second-last
#    element of the array.
'''print(a[-1])
print(a[-2])'''

# 3. Create an array from 1 to 10 and print the first element,
#    last element, and middle element using indexing.
a = np.arange(1,11)
'''print(a)
print(a[0])
print(a[-1])
print(a[4])'''

# 4. Create the following 2D array:

a = np.array( [[10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]])

'''#    Print:
print(a)
#    a. 10
print(a[0,0])

#    b. 60
print(a[1,2])
#    c. 80
print(a[2,1])'''

# 5. Using the same 2D array, print the last element using
#    negatiove indexing.
print(a[-1,-1])

# LEVEL 2 — BASIC SLICING
# ================================

# 6. Create an array:
a=np.array( [10, 20, 30, 40, 50, 60])

'''#    Print elements from index 1 to 4.
print(a[1:4])'''
# 7. Print the first 3 elements using slicing.

# 8. Print the last 3 elements using slicing.
'''print(a[-3:])'''
# 9. Print all elements except the first element.
'''print(a[1:])
# 10. Print all elements except the last element.
print(a[:-1])'''

# LEVEL 3 — START, STOP & STEP
# ================================

# 11. Create an array from 1 to 10 and print every second element.
'''arr = np.arange(1,11)
print(arr)
print(arr[1:11:2])'''

'''# 12. Create an array from 1 to 20 and print every third element.
arr = np.arange(1,21)
print(arr[1:20:3])

# 13. From:
a = np.array([10, 20, 30, 40, 50, 60, 70])
#     Print elements from index 1 to 6 with step 2.
print(a[1:6:2])

# 14. Reverse the complete array using slicing.
print(a[::-1])
# 15. Print every second element in reverse order.
print(a[: :-2])

# LEVEL 4 — NEGATIVE SLICING
# ================================

# 16. Create an array from 1 to 10.
a = np.arange(1,11)
print(a)
# Using negative slicing, print the last 4 elements.
print(a[-4:])
# 17. Using negative slicing, print all elements except the last
#     two elements.
print(a[:-2])
# 18. Using negative slicing, print the array in reverse order.

# 19. Print the last 5 elements in reverse order.'''


# LEVEL 5 — 2D ROW & COLUMN SLICING
# ================================

# 20. Given:

arr = np.array([
        [10, 20, 30, 40],
        [50, 60, 70, 80],
        [90, 100, 110, 120]
    ])

'''#     Print the first row.
print(arr[0,])
# 21. Print the last row.
print(arr[2,])
# 22. Print the first two rows.
print(arr[0:2])
# 23. Print the first column.
print(arr[:,0])
# 24. Print the last column.
print(arr[:,3])
# 25. Print the first two columns.
print(arr[:,:2])'''

# LEVEL 6 — 2D SLICING
# ================================
arr = np.array([
        [10, 20, 30, 40],
        [50, 60, 70, 80],
        [90, 100, 110, 120],
        [130, 140, 150, 160]
    ])

# 26. Using the same 2D array, select:

'''#     First 2 rows
#     First 2 columns
print(arr[0:2])
print(arr[:,0:2])
# 27. Select the last 2 rows and last 2 columns.
print(arr[-2:])
print(arr[:,-2:])
# 28. Select every second row.
print(arr[::2])
# 29. Select every second column.
print(arr[:,::2])'''
# 30. FINAL CHALLENGE:

#     Create a 5 × 5 NumPy array containing numbers from 1 to 25.
'''arr = np.arange(1,26).reshape(5,5)
print(arr)
#     Using ONLY indexing and slicing, find:
#     a. First row
print(arr[0])
#     b. Last column
print(arr[:,-1])
#     c. First 2 rows
print(arr[0:2])
#     d. Last 2 columns
print(arr[:,-2:])
#     e. Center 3 × 3 matrix
print(arr[1:4,1:4])
#     f. Alternate rows
print(arr[::2])
#     g. Alternate columns
print(arr[:,::2])
#     h. Reverse the complete matrix
print(arr[::-1])'''