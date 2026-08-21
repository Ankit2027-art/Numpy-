
import numpy as np

# # ================================
# # LEVEL 1 — BASIC
# # ================================

# # 1. A dataset contains daily sales:
sales = np.array([120, 150, 180, 200, 250])

# # Calculate the total sales.
print(np.sum(sales))

# # 2. A dataset contains employee salaries:
salary = np.array([25000, 30000, 28000, 35000, 40000])

# # Find the minimum and maximum salary.
print("Minimun:",np.min(salary))
print("Maximun:",np.max(salary))

# # 3. A dataset contains customer ages:
ages = np.array([18, 21, 25, 30, 35, 40])

# # Calculate the average age.
print("Avg Age:",np.average(ages))

# # 4. A dataset contains the following values:
values = np.array([10, 20, 30, 40, 50])

# # Calculate the median value.
print("Median",np.median(values))

# # 5. A dataset contains:
values = np.array([2, 3, 4, 5])

# # Calculate the product of all values.
print("Product:",np.prod(values))

# # ================================
# # LEVEL 2 — STATISTICS
# # ================================

# # 6. A company's monthly profits are:
profit = np.array([1200, 1500, 1100, 1800, 2000, 1700])

# # Calculate:
# # a. Mean
print("Mean:",np.mean(profit))
# # b. Median
print("Median:",np.median(profit))
# # c. Standard deviation
print("S.D",np.std(profit))
# # d. Variance
print("Variance:",np.var(profit))

# # 7. A dataset contains student marks:
marks = np.array([45, 50, 55, 60, 65, 70, 75, 80])

# # Find:
# # a. Minimum
print("Min:",np.min(marks))
# # b. Maximum
print("Max:",np.max(marks))
# # c. Mean
print("Mean:",np.mean(marks))
# # d. Median
print("Median:",np.median(marks))


# # 8. A company records the number of products sold:
products = np.array([5, 10, 15, 20])

# # Calculate the total and product of all values.
print("Total",np.sum(products))
print("Product:",np.prod(products))

# # ================================
# # LEVEL 3 — PERCENTILE & QUANTILE
# # ================================

# # 9. A dataset contains employee performance scores:
scores = np.array([45, 50, 55, 60, 65, 70, 75, 80, 85, 90])

# # Calculate the:
# # a. 25th percentile
print(np.percentile(scores,25))
# # b. 50th percentile
print(np.percentile(scores,50))
# # c. 75th percentile
print(np.percentile(scores,75))

# # 10. A dataset contains customer spending:
spending = np.array([100, 200, 300, 400, 500, 600, 700, 800])
# # Calculate:
# # a. 0.25 quantile
print(np.quantile(spending,0.25))
# # b. 0.50 quantile
print(np.quantile(spending,0.50))
# # c. 0.75 quantile
print(np.quantile(spending,0.75))


# # 11. A dataset contains delivery times:
delivery = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10])

# # Find the 90th percentile.
print(np.percentile(delivery,90))

# # ================================
# # LEVEL 4 — 2D ARRAYS + AXIS
# # ================================

# 12. A company records monthly sales for three stores:
sales = np.array([
    [100, 200, 300],
    [150, 250, 350],
    [200, 300, 400]
])

# # Calculate the total sales:
print("Total Sales:",np.sum(sales))
# # a. Column-wise using axis=0
print("c.w:",np.sum(sales,axis=0))
# # b. Row-wise using axis=1
print("R.W:",np.sum(sales,axis=1))


# # 13. Using the same dataset:
sales = np.array([
    [100, 200, 300],
    [150, 250, 350],
    [200, 300, 400]
])

# # Calculate the average:
print("Average:",np.average(sales))
# # a. Column-wise
print("Avg C.W",np.average(sales,axis=0))
# # b. Row-wise
print("Avg R.W",np.average(sales,axis=1))


# # 14. Using the following dataset:
marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [90, 95, 88]
])

# # Find the:
# # a. Minimum value column-wise
print(np.min(marks,axis=0))
# # b. Maximum value column-wise
print(np.max(marks,axis=0))
# # c. Minimum value row-wise
print(np.min(marks,axis=1))
# # d. Maximum value row-wise
print(np.max(marks,axis=1))


# # ================================
# # LEVEL 5 — DATA ANALYTICS
# # ================================

# # 15. A company has sales data for 4 stores across 3 months:
import numpy as np
sales = np.array([
    [120, 150, 180],
    [200, 220, 250],
    [100, 130, 160],
    [300, 350, 400]
])

# # Calculate:
# # a. Total sales for each store
print(np.sum(sales,axis=1))
# # b. Average sales for each store
print(np.average(sales,axis=1))
# # c. Total sales for each month
print(np.sum(sales,axis=0))
# # d. Average sales for each month
print(np.average(sales,axis=0))

# # 16. A company records employee performance:
performance = np.array([
    [70, 80, 75],
    [90, 85, 95],
    [60, 65, 70],
    [80, 75, 85]
])

# # Calculate the standard deviation:
# # a. For each employee
print(np.std(performance,axis=1))
# # b. For each performance metric
print(np.std(performance,axis=0))

# # 17. Using the same performance dataset:
performance = np.array([
    [70, 80, 75],
    [90, 85, 95],
    [60, 65, 70],
    [80, 75, 85]
])

# # Calculate the variance:
# # a. Row-wise
print("R.W",np.var(performance,axis=1))
# # b. Column-wise
print("R.W",np.var(performance,axis=0))

# # ================================
# # LEVEL 6 — FINAL CHALLENGE
# # ================================

# # 18. A data analyst receives the following sales dataset:
sales = np.array([
    [120, 150, 180, 200],
    [250, 300, 280, 320],
    [100, 130, 150, 170],
    [400, 420, 450, 500]
])

# # Perform the following:
# # a. Find the total sales.
print(np.sum(sales))
# # b. Find the minimum sales value.
print(np.min(sales))
# # c. Find the maximum sales value.
print(np.max(sales))
# # d. Find the overall mean.
print(np.mean(sales))
# # e. Find the overall median.
print(np.median(sales))
# # f. Find the standard deviation.
print(np.std(sales))
# # g. Find the variance.
print(np.var(sales))
# # h. Find the product of all values.
print(np.prod(sales))
# # i. Find the 25th percentile.
print(np.percentile(sales,25))
# # j. Find the 75th percentile.
print(np.percentile(sales,75))
# # k. Find the 0.25 quantile.
print(np.quantile(sales,0.25))
# # l. Find the 0.75 quantile.
print(np.quantile(sales,0.75))
# # m. Find column-wise totals.
print(np.sum(sales,axis=0))
# # n. Find row-wise totals.
print(np.sum(sales,axis=1))
# # o. Find column-wise averages.
print(np.average(sales,axis=0))
# # p. Find row-wise averages.
print(np.average(sales,axis=1))
# # q. Find column-wise minimum values.
print(np.min(sales,axis=0))
# # r. Find row-wise maximum values.
print(np.max(sales,axis=1))