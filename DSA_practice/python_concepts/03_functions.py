"""
FUNCTIONS & SCOPE - Deep Dive into Python Functions
====================================================
Topics: Functions, Arguments, *args/**kwargs, Lambda, Recursion, Decorators
Difficulty: Easy to Medium
Time to master: 3-4 hours
"""

# ============================================================================
# SECTION 1: FUNCTION BASICS
# ============================================================================

print("="*70)
print("SECTION 1: FUNCTION BASICS")
print("="*70)

# Q1: Define and call a function
print("\nQ1: Basic Function")
print("-" * 70)

def greet(name):
    """Greet a person by name"""
    return f"Hello, {name}!"

print(greet("Alice"))
print(greet("Bob"))

"""
FUNCTION SYNTAX:
def function_name(parameters):
    '''Docstring - describes function'''
    # function body
    return value

PARTS:
- def: keyword to define function
- parameters: inputs (optional)
- docstring: documentation (optional but recommended)
- return: output (optional, returns None if omitted)
"""
print()

# Q2: Function with multiple parameters
print("Q2: Multiple Parameters")
print("-" * 70)

def add(a, b):
    """Add two numbers"""
    return a + b

def multiply(a, b, c):
    """Multiply three numbers"""
    return a * b * c

print(f"add(5, 3) = {add(5, 3)}")
print(f"multiply(2, 3, 4) = {multiply(2, 3, 4)}")

"""
INTERVIEW TIP: Functions can have any number of parameters
No limit on parameters, but keep it reasonable (<5 for readability)
"""
print()

# Q3: Function with default arguments
print("Q3: Default Arguments")
print("-" * 70)

def power(base, exponent=2):
    """Calculate power with default exponent=2"""
    return base ** exponent

print(f"power(5) = {power(5)}")         # Uses default exponent=2
print(f"power(5, 3) = {power(5, 3)}")   # Overrides default

"""
DEFAULT ARGUMENTS:
- Must come after non-default parameters
- Allows optional parameters
- def func(a, b=10, c=20): ✓
- def func(a=10, b, c): ✗ (SyntaxError)
"""
print()

# Q4: Keyword arguments
print("Q4: Keyword Arguments")
print("-" * 70)

def describe_person(name, age, city):
    """Describe a person"""
    return f"{name} is {age} years old and lives in {city}"

# Positional arguments
print(describe_person("Alice", 25, "NYC"))

# Keyword arguments (order doesn't matter)
print(describe_person(city="LA", name="Bob", age=30))

# Mixed (positional first, then keyword)
print(describe_person("Charlie", age=35, city="SF"))

"""
ARGUMENT TYPES:
1. Positional: Order matters
2. Keyword: Name specified, order doesn't matter
3. Mixed: Positional first, then keyword

RULE: Positional arguments must come before keyword arguments!
"""
print()


# ============================================================================
# SECTION 2: *ARGS AND **KWARGS
# ============================================================================

print("="*70)
print("SECTION 2: *ARGS AND **KWARGS")
print("="*70)

# Q5: *args (variable positional arguments)
print("\nQ5: *args - Variable Positional Arguments")
print("-" * 70)

def sum_all(*args):
    """Sum any number of arguments"""
    print(f"args type: {type(args)}")  # tuple
    print(f"args value: {args}")
    return sum(args)

print(f"sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
print(f"sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")

"""
*args CONCEPT:
- Collects extra positional arguments into a TUPLE
- Name 'args' is convention (can use any name)
- *numbers, *values also valid

USAGE: When you don't know how many arguments will be passed
"""
print()

# Q6: **kwargs (variable keyword arguments)
print("Q6: **kwargs - Variable Keyword Arguments")
print("-" * 70)

def display_info(**kwargs):
    """Display information from keyword arguments"""
    print(f"kwargs type: {type(kwargs)}")  # dict
    print(f"kwargs value: {kwargs}")
    
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

display_info(name="Alice", age=25, city="NYC")
display_info(language="Python", version=3.11)

"""
**kwargs CONCEPT:
- Collects extra keyword arguments into a DICT
- Name 'kwargs' is convention
- **info, **params also valid

USAGE: When you want flexible keyword arguments
"""
print()

# Q7: Combining regular args, *args, and **kwargs
print("Q7: Combining All Argument Types")
print("-" * 70)

def complex_function(a, b, *args, **kwargs):
    """Function with all argument types"""
    print(f"Regular args: a={a}, b={b}")
    print(f"*args (tuple): {args}")
    print(f"**kwargs (dict): {kwargs}")

complex_function(1, 2, 3, 4, 5, name="Alice", age=25)

"""
ORDER MATTERS:
1. Regular positional parameters
2. *args
3. Keyword-only parameters (optional)
4. **kwargs

def func(a, b, *args, key_only, **kwargs): ✓
"""
print()


# ============================================================================
# SECTION 3: LAMBDA FUNCTIONS
# ============================================================================

print("="*70)
print("SECTION 3: LAMBDA FUNCTIONS")
print("="*70)

# Q8: Basic lambda
print("\nQ8: Lambda Functions")
print("-" * 70)

# Regular function
def square(x):
    return x ** 2

# Lambda (anonymous function)
square_lambda = lambda x: x ** 2

print(f"Regular: square(5) = {square(5)}")
print(f"Lambda: square_lambda(5) = {square_lambda(5)}")

"""
LAMBDA SYNTAX: lambda arguments: expression

CHARACTERISTICS:
- Single expression only
- Returns expression result automatically
- Can't have multiple statements
- Anonymous (no name needed)

USE WHEN: Simple, one-line functions
"""
print()

# Q9: Lambda with multiple arguments
print("Q9: Lambda with Multiple Arguments")
print("-" * 70)

add = lambda a, b: a + b
multiply = lambda a, b, c: a * b * c

print(f"add(3, 4) = {add(3, 4)}")
print(f"multiply(2, 3, 4) = {multiply(2, 3, 4)}")

"""
INTERVIEW TIP: Lambda can have multiple arguments
lambda a, b, c: expression
"""
print()

# Q10: Lambda with map, filter, sorted
print("Q10: Lambda with Built-in Functions")
print("-" * 70)

numbers = [1, 2, 3, 4, 5]

# map: Apply function to each element
squared = list(map(lambda x: x**2, numbers))
print(f"Squared: {squared}")

# filter: Keep elements matching condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens: {evens}")

# sorted with key
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(f"Sorted by marks: {sorted_students}")

"""
COMMON USES:
- map(func, iterable): Transform elements
- filter(func, iterable): Filter elements
- sorted(iterable, key=func): Custom sorting

Lambda perfect for these short operations!
"""
print()


# ============================================================================
# SECTION 4: RECURSION
# ============================================================================

print("="*70)
print("SECTION 4: RECURSION")
print("="*70)

# Q11: Factorial using recursion
print("\nQ11: Factorial (Recursion)")
print("-" * 70)

def factorial(n):
    """Calculate factorial recursively"""
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)

print(f"5! = {factorial(5)}")
print(f"0! = {factorial(0)}")

"""
RECURSION: Function calling itself

REQUIREMENTS:
1. Base case: Stops recursion
2. Recursive case: Calls itself with simpler input
3. Progress: Each call must move toward base case

factorial(5):
5 * factorial(4)
5 * (4 * factorial(3))
5 * (4 * (3 * factorial(2)))
5 * (4 * (3 * (2 * factorial(1))))
5 * (4 * (3 * (2 * 1))) = 120
"""
print()

# Q12: Fibonacci using recursion
print("Q12: Fibonacci (Recursion)")
print("-" * 70)

def fibonacci(n):
    """Calculate nth Fibonacci number"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(8):
    print(f"fib({i}) = {fibonacci(i)}")

"""
FIBONACCI RECURSION:
fib(0) = 0
fib(1) = 1
fib(n) = fib(n-1) + fib(n-2)

WARNING: Inefficient for large n (exponential time!)
Better: Use loop or memoization
"""
print()

# Q13: Sum of list using recursion
print("Q13: Sum of List (Recursion)")
print("-" * 70)

def sum_list(arr):
    """Sum list elements recursively"""
    if not arr:  # Empty list
        return 0
    return arr[0] + sum_list(arr[1:])

numbers = [1, 2, 3, 4, 5]
print(f"Sum of {numbers} = {sum_list(numbers)}")

"""
RECURSIVE THINKING:
sum([1,2,3,4,5]) = 1 + sum([2,3,4,5])
                 = 1 + (2 + sum([3,4,5]))
                 = 1 + (2 + (3 + sum([4,5])))
                 ...
                 = 1 + 2 + 3 + 4 + 5 = 15
"""
print()


# ============================================================================
# SECTION 5: SCOPE AND LIFETIME
# ============================================================================

print("="*70)
print("SECTION 5: SCOPE AND LIFETIME")
print("="*70)

# Q14: Local vs Global scope
print("\nQ14: Local vs Global Scope")
print("-" * 70)

global_var = "I'm global"

def test_scope():
    local_var = "I'm local"
    print(f"Inside function: {global_var}")
    print(f"Inside function: {local_var}")

test_scope()
print(f"Outside function: {global_var}")
# print(local_var)  # NameError: not defined

"""
SCOPE RULES (LEGB):
L - Local: Inside function
E - Enclosing: Inside outer function (nested)
G - Global: Module level
B - Built-in: Python built-ins

SEARCH ORDER: L → E → G → B
"""
print()

# Q15: Global keyword
print("Q15: Global Keyword")
print("-" * 70)

counter = 0

def increment():
    global counter  # Modify global variable
    counter += 1

print(f"Before: counter = {counter}")
increment()
increment()
print(f"After: counter = {counter}")

"""
GLOBAL KEYWORD:
- Use to modify global variable inside function
- Without global: Creates new local variable
- Best practice: Avoid global, use return values

BAD: global everywhere
GOOD: Return values, pass parameters
"""
print()

# Q16: Nonlocal keyword (nested functions)
print("Q16: Nonlocal Keyword")
print("-" * 70)

def outer():
    count = 0
    
    def inner():
        nonlocal count  # Modify enclosing scope variable
        count += 1
        print(f"Inner: count = {count}")
    
    inner()
    inner()
    print(f"Outer: count = {count}")

outer()

"""
NONLOCAL KEYWORD:
- Use in nested functions
- Modifies variable from enclosing (outer) function
- Not global, not local, but "enclosing"
"""
print()


# ============================================================================
# SECTION 6: DECORATORS (ADVANCED)
# ============================================================================

print("="*70)
print("SECTION 6: DECORATORS")
print("="*70)

# Q17: Basic decorator
print("\nQ17: Basic Decorator")
print("-" * 70)

def my_decorator(func):
    """Decorator that prints before and after function call"""
    def wrapper(*args, **kwargs):
        print(f"Before calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"After calling {func.__name__}")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")

"""
DECORATOR: Function that modifies another function

SYNTAX:
@decorator
def function():
    pass

EQUIVALENT TO:
function = decorator(function)

USE CASES:
- Logging
- Timing
- Authentication
- Caching
"""
print()

# Q18: Timer decorator
print("Q18: Timer Decorator")
print("-" * 70)

import time

def timer(func):
    """Measure function execution time"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(0.1)
    return "Done"

result = slow_function()

"""
PRACTICAL DECORATOR: Performance measurement
Common in:
- API endpoints
- Database queries
- Complex calculations
"""
print()


# ============================================================================
# SECTION 7: INTERVIEW PROBLEMS
# ============================================================================

print("="*70)
print("SECTION 7: INTERVIEW PROBLEMS")
print("="*70)

# Q19: Check palindrome
print("\nQ19: Check Palindrome")
print("-" * 70)

def is_palindrome(s):
    """Check if string is palindrome"""
    s = s.lower().replace(" ", "")
    return s == s[::-1]

for text in ["racecar", "hello", "A man a plan a canal Panama"]:
    result = "Palindrome" if is_palindrome(text) else "Not palindrome"
    print(f"'{text}': {result}")

"""
PALINDROME: Reads same forwards and backwards
- racecar ✓
- hello ✗
- A man a plan a canal Panama ✓ (ignoring spaces/case)
"""
print()

# Q20: Find all prime numbers up to n
print("Q20: Prime Numbers (Sieve of Eratosthenes)")
print("-" * 70)

def sieve_of_eratosthenes(n):
    """Find all primes up to n"""
    if n < 2:
        return []
    
    # Create boolean array
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Mark multiples as not prime
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    
    return [i for i in range(n + 1) if is_prime[i]]

primes = sieve_of_eratosthenes(30)
print(f"Primes up to 30: {primes}")

"""
SIEVE ALGORITHM: Efficient prime finding
1. Create boolean array (all True)
2. Mark 0, 1 as not prime
3. For each prime i, mark multiples as not prime
4. Collect remaining True values

TIME: O(n log log n)
SPACE: O(n)
"""
print()

# Q21: Count vowels and consonants
print("Q21: Count Vowels and Consonants")
print("-" * 70)

def count_vowels_consonants(s):
    """Count vowels and consonants"""
    vowels = "aeiouAEIOU"
    v_count = sum(1 for char in s if char in vowels)
    c_count = sum(1 for char in s if char.isalpha() and char not in vowels)
    
    return v_count, c_count

text = "Hello World"
v, c = count_vowels_consonants(text)
print(f"'{text}': {v} vowels, {c} consonants")

"""
TECHNIQUE: Generator expression with sum()
sum(1 for item in collection if condition)

More efficient than:
count = 0
for item in collection:
    if condition:
        count += 1
"""
print()


# ============================================================================
# SUMMARY - KEY TAKEAWAYS
# ============================================================================

print("="*70)
print("SUMMARY - FUNCTIONS KEY POINTS")
print("="*70)

print("""
1. FUNCTION BASICS:
   - def function_name(params):
   - return value (None if omitted)
   - Docstrings for documentation

2. ARGUMENTS:
   - Positional: Order matters
   - Keyword: Name specified
   - Default: param=value
   - *args: Variable positional (tuple)
   - **kwargs: Variable keyword (dict)

3. LAMBDA:
   - lambda args: expression
   - Single expression only
   - Use with map(), filter(), sorted()

4. RECURSION:
   - Function calls itself
   - Need base case
   - Need recursive case
   - Must progress toward base case

5. SCOPE (LEGB):
   - Local > Enclosing > Global > Built-in
   - global: Modify global variable
   - nonlocal: Modify enclosing variable

6. DECORATORS:
   - @decorator before function
   - Modify function behavior
   - Common: @timer, @logger, @cache

INTERVIEW TIPS:
✓ Know *args vs **kwargs
✓ Master recursion base case
✓ Understand scope rules
✓ Lambda for simple operations
✓ Default args must be after positional
✓ Decorators are higher-order functions

COMMON PATTERNS:
- Palindrome: s == s[::-1]
- Prime: Check up to sqrt(n)
- Count: Use sum() with generator
""")

print("="*70)
print("Functions are 30% of interviews - master these concepts!")
print("="*70)
