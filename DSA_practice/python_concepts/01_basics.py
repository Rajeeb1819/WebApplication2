"""
PYTHON BASICS - Fundamentals & Interview Questions
===================================================
Topics: Variables, Data Types, Operators, Input/Output, Type Conversion
Difficulty: Easy
Time to master: 2-3 hours
"""

# ============================================================================
# SECTION 1: VARIABLES AND DATA TYPES
# ============================================================================

print("="*70)
print("SECTION 1: VARIABLES AND DATA TYPES")
print("="*70)

# Q1: What are the basic data types in Python?
print("\nQ1: Basic Data Types")
print("-" * 70)

# Integer
age = 25
print(f"Integer: {age}, type: {type(age)}")

# Float
price = 99.99
print(f"Float: {price}, type: {type(price)}")

# String
name = "Python"
print(f"String: {name}, type: {type(name)}")

# Boolean
is_active = True
print(f"Boolean: {is_active}, type: {type(is_active)}")

# None
value = None
print(f"NoneType: {value}, type: {type(value)}")

"""
CONCEPT: Python has 5 basic built-in types
- int: whole numbers (no size limit!)
- float: decimal numbers
- str: text (immutable sequence)
- bool: True/False
- NoneType: represents absence of value
"""
print()

# Q2: Variable naming rules and conventions
print("Q2: Variable Naming")
print("-" * 70)

# Valid variable names
user_name = "John"          # snake_case (preferred)
userName = "Jane"           # camelCase (not preferred)
_private = "hidden"         # underscore prefix
CONSTANT = 100              # UPPERCASE for constants
number123 = 456             # can end with numbers

# Invalid names (will cause errors):
# 123number = "error"       # can't start with number
# user-name = "error"       # no hyphens
# class = "error"           # can't use keywords

print(f"Valid names: {user_name}, {userName}, {_private}, {CONSTANT}")

"""
RULES:
1. Start with letter or underscore
2. Can contain letters, numbers, underscores
3. Case-sensitive (age ≠ Age)
4. No Python keywords (if, for, class, etc.)

CONVENTIONS (PEP 8):
- snake_case for variables and functions
- UPPER_CASE for constants
- CapitalCase for classes
"""
print()

# Q3: Dynamic typing
print("Q3: Dynamic Typing")
print("-" * 70)

x = 10          # x is int
print(f"x = {x}, type: {type(x)}")

x = "hello"     # Now x is str (no error!)
print(f"x = {x}, type: {type(x)}")

x = [1, 2, 3]   # Now x is list
print(f"x = {x}, type: {type(x)}")

"""
CONCEPT: Python is dynamically typed
- Don't need to declare type
- Variable type can change
- Type determined at runtime
- Different from Java/C++ (statically typed)
"""
print()


# ============================================================================
# SECTION 2: TYPE CONVERSION (CASTING)
# ============================================================================

print("="*70)
print("SECTION 2: TYPE CONVERSION")
print("="*70)

# Q4: How to convert between types?
print("\nQ4: Type Conversion Functions")
print("-" * 70)

# String to Integer
s = "123"
num = int(s)
print(f"String '{s}' to int: {num}")

# Integer to String
n = 456
text = str(n)
print(f"Int {n} to string: '{text}'")

# String to Float
price_str = "19.99"
price_float = float(price_str)
print(f"String '{price_str}' to float: {price_float}")

# Float to Int (truncates decimal)
f = 9.99
i = int(f)
print(f"Float {f} to int: {i}")

# Integer/Float to Boolean
print(f"int(0) to bool: {bool(0)}")        # False
print(f"int(1) to bool: {bool(1)}")        # True
print(f"int(-5) to bool: {bool(-5)}")      # True (any non-zero)

"""
INTERVIEW TIP: Know what values are "falsy"
- 0, 0.0
- Empty string ""
- Empty collections: [], {}, ()
- None
- False

Everything else is "truthy"
"""
print()

# Q5: Common type conversion errors
print("Q5: Type Conversion Errors")
print("-" * 70)

try:
    num = int("abc")  # ValueError
except ValueError as e:
    print(f"Error: {e}")

try:
    num = int("12.5")  # ValueError (has decimal)
except ValueError as e:
    print(f"Error: {e}")
    print("Solution: Use float() first, then int()")
    num = int(float("12.5"))
    print(f"Correct: {num}")

"""
COMMON MISTAKES:
1. int("12.5") → Error (use int(float("12.5")))
2. int("") → Error (empty string)
3. float("abc") → Error (not a number)

ALWAYS validate input in real code!
"""
print()


# ============================================================================
# SECTION 3: OPERATORS
# ============================================================================

print("="*70)
print("SECTION 3: OPERATORS")
print("="*70)

# Q6: Arithmetic operators
print("\nQ6: Arithmetic Operators")
print("-" * 70)

a, b = 10, 3

print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")           # Always returns float
print(f"Floor Division: {a} // {b} = {a // b}")   # Integer division
print(f"Modulus: {a} % {b} = {a % b}")            # Remainder
print(f"Exponentiation: {a} ** {b} = {a ** b}")   # Power

"""
INTERVIEW QUESTION: Difference between / and //?
- / (division): Always returns float (10/3 = 3.333...)
- // (floor division): Returns int, rounds down (10//3 = 3)

TRICKY: -10 // 3 = -4 (not -3!)
Because floor rounds DOWN: -3.33... → -4
"""
print()

# Q7: Comparison operators
print("Q7: Comparison Operators")
print("-" * 70)

x, y = 5, 10

print(f"{x} == {y}: {x == y}")   # Equal
print(f"{x} != {y}: {x != y}")   # Not equal
print(f"{x} < {y}: {x < y}")     # Less than
print(f"{x} > {y}: {x > y}")     # Greater than
print(f"{x} <= {y}: {x <= y}")   # Less than or equal
print(f"{x} >= {y}: {x >= y}")   # Greater than or equal

"""
INTERVIEW TIP: Chaining comparisons
Instead of: x > 5 and x < 10
Write: 5 < x < 10 (more Pythonic!)
"""
print(f"Chained: 5 < 7 < 10 = {5 < 7 < 10}")
print()

# Q8: Logical operators
print("Q8: Logical Operators")
print("-" * 70)

print(f"True and False: {True and False}")
print(f"True or False: {True or False}")
print(f"not True: {not True}")

# Short-circuit evaluation
print("\nShort-circuit:")
print(f"False and print('This never runs'): {False and print('Never')}")
print(f"True or print('This never runs'): {True or print('Never')}")

"""
CONCEPT: Short-circuit evaluation
- `and`: Returns first falsy value or last value
- `or`: Returns first truthy value or last value

Examples:
- 0 and 5 → 0 (first falsy)
- 5 and 10 → 10 (both truthy, return last)
- 0 or 5 → 5 (first truthy)
- 0 or "" → "" (both falsy, return last)
"""
print()

# Q9: Identity and Membership operators
print("Q9: Identity & Membership Operators")
print("-" * 70)

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a == b: {a == b}")       # True (same values)
print(f"a is b: {a is b}")       # False (different objects)
print(f"a is c: {a is c}")       # True (same object)

print(f"\n2 in [1,2,3]: {2 in [1, 2, 3]}")
print(f"'x' not in 'hello': {'x' not in 'hello'}")

"""
INTERVIEW QUESTION: == vs is?
- == compares VALUES (equality)
- is compares IDENTITY (same object in memory)

Special case: Small integers (-5 to 256) are cached
a = 10; b = 10 → a is b (True)
a = 1000; b = 1000 → a is b (False, different objects)
"""
print()


# ============================================================================
# SECTION 4: INPUT AND OUTPUT
# ============================================================================

print("="*70)
print("SECTION 4: INPUT AND OUTPUT")
print("="*70)

# Q10: Taking input from user
print("\nQ10: Input Functions")
print("-" * 70)

# input() always returns string
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))

# For demonstration (without user input):
name = "Alice"
age = 25
print(f"Name: {name}, Age: {age}")

"""
IMPORTANT: input() ALWAYS returns string!
Must convert: int(input()), float(input())

INTERVIEW TIP: Handle invalid input
try:
    age = int(input("Age: "))
except ValueError:
    print("Invalid number!")
"""
print()

# Q11: Print function
print("Q11: Print Function")
print("-" * 70)

# Multiple arguments
print("Hello", "World", "!")

# Custom separator
print("2026", "05", "07", sep="-")

# Custom end (default is '\n')
print("Line 1", end=" | ")
print("Line 2")

# Formatted output
name = "Bob"
age = 30
print(f"Name: {name}, Age: {age}")                    # f-string (Python 3.6+)
print("Name: {}, Age: {}".format(name, age))          # .format()
print("Name: %s, Age: %d" % (name, age))              # % formatting (old)

"""
BEST PRACTICE: Use f-strings (fastest and most readable)
f"Value: {variable}"
f"Result: {expression + 10}"
f"Float: {3.14159:.2f}"  # Format to 2 decimals
"""
print()


# ============================================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================================

print("="*70)
print("SECTION 5: COMMON INTERVIEW QUESTIONS")
print("="*70)

# Q12: Swap two variables
print("\nQ12: Swap Two Variables")
print("-" * 70)

a, b = 5, 10
print(f"Before: a={a}, b={b}")

# Python way (single line!)
a, b = b, a
print(f"After: a={a}, b={b}")

"""
INTERVIEW QUESTION: Swap without temp variable?
Python: a, b = b, a (tuple unpacking)

Other languages need:
temp = a
a = b
b = temp

Or: a = a + b; b = a - b; a = a - b
"""
print()

# Q13: Check even or odd
print("Q13: Check Even or Odd")
print("-" * 70)

def is_even(n):
    """Return True if n is even"""
    return n % 2 == 0

for num in [4, 7, 0, -3]:
    result = "even" if is_even(num) else "odd"
    print(f"{num} is {result}")

"""
CONCEPT: Modulus operator %
- n % 2 == 0 → even
- n % 2 == 1 → odd (for positive)
- n % 2 != 0 → odd (works for negative too)
"""
print()

# Q14: Check if number is positive, negative, or zero
print("Q14: Check Number Sign")
print("-" * 70)

def check_sign(n):
    """Check if number is positive, negative, or zero"""
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"

for num in [10, -5, 0]:
    print(f"{num} is {check_sign(num)}")

"""
INTERVIEW TIP: Multiple conditions
Use if-elif-else chain
Order matters! First match wins
"""
print()

# Q15: Find maximum of three numbers
print("Q15: Maximum of Three Numbers")
print("-" * 70)

def max_of_three(a, b, c):
    """Find maximum of three numbers"""
    return max(a, b, c)  # Built-in max()

# Without built-in
def max_of_three_manual(a, b, c):
    """Find maximum without built-in"""
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c

print(f"Max of (5, 12, 8): {max_of_three(5, 12, 8)}")
print(f"Max (manual): {max_of_three_manual(5, 12, 8)}")

"""
INTERVIEW TIP: Know both approaches
1. Using built-ins: max(), min()
2. Manual logic (shows understanding)

For multiple values: max([1, 5, 3, 9, 2])
"""
print()

# Q16: Calculate simple interest
print("Q16: Calculate Simple Interest")
print("-" * 70)

def simple_interest(principal, rate, time):
    """
    Calculate simple interest
    Formula: SI = (P × R × T) / 100
    """
    return (principal * rate * time) / 100

p, r, t = 1000, 5, 2
si = simple_interest(p, r, t)
print(f"Principal: {p}, Rate: {r}%, Time: {t} years")
print(f"Simple Interest: {si}")

"""
INTERVIEW TIP: Document formulas in docstring
Shows you understand the problem domain
"""
print()


# ============================================================================
# SECTION 6: TRICKY INTERVIEW QUESTIONS
# ============================================================================

print("="*70)
print("SECTION 6: TRICKY QUESTIONS")
print("="*70)

# Q17: What is the output?
print("\nQ17: Tricky Output Questions")
print("-" * 70)

print(f"10 / 3 = {10 / 3}")        # 3.333... (float)
print(f"10 // 3 = {10 // 3}")      # 3 (int)
print(f"-10 // 3 = {-10 // 3}")    # -4 (floors down!)

print(f"\n5 * 'A' = {'5' * 'A'}")  # String repetition (not multiplication!)
print(f"'ABC' * 3 = {'ABC' * 3}")

"""
TRICKY POINTS:
1. Division (/) ALWAYS returns float, even for whole numbers
2. Floor division (//) with negatives floors DOWN (toward -∞)
3. String * int = repetition
"""
print()

# Q18: Operator precedence
print("Q18: Operator Precedence")
print("-" * 70)

result = 2 + 3 * 4      # Multiplication first
print(f"2 + 3 * 4 = {result}")

result = (2 + 3) * 4    # Parentheses first
print(f"(2 + 3) * 4 = {result}")

result = 2 ** 3 ** 2    # Right-to-left for **
print(f"2 ** 3 ** 2 = {result}")  # 2^(3^2) = 2^9 = 512

"""
PRECEDENCE (High to Low):
1. Parentheses ()
2. Exponentiation **
3. Unary +, -, not
4. *, /, //, %
5. +, -
6. Comparisons ==, !=, <, >, <=, >=
7. Logical and, or, not

TIP: Use parentheses for clarity!
"""
print()


# ============================================================================
# SUMMARY - KEY TAKEAWAYS
# ============================================================================

print("="*70)
print("SUMMARY - KEY POINTS FOR INTERVIEWS")
print("="*70)

print("""
1. DATA TYPES:
   - int, float, str, bool, None
   - Python is dynamically typed
   - Use type() to check type

2. TYPE CONVERSION:
   - int(), float(), str(), bool()
   - input() always returns string
   - Handle ValueError for invalid conversion

3. OPERATORS:
   - / returns float, // returns int
   - % is remainder (modulus)
   - ** is exponentiation
   - Use `is` for identity, == for equality

4. FALSY VALUES:
   - 0, 0.0, "", [], {}, (), None, False

5. INPUT/OUTPUT:
   - input() returns string
   - Use f-strings for formatting
   - print() can take multiple args

6. COMMON PATTERNS:
   - Swap: a, b = b, a
   - Even/odd: n % 2 == 0
   - Chained comparison: 5 < x < 10

INTERVIEW TIPS:
✓ Know difference between / and //
✓ Understand operator precedence
✓ Remember input() returns string
✓ Know falsy values
✓ Use f-strings for output
✓ Validate user input
""")

print("="*70)
print("Practice these basics - they appear in 90% of Python interviews!")
print("="*70)
