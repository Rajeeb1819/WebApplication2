"""
PYTHON ESSENTIALS FOR CODING INTERVIEWS
========================================
Must-know Python tricks, built-ins, and patterns for fast coding
Time to master: 1-2 hours
"""

# ============================================================================
# SECTION 1: ESSENTIAL BUILT-IN FUNCTIONS
# ============================================================================

print("="*70)
print("SECTION 1: ESSENTIAL BUILT-INS")
print("="*70)

# enumerate() - Get index and value
arr = ['a', 'b', 'c']
for i, val in enumerate(arr):
    print(f"{i}: {val}")
print()

# zip() - Iterate multiple lists together
names = ['Alice', 'Bob']
scores = [95, 87]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
print()

# map() - Apply function to all elements
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(f"Squared: {squared}")
print()

# filter() - Keep elements matching condition
evens = list(filter(lambda x: x % 2 == 0, nums))
print(f"Evens: {evens}")
print()

# sum(), min(), max(), all(), any()
print(f"Sum: {sum(nums)}")
print(f"Min: {min(nums)}")
print(f"Max: {max(nums)}")
print(f"All positive: {all(x > 0 for x in nums)}")
print(f"Any even: {any(x % 2 == 0 for x in nums)}")
print()


# ============================================================================
# SECTION 2: LIST COMPREHENSIONS (FAST AND READABLE)
# ============================================================================

print("="*70)
print("SECTION 2: LIST COMPREHENSIONS")
print("="*70)

# Basic list comprehension
squares = [x**2 for x in range(5)]
print(f"Squares: {squares}")

# With condition
evens = [x for x in range(10) if x % 2 == 0]
print(f"Evens: {evens}")

# Nested comprehension (2D matrix)
matrix = [[i*j for j in range(3)] for i in range(3)]
print(f"Matrix: {matrix}")

# Flatten 2D list
flat = [num for row in matrix for num in row]
print(f"Flattened: {flat}")

# Dictionary comprehension
char_count = {char: ord(char) for char in 'abc'}
print(f"Char codes: {char_count}")

# Set comprehension
unique_lengths = {len(word) for word in ['cat', 'dog', 'bird']}
print(f"Unique lengths: {unique_lengths}")
print()


# ============================================================================
# SECTION 3: STRING OPERATIONS
# ============================================================================

print("="*70)
print("SECTION 3: STRING OPERATIONS")
print("="*70)

s = "Hello World"

# Common string methods
print(f"Lower: {s.lower()}")
print(f"Upper: {s.upper()}")
print(f"Strip: '  hello  '.strip() = '{'  hello  '.strip()}'")
print(f"Replace: {s.replace('World', 'Python')}")
print(f"Split: {s.split()}")
print(f"Join: {'-'.join(['a', 'b', 'c'])}")

# String checking
print(f"Is alphanumeric: {'abc123'.isalnum()}")
print(f"Is digit: {'123'.isdigit()}")
print(f"Is alpha: {'abc'.isalpha()}")

# String slicing
print(f"Reverse: {s[::-1]}")
print(f"First 5: {s[:5]}")
print(f"Last 5: {s[-5:]}")
print()


# ============================================================================
# SECTION 4: COLLECTIONS MODULE
# ============================================================================

print("="*70)
print("SECTION 4: COLLECTIONS MODULE")
print("="*70)

from collections import Counter, defaultdict, deque

# Counter - Count frequencies
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
counter = Counter(words)
print(f"Frequencies: {counter}")
print(f"Most common 2: {counter.most_common(2)}")

# defaultdict - Dictionary with default values
dd = defaultdict(int)
for word in words:
    dd[word] += 1
print(f"DefaultDict: {dict(dd)}")

# defaultdict with list
graph = defaultdict(list)
graph['A'].append('B')
graph['A'].append('C')
print(f"Graph: {dict(graph)}")

# deque - Double-ended queue (O(1) operations at both ends)
dq = deque([1, 2, 3])
dq.append(4)       # Add to right
dq.appendleft(0)   # Add to left
print(f"Deque: {dq}")
dq.pop()           # Remove from right
dq.popleft()       # Remove from left
print(f"After pops: {dq}")
print()


# ============================================================================
# SECTION 5: SORTING & SORTING KEYS
# ============================================================================

print("="*70)
print("SECTION 5: SORTING")
print("="*70)

# Basic sorting
arr = [3, 1, 4, 1, 5]
print(f"Sorted: {sorted(arr)}")
print(f"Reverse: {sorted(arr, reverse=True)}")

# Sort strings by length
words = ['python', 'is', 'awesome']
print(f"By length: {sorted(words, key=len)}")

# Sort by custom key (tuples - multiple criteria)
students = [('Alice', 25), ('Bob', 20), ('Charlie', 25)]
by_age_then_name = sorted(students, key=lambda x: (x[1], x[0]))
print(f"Students sorted: {by_age_then_name}")

# Sort dictionary by value
scores = {'Alice': 95, 'Bob': 87, 'Charlie': 92}
sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
print(f"Sorted scores: {sorted_scores}")
print()


# ============================================================================
# SECTION 6: SLICING TRICKS
# ============================================================================

print("="*70)
print("SECTION 6: SLICING TRICKS")
print("="*70)

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"Original: {arr}")
print(f"First 5: {arr[:5]}")
print(f"Last 5: {arr[-5:]}")
print(f"Middle: {arr[3:7]}")
print(f"Every 2nd: {arr[::2]}")
print(f"Reverse: {arr[::-1]}")
print(f"Every 2nd reversed: {arr[::-2]}")

# Shallow copy
copy = arr[:]
print(f"Copy: {copy}")
print()


# ============================================================================
# SECTION 7: UNPACKING & SWAPPING
# ============================================================================

print("="*70)
print("SECTION 7: UNPACKING & SWAPPING")
print("="*70)

# Tuple unpacking
a, b, c = 1, 2, 3
print(f"a={a}, b={b}, c={c}")

# Extended unpacking
first, *middle, last = [1, 2, 3, 4, 5]
print(f"First: {first}, Middle: {middle}, Last: {last}")

# Swap without temp variable
a, b = 5, 10
print(f"Before: a={a}, b={b}")
a, b = b, a
print(f"After: a={a}, b={b}")

# Multiple assignment
x = y = z = 0
print(f"x={x}, y={y}, z={z}")
print()


# ============================================================================
# SECTION 8: BITWISE OPERATIONS
# ============================================================================

print("="*70)
print("SECTION 8: BITWISE OPERATIONS")
print("="*70)

a, b = 5, 3  # 101, 011 in binary

print(f"AND: {a & b}")   # 001 = 1
print(f"OR: {a | b}")    # 111 = 7
print(f"XOR: {a ^ b}")   # 110 = 6
print(f"NOT: {~a}")      # -6 (two's complement)
print(f"Left shift: {a << 1}")   # 1010 = 10
print(f"Right shift: {a >> 1}")  # 10 = 2

# Common bit tricks
n = 8
print(f"Is power of 2: {n & (n-1) == 0}")  # True for 8
print(f"Count set bits: {bin(7).count('1')}")  # 3 (111)
print(f"Toggle bit: {5 ^ 1}")  # Toggle last bit: 101 → 100 = 4
print()


# ============================================================================
# SECTION 9: LAMBDA & FUNCTIONAL PROGRAMMING
# ============================================================================

print("="*70)
print("SECTION 9: LAMBDA FUNCTIONS")
print("="*70)

# Lambda basics
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

add = lambda a, b: a + b
print(f"3 + 4 = {add(3, 4)}")

# Lambda with map/filter/sorted
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))
print(f"Doubled: {doubled}")

evens = list(filter(lambda x: x % 2 == 0, nums))
print(f"Evens: {evens}")

# Reduce (need to import)
from functools import reduce
product = reduce(lambda x, y: x * y, nums)
print(f"Product: {product}")
print()


# ============================================================================
# SECTION 10: COMMON PATTERNS & TEMPLATES
# ============================================================================

print("="*70)
print("SECTION 10: COMMON PATTERNS")
print("="*70)

# Two pointers
def two_pointers_template(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        # Process arr[left] and arr[right]
        left += 1
        right -= 1

# Sliding window
def sliding_window_template(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Binary search
def binary_search_template(arr, target):
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

# DFS on graph
def dfs_template(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        
        visited.add(node)
        for neighbor in graph[node]:
            stack.append(neighbor)
    
    return visited

# BFS on graph
def bfs_template(graph, start):
    from collections import deque
    visited = set([start])
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return visited

print("Templates defined (not executed)")
print()


# ============================================================================
# SECTION 11: HANDY TRICKS
# ============================================================================

print("="*70)
print("SECTION 11: HANDY TRICKS")
print("="*70)

# Infinity
pos_inf = float('inf')
neg_inf = float('-inf')
print(f"Infinity: {pos_inf}, {neg_inf}")

# Multiple conditions
x = 5
if 3 < x < 10:
    print(f"{x} is between 3 and 10")

# Ternary operator
result = "even" if x % 2 == 0 else "odd"
print(f"{x} is {result}")

# Check if all elements same
arr = [1, 1, 1, 1]
print(f"All same: {len(set(arr)) == 1}")

# Get max with index
nums = [3, 7, 2, 9, 5]
max_val = max(nums)
max_idx = nums.index(max_val)
print(f"Max {max_val} at index {max_idx}")

# String to list and back
s = "hello"
chars = list(s)
s_back = ''.join(chars)
print(f"String → List → String: {s} → {chars} → {s_back}")

# Count occurrences
arr = [1, 2, 2, 3, 3, 3]
print(f"Count of 3: {arr.count(3)}")
print()


# ============================================================================
# SECTION 12: INPUT/OUTPUT FOR COMPETITIVE PROGRAMMING
# ============================================================================

print("="*70)
print("SECTION 12: INPUT/OUTPUT PATTERNS")
print("="*70)

# Common input patterns (examples, not executed)
print("""
# Single integer
n = int(input())

# Multiple integers on one line
a, b, c = map(int, input().split())

# List of integers
arr = list(map(int, input().split()))

# Multiple lines
n = int(input())
for _ in range(n):
    line = input().strip()

# Matrix input
n, m = map(int, input().split())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Fast output
print(*arr)  # Print list elements space-separated
print('\\n'.join(map(str, arr)))  # Print each on new line
""")


# ============================================================================
# SUMMARY - PYTHON INTERVIEW CHEATSHEET
# ============================================================================
print("="*70)
print("QUICK REFERENCE")
print("="*70)
print("""
ESSENTIAL IMPORTS:
from collections import Counter, defaultdict, deque
from functools import reduce
import heapq

LIST OPERATIONS:
arr.append(x)      # O(1) add to end
arr.pop()          # O(1) remove from end
arr.insert(i, x)   # O(n) insert at position
arr.remove(x)      # O(n) remove first occurrence
arr.index(x)       # O(n) find index
arr.count(x)       # O(n) count occurrences
arr.sort()         # O(n log n) in-place
sorted(arr)        # O(n log n) returns new list

STRING OPERATIONS:
s.split()          # Split by whitespace
s.strip()          # Remove leading/trailing whitespace
s.replace(old, new)
s.lower() / s.upper()
s.isalnum() / s.isdigit() / s.isalpha()
''.join(arr)       # Join list into string

DICT OPERATIONS:
d.get(key, default)
d.setdefault(key, default)
d.keys() / d.values() / d.items()
d.pop(key)
key in d           # O(1) membership

SET OPERATIONS:
s.add(x)           # O(1)
s.remove(x)        # O(1), raises error if not found
s.discard(x)       # O(1), no error if not found
s1 & s2            # Intersection
s1 | s2            # Union
s1 - s2            # Difference

TIME COMPLEXITIES:
List append/pop: O(1)
List insert/remove: O(n)
Dict/Set operations: O(1) average
Sorting: O(n log n)
Binary search: O(log n)
""")
