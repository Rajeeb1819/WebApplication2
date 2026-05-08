"""
CONTROL FLOW - If-Else, Loops & Pattern Programming
====================================================
Topics: Conditional Statements, For/While Loops, Break/Continue, Patterns
Difficulty: Easy to Medium
Time to master: 3-4 hours
"""

# ============================================================================
# SECTION 1: IF-ELSE STATEMENTS
# ============================================================================

print("="*70)
print("SECTION 1: CONDITIONAL STATEMENTS")
print("="*70)

# Q1: Basic if-else
print("\nQ1: If-Else Basics")
print("-" * 70)

age = 18

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

"""
SYNTAX:
if condition:
    # code block
elif condition2:
    # code block
else:
    # code block

IMPORTANT: Indentation matters in Python! (4 spaces)
"""
print()

# Q2: Nested if-else
print("Q2: Nested If-Else")
print("-" * 70)

marks = 85

if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Marks: {marks}, Grade: {grade}")

"""
INTERVIEW TIP: Use elif, not multiple ifs
Wrong: if, if, if → checks all conditions
Right: if, elif, elif → stops at first match (efficient!)
"""
print()

# Q3: Ternary operator (conditional expression)
print("Q3: Ternary Operator")
print("-" * 70)

age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")

# Multiple ternary (less readable)
marks = 75
grade = 'A' if marks >= 90 else 'B' if marks >= 80 else 'C' if marks >= 70 else 'F'
print(f"Grade: {grade}")

"""
SYNTAX: value_if_true if condition else value_if_false

BEST PRACTICE:
- Use for simple conditions
- Use regular if-else for complex logic
"""
print()

# Q4: Check leap year
print("Q4: Check Leap Year")
print("-" * 70)

def is_leap_year(year):
    """
    Leap year rules:
    1. Divisible by 4
    2. If divisible by 100, must also be divisible by 400
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

# Test cases
for year in [2000, 1900, 2024, 2023]:
    result = "Leap year" if is_leap_year(year) else "Not leap year"
    print(f"{year}: {result}")

"""
INTERVIEW CLASSIC: Leap year logic
- 2000: Yes (divisible by 400)
- 1900: No (divisible by 100 but not 400)
- 2024: Yes (divisible by 4)
- 2023: No (not divisible by 4)
"""
print()


# ============================================================================
# SECTION 2: FOR LOOPS
# ============================================================================

print("="*70)
print("SECTION 2: FOR LOOPS")
print("="*70)

# Q5: Basic for loop with range
print("\nQ5: For Loop with Range")
print("-" * 70)

# range(stop)
print("range(5):", end=" ")
for i in range(5):
    print(i, end=" ")
print()

# range(start, stop)
print("range(1, 6):", end=" ")
for i in range(1, 6):
    print(i, end=" ")
print()

# range(start, stop, step)
print("range(0, 10, 2):", end=" ")
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# Reverse range
print("range(5, 0, -1):", end=" ")
for i in range(5, 0, -1):
    print(i, end=" ")
print()

"""
RANGE FUNCTION:
- range(n): 0 to n-1
- range(start, stop): start to stop-1
- range(start, stop, step): with custom increment

INTERVIEW TIP: range() generates numbers on demand (memory efficient)
"""
print()

# Q6: Iterate over list/string
print("Q6: Iterate Over Collections")
print("-" * 70)

# List
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(f"Fruit: {fruit}")

# String
for char in "Python":
    print(char, end=" ")
print()

# With index (enumerate)
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

"""
PYTHONIC WAY:
- Iterate directly: for item in collection
- Need index? Use enumerate()
- Don't do: for i in range(len(arr))
"""
print()

# Q7: Nested for loops
print("Q7: Nested For Loops")
print("-" * 70)

# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end="  ")
    print()

"""
CONCEPT: Nested loops
Outer loop runs N times
Inner loop runs M times each
Total iterations: N × M

COMPLEXITY: O(N × M)
"""
print()


# ============================================================================
# SECTION 3: WHILE LOOPS
# ============================================================================

print("="*70)
print("SECTION 3: WHILE LOOPS")
print("="*70)

# Q8: Basic while loop
print("\nQ8: While Loop Basics")
print("-" * 70)

count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

"""
WHILE LOOP: Runs while condition is True
DANGER: Infinite loop if condition never becomes False!

while True:  # Runs forever!
    pass
"""
print()

# Q9: Sum of digits
print("Q9: Sum of Digits")
print("-" * 70)

def sum_of_digits(n):
    """Calculate sum of digits of a number"""
    total = 0
    n = abs(n)  # Handle negative numbers
    
    while n > 0:
        digit = n % 10      # Get last digit
        total += digit
        n = n // 10         # Remove last digit
    
    return total

number = 12345
print(f"Sum of digits of {number}: {sum_of_digits(number)}")

"""
INTERVIEW CLASSIC: Digit manipulation
- Get last digit: n % 10
- Remove last digit: n // 10
- Reverse number: build digit by digit
"""
print()

# Q10: Reverse a number
print("Q10: Reverse a Number")
print("-" * 70)

def reverse_number(n):
    """Reverse digits of a number"""
    reversed_num = 0
    n = abs(n)
    
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10
    
    return reversed_num

number = 12345
print(f"Original: {number}")
print(f"Reversed: {reverse_number(number)}")

"""
ALGORITHM:
1. Extract last digit: n % 10
2. Add to reversed: reversed * 10 + digit
3. Remove last digit: n // 10
4. Repeat

Example: 123
- 0*10 + 3 = 3, n=12
- 3*10 + 2 = 32, n=1
- 32*10 + 1 = 321, n=0
"""
print()


# ============================================================================
# SECTION 4: BREAK, CONTINUE, PASS
# ============================================================================

print("="*70)
print("SECTION 4: BREAK, CONTINUE, PASS")
print("="*70)

# Q11: Break statement
print("\nQ11: Break Statement")
print("-" * 70)

# Find first number divisible by 7
for num in range(1, 20):
    if num % 7 == 0:
        print(f"First number divisible by 7: {num}")
        break  # Exit loop immediately

"""
BREAK: Exits the innermost loop immediately
Use when: Found what you need, no point continuing
"""
print()

# Q12: Continue statement
print("Q12: Continue Statement")
print("-" * 70)

# Print only odd numbers
print("Odd numbers:", end=" ")
for num in range(1, 11):
    if num % 2 == 0:
        continue  # Skip rest of loop, go to next iteration
    print(num, end=" ")
print()

"""
CONTINUE: Skips rest of current iteration
Use when: Want to skip certain items
"""
print()

# Q13: Pass statement
print("Q13: Pass Statement")
print("-" * 70)

def future_function():
    """To be implemented later"""
    pass  # Placeholder

class EmptyClass:
    pass  # Placeholder for class

"""
PASS: Does nothing (placeholder)
Use when: Need syntactically valid empty block
"""
print()

# Q14: Else with loops
print("Q14: Loop Else Clause")
print("-" * 70)

# Search for a number
def search_number(arr, target):
    """Search with for-else"""
    for num in arr:
        if num == target:
            print(f"Found {target}!")
            break
    else:
        # Runs only if loop completed without break
        print(f"{target} not found!")

search_number([1, 2, 3, 4], 3)  # Found
search_number([1, 2, 3, 4], 9)  # Not found

"""
LOOP ELSE: Runs if loop completes without break
Useful for: Search algorithms
- Break → found item
- Else → item not found
"""
print()


# ============================================================================
# SECTION 5: PATTERN PROGRAMMING (INTERVIEW FAVORITE!)
# ============================================================================

print("="*70)
print("SECTION 5: PATTERN PROGRAMMING")
print("="*70)

# Q15: Square pattern
print("\nQ15: Square Pattern")
print("-" * 70)

n = 4
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

print()

# Q16: Right triangle pattern
print("Q16: Right Triangle Pattern")
print("-" * 70)

n = 5
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()

"""
PATTERN LOGIC:
Row 1: 1 star
Row 2: 2 stars
Row i: i stars

Outer loop: rows (1 to n)
Inner loop: stars per row (1 to i)
"""
print()

# Q17: Inverted right triangle
print("Q17: Inverted Triangle")
print("-" * 70)

n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

"""
PATTERN LOGIC:
Row 1: n stars
Row 2: n-1 stars
Row i: decreasing
"""
print()

# Q18: Pyramid pattern
print("Q18: Pyramid Pattern")
print("-" * 70)

n = 5
for i in range(1, n+1):
    # Print spaces
    for j in range(n-i):
        print(" ", end="")
    # Print stars
    for j in range(2*i-1):
        print("*", end="")
    print()

"""
PYRAMID LOGIC:
Row 1: (n-1) spaces, 1 star
Row 2: (n-2) spaces, 3 stars
Row i: (n-i) spaces, (2*i-1) stars

Pattern:
    *      4 spaces, 1 star
   ***     3 spaces, 3 stars
  *****    2 spaces, 5 stars
 *******   1 space, 7 stars
*********  0 spaces, 9 stars
"""
print()

# Q19: Number pattern
print("Q19: Number Pattern")
print("-" * 70)

n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

"""
OUTPUT:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
print()

# Q20: Floyd's Triangle
print("Q20: Floyd's Triangle")
print("-" * 70)

n = 5
num = 1
for i in range(1, n+1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

"""
FLOYD'S TRIANGLE: Sequential numbers
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""
print()


# ============================================================================
# SECTION 6: ADVANCED LOOP PROBLEMS
# ============================================================================

print("="*70)
print("SECTION 6: ADVANCED PROBLEMS")
print("="*70)

# Q21: Check prime number
print("\nQ21: Check Prime Number")
print("-" * 70)

def is_prime(n):
    """Check if number is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

for num in [2, 17, 25, 29, 100]:
    result = "Prime" if is_prime(num) else "Not Prime"
    print(f"{num}: {result}")

"""
PRIME NUMBER: Divisible only by 1 and itself
OPTIMIZATION:
1. Check only up to sqrt(n)
2. Skip even numbers (except 2)
3. Check only odd divisors

TIME COMPLEXITY: O(sqrt(n))
"""
print()

# Q22: Factorial
print("Q22: Calculate Factorial")
print("-" * 70)

def factorial(n):
    """Calculate factorial using loop"""
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

for n in [5, 0, 10]:
    print(f"{n}! = {factorial(n)}")

"""
FACTORIAL: n! = n × (n-1) × ... × 2 × 1
5! = 5 × 4 × 3 × 2 × 1 = 120

EDGE CASES:
- 0! = 1 (by definition)
- 1! = 1
"""
print()

# Q23: Fibonacci series
print("Q23: Fibonacci Series")
print("-" * 70)

def fibonacci(n):
    """Generate first n Fibonacci numbers"""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    
    return fib

n = 10
print(f"First {n} Fibonacci numbers:")
print(fibonacci(n))

"""
FIBONACCI: Each number is sum of previous two
0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

FORMULA: F(n) = F(n-1) + F(n-2)
F(0) = 0, F(1) = 1
"""
print()

# Q24: GCD (Greatest Common Divisor)
print("Q24: GCD using Euclidean Algorithm")
print("-" * 70)

def gcd(a, b):
    """Calculate GCD using Euclidean algorithm"""
    while b:
        a, b = b, a % b
    return a

print(f"GCD(48, 18) = {gcd(48, 18)}")
print(f"GCD(100, 50) = {gcd(100, 50)}")

"""
EUCLIDEAN ALGORITHM:
gcd(48, 18):
48 % 18 = 12  → gcd(18, 12)
18 % 12 = 6   → gcd(12, 6)
12 % 6 = 0    → gcd(6, 0) = 6

TIME COMPLEXITY: O(log(min(a,b)))
"""
print()

# Q25: Armstrong number
print("Q25: Check Armstrong Number")
print("-" * 70)

def is_armstrong(n):
    """
    Armstrong number: Sum of cubes of digits equals number
    153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153
    """
    num_str = str(abs(n))
    num_digits = len(num_str)
    total = sum(int(digit) ** num_digits for digit in num_str)
    
    return total == abs(n)

for num in [153, 9474, 123]:
    result = "Armstrong" if is_armstrong(num) else "Not Armstrong"
    print(f"{num}: {result}")

"""
ARMSTRONG NUMBER: Sum of nth power of digits = number
(n = number of digits)

Examples:
153 = 1³ + 5³ + 3³ (3 digits, power 3)
9474 = 9⁴ + 4⁴ + 7⁴ + 4⁴ (4 digits, power 4)
"""
print()


# ============================================================================
# SUMMARY - KEY TAKEAWAYS
# ============================================================================

print("="*70)
print("SUMMARY - CONTROL FLOW KEY POINTS")
print("="*70)

print("""
1. IF-ELSE:
   - Use elif, not multiple ifs
   - Ternary: value_if_true if condition else value_if_false
   - Indentation matters!
    """)