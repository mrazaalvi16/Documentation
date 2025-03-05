# Arithmetic Operators
# Addition
x = 5
y = 8
print(x +y)
# Subtraction
x = 8
y = 5
print(x - y)
# Multiplication
x = 5
y = 8
print(x * y)
# Division
x = 5
y = 8
print(x / y )

# Modulus
x = 8
y = 3
print(x % y)

# Exponentiatiion
x = 5
y = 2
print(x ** y)

# Floor Division

x = 25
y = 4
print(x // y)

# Assignment Operators "assign values to variables"
# =
x = 5
print(x)
# +=
x = 5
x += 3
print(x)
# -=
x = 5
x -= 3
print(x)
# *=
x = 5
x *= 3
print(x)
# /=
x = 5
x /= 3
print(x)
# %=
x = 5
x %= 3
print(x)
# //=
x = 5
x //= 3
print(x)
# **=
x = 5
x **= 3
print(x)
# &=
x = 11
x &= 3
print(x)
# |=
x = 9
x |= 3
print(x)
# ^=
x = 5
x ^= 3
print(x)
# >>=
x = 9
x >>= 3
print(x)
# <<=
x = 6
x <<= 3
print(x)
# :=
x = 3
print(x)

# Comparison Operators
# Equal ==
x = 3
y = 3
print(x == y )
# Not equal !=
x = 3
y = 3
print(x != y )
# Greater than >
x = 3
y = 3
print(x > y )
# Less than <
x = 3
y = 3
print(x < y )
# Greater than or equal to >=
x = 9
y = 3
print(x >= y )
# Lessthan or equal to <=
x = 3
y = 3
print(x <= y )

# Logical Operators
# Return True if both statements are ture 'and'
x = 5
print(x > 3 and x < 10)
# Return True if one of the statements is ture 'or'
x = 5
print(x > 3 or x < 4 )
# Reverse the result, returns False if the result is true 'not'
x = 5
print(not(x > 3 and x < 10))

# Identity Operators "used to compare the objects, not if they are equal, 
# but if they are actually the same object,with the same memory location"

# Return True if both variables are the same object 'is'
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x ==y)

# Return True if both variables are not the same object 'is not '

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z)
print(x is not y)
print(x !=y)

# Membership Operators"is used to test if a sequence is presented in an object"

# Return True if a sequence with the specified value is present in the object 'in'
x = ["apple", "banana"]
print("banana" in x)

# Return True if a sequence with the specified value is not present in the object 'not in '
x = ["apple", "banana"]
print("pineapple" not in x)

# Bitwise Operators used to compare binary numbers

# Set each bit to 1 if both bits are 1 '& name AND'
print(4 & 3)

# Set each bit to 1 if one of the two bits is 1 '| name OR'
print(9 | 3)

# Set each bit to 1 if only one of two bits is 1 '^ name XOR'
print(7 ^ 3)

# Invers all the  bit '~ name NOT'
print(~4)

# Shift left by pushing zeros in from the right and let the leftmost bits fall off 
# '<< name Zero fill let shit'
print(4 << 2)

# Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
# '>> name Signed right shift'
print(9 >> 2)
