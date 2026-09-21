# DAY 15: NUMPY DATA TYPES
# ========================

# 1. INTEGER (int)
# ----------------
# Integer means whole numbers without decimal values.

# Example:
# arr = np.array([10, 20, 30, 40])

# Examples of integers:
# 10    
# -5
# 0
# 100


# 2. FLOAT (float)
# ----------------
# Float means numbers that contain decimal values.

# Example:
# arr = np.array([10.5, 20.2, 30.7])

# Examples:
# 10.5
# -2.3
# 0.5
# 100.0


# 3. BOOLEAN (bool)
# -----------------
# Boolean has only two possible values:

# True
# False

# Example:
# arr = np.array([True, False, True])


# 4. COMPLEX (complex)
# --------------------
# A complex number contains:

# Real part + Imaginary part

# Example:
# arr = np.array([2+3j, 4+5j])

# 2 → Real part
# 3j → Imaginary part


# 5. STRING (str)
# ---------------
# String means text or characters.

# Example:
# arr = np.array(["Python", "SQL", "Excel"])

# Examples:
# "Ankit"
# "Python"
# "Data Analytics"


# 6. OBJECT (object)
# ------------------
# Object is a flexible data type that can store
# different types of Python objects.

# Example:
# arr = np.array([10, "Python", 3.5], dtype=object)

# It can contain different types of values.

# Object dtype is useful when NumPy needs to store
# different kinds of Python objects in one array.


# 7. dtype
# --------
# dtype tells us the data type of the elements
# stored inside a NumPy array.

# Example:

# arr = np.array([10, 20, 30])

# print(arr.dtype)

# Output may be:
# int64

# Another example:

# arr = np.array([10.5, 20.5, 30.5])

# print(arr.dtype)

# Output may be:
# float64

# Simple definition:

# dtype → tells the data type of an array.


# 8. astype()
# -----------
# astype() is used to convert an array from
# one data type to another.

# Example:

# arr = np.array([10, 20, 30])

# new_arr = arr.astype(float)

# print(new_arr)

# Output:
# [10. 20. 30.]


# Another example:

# arr = np.array([10.5, 20.8, 30.2])

# new_arr = arr.astype(int)

# print(new_arr)

# Output:
# [10 20 30]

# When float is converted to int,
# the decimal part is removed.


# 9. TYPE CONVERSION
# ------------------
# Type conversion means changing data from
# one data type to another.

# Common conversions:

# int → float
# float → int
# int → string
# string → int
# int → bool

# Example:

# arr = np.array([10, 20, 30])

# new_arr = arr.astype(float)

# Here:

# int → float


# IMPORTANT POINTS
# ----------------

# 1. dtype checks the data type.

# 2. astype() converts the data type.

# 3. float → int removes the decimal part.

# 4. 0 converted to bool becomes False.

# 5. Non-zero numbers converted to bool become True.

# 6. String numbers can be converted to integers
#    if they contain valid numeric values.


# QUICK REVISION
# --------------

# int      → Whole numbers
# float    → Decimal numbers
# bool     → True / False
# complex  → Real + Imaginary
# string   → Text
# object   → Python objects / mixed types

# dtype    → Check data type
# astype() → Convert data type


# ONE-LINE MEMORY TRICK
# ---------------------

# dtype  → "What type is it?"
# astype → "Change its type"