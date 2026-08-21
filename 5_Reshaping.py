# Use NumPy for all questions.
import numpy as np


# ============================================================
# LEVEL 1 — BASIC
# ============================================================

# 1. Create a NumPy array containing numbers from 1 to 12.
#    Reshape it into a 3 × 4 array.
'''arr = np.arange(1,13)
print(arr.reshape(3,4))'''

# 2. Create an array containing numbers from 1 to 20.
#    Reshape it into a 4 × 5 array.
'''arr = np.arange(1,21)
print(arr.reshape(4,5))'''

# 3. Create a 3 × 4 array containing numbers from 1 to 12.
#    Reshape it into a 2 × 6 array.
'''arr = np.arange(1,13).reshape(3,4)
print(arr)
print(arr.reshape(2,6))'''

# 4. Create a 2 × 3 array:
#
'''arr =np.array([[10, 20, 30],
    [40, 50, 60]])'''
#
#    Convert it into a 1D array using flatten().

'''print("Flatten:",arr.flatten())'''

# 5. Using the same array, convert it into a 1D array
#    using ravel().
'''print(arr.ravel())'''

# 6. Create the following 2D array:
#
#    [[1, 2, 3],
#     [4, 5, 6]]
#
#    Transpose the array using transpose().
'''print("Transpose:",arr.transpose())'''

# 7. Transpose the following array using .T:
#
'''arr= np.array([[10, 20],
    [30, 40],
    [50, 60]])
print(arr.T)'''

# ============================================================
# LEVEL 2 — RESHAPING + DIMENSIONS
# ============================================================

# 8. Create an array from 1 to 24.
#    Reshape it into:
'''arr = np.arange(1,25)
#    a. 4 × 6
print(arr.reshape(4,6))
#    b. 6 × 4
print(arr.reshape(6,4))
#    c. 2 × 12
print(arr.reshape(2,12))'''


# 9. Create a 3 × 4 array containing numbers from 1 to 12.
'''arr = np.arange(1,13).reshape(3,4)
print(arr)
#    Flatten it and verify its shape.
b = arr.flatten()
print(b)'''

# 10. Create a 2 × 5 array containing numbers from 1 to 10.
'''arr = np.arange(1,11).reshape(2,5)
#     Convert it into 1D using ravel()
reshape = arr.flatten()
#     and verify its shape.
print(reshape)'''

# 11. Create the following array:
#
'''arr = np.array([[1, 2, 3],
     [4, 5, 6]])
#     Find its:
#     a. Original shape
print(arr.shape)
#     b. Transposed shape
transpose = arr.T
print(transpose.shape)'''

# 12. Create an array:
#
'''arr= np.array([[10, 20, 30, 40]])
#     Remove the unnecessary dimension using squeeze().
re = arr.squeeze()
print(re)
#     Check the shape before and after squeezing.
print("Before",arr.shape)
print("After",re.shape)'''

# 13. Create:
#
'''arr=np.array([[[10, 20, 30]]])
#
#     Use squeeze() to convert it into a 1D array.
print(arr.squeeze())'''

# 14. Create a 1D array:
#
'''arr = np.array([10, 20, 30, 40])
# Add a new dimension at axis=0 using expand_dims().
print(np.expand_dims(arr,axis=0))

# 15. Create the same 1D array.
#     Add a new dimension at axis=1 using expand_dims().
print(np.expand_dims(arr,axis=1))'''

# ============================================================
# LEVEL 3 — NEWAXIS + DIMENSION CONTROL
# ============================================================

# 16. Create:
#
'''arr = np.array([10, 20, 30, 40])
# Convert the array into a row vector.print
print(arr.shape)
b= arr[np.newaxis,:]
print(b.shape)
# 17. Convert the same array into a column vector.
new =arr[: ,np.newaxis]

# 18. Create:
arr=  np.array([1, 2, 3, 4, 5])
# Create both:
# a. Shape (1, 5)
print(arr.reshape(1,5))
# b. Shape (5, 1)
print(arr.reshape(5,1))'''

# 19. Create:

'''arr = np.array([10, 20, 30])
# Create a row vector in two different ways.
print(arr)
m1 = arr[np.newaxis,:]
print(m1)

m2 = arr.reshape(1,3)
print(m2)'''

# 20. Create:

'''arr= np.array([10, 20, 30])

# Create a column vector in two different ways.
m1 =arr[:,np.newaxis]
print(m1)
m2 = arr.reshape(3,1)
print(m2)'''


# ============================================================
# LEVEL 4 — DATA ANALYTICS
# ============================================================

# 21. A company records monthly sales for 12 months:
#
'''sales = np.array([
    120, 150, 180, 200,
    220, 250, 270, 300,
    320, 350, 380, 400
])
#
# Organize the data into a 4 × 3 structure,
str = sales.reshape(4,3)
print(str)
# representing 4 quarters with 3 months each.
print(np.sum(str,axis=1))'''


# 22. A company has sales data for 6 stores across 4 months:
#
'''sales = np.arange(1, 25)
# Organize the data into a 6 × 4 matrix.
data = sales.reshape(6,4)
print(data)

# 23. Using the sales matrix from Q22:

# Change the orientation of the matrix so that
# rows become columns and columns become rows.
print(data.T)'''

# 24. A dataset contains:
#
'''data = np.array([
    [100, 200, 300],
    [150, 250, 350],
    [200, 300, 400]
])
#
# Convert the dataset into a one-dimensional array.
print(data.flatten())

# 25. A customer transaction dataset contains:
#
transactions = np.array([
    [120, 250, 300],
    [450, 500, 650],
    [700, 800, 900]
])
#
# Convert the dataset into a one-dimensional array.
print(transactions.flatten())'''

# 26. A company stores employee performance data:
#
performance = np.array([
    [70, 80, 75],
    [85, 90, 88],
    [60, 65, 70],
    [90, 95, 92]
])
#
# Rearrange the dataset so that rows represent
# performance metrics and columns represent employees.
'''print(performance.T)'''

# ============================================================
# LEVEL 5 — ADVANCED DATA ANALYTICS
# ============================================================

# 27. A dataset has the shape (1, 4, 1):
#
'''data = np.array([[[10], [20], [30], [40]]])
#
# Remove the unnecessary dimensions.
clean = np.squeeze(data)
print(clean)
# Check the shape before and after.
print(data.shape)
print(clean.shape)'''

# 28. A machine-learning model expects input data
# in the shape (1, 5).

'''features = np.array([10, 20, 30, 40, 50])

# Convert the data into the required shape.
print(features.shape)
sha = features[np.newaxis,:]
print(sha)
print(sha.shape)
# Solve this in two different ways.
m2 = features.reshape(1,5)
print(m2.shape)
print(m2)'''

# 29. A dataset contains 24 hourly sales values:
#
'''sales = np.arange(100, 124)
#
# Perform the following:
# a. Organize the data into a 4 × 6 matrix.
data =sales.reshape(4,6)
print(data)
# b. Change its orientation.
print(data.T)
# c. Convert the result into a one-dimensional array.
dd = sales.flatten()
print(dd)
# d. Convert the resulting array back into a 4 × 6 matrix.
back = dd.reshape(4,6)
print(back)'''

# ============================================================
# LEVEL 6 — FINAL MASTER CHALLENGE
# ============================================================

# 30. A data analyst receives the following quarterly dataset:
#
sales = np.array([
    [120, 150, 180],
    [200, 220, 250],
    [300, 320, 350],
    [400, 450, 500]
])
#
# Perform the following:
#
# a. Find the shape of the original dataset.
print(sales.shape)

# b. Convert the dataset into a one-dimensional array.
flat = sales.flatten()
print(flat)

# c. Convert the dataset into a one-dimensional array
#    using another approach.
oned= sales.reshape(12)
print(oned)


# d. Change the rows into columns.
change = sales.transpose()
print(change)

# e. Organize the original data into a 2 × 6 matrix.
res = sales.reshape(2,6)
print(res)

# f. Convert the one-dimensional data into a row vector.
row_vector = flat[np.newaxis,:]

# g. Convert the one-dimensional data into a column vector.
col_vector =flat[:,np.newaxis]

# h. Create a row vector using another approach.
m1 = flat.reshape(1,12)
print(m1)

# i. Create a column vector using another approach.
m1 = flat.reshape(12,1)
print(m1)

# j. Create an unnecessary dimension in the dataset
#    and then remove that dimension.

#Create an unnecessary dimension
extra = flat[np.newaxis, :]
print(extra)
print(extra.shape)

# Remove unnecessary dimension
clean = np.squeeze(extra)
print(clean)
print(clean.shape)