"""
SORTING & GREEDY ALGORITHMS - Essential Problems
=================================================
Topics: Merge Sort, Quick Sort, Intervals, Greedy Choices
Time to master: 2-3 hours
"""

# ============================================================================
# PROBLEM 1: Merge Sort (Divide and Conquer)
# ============================================================================
# Sort array using merge sort
# Time: O(n log n), Space: O(n)

def merge_sort(arr):
    """
    CONCEPT: Divide array in half, recursively sort, merge sorted halves
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    """Merge two sorted arrays"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Test cases
print("Problem 1: Merge Sort")
print(merge_sort([5, 2, 3, 1]))           # [1, 2, 3, 5]
print(merge_sort([5, 1, 1, 2, 0, 0]))     # [0, 0, 1, 1, 2, 5]
print()


# ============================================================================
# PROBLEM 2: Quick Sort (Divide and Conquer)
# ============================================================================
# Sort array using quick sort
# Time: O(n log n) average, O(n²) worst, Space: O(log n)

def quick_sort(arr):
    """
    CONCEPT: Pick pivot, partition around it, recursively sort partitions
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Test cases
print("Problem 2: Quick Sort")
print(quick_sort([3, 6, 8, 10, 1, 2, 1]))  # [1, 1, 2, 3, 6, 8, 10]
print()


# ============================================================================
# PROBLEM 3: Merge Intervals
# ============================================================================
# Merge overlapping intervals
# Example: [[1,3],[2,6],[8,10],[15,18]] → [[1,6],[8,10],[15,18]]
# Time: O(n log n), Space: O(n)

def merge_intervals(intervals):
    """
    CONCEPT: Sort by start time, merge if overlap
    """
    if not intervals:
        return []
    
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        
        if current[0] <= last[1]:  # Overlap
            merged[-1] = [last[0], max(last[1], current[1])]
        else:
            merged.append(current)
    
    return merged

# Test cases
print("Problem 3: Merge Intervals")
print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
# [[1, 6], [8, 10], [15, 18]]
print(merge_intervals([[1, 4], [4, 5]]))  # [[1, 5]]
print()


# ============================================================================
# PROBLEM 4: Meeting Rooms II (Min Rooms Needed)
# ============================================================================
# Find minimum number of meeting rooms required
# Example: [[0,30],[5,10],[15,20]] → 2
# Time: O(n log n), Space: O(n)

def min_meeting_rooms(intervals):
    """
    CONCEPT: Track start and end times separately
    Sort both, count overlaps using two pointers
    """
    if not intervals:
        return 0
    
    starts = sorted([i[0] for i in intervals])
    ends = sorted([i[1] for i in intervals])
    
    rooms = 0
    max_rooms = 0
    s = e = 0
    
    while s < len(starts):
        if starts[s] < ends[e]:
            rooms += 1
            max_rooms = max(max_rooms, rooms)
            s += 1
        else:
            rooms -= 1
            e += 1
    
    return max_rooms

# Test cases
print("Problem 4: Meeting Rooms II")
print(min_meeting_rooms([[0, 30], [5, 10], [15, 20]]))  # 2
print(min_meeting_rooms([[7, 10], [2, 4]]))  # 1
print()


# ============================================================================
# PROBLEM 5: Sort Colors (Dutch National Flag)
# ============================================================================
# Sort array with 0s, 1s, 2s in-place
# Example: [2,0,2,1,1,0] → [0,0,1,1,2,2]
# Time: O(n), Space: O(1)

def sort_colors(nums):
    """
    CONCEPT: Three pointers (low, mid, high)
    - low tracks position for 0s
    - high tracks position for 2s
    - mid scans array
    """
    low = mid = 0
    high = len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

# Test cases
print("Problem 5: Sort Colors")
arr1 = [2, 0, 2, 1, 1, 0]
sort_colors(arr1)
print(arr1)  # [0, 0, 1, 1, 2, 2]
print()


# ============================================================================
# PROBLEM 6: Kth Largest Element (Quick Select)
# ============================================================================
# Find kth largest element in array
# Example: [3,2,1,5,6,4], k=2 → 5
# Time: O(n) average, O(n²) worst, Space: O(1)

def find_kth_largest(nums, k):
    """
    CONCEPT: Quick Select - partition array, recurse on one side
    """
    def partition(left, right, pivot_idx):
        pivot = nums[pivot_idx]
        # Move pivot to end
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        
        store_idx = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_idx], nums[i] = nums[i], nums[store_idx]
                store_idx += 1
        
        # Move pivot to final position
        nums[right], nums[store_idx] = nums[store_idx], nums[right]
        return store_idx
    
    def select(left, right, k_smallest):
        if left == right:
            return nums[left]
        
        pivot_idx = (left + right) // 2
        pivot_idx = partition(left, right, pivot_idx)
        
        if k_smallest == pivot_idx:
            return nums[k_smallest]
        elif k_smallest < pivot_idx:
            return select(left, pivot_idx - 1, k_smallest)
        else:
            return select(pivot_idx + 1, right, k_smallest)
    
    return select(0, len(nums) - 1, len(nums) - k)

# Test cases
print("Problem 6: Kth Largest Element")
print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))  # 5
print(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
print()


# ============================================================================
# PROBLEM 7: Non-overlapping Intervals (Greedy)
# ============================================================================
# Find minimum removals to make intervals non-overlapping
# Example: [[1,2],[2,3],[3,4],[1,3]] → 1 (remove [1,3])
# Time: O(n log n), Space: O(1)

def erase_overlap_intervals(intervals):
    """
    CONCEPT: Greedy - sort by end time, keep earliest ending
    """
    if not intervals:
        return 0
    
    intervals.sort(key=lambda x: x[1])  # Sort by end time
    count = 0
    end = intervals[0][1]
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < end:  # Overlap
            count += 1
        else:
            end = intervals[i][1]
    
    return count

# Test cases
print("Problem 7: Non-overlapping Intervals")
print(erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]))  # 1
print(erase_overlap_intervals([[1, 2], [1, 2], [1, 2]]))  # 2
print()

# ============================================================================
# PROBLEM 8: Jump Game (Greedy)
# ============================================================================
# Can reach last index from first (each element is max jump length)
# Example: [2,3,1,1,4] → True
# Time: O(n), Space: O(1)

def can_jump(nums):
    """
    CONCEPT: Track farthest reachable position
    If current index > farthest, can't reach it
    """
    farthest = 0
    
    for i in range(len(nums)):
        if i > farthest:
            return False
        farthest = max(farthest, i + nums[i])
        
        if farthest >= len(nums) - 1:
            return True
    
    return True

# Test cases
print("Problem 8: Jump Game")
print(can_jump([2, 3, 1, 1, 4]))  # True
print(can_jump([3, 2, 1, 0, 4]))  # False
print()


# ============================================================================
# PROBLEM 9: Gas Station (Greedy)
# ============================================================================
# Find starting gas station to complete circuit
# Example: gas=[1,2,3,4,5], cost=[3,4,5,1,2] → 3
# Time: O(n), Space: O(1)

def can_complete_circuit(gas, cost):
    """
    CONCEPT: If total gas >= total cost, solution exists
    Start from station where tank would have gone negative
    """
    if sum(gas) < sum(cost):
        return -1
    
    tank = 0
    start = 0
    
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        
        if tank < 0:
            start = i + 1
            tank = 0
    
    return start

# Test cases
print("Problem 9: Gas Station")
print(can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))  # 3
print(can_complete_circuit([2, 3, 4], [3, 4, 3]))  # -1
print()


# ============================================================================
# PROBLEM 10: Top K Frequent Elements (Heap/Bucket Sort)
# ============================================================================
# Find k most frequent elements
# Example: [1,1,1,2,2,3], k=2 → [1,2]
# Time: O(n), Space: O(n)

def top_k_frequent(nums, k):
    """
    CONCEPT: Bucket sort by frequency
    Frequency can be at most n, create buckets for each frequency
    """
    from collections import Counter
    
    # Count frequencies
    count = Counter(nums)
    
    # Create buckets
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in count.items():
        buckets[freq].append(num)
    
    # Collect k most frequent
    result = []
    for i in range(len(buckets) - 1, -1, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result
    
    return result

# Test cases
print("Problem 10: Top K Frequent")
print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
print(top_k_frequent([1], 1))  # [1]
print()


# ============================================================================
# SUMMARY - SORTING & GREEDY PATTERNS
# ============================================================================
"""
SORTING ALGORITHMS:

1. MERGE SORT:
   - Stable, guaranteed O(n log n)
   - Good for linked lists
   - Requires O(n) extra space

2. QUICK SORT:
   - In-place, O(n log n) average
   - Unstable, O(n²) worst case
   - Good for arrays

3. COUNTING/BUCKET SORT:
   - O(n) when range is small
   - Use for frequency problems

GREEDY PATTERNS:

1. INTERVAL PROBLEMS:
   - Sort by start or end time
   - Make locally optimal choice
   - Examples: meeting rooms, non-overlapping

2. JUMP/REACH PROBLEMS:
   - Track farthest reachable
   - Make decision at each step

3. OPTIMIZATION PROBLEMS:
   - Prove greedy choice is optimal
   - Sort by some criterion
   - Take best available option

COMMON SORTING APPLICATIONS:
- Intervals: Sort by start/end
- Two pointers: Sort first for O(n) solution
- Binary search: Requires sorted input
- Anagrams: Sort characters as key

KEY INSIGHTS:

1. When to sort?
   - Problem involves ranges/intervals
   - Need to find pairs/triplets
   - Looking for closest/farthest

2. Greedy vs DP?
   - Greedy: local choice leads to global optimum
   - DP: need to consider multiple choices

3. Custom sort keys:
   intervals.sort(key=lambda x: x[1])  # By end time
   words.sort(key=lambda x: (len(x), x))  # By length, then lexicographically

TIME COMPLEXITIES:
- Merge Sort: O(n log n) always
- Quick Sort: O(n log n) average, O(n²) worst
- Counting Sort: O(n + k) where k is range
- Bucket Sort: O(n + k) where k is buckets
- Quick Select: O(n) average for kth element

SPACE COMPLEXITIES:
- Merge Sort: O(n)
- Quick Sort: O(log n) for recursion
- In-place sorts: O(1) extra space
"""
