"""
STACKS & QUEUES - Essential Problems for Interviews
====================================================
Topics: Parentheses Matching, Monotonic Stack, Deque Operations
Time to master: 2 hours
"""

from collections import deque

# ============================================================================
# PROBLEM 1: Valid Parentheses
# ============================================================================
# Check if string of brackets is valid
# Example: "()[]{}" → True, "([)]" → False
# Time: O(n), Space: O(n)

def is_valid_parentheses(s):
    """
    CONCEPT: Use stack for matching pairs
    Push opening brackets, pop and match closing brackets
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:  # Closing bracket
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:  # Opening bracket
            stack.append(char)
    
    return len(stack) == 0

# Test cases
print("Problem 1: Valid Parentheses")
print(is_valid_parentheses("()[]{}"))    # True
print(is_valid_parentheses("([)]"))      # False
print(is_valid_parentheses("{[]}"))      # True
print()


# ============================================================================
# PROBLEM 2: Min Stack (Stack with O(1) min)
# ============================================================================
# Design stack that supports push, pop, top, and retrieving min in O(1)
# Time: O(1) for all operations, Space: O(n)

class MinStack:
    """
    CONCEPT: Keep parallel stack tracking minimums
    Each element stores (value, current_min)
    """
    def __init__(self):
        self.stack = []
    
    def push(self, val):
        if not self.stack:
            self.stack.append((val, val))
        else:
            current_min = min(val, self.stack[-1][1])
            self.stack.append((val, current_min))
    
    def pop(self):
        if self.stack:
            self.stack.pop()
    
    def top(self):
        return self.stack[-1][0] if self.stack else None
    
    def get_min(self):
        return self.stack[-1][1] if self.stack else None

# Test cases
print("Problem 2: Min Stack")
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(f"Min: {min_stack.get_min()}")  # -3
min_stack.pop()
print(f"Top: {min_stack.top()}")      # 0
print(f"Min: {min_stack.get_min()}")  # -2
print()


# ============================================================================
# PROBLEM 3: Daily Temperatures (Monotonic Stack)
# ============================================================================
# For each day, find how many days until warmer temperature
# Example: [73,74,75,71,69,72,76,73] → [1,1,4,2,1,1,0,0]
# Time: O(n), Space: O(n)

def daily_temperatures(temps):
    """
    CONCEPT: Monotonic decreasing stack
    Stack stores indices of temperatures waiting for warmer day
    When we find warmer temp, pop all colder temps and calculate distance
    """
    result = [0] * len(temps)
    stack = []  # Stores indices
    
    for i, temp in enumerate(temps):
        # Pop all colder temperatures
        while stack and temps[stack[-1]] < temp:
            prev_idx = stack.pop()
            result[prev_idx] = i - prev_idx
        
        stack.append(i)
    
    return result

# Test cases
print("Problem 3: Daily Temperatures")
print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# [1, 1, 4, 2, 1, 1, 0, 0]
print(daily_temperatures([30, 40, 50, 60]))  # [1, 1, 1, 0]
print()


# ============================================================================
# PROBLEM 4: Next Greater Element (Monotonic Stack)
# ============================================================================
# For each element, find next greater element
# Example: [4,5,2,25] → [5,25,25,-1]
# Time: O(n), Space: O(n)

def next_greater_elements(arr):
    """
    CONCEPT: Monotonic stack + traverse from right
    Stack maintains elements in decreasing order
    """
    result = [-1] * len(arr)
    stack = []
    
    # Traverse from right to left
    for i in range(len(arr) - 1, -1, -1):
        # Pop smaller elements
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        
        if stack:
            result[i] = stack[-1]
        
        stack.append(arr[i])
    
    return result

# Test cases
print("Problem 4: Next Greater Element")
print(next_greater_elements([4, 5, 2, 25]))  # [5, 25, 25, -1]
print(next_greater_elements([13, 7, 6, 12]))  # [-1, 12, 12, -1]
print()


# ============================================================================
# PROBLEM 5: Largest Rectangle in Histogram (Monotonic Stack)
# ============================================================================
# Find largest rectangular area in histogram
# Example: [2,1,5,6,2,3] → 10 (5x2 rectangle)
# Time: O(n), Space: O(n)

def largest_rectangle_area(heights):
    """
    CONCEPT: Monotonic increasing stack
    When we hit smaller bar, calculate area of all taller bars
    """
    stack = []  # Stores indices
    max_area = 0
    
    for i, h in enumerate(heights):
        # Pop taller bars and calculate their areas
        while stack and heights[stack[-1]] > h:
            height_idx = stack.pop()
            height = heights[height_idx]
            # Width from previous bar to current bar
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        
        stack.append(i)
    
    # Process remaining bars
    while stack:
        height_idx = stack.pop()
        height = heights[height_idx]
        width = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, height * width)
    
    return max_area

# Test cases
print("Problem 5: Largest Rectangle in Histogram")
print(largest_rectangle_area([2, 1, 5, 6, 2, 3]))  # 10
print(largest_rectangle_area([2, 4]))  # 4
print()


# ============================================================================
# PROBLEM 6: Sliding Window Maximum (Deque)
# ============================================================================
# Find maximum in each sliding window of size k
# Example: [1,3,-1,-3,5,3,6,7], k=3 → [3,3,5,5,6,7]
# Time: O(n), Space: O(k)

def max_sliding_window(nums, k):
    """
    CONCEPT: Monotonic decreasing deque
    Deque stores indices, front has max element
    Remove indices outside window and smaller elements
    """
    result = []
    dq = deque()  # Stores indices
    
    for i, num in enumerate(nums):
        # Remove indices outside window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # Remove smaller elements from back
        while dq and nums[dq[-1]] < num:
            dq.pop()
        
        dq.append(i)
        
        # Add to result if window is complete
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result
# Test cases
print("Problem 6: Sliding Window Maximum")
print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))
# [3, 3, 5, 5, 6, 7]
print(max_sliding_window([1], 1))  # [1]
print()


# ============================================================================
# PROBLEM 7: Implement Queue using Stacks
# ============================================================================
# Implement queue using two stacks
# Time: O(1) amortized for all operations, Space: O(n)

class MyQueue:
    """
    CONCEPT: Two stacks - input and output
    Push to input stack
    Pop from output stack (transfer from input if needed)
    """
    def __init__(self):
        self.input_stack = []
        self.output_stack = []
    
    def push(self, x):
        self.input_stack.append(x)
    
    def pop(self):
        self._move_if_needed()
        return self.output_stack.pop() if self.output_stack else None
    
    def peek(self):
        self._move_if_needed()
        return self.output_stack[-1] if self.output_stack else None
    
    def empty(self):
        return len(self.input_stack) == 0 and len(self.output_stack) == 0
    
    def _move_if_needed(self):
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())

# Test cases
print("Problem 7: Queue using Stacks")
q = MyQueue()
q.push(1)
q.push(2)
print(q.peek())   # 1
print(q.pop())    # 1
print(q.empty())  # False
print()


# ============================================================================
# PROBLEM 8: Evaluate Reverse Polish Notation
# ============================================================================
# Evaluate arithmetic expression in postfix notation
# Example: ["2","1","+","3","*"] → ((2+1)*3) = 9
# Time: O(n), Space: O(n)

def eval_rpn(tokens):
    """
    CONCEPT: Stack-based evaluation
    Push numbers, pop operands for operators
    """
    stack = []
    operators = {'+', '-', '*', '/'}
    
    for token in tokens:
        if token in operators:
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:  # Division
                stack.append(int(a / b))  # Truncate toward zero
        else:
            stack.append(int(token))
    
    return stack[0]

# Test cases
print("Problem 8: Evaluate RPN")
print(eval_rpn(["2", "1", "+", "3", "*"]))  # 9
print(eval_rpn(["4", "13", "5", "/", "+"]))  # 6
print()


# ============================================================================
# PROBLEM 9: Remove K Digits (Greedy + Stack)
# ============================================================================
# Remove k digits to make smallest number
# Example: "1432219", k=3 → "1219"
# Time: O(n), Space: O(n)

def remove_k_digits(num, k):
    """
    CONCEPT: Monotonic increasing stack
    Remove larger digits that come before smaller ones
    """
    stack = []
    
    for digit in num:
        # Remove larger digits
        while stack and k > 0 and stack[-1] > digit:
            stack.pop()
            k -= 1
        
        stack.append(digit)
    
    # Remove remaining k digits from end
    stack = stack[:-k] if k > 0 else stack
    
    # Remove leading zeros and return
    result = ''.join(stack).lstrip('0')
    return result if result else '0'

# Test cases
print("Problem 9: Remove K Digits")
print(remove_k_digits("1432219", 3))  # "1219"
print(remove_k_digits("10200", 1))    # "200"
print(remove_k_digits("10", 2))       # "0"
print()


# ============================================================================
# PROBLEM 10: Simplify Path (Stack)
# ============================================================================
# Simplify Unix file path
# Example: "/a/./b/../../c/" → "/c"
# Time: O(n), Space: O(n)

def simplify_path(path):
    """
    CONCEPT: Stack for directory navigation
    ".." = go up (pop), "." = stay (skip), others = go down (push)
    """
    stack = []
    parts = path.split('/')
    
    for part in parts:
        if part == '..' and stack:
            stack.pop()
        elif part and part != '.' and part != '..':
            stack.append(part)
    
    return '/' + '/'.join(stack)

# Test cases
print("Problem 10: Simplify Path")
print(simplify_path("/home/"))                # "/home"
print(simplify_path("/../"))                  # "/"
print(simplify_path("/home//foo/"))           # "/home/foo"
print(simplify_path("/a/./b/../../c/"))       # "/c"
print()


# ============================================================================
# SUMMARY - STACK & QUEUE PATTERNS
# ============================================================================
"""
KEY PATTERNS:

1. MATCHING PROBLEMS:
   - Parentheses, tags, brackets
   - Push opening, pop and match closing

2. MONOTONIC STACK:
   - Next/previous greater/smaller element
   - Stack maintains increasing/decreasing order
   - When violating order, pop and process

3. CALCULATOR/EXPRESSION:
   - Infix, prefix, postfix notation
   - Use stack to track operands and operators

4. TWO STACKS FOR QUEUE:
   - Input stack for push
   - Output stack for pop/peek
   - Transfer when output empty

5. DEQUE FOR SLIDING WINDOW:
   - Track max/min in window
   - Remove out-of-range indices
   - Maintain monotonic property

MONOTONIC STACK TYPES:

# Monotonic Increasing (small to large)
while stack and stack[-1] > current:
    stack.pop()
stack.append(current)
# Use for: Next smaller element

# Monotonic Decreasing (large to small)
while stack and stack[-1] < current:
    stack.pop()
stack.append(current)
# Use for: Next greater element

COMMON OPERATIONS:
- Stack: append(), pop(), [-1] for peek
- Deque: append(), appendleft(), pop(), popleft()
- Queue: enqueue (append), dequeue (popleft)

TIME COMPLEXITIES:
- All basic operations: O(1)
- Monotonic stack problems: O(n) - each element pushed/popped once

COMMON MISTAKES:
1. Not checking if stack is empty before pop
2. Wrong monotonic property (increasing vs decreasing)
3. Storing values instead of indices (lose position info)
4. Not handling edge cases (empty input, k=0, etc.)
"""
