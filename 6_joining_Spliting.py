import numpy as np

# ============================================================
# 🟢 LEVEL 1 — BASIC
# ============================================================

# Q1. Create the following two 1-D NumPy arrays and combine
# them into a single array.

'''a = np.array([10, 20, 30, 40, 50])
b = np.array([60, 70, 80, 90, 100])

combine = np.concatenate((a,b),axis=0)
print(combine)'''

# Q2. The monthly sales of two regions are given below.
'''North = np.array([120, 150, 180, 200, 220, 250])
South = np.array([100, 140, 170, 190, 210, 230])

# Combine both arrays into one array.
combine =np.concatenate((North,South))
print(combine)'''

# Q3. Given the following two 2-D arrays:

'''a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

b = np.array([
    [7, 8, 9],
    [10, 11, 12]
])

# Combine them so that the rows are joined.
combine = np.vstack((a,b))
print(combine)'''

# Q4. Given:

'''a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

# Combine them so that the columns are joined.
combine = np.hstack((a,b))
print(combine)'''

# Q5. Given:

'''a = np.array([10, 20, 30])
b = np.array([40, 50, 60])

# Combine them so that the result contains two rows.
combine  = np.vstack((a,b))
print(combine)'''

# Q6. Given:

'''a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Combine them so that the result contains one row
# with six elements.
combine = np.concatenate((a,b))
print(combine)'''

# Q7. Given:
'''a = np.array([10, 20, 30])
b = np.array([40, 50, 60])

# Combine both arrays into a 2-D structure where each
# original array becomes a separate row.
combine = np.vstack((a,b))
print(combine)'''

# Q8. Given:

arr = np.array([
    1, 2, 3, 4, 5, 6,
    7, 8, 9, 10, 11, 12
])

# Divide the array into 3 equal parts.
'''divide = np.split(arr,3)
print(divide)'''

# Q9. Given:

arr = np.array([
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10
])

# Divide the array into 5 equal parts.
'''divide =np.split(arr,5)
print(divide)'''

# Q10. Given:

arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

# Divide the matrix into two equal row groups.
'''group = np.vsplit(arr,2)
print(group)'''

# ============================================================
# 🟡 LEVEL 2 — INTERMEDIATE
# ============================================================

# Q11. The performance data of 6 employees is:

data = np.array([
    [85, 90, 88, 92],
    [78, 82, 80, 85],
    [92, 95, 94, 96],
    [70, 75, 72, 78],
    [88, 86, 90, 91],
    [95, 93, 97, 98]
])

# Divide the dataset into 3 equal row groups.
'''group = np.vsplit(data,3)
print(group)'''

# Q12. Given:

data = np.array([
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24]
])

# Divide the dataset into 3 equal column groups.
'''group = np.hsplit(data,3)
print(group)'''

# Q13. Given:

'''arr = np.array([
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10,
    11, 12, 13, 14, 15
])

# Divide the array into 4 parts even though the parts
# cannot have the same number of elements.
divide = np.array_split(arr,4)
print(divide)'''

# Q14. The quarterly sales of two branches are:

Branch_A = np.array([
    [120, 150, 180, 200],
    [130, 160, 190, 210],
    [140, 170, 200, 220]
])

Branch_B = np.array([
    [100, 130, 160, 190],
    [110, 140, 170, 200],
    [125, 155, 185, 215]
])

# Combine both branch datasets into a single dataset with
# Branch_B data below Branch_A data.
combine = np.vstack((Branch_A,Branch_B))
print(combine)

# Q15. First-half and second-half sales are:

first_half = np.array([
    [100, 120, 140, 160],
    [110, 130, 150, 170],
    [120, 140, 160, 180],
    [130, 150, 170, 190],
    [140, 160, 180, 200],
    [150, 170, 190, 210]
])

second_half = np.array([
    [160, 180, 200, 220],
    [170, 190, 210, 230],
    [180, 200, 220, 240],
    [190, 210, 230, 250],
    [200, 220, 240, 260],
    [210, 230, 250, 270]
])

# Combine both datasets into a complete yearly dataset.
combine = np.concatenate((first_half,second_half))
print(combine)

# Q16. Two employee datasets are given:

employee_basic = np.array([
    [101, 22, 3],
    [102, 25, 4],
    [103, 21, 2],
    [104, 28, 5],
    [105, 24, 3]
])

employee_performance = np.array([
    [85, 90, 88, 92],
    [78, 82, 80, 85],
    [92, 95, 94, 96],
    [88, 86, 90, 91],
    [95, 93, 97, 98]
])

# Combine both datasets so that every employee has
# all 7 features.
'''combine = np.hstack((employee_basic,employee_performance))
print(combine)'''

# Q17. Given:

'''a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

b = np.array([
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
])

# Combine these two matrices into a structure where the
# original matrices are preserved as separate layers.
combine = np.stack((a, b), axis=0)
print(combine)

print(combine.shape)'''

# Q18. Regional sales are:

'''North = np.array([120, 150, 180, 200, 220])
South = np.array([100, 140, 170, 190, 210])
East = np.array([130, 160, 175, 210, 230])

# Combine them into a single 2-D dataset where each
# region becomes one row.
combine =np.vstack((North,South,East))
print(combine)'''

# Q19. Given:

'''data = np.array([
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [20, 30, 40, 50],
    [25, 35, 45, 55],
    [30, 40, 50, 60],
    [35, 45, 55, 65],
    [40, 50, 60, 70],
    [45, 55, 65, 75],
    [50, 60, 70, 80],
    [55, 65, 75, 85],
    [60, 70, 80, 90],
    [65, 75, 85, 95]
])

# Divide the dataset into four equal sections.
split = np.split(data,4)
print(split)'''

# Q20. Given:

'''data = np.array([
    [1, 2, 3, 4, 5, 6, 7, 8],
    [9, 10, 11, 12, 13, 14, 15, 16],
    [17, 18, 19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30, 31, 32],
    [33, 34, 35, 36, 37, 38, 39, 40]
])

# Divide the columns into four equal groups.
divide = np.hsplit(data,4)
print(divide)''' 

# ============================================================
# 🔴 LEVEL 3 — ADVANCED / DATA ANALYTICS
# ============================================================

# Q21. Regional sales data:

'''North = np.array([120, 150, 180, 200])
South = np.array([100, 140, 170, 190])
East = np.array([130, 160, 175, 210])

# Create a single NumPy dataset where each region
# represents one row.
combine = np.vstack((North,South,East))
print(combine)'''

# Q22. Two customer datasets are given below:

customers_1 = np.array([
    [101, 25, 50000],
    [102, 28, 55000],
    [103, 31, 62000],
    [104, 24, 48000],
    [105, 29, 58000]
])

customers_2 = np.array([
    [106, 27, 51000],
    [107, 32, 67000],
    [108, 26, 53000],
    [109, 30, 61000],
    [110, 23, 45000]
])

# Combine both datasets into one customer dataset.
combine =np.concatenate((customers_1,customers_2))
print(combine)

# Q23. First-half and second-half yearly sales:

first_half = np.array([
    [100, 120, 140, 160],
    [110, 130, 150, 170],
    [120, 140, 160, 180],
    [130, 150, 170, 190],
    [140, 160, 180, 200],
    [150, 170, 190, 210]
])

second_half = np.array([
    [160, 180, 200, 220],
    [170, 190, 210, 230],
    [180, 200, 220, 240],
    [190, 210, 230, 250],
    [200, 220, 240, 260],
    [210, 230, 250, 270]
])

# Combine them into one 12 × 4 dataset.


# Q24. Given a 24 × 6 dataset:

data = np.arange(1, 145).reshape(24, 6)

# Divide the dataset into 4 equal sections based on rows.


# Q25. Given:

data = np.arange(1, 121).reshape(10, 12)

# Divide the dataset into 3 column groups even though the
# number of columns cannot be divided equally.


# Q26. Monthly sales of three channels are:

Online = np.array([
    120, 130, 150, 160, 180, 190,
    200, 220, 230, 250, 270, 300
])

Retail = np.array([
    100, 110, 125, 140, 150, 170,
    185, 200, 210, 230, 250, 280
])

Wholesale = np.array([
    80, 95, 110, 120, 135, 150,
    165, 180, 195, 210, 225, 250
])

# Combine all three datasets into one dataset where each
# sales channel becomes a separate row.


# Q27. Customer demographic and purchasing data:

demographic = np.array([
    [21, 1, 25],
    [24, 0, 30],
    [28, 1, 35],
    [32, 0, 40],
    [26, 1, 28]
])

purchasing = np.array([
    [5000, 3, 1200, 4],
    [6500, 5, 1800, 6],
    [7200, 4, 2100, 5],
    [8500, 7, 3000, 8],
    [6000, 3, 1500, 4]
])

# Combine both datasets into one dataset containing
# 7 features for every customer.


# Q28. Given:

data = np.arange(1, 1001).reshape(100, 10)

# Divide the dataset into 5 equal batches for batch-wise
# analysis.

# Display the shape of every batch.


# Q29. Create the following dataset:

data = np.arange(1, 97).reshape(12, 8)

# Perform the following:

# 1. Divide the dataset into 4 equal row groups.

# 2. Divide the original dataset into 2 equal column groups.

# 3. Combine the row groups back into the original dataset.

# 4. Combine the column groups back into the original dataset.

# 5. Verify that the reconstructed row dataset is identical
#    to the original dataset.

# 6. Verify that the reconstructed column dataset is identical
#    to the original dataset.

# 7. Display the shape of every important result.


# ============================================================
# 🔥 Q30 — MASTER CHALLENGE
# ============================================================

# Create the following quarterly datasets:

Q1 = np.array([
    [100, 120, 140, 160],
    [110, 130, 150, 170],
    [120, 140, 160, 180]
])

Q2 = np.array([
    [130, 150, 170, 190],
    [140, 160, 180, 200],
    [150, 170, 190, 210]
])

Q3 = np.array([
    [160, 180, 200, 220],
    [170, 190, 210, 230],
    [180, 200, 220, 240]
])

Q4 = np.array([
    [190, 210, 230, 250],
    [200, 220, 240, 260],
    [210, 230, 250, 270]
])

# Each row represents a product and each column represents
# a monthly sales value.

# Perform the following:

# 1. Create all four quarterly datasets.

# 2. Combine all four quarterly datasets into one yearly
#    dataset.

# 3. Divide the yearly dataset into four quarterly sections.

# 4. Divide the yearly dataset column-wise into two groups.

# 5. Create a separate 3-D structure containing all four
#    quarterly datasets.

# 6. Display the shape after every major operation.

# 7. Verify that splitting the yearly dataset produces the
#    original quarterly datasets.

# 8. Verify that combining the quarterly datasets again
#    reconstructs the original yearly dataset.

# 9. Verify that the reconstructed yearly dataset is exactly
#    equal to the original yearly dataset.

# 10. Display the final shape of the 3-D structure.

# ============================================================