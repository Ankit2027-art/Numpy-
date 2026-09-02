# # NumPy Broadcasting — Quick Revision

# ### 1. What is Broadcasting?

# Broadcasting allows NumPy to perform operations on arrays with different but **compatible shapes**.

# ### 2. Why is Broadcasting Used?

# * Avoids unnecessary loops
# * Makes code short and simple
# * Faster calculations
# * Useful in Data Analytics and ML

# ### 3. Broadcasting Rules

# Compare shapes **from right to left**.

# Compatible when:

# * Dimensions are same → ✅
# * One dimension is `1` → ✅
# * Dimension is missing → ✅

# Otherwise → ❌ Incompatible

# ### 4. Scalar + Array

# ```python
# a = np.array([10, 20, 30])

# a + 5
# # [15 25 35]
# ```

# ### 5. 1D + 2D

# ```text
# A → (2,3)
# B → (3,)

# [10 20 30]    [1 2 3]
# [40 50 60] +  [1 2 3]

# Result:
# [11 22 33]
# [41 52 63]
# ```

# ### 6. Compatible Shapes

# ```text
# (3,3) + (3,)    → ✅
# (3,3) + (3,1)   → ✅
# (2,3) + (1,3)   → ✅
# ```

# Example:

# ```text
# (2,3)
# (1,3)

# → 3 = 3 ✅
# → 2 vs 1 → 1 can expand ✅
# ```

# ### 7. Incompatible Shapes

# ```text
# (2,3) + (2,) → ❌
# ```

# Because:

# ```text
# 3 ≠ 2
# ```

# Neither dimension is `1`.

# ### Remember

# ```text
# Same dimension → ✅
# One dimension is 1 → ✅
# Dimension missing → ✅
# Different dimension → ❌
# ```

# **Broadcasting = Automatically adjusting compatible array shapes for operations.**
