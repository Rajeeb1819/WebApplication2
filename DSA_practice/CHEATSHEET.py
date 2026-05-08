"""
QUICK REFERENCE CHEAT SHEET - Print This Before Test!
======================================================
Last-minute review of essential concepts
"""

print("="*70)
print("PYTHON DSA CHEAT SHEET FOR INTERVIEWS")
print("="*70)

# ============================================================================
# TIME COMPLEXITY BY INPUT SIZE
# ============================================================================
print("""
TIME COMPLEXITY TARGETS:
------------------------
n ≤ 10        → O(n!) permutations, brute force
n ≤ 20        → O(2^n) subsets, backtracking
n ≤ 500       → O(n³) triple nested loops
n ≤ 5,000     → O(n²) nested loops, bubble sort
n ≤ 100,000   → O(n log n) merge sort, heap
n ≤ 1,000,000 → O(n) hash map, two pointers
n > 1,000,000 → O(log n) binary search

""")

# ============================================================================
# PATTERN RECOGNITION
# ============================================================================
print("""
PATTERN RECOGNITION:
--------------------
"sorted array" → Binary Search
"subarray/substring with condition" → Sliding Window
"two elements sum to target" → Two Pointers or Hash Map
"k-th smallest/largest" → Heap or Quick Select
"longest/shortest path" → BFS/DP
"matching pairs" → Stack
"next greater/smaller" → Monotonic Stack
"count ways to..." → Dynamic Programming
"intervals" → Sort + Greedy
"can partition..." → DP/Backtracking

""")

# ============================================================================
# TEMPLATES
# ============================================================================
print("""
ESSENTIAL TEMPLATES:
--------------------

1. TWO POINTERS:
   left, right = 0, len(arr) - 1
   while left < right:
       if condition:
           left += 1
       else:
           right -= 1

2. SLIDING WINDOW:
   left = 0
   for right in range(len(arr)):
       # expand window
       while not valid:
           # shrink from left
           left += 1

3. BINARY SEARCH:
   left, right = 0, len(arr) - 1
   while left <= right:
       mid = (left + right) // 2
       if arr[mid] == target:
           return mid
       elif arr[mid] < target:
           left = mid + 1
       else:
           right = mid - 1

4. MONOTONIC STACK (Next Greater):
   stack = []
   for i in range(len(arr) - 1, -1, -1):
       while stack and stack[-1] <= arr[i]:
           stack.pop()
       result[i] = stack[-1] if stack else -1
       stack.append(arr[i])

5. DP (1D):
   dp = [0] * (n + 1)
   dp[0] = base_case
   for i in range(1, n + 1):
       dp[i] = transition(dp[i-1], dp[i-2])

6. DP (2D):
   dp = [[0] * (m+1) for _ in range(n+1)]
   for i in range(1, n+1):
       for j in range(1, m+1):
           dp[i][j] = transition()

""")

# ============================================================================
# PYTHON ESSENTIALS
# ============================================================================
print("""
PYTHON QUICK REFERENCE:
-----------------------

IMPORTS:
from collections import Counter, defaultdict, deque
import heapq

LIST:
arr.append(x)           # O(1)
arr.pop()               # O(1)
arr.insert(i, x)        # O(n)
arr.remove(x)           # O(n)
arr.sort()              # O(n log n)
sorted(arr)             # returns new list

STRING:
s.split()               # split by space
s.strip()               # remove whitespace
s.lower() / s.upper()
s.isalnum() / s.isdigit() / s.isalpha()
''.join(arr)            # join list to string

DICT:
d.get(key, default)
d.setdefault(key, default)
Counter(arr)            # count frequencies
defaultdict(int)        # default value 0

SET:
s.add(x)                # O(1)
s.remove(x)             # O(1)
x in s                  # O(1)

COMPREHENSIONS:
[x*2 for x in arr if x > 0]
{x: x**2 for x in range(5)}
{x for x in arr if x % 2 == 0}

SORTING:
sorted(arr, key=lambda x: x[1])
arr.sort(key=len)

SLICING:
arr[::-1]               # reverse
arr[::2]                # every 2nd element
arr[-3:]                # last 3 elements

OTHERS:
enumerate(arr)          # (index, value) pairs
zip(arr1, arr2)         # pair elements
map(func, arr)          # apply function
filter(func, arr)       # keep matching

""")

# ============================================================================
# EDGE CASES CHECKLIST
# ============================================================================
print("""
EDGE CASES TO TEST:
-------------------
☐ Empty input ([], "", None)
☐ Single element [1]
☐ Two elements [1, 2]
☐ All same elements [5, 5, 5, 5]
☐ Sorted array [1, 2, 3, 4]
☐ Reverse sorted [4, 3, 2, 1]
☐ Negative numbers [-1, -2, 0, 1]
☐ Duplicates [1, 2, 2, 3]
☐ Very large/small values (10^9, -10^9)

""")

# ============================================================================
# TEST DAY STRATEGY
# ============================================================================
print("""
TEST DAY STRATEGY:
------------------
1. Read ALL problems first (5 min)
2. Solve EASIEST problems first
3. Don't spend >10 min stuck on one problem
4. Write BRUTE FORCE if stuck (partial credit!)
5. Add COMMENTS explaining logic
6. Test with EDGE CASES

PER PROBLEM (20 min target):
- Understand (2 min)
- Plan & identify pattern (3 min)
- Code (10 min)
- Test (3 min)
- Review (2 min)

TIME MANAGEMENT (90 min, 4 problems):
- Problem 1 (Easy): 15 min
- Problem 2 (Medium): 20 min
- Problem 3 (Medium): 25 min
- Problem 4 (Hard): 30 min

""")

# ============================================================================
# COMPLEXITY REFERENCE
# ============================================================================
print("""
OPERATION COMPLEXITIES:
-----------------------
O(1):  dict/set access, list append/pop
O(log n):  binary search, balanced tree
O(n):  linear scan, hash map creation
O(n log n):  merge sort, heap operations
O(n²):  nested loops, bubble sort

SPACE COMPLEXITY:
- Hash Map: O(n)
- Recursion: O(depth)
- DP table: O(n) or O(n*m)
- In-place: O(1)

""")

# ============================================================================
# COMMON MISTAKES
# ============================================================================
print("""
AVOID THESE MISTAKES:
---------------------
❌ Not reading problem fully
❌ Jumping to code without plan
❌ Ignoring constraints (n size!)
❌ Poor variable names (use left/right, not i/j)
❌ Not handling edge cases
❌ Off-by-one errors
❌ Not testing before submitting
❌ Wasting time on one problem

""")

# ============================================================================
# FINAL CHECKLIST
# ============================================================================
print("""
FINAL CHECKLIST:
----------------
☐ I know Two Pointers template
☐ I know Sliding Window template  
☐ I know Binary Search template
☐ I understand Monotonic Stack
☐ I can identify DP problems
☐ I know when to use Hash Map
☐ I'm familiar with Python built-ins
☐ I will test edge cases
☐ I will manage my time
☐ I will stay calm!

""")

print("="*70)
print("YOU'VE GOT THIS! 🚀 STAY CALM AND CODE ON!")
print("="*70)
