# Operators in Python :-
# Arithmetic Operators

# Addition (+)
a = 10
b = 20
c = a + b
print(c)

# Subtraction (-)
a = 30
b = 20
c = a - b
print(c)

# Multiplication (*)
a = 5
b = 11
c = a * b
print(c)

# Division (/)
a = 200
b = 20
c = a / b
print(c)

# Modulus (%)
a = 120
b = 7
c = a % b
print(c)

# Exponentiation (**)
a = 4
b = 6
c = a ** b
print(c)  # return 'a' to the power of 'b'

# Floor division (//)
a = 30
b = 7
c = a ** b
print(c)  # returns nearest divisible whole number

# ----------------------------------------------
# Assignment Operators
"""
=	    x = 5	    x = 5	
+=	    x += 3	    x = x + 3	
-=	    x -= 3	    x = x - 3	
*=	    x *= 3	    x = x * 3	
/=	    x /= 3	    x = x / 3	
%=	    x %= 3	    x = x % 3	
//=	    x //= 3	    x = x ** 3	
&=	    x &= 3	    x = x & 3	
|=	    x |= 3	    x = x | 3	
^=	    x ^= 3	    x = x ^ 3	
>>=	    x >>= 3	    x = x >> 3	
<<=	    x <<= 3	    x = x << 3	

"""

# Comparison Operators
# Equal (==)
a = 20
b = 30
print(a == b)  # return true if 'a' is equal to 'b' otherwise false

# Not equal (!=)
a = 20
b = 30
print(a == b)  # return true if 'a' is not equal to 'b' otherwise false

# Greater than (>)
a = 20
b = 30
print(a > b)  # return true if 'a' is greater than to 'b' otherwise false

# Less than (<)
a = 20
b = 30
print(a < b)  # return true if 'a' is less than to 'b' otherwise false

# Greater than or equal to than (>)
a = 20
b = 30
print(a >= b)  # return true if 'a' is greater than or equal to 'b' otherwise false

# Less than or equal to than (>)
a = 20
b = 30
print(a <= b)  # return true if 'a' is less than or equal to 'b' otherwise false

# Logical Operators
# Logical "and"
a = 10
b = 20
c = 30
print(a < b and a < c)  # Returns True if both statements are true

# Logical "or"
a = 10
b = 20
c = 30
print(a < b or a > c)  # Returns True if any one the statement is true

# Logical "not"
a = 10
b = 20
c = 30
print(not(a < b and a < c))  # Reverse the result, returns False if the result is true

# Identity Operators
# 'is' Operator
a = ["javascript","python"]
b = ["javascript","python"]
print(a is b)  # returns true if 'a' is the same object as 'b'
print(a is not b)  # returns true if both the variable are not the same object

