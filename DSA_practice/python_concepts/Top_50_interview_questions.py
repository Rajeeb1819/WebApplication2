"""
TOP 50 INTERVIEW QUESTIONS - Most Asked in Python Interviews
=============================================================
Curated list of most frequently asked programming questions
Difficulty: Easy to Medium
Category: String, Array, Math, Logic, Pattern Recognition
Time to master: 6-8 hours
"""

# ============================================================================
# SECTION 1: STRING MANIPULATION (Most Asked!)
# ============================================================================

print("="*70)
print("SECTION 1: STRING MANIPULATION - TOP 10")
print("="*70)

# Q1: Reverse a string
print("\nQ1: Reverse a String")
print("-" * 70)

def reverse_string(s):
    """Method 1: Slicing (Pythonic)"""
    return s[::-1]

def reverse_string_loop(s):
    """Method 2: Using loop"""
    result = ""
    for char in s:
        result = char + result
    return result

text = "Hello World"
print(f"Original: {text}")
print(f"Reversed (slicing): {reverse_string(text)}")
print(f"Reversed (loop): {reverse_string_loop(text)}")

"""
INTERVIEW FAVORITE: Asked in 80% of interviews!
BEST ANSWER: s[::-1] (shows Python knowledge)
ALTERNATIVES: reversed(), loop, recursion
TIME: O(n), SPACE: O(n)
"""
print()

# Q2: Check if string is palindrome
print("Q2: Check Palindrome")
print("-" * 70)

def is_palindrome(s):
    """Check if string reads same forwards and backwards"""
    # Clean string: lowercase, remove spaces
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def is_palindrome_two_pointers(s):
    """Method 2: Two pointers (more efficient)"""
    s = s.lower().replace(" ", "")
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

test_cases = ["racecar", "hello", "A man a plan a canal Panama", "madam"]
for text in test_cases:
    result = "Yes" if is_palindrome(text) else "No"
    print(f"'{text}': Palindrome? {result}")

"""
FOLLOW-UP QUESTIONS:
- Ignore spaces and punctuation? → Use regex or isalnum()
- Case-sensitive? → Usually no, use lower()
- Numbers considered palindrome? → Clarify with interviewer

TIME: O(n), SPACE: O(1) with two pointers
"""
print()

# Q3: Count vowels and consonants
print("Q3: Count Vowels and Consonants")
print("-" * 70)

def count_vowels_consonants(s):
    """Count vowels and consonants in string"""
    vowels = "aeiouAEIOU"
    v_count = sum(1 for char in s if char in vowels)
    c_count = sum(1 for char in s if char.isalpha() and char not in vowels)
    
    return v_count, c_count

text = "Hello World"
vowels, consonants = count_vowels_consonants(text)
print(f"'{text}': Vowels={vowels}, Consonants={consonants}")

"""
VARIATION: Count only vowels, or specific characters
PYTHONIC: Use generator expression with sum()
TIME: O(n), SPACE: O(1)
"""
print()

# Q4: Remove duplicates from string
print("Q4: Remove Duplicate Characters")
print("-" * 70)

def remove_duplicates(s):
    """Method 1: Using set (order not preserved)"""
    return ''.join(set(s))

def remove_duplicates_order(s):
    """Method 2: Preserve order"""
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

text = "programming"
print(f"Original: {text}")
print(f"Duplicates removed (no order): {remove_duplicates(text)}")
print(f"Duplicates removed (order): {remove_duplicates_order(text)}")

"""
IMPORTANT: Clarify if order matters!
- No order: Use set() - O(n) time, O(n) space
- Preserve order: Use seen set + list - O(n) time, O(n) space
"""
print()

# Q5: Check if two strings are anagrams
print("Q5: Check Anagram")
print("-" * 70)

def is_anagram(s1, s2):
    """Method 1: Sort and compare"""
    return sorted(s1.lower()) == sorted(s2.lower())

def is_anagram_counter(s1, s2):
    """Method 2: Using Counter (efficient)"""
    from collections import Counter
    return Counter(s1.lower()) == Counter(s2.lower())

pairs = [("listen", "silent"), ("hello", "world"), ("Dormitory", "Dirty room")]
for s1, s2 in pairs:
    result = "Yes" if is_anagram(s1, s2) else "No"
    print(f"'{s1}' & '{s2}': Anagram? {result}")

"""
ANAGRAM: Same letters, different order
BEST METHOD: Counter (shows library knowledge)
ALTERNATIVES: Sort, frequency dict
TIME: O(n log n) sort, O(n) Counter
"""
print()

# Q6: Find first non-repeating character
print("Q6: First Non-Repeating Character")
print("-" * 70)

def first_non_repeating(s):
    """Find first character that appears only once"""
    from collections import Counter
    
    count = Counter(s)
    
    for char in s:
        if count[char] == 1:
            return char
    
    return None

text = "programming"
result = first_non_repeating(text)
print(f"'{text}': First non-repeating = '{result}'")

"""
LOGIC: Two-pass algorithm
1. Count frequency (Counter)
2. Find first with count=1

TIME: O(n), SPACE: O(n)
"""
print()

# Q7: Count occurrences of each character
print("Q7: Character Frequency")
print("-" * 70)

def char_frequency(s):
    """Count frequency of each character"""
    from collections import Counter
    return Counter(s)

def char_frequency_dict(s):
    """Method 2: Manual dictionary"""
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

text = "hello"
print(f"'{text}' frequency: {char_frequency(text)}")

"""
MUST KNOW: Counter from collections
ALTERNATIVE: defaultdict(int), regular dict
FOLLOW-UP: Sort by frequency
"""
print()

# Q8: Capitalize first letter of each word
print("Q8: Capitalize Each Word")
print("-" * 70)

def capitalize_words(s):
    """Method 1: Built-in"""
    return s.title()

def capitalize_words_manual(s):
    """Method 2: Manual"""
    words = s.split()
    capitalized = [word.capitalize() for word in words]
    return ' '.join(capitalized)

text = "hello world from python"
print(f"Original: {text}")
print(f"Capitalized: {capitalize_words(text)}")

"""
BUILT-IN: .title() or .capitalize()
DIFFERENCE:
- .capitalize(): Only first letter of string
- .title(): First letter of each word
"""
print()

# Q9: Check if string contains only digits
print("Q9: Check if String is Numeric")
print("-" * 70)

def is_numeric(s):
    """Check if string contains only digits"""
    return s.isdigit()

test_cases = ["12345", "123a45", "0", "-123"]
for text in test_cases:
    result = "Yes" if is_numeric(text) else "No"
    print(f"'{text}' is numeric? {result}")

"""
STRING METHODS:
- .isdigit(): Only digits (0-9)
- .isnumeric(): Digits + numeric chars (½, ²)
- .isdecimal(): Only decimal digits

NEGATIVE NUMBERS: isdigit() returns False for "-123"
"""
print()

# Q10: Replace spaces with a character
print("Q10: Replace Spaces")
print("-" * 70)

def replace_spaces(s, char='%20'):
    """Replace spaces with given character"""
    return s.replace(' ', char)

text = "Hello World from Python"
print(f"Original: {text}")
print(f"Replaced: {replace_spaces(text)}")

"""
SIMPLE: Use .replace() method
URL ENCODING: Common interview question
ALTERNATIVE: Use loop for custom logic
"""
print()


# ============================================================================
# SECTION 2: ARRAY/LIST PROBLEMS (Most Asked!)
# ============================================================================

print("="*70)
print("SECTION 2: ARRAY/LIST PROBLEMS - TOP 10")
print("="*70)

# Q11: Find largest and smallest in array
print("\nQ11: Find Max and Min")
print("-" * 70)

def find_max_min(arr):
    """Find maximum and minimum in array"""
    if not arr:
        return None, None
    return max(arr), min(arr)

def find_max_min_loop(arr):
    """Method 2: Using loop"""
    if not arr:
        return None, None
    
    max_val = min_val = arr[0]
    
    for num in arr:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    
    return max_val, min_val

numbers = [3, 7, 1, 9, 2, 5]
max_val, min_val = find_max_min(numbers)
print(f"Array: {numbers}")
print(f"Max: {max_val}, Min: {min_val}")

"""
BUILT-IN: max(), min() - O(n)
MANUAL: Single pass - O(n)
FOLLOW-UP: Find second largest (track top 2)
"""
print()

# Q12: Remove duplicates from array
print("Q12: Remove Duplicates from Array")
print("-" * 70)

def remove_duplicates_array(arr):
    """Method 1: Using set (order not preserved)"""
    return list(set(arr))

def remove_duplicates_order_array(arr):
    """Method 2: Preserve order"""
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

numbers = [1, 2, 3, 2, 4, 1, 5]
print(f"Original: {numbers}")
print(f"No duplicates (no order): {remove_duplicates_array(numbers)}")
print(f"No duplicates (order): {remove_duplicates_order_array(numbers)}")

"""
SAME AS STRING DUPLICATES
- Order doesn't matter: set()
- Order matters: seen set + list
"""
print()

# Q13: Find second largest element
print("Q13: Second Largest Element")
print("-" * 70)

def second_largest(arr):
    """Find second largest element"""
    if len(arr) < 2:
        return None
    
    # Remove duplicates and sort
    unique = list(set(arr))
    unique.sort(reverse=True)
    
    return unique[1] if len(unique) > 1 else None

def second_largest_efficient(arr):
    """Method 2: Single pass (more efficient)"""
    if len(arr) < 2:
        return None
    
    first = second = float('-inf')
    
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    
    return second if second != float('-inf') else None

numbers = [12, 35, 1, 10, 34, 1]
print(f"Array: {numbers}")
print(f"Second largest: {second_largest(numbers)}")

"""
COMMON INTERVIEW QUESTION!
METHOD 1: Sort - O(n log n)
METHOD 2: Single pass - O(n) ✓ Better!
EDGE CASE: All same numbers, less than 2 elements
"""
print()

# Q14: Reverse an array
print("Q14: Reverse an Array")
print("-" * 70)

def reverse_array(arr):
    """Method 1: Slicing"""
    return arr[::-1]

def reverse_array_inplace(arr):
    """Method 2: In-place (two pointers)"""
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

numbers = [1, 2, 3, 4, 5]
print(f"Original: {numbers}")
print(f"Reversed: {reverse_array(numbers.copy())}")

"""
PYTHONIC: arr[::-1] or reversed()
IN-PLACE: Two pointers (space efficient)
TIME: O(n), SPACE: O(1) for in-place
"""
print()

# Q15: Find missing number in array
print("Q15: Find Missing Number")
print("-" * 70)

def find_missing_number(arr, n):
    """
    Find missing number in array [1, 2, ..., n]
    Example: [1, 2, 4, 5] → Missing: 3
    """
    # Method 1: Sum formula
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

numbers = [1, 2, 4, 5, 6]
n = 6
missing = find_missing_number(numbers, n)
print(f"Array: {numbers}")
print(f"Missing number: {missing}")

"""
CLASSIC PROBLEM: Missing number from 1 to n
FORMULA: Sum(1 to n) = n*(n+1)/2
ALTERNATIVE: XOR approach
TIME: O(n), SPACE: O(1)
"""
print()

# Q16: Rotate array by k positions
print("Q16: Rotate Array")
print("-" * 70)

def rotate_array(arr, k):
    """Rotate array to right by k positions"""
    k = k % len(arr)  # Handle k > len
    return arr[-k:] + arr[:-k]

numbers = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(f"Original: {numbers}")
print(f"Rotated by {k}: {rotate_array(numbers, k)}")

"""
LOGIC: Move last k elements to front
[1,2,3,4,5,6,7] rotated by 3 → [5,6,7,1,2,3,4]
HANDLE: k > len(arr) using modulo
TIME: O(n), SPACE: O(n)
"""
print()

# Q17: Merge two sorted arrays
print("Q17: Merge Two Sorted Arrays")
print("-" * 70)

def merge_sorted_arrays(arr1, arr2):
    """Merge two sorted arrays into one sorted array"""
    result = []
    i = j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    # Add remaining elements
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    
    return result

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
print(f"Array 1: {arr1}")
print(f"Array 2: {arr2}")
print(f"Merged: {merge_sorted_arrays(arr1, arr2)}")

"""
TWO POINTERS ALGORITHM
Used in merge sort
TIME: O(m + n), SPACE: O(m + n)
"""
print()

# Q18: Check if array is sorted
print("Q18: Check if Array is Sorted")
print("-" * 70)

def is_sorted(arr):
    """Check if array is sorted in ascending order"""
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True

def is_sorted_pythonic(arr):
    """Pythonic way"""
    return arr == sorted(arr)

test_arrays = [[1, 2, 3, 4, 5], [1, 3, 2, 4], [5, 4, 3, 2, 1]]
for arr in test_arrays:
    result = "Yes" if is_sorted(arr) else "No"
    print(f"{arr}: Sorted? {result}")

"""
SIMPLE CHECK: Compare with sorted version
EFFICIENT: Single pass comparison
TIME: O(n)
"""
print()

# Q19: Find common elements in two arrays
print("Q19: Common Elements (Intersection)")
print("-" * 70)

def find_common(arr1, arr2):
    """Find common elements in two arrays"""
    return list(set(arr1) & set(arr2))

def find_common_sorted(arr1, arr2):
    """Method 2: For sorted arrays (two pointers)"""
    result = []
    i = j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            result.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    
    return result

arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]
print(f"Array 1: {arr1}")
print(f"Array 2: {arr2}")
print(f"Common: {find_common(arr1, arr2)}")

"""
SET INTERSECTION: set1 & set2
TWO POINTERS: For sorted arrays
TIME: O(n + m) with sets
"""
print()

# Q20: Move zeros to end
print("Q20: Move Zeros to End")
print("-" * 70)

def move_zeros(arr):
    """Move all zeros to end of array"""
    non_zero_pos = 0
    
    # Move non-zeros to front
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_pos], arr[i] = arr[i], arr[non_zero_pos]
            non_zero_pos += 1
    
    return arr


numbers = [0, 1, 0, 3, 12]
print(f"Original: {numbers}")
print(f"Zeros moved: {move_zeros(numbers.copy())}")

"""
TWO POINTERS TECHNIQUE
Track position for non-zero elements
TIME: O(n), SPACE: O(1)
"""
print()


# ============================================================================
# SECTION 3: NUMBER/MATH PROBLEMS (Top 10)
# ============================================================================

print("="*70)
print("SECTION 3: MATHEMATICAL PROBLEMS - TOP 10")
print("="*70)

# Q21: Check if number is prime
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

test_numbers = [2, 17, 25, 29, 100, 97]
for num in test_numbers:
    result = "Prime" if is_prime(num) else "Not Prime"
    print(f"{num}: {result}")

"""
MUST KNOW ALGORITHM!
OPTIMIZATION: Check up to sqrt(n), skip even numbers
TIME: O(sqrt(n))
"""
print()

# Q22: Factorial
print("Q22: Calculate Factorial")
print("-" * 70)

def factorial_iterative(n):
    """Factorial using loop"""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    """Factorial using recursion"""
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

for n in [5, 0, 10]:
    print(f"{n}! = {factorial_iterative(n)}")

"""
CLASSIC RECURSION PROBLEM
n! = n × (n-1) × ... × 2 × 1
EDGE CASE: 0! = 1
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
MOST ASKED RECURSION PROBLEM!
F(n) = F(n-1) + F(n-2)
F(0) = 0, F(1) = 1
"""
print()

# Q24: Sum of digits
print("Q24: Sum of Digits")
print("-" * 70)

def sum_of_digits(n):
    """Calculate sum of digits"""
    total = 0
    n = abs(n)
    
    while n > 0:
        total += n % 10
        n //= 10
    
    return total

numbers = [12345, 9876, 100]
for num in numbers:
    print(f"Sum of digits of {num}: {sum_of_digits(num)}")

"""
DIGIT MANIPULATION:
- Get last digit: n % 10
- Remove last digit: n // 10
"""
print()

# Q25: Check Armstrong number
print("Q25: Armstrong Number")
print("-" * 70)

def is_armstrong(n):
    """Check if number is Armstrong number"""
    digits = str(abs(n))
    num_digits = len(digits)
    total = sum(int(d) ** num_digits for d in digits)
    return total == abs(n)

test_numbers = [153, 9474, 123, 1634]
for num in test_numbers:
    result = "Armstrong" if is_armstrong(num) else "Not Armstrong"
    print(f"{num}: {result}")

"""
ARMSTRONG: Sum of nth power of digits = number
153 = 1³ + 5³ + 3³ = 1 + 125 + 27
"""
print()

# Q26: GCD (Greatest Common Divisor)
print("Q26: GCD - Euclidean Algorithm")
print("-" * 70)

def gcd(a, b):
    """Calculate GCD using Euclidean algorithm"""
    while b:
        a, b = b, a % b
    return a

print(f"GCD(48, 18) = {gcd(48, 18)}")
print(f"GCD(100, 50) = {gcd(100, 50)}")

"""
EUCLIDEAN ALGORITHM: Most efficient
gcd(a, b) = gcd(b, a % b)
TIME: O(log(min(a, b)))
"""
print()

# Q27: LCM (Least Common Multiple)
print("Q27: LCM")
print("-" * 70)

def lcm(a, b):
    """Calculate LCM using GCD"""
    return (a * b) // gcd(a, b)

print(f"LCM(12, 18) = {lcm(12, 18)}")
print(f"LCM(4, 6) = {lcm(4, 6)}")

"""
FORMULA: LCM(a, b) = (a × b) / GCD(a, b)
MUST KNOW: Relationship between GCD and LCM
"""
print()

# Q28: Power of a number
print("Q28: Calculate Power")
print("-" * 70)

def power_iterative(base, exp):
    """Calculate base^exp using loop"""
    result = 1
    for _ in range(exp):
        result *= base
    return result

def power_recursive(base, exp):
    """Calculate using recursion"""
    if exp == 0:
        return 1
    return base * power_recursive(base, exp - 1)

print(f"2^5 = {power_iterative(2, 5)}")
print(f"3^4 = {power_recursive(3, 4)}")

"""
BUILT-IN: ** operator or pow()
RECURSION: power(base, exp) = base * power(base, exp-1)
"""
print()

# Q29: Check perfect number
print("Q29: Perfect Number")
print("-" * 70)

def is_perfect(n):
    """
    Perfect number: Sum of divisors = number
    Example: 6 = 1 + 2 + 3
    """
    if n < 2:
        return False
    
    divisor_sum = 1  # 1 is always a divisor
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:  # Add the pair divisor
                divisor_sum += n // i
    
    return divisor_sum == n

test_numbers = [6, 28, 12, 496]
for num in test_numbers:
    result = "Perfect" if is_perfect(num) else "Not Perfect"
    print(f"{num}: {result}")

"""
PERFECT NUMBER: Sum of proper divisors = number
6: divisors 1,2,3 → 1+2+3 = 6
28: divisors 1,2,4,7,14 → sum = 28
"""
print()

# Q30: Swap two numbers without temp
print("Q30: Swap Without Temp Variable")
print("-" * 70)

def swap_without_temp(a, b):
    """Method 1: Arithmetic"""
    print(f"Before: a={a}, b={b}")
    a = a + b
    b = a - b
    a = a - b
    print(f"After: a={a}, b={b}")
    return a, b

def swap_pythonic(a, b):
    """Method 2: Tuple unpacking (Pythonic!)"""
    a, b = b, a
    return a, b

swap_without_temp(5, 10)
print()
a, b = 15, 25
print(f"Before: a={a}, b={b}")
a, b = swap_pythonic(a, b)
print(f"After: a={a}, b={b}")

"""
PYTHON WAY: a, b = b, a (tuple unpacking)
OTHER WAYS: Arithmetic, XOR
BEST ANSWER: Show Python way first!
"""
print()


# ============================================================================
# SECTION 4: PATTERN & LOGIC (Top 10)
# ============================================================================

print("="*70)
print("SECTION 4: PATTERN & LOGIC - TOP 10")
print("="*70)


# Q31: FizzBuzz
print("\nQ31: FizzBuzz (MOST FAMOUS!)")
print("-" * 70)

def fizzbuzz(n):
    """
    Print numbers 1 to n:
    - Fizz for multiples of 3
    - Buzz for multiples of 5
    - FizzBuzz for multiples of both
    """
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
    print()

fizzbuzz(20)

"""
CLASSIC INTERVIEW QUESTION!
LOGIC: Check 15 first, then 3, then 5
VARIATION: Different multiples
"""
print()

# Q32: Print pyramid pattern
print("Q32: Pyramid Pattern")
print("-" * 70)

def print_pyramid(n):
    """Print pyramid of stars"""
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2*i - 1))

print_pyramid(5)

"""
PATTERN LOGIC:
Row 1: 4 spaces, 1 star
Row 2: 3 spaces, 3 stars
Row i: (n-i) spaces, (2i-1) stars
"""
print()

# Q33: Count words in string
print("Q33: Count Words in String")
print("-" * 70)

def count_words(s):
    """Count number of words"""
    return len(s.split())

text = "Hello World from Python Programming"
print(f"'{text}'")
print(f"Word count: {count_words(text)}")

"""
SIMPLE: Use .split() method
HANDLES: Multiple spaces automatically
"""
print()

# Q34: Find duplicate elements
print("Q34: Find Duplicates in Array")
print("-" * 70)

def find_duplicates(arr):
    """Find all duplicate elements"""
    from collections import Counter
    
    count = Counter(arr)
    return [num for num, freq in count.items() if freq > 1]

numbers = [1, 2, 3, 2, 4, 5, 1, 6]
print(f"Array: {numbers}")
print(f"Duplicates: {find_duplicates(numbers)}")

"""
USING COUNTER: Most Pythonic
ALTERNATIVE: Set to track seen elements
"""
print()

# Q35: Sum of array elements
print("Q35: Sum of Array")
print("-" * 70)

def array_sum(arr):
    """Calculate sum of array elements"""
    return sum(arr)

def array_sum_loop(arr):
    """Using loop"""
    total = 0
    for num in arr:
        total += num
    return total

numbers = [1, 2, 3, 4, 5]
print(f"Array: {numbers}")
print(f"Sum: {array_sum(numbers)}")

"""
BUILT-IN: sum() function
MANUAL: Use loop (show understanding)
"""
print()

# Q36: Check if number is even or odd
print("Q36: Even or Odd")
print("-" * 70)

def is_even(n):
    """Check if number is even"""
    return n % 2 == 0

for num in [4, 7, 0, -3]:
    result = "Even" if is_even(num) else "Odd"
    print(f"{num}: {result}")

"""
SIMPLE: n % 2 == 0
WORKS FOR: Negative numbers too
"""
print()

# Q37: Find largest element in array
print("Q37: Find Maximum Element")
print("-" * 70)

def find_max(arr):
    """Find maximum element"""
    if not arr:
        return None
    
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    
    return max_val

numbers = [3, 7, 1, 9, 2, 5]
print(f"Array: {numbers}")
print(f"Maximum: {find_max(numbers)}")
print(f"Using built-in: {max(numbers)}")

"""
BUILT-IN: max()
MANUAL: Single pass comparison
"""
print()

# Q38: Linear search
print("Q38: Linear Search")
print("-" * 70)

def linear_search(arr, target):
    """Search for target in array"""
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

numbers = [3, 7, 1, 9, 2, 5]
target = 9
result = linear_search(numbers, target)
print(f"Array: {numbers}")
print(f"Search for {target}: Found at index {result}")

"""
SIMPLE SEARCH: Check each element
TIME: O(n)
BETTER: Binary search for sorted arrays
"""
print()

# Q39: Binary search
print("Q39: Binary Search")
print("-" * 70)

def binary_search(arr, target):
    """Binary search in sorted array"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

numbers = [1, 3, 5, 7, 9, 11, 13]
target = 7
result = binary_search(numbers, target)
print(f"Sorted array: {numbers}")
print(f"Search for {target}: Found at index {result}")

"""
REQUIRES: Sorted array
TIME: O(log n) - Much faster than linear!
MUST KNOW ALGORITHM
"""
print()

# Q40: Count frequency of elements
print("Q40: Frequency of Elements")
print("-" * 70)

def count_frequency(arr):
    """Count frequency of each element"""
    from collections import Counter
    return dict(Counter(arr))

numbers = [1, 2, 2, 3, 3, 3, 4]
freq = count_frequency(numbers)
print(f"Array: {numbers}")
print(f"Frequency: {freq}")

"""
COUNTER: Best tool for frequency counting
OUTPUT: {element: count}
"""
print()


# ============================================================================
# SECTION 5: BONUS - TRICKY INTERVIEW QUESTIONS (Top 10)
# ============================================================================

print("="*70)
print("SECTION 5: TRICKY QUESTIONS - TOP 10")
print("="*70)

# Q41: Two Sum problem
print("\nQ41: Two Sum (LEETCODE #1)")
print("-" * 70)

def two_sum(arr, target):
    """Find two numbers that sum to target"""
    seen = {}
    
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return []

numbers = [2, 7, 11, 15]
target = 9
result = two_sum(numbers, target)
print(f"Array: {numbers}, Target: {target}")
print(f"Indices: {result} → {numbers[result[0]]} + {numbers[result[1]]} = {target}")

"""
MOST ASKED PROBLEM ON LEETCODE!
HASH MAP: O(n) time, O(n) space
BRUTE FORCE: O(n²) with nested loops
"""
print()

# Q42: Remove element from list
print("Q42: Remove All Occurrences")
print("-" * 70)

def remove_element(arr, val):
    """Remove all occurrences of value"""
    return [x for x in arr if x != val]

numbers = [3, 2, 2, 3, 4, 2, 5]
val = 2
print(f"Original: {numbers}")
print(f"Remove {val}: {remove_element(numbers, val)}")

"""
LIST COMPREHENSION: Pythonic way
ALTERNATIVE: .remove() in loop (modifies original)
"""
print()

# Q43: Reverse words in string
print("Q43: Reverse Words in String")
print("-" * 70)

def reverse_words(s):
    """Reverse order of words"""
    return ' '.join(s.split()[::-1])

text = "Hello World from Python"
print(f"Original: {text}")
print(f"Reversed: {reverse_words(text)}")

"""
LOGIC: Split → Reverse list → Join
split() handles multiple spaces
"""
print()

# Q44: Check substring
print("Q44: Check if Substring Exists")
print("-" * 70)

def contains_substring(s, sub):
    """Check if substring exists"""
    return sub in s

text = "Hello World"
substring = "World"
result = "Yes" if contains_substring(text, substring) else "No"
print(f"'{substring}' in '{text}': {result}")

"""
PYTHONIC: Use 'in' operator
ALTERNATIVE: .find(), .index()
"""
print()

# Q45: Flatten nested list
print("Q45: Flatten Nested List")
print("-" * 70)

def flatten(nested_list):
    """Flatten nested list"""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

nested = [1, [2, 3], [4, [5, 6]], 7]
print(f"Nested: {nested}")
print(f"Flattened: {flatten(nested)}")

"""
RECURSION: Handle arbitrary nesting
ALTERNATIVE: itertools.chain() for simple cases
"""
print()

# Q46: Check if lists are equal
print("Q46: Compare Two Lists")
print("-" * 70)

def are_lists_equal(list1, list2):
    """Check if two lists are equal"""
    return list1 == list2

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2, 4]
print(f"{list1} == {list2}: {are_lists_equal(list1, list2)}")
print(f"{list1} == {list3}: {are_lists_equal(list1, list3)}")

"""
SIMPLE: Use == operator
COMPARES: Values and order
"""
print()

# Q47: Find single non-duplicate
print("Q47: Find Single Number")
print("-" * 70)

def find_single(arr):
    """
    Every element appears twice except one
    Find that single element
    """
    result = 0
    for num in arr:
        result ^= num  # XOR
    return result

numbers = [2, 3, 4, 2, 3]
print(f"Array: {numbers}")
print(f"Single number: {find_single(numbers)}")

"""
XOR TRICK: a ^ a = 0, a ^ 0 = a
All pairs cancel out, single remains
CLEVER SOLUTION!
"""
print()

# Q48: Check if string is rotation
print("Q48: Check String Rotation")
print("-" * 70)

def is_rotation(s1, s2):
    """Check if s2 is rotation of s1"""
    if len(s1) != len(s2):
        return False
    return s2 in (s1 + s1)

s1 = "abcde"
s2 = "cdeab"
result = "Yes" if is_rotation(s1, s2) else "No"
print(f"'{s2}' is rotation of '{s1}': {result}")

"""
CLEVER TRICK: Rotation will be substring of s1+s1
"abcde" + "abcde" = "abcdeabcde"
"cdeab" is in "abcdeabcde"
"""
print()

# Q49: Find majority element
print("Q49: Majority Element")
print("-" * 70)

def find_majority(arr):
    """
    Find element that appears more than n/2 times
    (Boyer-Moore Voting Algorithm)
    """
    candidate = None
    count = 0
    
    # Find candidate
    for num in arr:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    
    # Verify candidate
    if arr.count(candidate) > len(arr) // 2:
        return candidate
    return None

numbers = [2, 2, 1, 1, 1, 2, 2]
print(f"Array: {numbers}")
print(f"Majority element: {find_majority(numbers)}")

"""
BOYER-MOORE ALGORITHM: O(n) time, O(1) space
ELEGANT SOLUTION!
"""
print()

# Q50: Generate all subsets
print("Q50: Generate All Subsets (Power Set)")
print("-" * 70)

def generate_subsets(arr):
    """Generate all subsets of array"""
    result = [[]]
    
    for num in arr:
        result += [subset + [num] for subset in result]
    
    return result

numbers = [1, 2, 3]
subsets = generate_subsets(numbers)
print(f"Array: {numbers}")
print(f"All subsets ({len(subsets)} total):")
for subset in subsets:
    print(f"  {subset}")

"""
POWER SET: 2^n subsets for n elements
ITERATIVE APPROACH: Build incrementally
"""
print()


# ============================================================================
# SUMMARY - MUST KNOW FOR INTERVIEWS
# ============================================================================

print("="*70)
print("SUMMARY - TOP 50 INTERVIEW QUESTIONS")
print("="*70)

print("""
🔥 MOST FREQUENTLY ASKED (Practice These First!):

STRING (10):
1. Reverse string - s[::-1]
2. Check palindrome - s == s[::-1]
3. Anagram check - Counter(s1) == Counter(s2)
4. First non-repeating char - Counter + loop
5. Character frequency - Counter(s)

ARRAY (10):
6. Find max/min - max(), min()
7. Remove duplicates - set() or seen set
8. Second largest - single pass with two variables
9. Reverse array - arr[::-1]
10. Move zeros - two pointers

MATH (10):
11. Check prime - loop up to sqrt(n)
12. Factorial - loop or recursion
13. Fibonacci - F(n) = F(n-1) + F(n-2)
14. Sum of digits - n%10, n//10
15. Armstrong number - sum of powers

LOGIC (10):
16. FizzBuzz - check 15, then 3, then 5
17. Pyramid pattern - spaces + stars
18. Count words - .split()
19. Find duplicates - Counter
20. Linear/Binary search

ADVANCED (10):
21. Two Sum - hash map
22. Flatten list - recursion
23. String rotation - s2 in (s1+s1)
24. Majority element - Boyer-Moore
25. Generate subsets - iterative

💡 INTERVIEW TIPS:

1. ALWAYS CLARIFY:
   - Input constraints (size, range, type)
   - Edge cases (empty, negative, duplicates)
   - Expected output format

2. START SIMPLE:
   - Brute force solution first
   - Then optimize
   - Explain trade-offs

3. THINK ALOUD:
   - Explain your approach
   - Walk through example
   - Mention alternatives

4. TEST YOUR CODE:
   - Normal case
   - Edge cases
   - Large inputs

5. KNOW COMPLEXITIES:
   - State time complexity
   - State space complexity
   - Justify your approach

⏱️ TIME COMPLEXITIES TO KNOW:
O(1) - Hash map lookup, array index
O(log n) - Binary search
O(n) - Linear scan, hash map creation
O(n log n) - Sorting
O(n²) - Nested loops

📚 PYTHON MUST-KNOWS:
- String: .split(), .join(), .replace(), .strip()
- List: .append(), .extend(), slicing, comprehension
- Dict: .get(), .keys(), .values(), .items()
- Set: .add(), .remove(), set operations
- Collections: Counter, defaultdict
- Built-ins: sorted(), reversed(), enumerate(), zip()

🎯 PRACTICE SCHEDULE:
Week 1: String + Array (20 problems)
Week 2: Math + Logic (20 problems)
Week 3: Advanced (10 problems)
Week 4: Random mix, mock interviews

✅ YOU'RE READY WHEN:
- Can solve any problem in 20 minutes
- Can explain multiple approaches
- Know time/space complexities
- Handle edge cases automatically
- Write clean, readable code
""")

print("="*70)
print("MASTER THESE 50 - YOU'LL ACE 90% OF INTERVIEWS!")
print("="*70)
