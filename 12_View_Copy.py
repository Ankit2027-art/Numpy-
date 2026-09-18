# VIEW
# → Looks at the same underlying data
# → Memory can be shared
# → Changes may affect the original
# → arr.view()

# COPY
# → Creates separate data
# → Memory is not shared with the original
# → Changes don't affect the original
# → arr.copy()

# np.shares_memory()
# → Checks whether two arrays share memory
# → True  = Memory shared
# → False = Memory not shared


# DAY 14 — COPY VS VIEW
# PRACTICE QUESTIONS
# ==================

# LEVEL 1 — BASIC
# ----------------
import numpy as np
# Q1. Create an array:

'''arr = np.array([10, 20, 30, 40, 50])

# Create another array that looks at the same underlying data.
new_array = arr.view()
# Change the first element of the new array to 100.
new_array[0] = 100
# Print both arrays and observe the result.
print(arr)
print(new_array)'''

# Q2. Create an array:

'''arr = np.array([10, 20, 30, 40, 50])

# Create a completely independent duplicate of this array.
new_array = arr.copy()
# Change the first element of the new array to 100.
new_array[0] = 100
# Print both arrays.
print(arr)
print(new_array)
# Check whether the original array changed.
print(np.shares_memory(arr,new_array))'''

# Q3. Given:

arr = np.array([1, 2, 3, 4, 5])

# Create another array from arr.
new_arr = arr.view()
# Change the third element of the new array to 99.
new_arr[2] = 99
# Check whether arr is also changed.
print(arr)
print(new_arr)

# Q4. Given:

arr = np.array([5, 10, 15, 20])

# Create an independent array from arr.
ind_array =arr.copy()
# Change the last element of the new array to 100.
ind_array[-1] = 100
# Print both arrays.
print(arr)
print(ind_array)

# Q5. Given:

arr = np.array([10, 20, 30])

# Create two arrays:

# a → should share data with arr
a = arr.view()
# b → should have separate data from arr
b = arr.copy()
# Change a and b separately.
a[0] = 100
b[0] = 50
# Observe the effect on arr.
print(a)
print(b)
print(arr)

# LEVEL 2 — MEMORY
# ----------------

# Q6. Given:

arr = np.array([10, 20, 30, 40])

# Create another array that shares memory with arr.
new_arr = arr.view()
# Check whether both arrays share memory.
print(arr)
print(new_arr)
# The expected result should be True.
print(np.shares_memory(arr,new_arr))

# Q7. Given:

arr = np.array([10, 20, 30, 40])

# Create another completely independent array.
ind_array = arr.copy()
# Check whether the two arrays share memory.
print(np.shares_memory(arr,ind_array))
# The expected result should be False.


# Q8. Create:

arr = np.array([1, 2, 3, 4, 5])

# Create:

view_arr = arr.view()

copy_arr = arr.copy()

# Check the memory relationship of:

# 1. arr and view_arr
# 2. arr and copy_arr

# Print both results.
print(np.shares_memory(arr,view_arr))
print(np.shares_memory(arr,copy_arr))

# Q9. Given:

arr = np.array([10, 20, 30])

# Create another array that shares the same underlying data.
Shares_arr = arr.view()
# Change the second element through the new array.
new_array = arr.copy()
# Then print:

# 1. Original array
print(arr)
# 2. New array
print(new_arr)
# 3. Whether they share memory
print(np.shares_memory(arr,Shares_arr))
print(np.shares_memory(arr,new_arr))


# Q10. Given:

arr = np.array([100, 200, 300])

# Create an independent duplicate.
duplicate = arr.copy()
# Change the second element of the duplicate.
duplicate[1] = 100 
# Then print:

# 1. Original array
print(arr)
# 2. Duplicate array
print(duplicate)
# 3. Whether they share memory
print(np.shares_memory(arr,duplicate))

# LEVEL 3 — THINKING QUESTIONS
# ----------------------------

# Q11. Predict the output before running the code:

arr = np.array([10, 20, 30])

new_arr = arr.view()

new_arr[0] = 500

print(arr)
print(new_arr)

# Then explain why.
'''Output = 
[500 20 30]
[500 20 30] 

Outputs are same because stoarge location are same
     '''

# Q12. Predict the output:

arr = np.array([10, 20, 30])

new_arr = arr.copy()

new_arr[0] = 500

print(arr)
print(new_arr)

# Explain why the original array does or does not change.
'''Beacause copy( function create a diffrent memory loaction so dont affect the origonal array)'''

# Q13. What will happen here?
import numpy as np
arr = np.array([1, 2, 3])

a = arr
b = arr.copy()

a[0] = 100
b[1] = 200

print(arr)
print(a)
print(b)

# Explain which changes affect the original and why.
'''when i change the value of a then automatically change thee value of arr because we are assign a = arr , and when i change in b then c they dont effect the origional aaray becaose we create a copy of origoanl aaray'''

# Q14. What will happen here?

arr = np.array([10, 20, 30, 40])

a = arr.view()
b = arr.copy()

a[1] = 200
b[2] = 300

# Print all three arrays.
print(arr)
print(a)
print(b)
# Explain the result.
''' when i chnage in a arays then the origonal array also changes because it share same memory it is way to looking at the same underlaying
 and b is  copletely separete array  so they dont effect origonal aar  copy crate another storage location'''

# Q15. Given:

# arr = np.array([10, 20, 30, 40, 50])

# Create three variables:

# a
# b
# c

# Requirements:

# a → same array/reference
# b → view of arr
# c → independent copy

# Then check memory sharing between:

# 1. arr and a
# 2. arr and b
# 3. arr and c


# LEVEL 4 — REAL-WORLD STYLE
# --------------------------

# Q16. Sales Data

# sales = np.array([1000, 2000, 3000, 4000, 5000])

# You want to create a temporary version of the sales data.

# Modify the temporary version without changing the original sales data.

# Print both arrays.

# Which approach did you use and why?


# Q17. Data Analysis

# marks = np.array([75, 82, 90, 65, 88])

# Create another array for experimentation.

# Change the marks of the first student to 100.

# The original marks must remain unchanged.

# Print both arrays.


# Q18. Large Dataset

# data = np.array([10, 20, 30, 40, 50])

# You want another array that can reflect changes made to the original data.

# Create it and test the behavior.

# Change the original array and observe the second array.


# Q19. Memory Investigation

# Given:

# arr = np.array([10, 20, 30, 40])

# Create:

# a
# b
# c

# where each one is created using a different approach.

# Check which ones share memory with arr.

# Print the results and identify the difference.


# Q20. FINAL CHALLENGE 🔥

# Given:

# data = np.array([100, 200, 300, 400, 500])

# Create:

# original
# view_data
# copy_data

# Perform these operations:

# 1. Change the first value of view_data to 999.
# 2. Change the second value of copy_data to 888.
# 3. Change the third value of original to 777.

# Finally print all three arrays.

# Also check the memory relationship between:

# original & view_data
# original & copy_data
# view_data & copy_data

# Explain why each array contains the values it contains.