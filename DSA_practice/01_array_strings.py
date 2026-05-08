"""
ARRAYS & STRINGS - Essential Problems for Interviews
=====================================================
Topics: Two Pointers, Sliding Window, String Manipulation
Time to master: 2-3 hours
"""

# ============================================================================
# PROBLEM 1: Two Sum (Hash Map Approach)
# ============================================================================
# Given array and target, find two indices that sum to target
# Example: [2,7,11,15], target=9 → [0,1] because 2+7=9
# Time: O(n), Space: O(n)

def two_sum(arr, target):
    """
    CONCEPT: Use hash map to store complements
    Key insight: If we need target, and see x, we look for (target-x)
    """
    seen = {}  # {value: index}
    
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return []

# Test cases
print("Problem 1: Two Sum")
print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
print(two_sum([3, 2, 4], 6))       # [1, 2]
print(two_sum([3, 3], 6))          # [0, 1]
print()


# ============================================================================
# PROBLEM 2: Remove Duplicates from Sorted Array (Two Pointers)
# ============================================================================
# Modify array in-place, return length of unique elements
# Example: [1,1,2] → 2, array becomes [1,2,_]
# Time: O(n), Space: O(1)

def remove_duplicates(arr):
    """
    CONCEPT: Two pointers - slow pointer tracks position for next unique
    Fast pointer scans array
    """
    if not arr:
        return 0
    
    slow = 0  # Position for next unique element
    
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    
    return slow + 1

# Test cases
print("Problem 2: Remove Duplicates")
arr1 = [1, 1, 2]
length = remove_duplicates(arr1)
print(f"Length: {length}, Array: {arr1[:length]}")  # 2, [1, 2]

arr2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
length = remove_duplicates(arr2)
print(f"Length: {length}, Array: {arr2[:length]}")  # 5, [0,1,2,3,4]
print()


# ============================================================================
# PROBLEM 3: Move Zeros to End (Two Pointers)
# ============================================================================
# Move all 0s to end while maintaining order of non-zeros
# Example: [0,1,0,3,12] → [1,3,12,0,0]
# Time: O(n), Space: O(1)

def move_zeros(arr):
    """
    CONCEPT: pos tracks where next non-zero should go
    Swap non-zeros to front, zeros naturally go to back
    """
    pos = 0  # Position for next non-zero
    
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[pos], arr[i] = arr[i], arr[pos]
            pos += 1

# Test cases
print("Problem 3: Move Zeros")
arr1 = [0, 1, 0, 3, 12]
move_zeros(arr1)
print(arr1)  # [1, 3, 12, 0, 0]

arr2 = [0, 0, 1]
move_zeros(arr2)
print(arr2)  # [1, 0, 0]
print()


# ============================================================================
# PROBLEM 4: Maximum Subarray Sum (Kadane's Algorithm)
# ============================================================================
# Find contiguous subarray with largest sum
# Example: [-2,1,-3,4,-1,2,1,-5,4] → 6 (subarray [4,-1,2,1])
# Time: O(n), Space: O(1)

def max_subarray_sum(arr):
    """
    CONCEPT: Kadane's Algorithm
    Keep running sum, if it goes negative, reset to 0
    Track maximum seen so far
    """
    max_sum = float('-inf')
    current_sum = 0
    
    for num in arr:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        
        if current_sum < 0:
            current_sum = 0
    
    return max_sum

# Test cases
print("Problem 4: Maximum Subarray Sum")
print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
print(max_subarray_sum([1]))  # 1
print(max_subarray_sum([5, 4, -1, 7, 8]))  # 23
print()


# ============================================================================
# PROBLEM 5: Valid Palindrome (Two Pointers)
# ============================================================================
# Check if string is palindrome (ignoring non-alphanumeric, case-insensitive)
# Example: "A man, a plan, a canal: Panama" → True
# Time: O(n), Space: O(1)

def is_palindrome(s):
    """
    CONCEPT: Two pointers from both ends
    Skip non-alphanumeric characters, compare characters
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1
        
        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True

# Test cases
print("Problem 5: Valid Palindrome")
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))  # False
print(is_palindrome(" "))  # True
print()


# ============================================================================
# PROBLEM 6: Longest Substring Without Repeating Characters (Sliding Window)
# ============================================================================
# Find length of longest substring without repeating characters
# Example: "abcabcbb" → 3 (substring "abc")
# Time: O(n), Space: O(min(n,m)) where m is charset size

def length_of_longest_substring(s):
    """
    CONCEPT: Sliding Window with Hash Set
    Expand right, if duplicate found, shrink from left
    Track maximum length seen
    """
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # Shrink window until no duplicates
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Test cases
print("Problem 6: Longest Substring Without Repeating")
print(length_of_longest_substring("abcabcbb"))  # 3 ("abc")
print(length_of_longest_substring("bbbbb"))     # 1 ("b")
print(length_of_longest_substring("pwwkew"))    # 3 ("wke")
print()


# ============================================================================
# PROBLEM 7: Container With Most Water (Two Pointers)
# ============================================================================
# Find two lines that form container with maximum water
# Example: [1,8,6,2,5,4,8,3,7] → 49
# Time: O(n), Space: O(1)

def max_area(heights):
    """
    CONCEPT: Two pointers from both ends
    Move pointer with smaller height (can't get bigger area with it)
    """
    left, right = 0, len(heights) - 1
    max_water = 0
    
    while left < right:
        # Calculate current area
        width = right - left
        height = min(heights[left], heights[right])
        max_water = max(max_water, width * height)
        
        # Move pointer with smaller height
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    
    return max_water

# Test cases
print("Problem 7: Container With Most Water")
print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
print(max_area([1, 1]))  # 1
print()

# ============================================================================
# PROBLEM 8: Product of Array Except Self (Prefix/Suffix)
# ============================================================================
# Return array where output[i] = product of all elements except arr[i]
# Example: [1,2,3,4] → [24,12,8,6]
# Time: O(n), Space: O(1) (output array doesn't count)

def product_except_self(arr):
    """
    CONCEPT: Two passes - prefix products and suffix products
    Pass 1: Multiply all elements to the left
    Pass 2: Multiply all elements to the right
    """
    n = len(arr)
    result = [1] * n
    
    # Calculate prefix products
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= arr[i]
    
    # Calculate suffix products and multiply
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= arr[i]
    
    return result

# Test cases
print("Problem 8: Product Except Self")
print(product_except_self([1, 2, 3, 4]))     # [24, 12, 8, 6]
print(product_except_self([-1, 1, 0, -3, 3]))  # [0, 0, 9, 0, 0]
print()


# ============================================================================
# PROBLEM 9: Reverse String (Two Pointers)
# ============================================================================
# Reverse string in-place (list of characters)
# Example: ['h','e','l','l','o'] → ['o','l','l','e','h']
# Time: O(n), Space: O(1)

def reverse_string(s):
    """
    CONCEPT: Two pointers swap from both ends
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# Test cases
print("Problem 9: Reverse String")
arr1 = ['h', 'e', 'l', 'l', 'o']
reverse_string(arr1)
print(''.join(arr1))  # "olleh"

arr2 = ['H', 'a', 'n', 'n', 'a', 'h']
reverse_string(arr2)
print(''.join(arr2))  # "hannaH"
print()


# ============================================================================
# PROBLEM 10: Group Anagrams (Hash Map)
# ============================================================================
# Group strings that are anagrams of each other
# Example: ["eat","tea","tan","ate","nat","bat"] → [["bat"],["nat","tan"],["ate","eat","tea"]]
# Time: O(n*k*log(k)) where n=strings, k=max length, Space: O(n*k)

def group_anagrams(strs):
    """
    CONCEPT: Use sorted string as key in hash map
    All anagrams have same sorted representation
    """
    from collections import defaultdict
    
    groups = defaultdict(list)
    
    for s in strs:
        # Sort string to create key
        key = ''.join(sorted(s))
        groups[key].append(s)
    
    return list(groups.values())

# Test cases
print("Problem 10: Group Anagrams")
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
print()


# ============================================================================
# SUMMARY - KEY PATTERNS TO REMEMBER
# ============================================================================
"""
1. TWO POINTERS:
   - One from each end (palindrome, container)
   - Slow/fast (remove duplicates)
   - Left/right window boundaries (sliding window)

2. SLIDING WINDOW:
   - For substring/subarray problems
   - Expand right, shrink left when condition violated
   - Track max/min during expansion

3. HASH MAP:
   - For O(1) lookups (two sum, anagrams)
   - Count frequencies
   - Track seen elements

4. PREFIX/SUFFIX ARRAYS:
   - Product except self
   - Range sum queries
   - Calculate cumulative results

TIME COMPLEXITIES TO KNOW:
- Two Pointers: O(n)
- Sliding Window: O(n)
- Hash Map operations: O(1) average
- Sorting: O(n log n)

COMMON MISTAKES:
1. Forgetting edge cases (empty array, single element)
2. Off-by-one errors in loops
3. Not handling duplicates
4. Mutating input when not allowed
"""
