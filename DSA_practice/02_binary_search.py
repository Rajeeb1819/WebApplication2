"""
BINARY SEARCH - Essential Problems for Interviews
==================================================
Topics: Classic BS, Search in Rotated Array, Matrix Search
Time to master: 2 hours
"""

# ============================================================================
# PROBLEM 1: Binary Search (Classic)
# ============================================================================
# Find target in sorted array, return index or -1
# Example: [1,2,3,4,5], target=4 → 3
# Time: O(log n), Space: O(1)

def binary_search(arr, target):
    """
    CONCEPT: Divide and conquer
    Compare middle element:
    - If equal: found
    - If target > mid: search right half
    - If target < mid: search left half
    """
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

# Test cases
print("Problem 1: Binary Search")
print(binary_search([1, 2, 3, 4, 5], 4))    # 3
print(binary_search([1, 2, 3, 4, 5], 6))    # -1
print(binary_search([1], 1))                # 0
print()


# ============================================================================
# PROBLEM 2: First and Last Position in Sorted Array
# ============================================================================
# Find starting and ending position of target
# Example: [5,7,7,8,8,10], target=8 → [3,4]
# Time: O(log n), Space: O(1)

def search_range(arr, target):
    """
    CONCEPT: Two binary searches
    1. Find leftmost (first) occurrence
    2. Find rightmost (last) occurrence
    """
    def find_bound(is_first):
        left, right = 0, len(arr) - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] == target:
                result = mid
                if is_first:
                    right = mid - 1  # Continue searching left
                else:
                    left = mid + 1   # Continue searching right
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    
    first = find_bound(True)
    last = find_bound(False)
    
    return [first, last]

# Test cases
print("Problem 2: First and Last Position")
print(search_range([5, 7, 7, 8, 8, 10], 8))  # [3, 4]
print(search_range([5, 7, 7, 8, 8, 10], 6))  # [-1, -1]
print(search_range([], 0))                    # [-1, -1]
print()


# ============================================================================
# PROBLEM 3: Search in Rotated Sorted Array
# ============================================================================
# Array was sorted then rotated. Find target.
# Example: [4,5,6,7,0,1,2], target=0 → 4
# Time: O(log n), Space: O(1)

def search_rotated(arr, target):
    """
    CONCEPT: Modified binary search
    One half is always sorted - use it to determine which side to search
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        
        # Determine which side is sorted
        if arr[left] <= arr[mid]:  # Left side is sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1  # Target in left sorted portion
            else:
                left = mid + 1
        else:  # Right side is sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1  # Target in right sorted portion
            else:
                right = mid - 1
    
    return -1

# Test cases
print("Problem 3: Search in Rotated Array")
print(search_rotated([4, 5, 6, 7, 0, 1, 2], 0))  # 4
print(search_rotated([4, 5, 6, 7, 0, 1, 2], 3))  # -1
print(search_rotated([1], 0))                     # -1
print()


# ============================================================================
# PROBLEM 4: Find Minimum in Rotated Sorted Array
# ============================================================================
# Array was sorted then rotated. Find minimum element.
# Example: [3,4,5,1,2] → 1
# Time: O(log n), Space: O(1)

def find_min_rotated(arr):
    """
    CONCEPT: Binary search for inflection point
    Minimum is where rotation happened
    Compare mid with right to determine which side has rotation
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] > arr[right]:
            # Minimum is in right half
            left = mid + 1
        else:
            # Minimum is in left half (including mid)
            right = mid
    
    return arr[left]

# Test cases
print("Problem 4: Find Minimum in Rotated Array")
print(find_min_rotated([3, 4, 5, 1, 2]))  # 1
print(find_min_rotated([4, 5, 6, 7, 0, 1, 2]))  # 0
print(find_min_rotated([11, 13, 15, 17]))  # 11
print()


# ============================================================================
# PROBLEM 5: Search 2D Matrix
# ============================================================================
# Matrix sorted row-wise and column-wise. Search for target.
# Example: [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=3 → True
# Time: O(log(m*n)), Space: O(1)

def search_matrix(matrix, target):
    """
    CONCEPT: Treat 2D matrix as 1D sorted array
    Convert index to row/col: row = idx // cols, col = idx % cols
    """
    if not matrix or not matrix[0]:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_value = matrix[mid // cols][mid % cols]
        
        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

# Test cases
print("Problem 5: Search 2D Matrix")
matrix1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
print(search_matrix(matrix1, 3))   # True
print(search_matrix(matrix1, 13))  # False
print()

# ============================================================================
# PROBLEM 6: Find Peak Element
# ============================================================================
# Peak is element greater than neighbors. Find any peak.
# Example: [1,2,3,1] → 2 (index where value is 3)
# Time: O(log n), Space: O(1)

def find_peak_element(arr):
    """
    CONCEPT: Binary search on slope
    If arr[mid] < arr[mid+1], peak is on right (going upward)
    Otherwise, peak is on left (going downward or at peak)
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] < arr[mid + 1]:
            # Going upward, peak on right
            left = mid + 1
        else:
            # Going downward or at peak
            right = mid
    
    return left

# Test cases
print("Problem 6: Find Peak Element")
print(find_peak_element([1, 2, 3, 1]))     # 2
print(find_peak_element([1, 2, 1, 3, 5, 6, 4]))  # 1 or 5
print()


# ============================================================================
# PROBLEM 7: Square Root (Integer)
# ============================================================================
# Find integer square root (floor of sqrt)
# Example: x=8 → 2 (because 2^2=4 < 8 < 9=3^2)
# Time: O(log n), Space: O(1)

def my_sqrt(x):
    """
    CONCEPT: Binary search on answer
    Search range [0, x] for largest num where num*num <= x
    """
    if x < 2:
        return x
    
    left, right = 1, x // 2
    
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        
        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return right  # Floor of square root

# Test cases
print("Problem 7: Square Root")
print(my_sqrt(4))   # 2
print(my_sqrt(8))   # 2
print(my_sqrt(16))  # 4
print()


# ============================================================================
# PROBLEM 8: Kth Smallest Element in Sorted Matrix
# ============================================================================
# Matrix sorted row-wise and column-wise. Find kth smallest.
# Example: [[1,5,9],[10,11,13],[12,13,15]], k=8 → 13
# Time: O(n*log(max-min)), Space: O(1)

def kth_smallest(matrix, k):
    """
    CONCEPT: Binary search on value range
    Count how many elements <= mid
    """
    def count_less_equal(mid):
        count = 0
        col = len(matrix[0]) - 1
        
        for row in range(len(matrix)):
            while col >= 0 and matrix[row][col] > mid:
                col -= 1
            count += (col + 1)
        
        return count
    
    left, right = matrix[0][0], matrix[-1][-1]
    
    while left < right:
        mid = (left + right) // 2
        
        if count_less_equal(mid) < k:
            left = mid + 1
        else:
            right = mid
    
    return left

# Test cases
print("Problem 8: Kth Smallest in Matrix")
matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
print(kth_smallest(matrix, 8))  # 13
print()


# ============================================================================
# SUMMARY - BINARY SEARCH PATTERNS
# ============================================================================
"""
KEY PATTERNS:

1. CLASSIC BINARY SEARCH:
   - Sorted array, find exact match
   - Template: while left <= right

2. FINDING BOUNDARIES:
   - First/last occurrence
   - Continue searching after finding target

3. ROTATED ARRAY:
   - Identify which half is sorted
   - Use sorted half to determine search direction

4. BINARY SEARCH ON ANSWER:
   - When searching for optimal value in range
   - Examples: sqrt, capacity problems

5. 2D MATRIX:
   - Treat as 1D: idx = row*cols + col
   - Or use staircase search from top-right

TEMPLATES:

# Standard Binary Search
while left <= right:
    mid = (left + right) // 2
    if found:
        return mid
    elif need_right:
        left = mid + 1
    else:
        right = mid - 1

# Finding Boundary
while left < right:
    mid = (left + right) // 2
    if condition:
        right = mid  # or left = mid + 1
    else:
        left = mid + 1  # or right = mid - 1

COMMON MISTAKES:
1. Integer overflow with (left + right) // 2
   - Better: left + (right - left) // 2
2. Infinite loop with wrong mid calculation
3. Off-by-one errors in boundary conditions
4. Not handling empty array

TIME COMPLEXITY:
- Binary Search: O(log n)
- Each iteration cuts search space in half
- n → n/2 → n/4 → ... → 1
- Number of steps = log₂(n)
"""
