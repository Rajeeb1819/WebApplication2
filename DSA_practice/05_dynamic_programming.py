"""
DYNAMIC PROGRAMMING - Essential Problems
=========================================
Topics: Fibonacci, Knapsack, LCS, Subsequences, DP on Strings
Time to master: 3-4 hours (most challenging topic!)
"""

# ============================================================================
# PROBLEM 1: Climbing Stairs (Classic DP Introduction)
# ============================================================================
# Ways to climb n stairs (1 or 2 steps at a time)
# Example: n=3 → 3 ways: (1+1+1), (1+2), (2+1)
# Time: O(n), Space: O(1)

def climb_stairs(n):
    """
    CONCEPT: DP - ways[i] = ways[i-1] + ways[i-2]
    Same as Fibonacci sequence
    """
    if n <= 2:
        return n
    
    prev2, prev1 = 1, 2
    
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    
    return prev1

# Test cases
print("Problem 1: Climbing Stairs")
print(climb_stairs(2))  # 2
print(climb_stairs(3))  # 3
print(climb_stairs(5))  # 8
print()


# ============================================================================
# PROBLEM 2: House Robber (Max Sum Non-Adjacent)
# ============================================================================
# Rob houses to maximize money (can't rob adjacent houses)
# Example: [1,2,3,1] → 4 (rob house 0 and 2)
# Time: O(n), Space: O(1)

def rob(nums):
    """
    CONCEPT: DP - at each house, choose max of:
    - Rob current + max from (i-2)
    - Don't rob current, take max from (i-1)
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    prev2, prev1 = 0, 0
    
    for num in nums:
        current = max(prev1, prev2 + num)
        prev2, prev1 = prev1, current
    
    return prev1

# Test cases
print("Problem 2: House Robber")
print(rob([1, 2, 3, 1]))      # 4
print(rob([2, 7, 9, 3, 1]))   # 12
print()


# ============================================================================
# PROBLEM 3: Longest Increasing Subsequence (LIS)
# ============================================================================
# Find length of longest strictly increasing subsequence
# Example: [10,9,2,5,3,7,101,18] → 4 ([2,3,7,101])
# Time: O(n²), Space: O(n) [O(n log n) solution exists with binary search]

def length_of_lis(nums):
    """
    CONCEPT: dp[i] = longest LIS ending at index i
    For each i, check all j < i: if nums[j] < nums[i], can extend
    """
    if not nums:
        return 0
    
    dp = [1] * len(nums)
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# Test cases
print("Problem 3: Longest Increasing Subsequence")
print(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
print(length_of_lis([0, 1, 0, 3, 2, 3]))  # 4
print()


# ============================================================================
# PROBLEM 4: Coin Change (Minimum Coins)
# ============================================================================
# Fewest coins to make amount (coins can be reused)
# Example: coins=[1,2,5], amount=11 → 3 (5+5+1)
# Time: O(amount * n), Space: O(amount)

def coin_change(coins, amount):
    """
    CONCEPT: dp[i] = min coins to make amount i
    For each amount, try each coin and take minimum
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

# Test cases
print("Problem 4: Coin Change")
print(coin_change([1, 2, 5], 11))  # 3
print(coin_change([2], 3))         # -1
print(coin_change([1], 0))         # 0
print()


# ============================================================================
# PROBLEM 5: 0/1 Knapsack (Classic DP)
# ============================================================================
# Max value with weight limit (each item used once)
# Time: O(n * W), Space: O(n * W)

def knapsack(weights, values, capacity):
    """
    CONCEPT: dp[i][w] = max value using first i items with capacity w
    For each item: take max of (include item, exclude item)
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Don't take item i
            dp[i][w] = dp[i-1][w]
            
            # Take item i (if it fits)
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], 
                              dp[i-1][w - weights[i-1]] + values[i-1])
    
    return dp[n][capacity]

# Test cases
print("Problem 5: 0/1 Knapsack")
print(knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7))  # 9
print()


# ============================================================================
# PROBLEM 6: Longest Common Subsequence (LCS)
# ============================================================================
# Length of longest subsequence common to both strings
# Example: "abcde", "ace" → 3 ("ace")
# Time: O(m * n), Space: O(m * n)

def longest_common_subsequence(text1, text2):
    """
    CONCEPT: dp[i][j] = LCS of text1[0:i] and text2[0:j]
    If chars match: dp[i][j] = dp[i-1][j-1] + 1
    Else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

# Test cases
print("Problem 6: Longest Common Subsequence")
print(longest_common_subsequence("abcde", "ace"))  # 3
print(longest_common_subsequence("abc", "abc"))    # 3
print(longest_common_subsequence("abc", "def"))    # 0
print()


# ============================================================================
# PROBLEM 7: Word Break (DP on Strings)
# ============================================================================
# Can string be segmented into dictionary words?
# Example: s="leetcode", dict=["leet","code"] → True
# Time: O(n² * m), Space: O(n)

def word_break(s, word_dict):
    """
    CONCEPT: dp[i] = can segment s[0:i]
    For each position, check if any word ends there
    """
    word_set = set(word_dict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    
    return dp[len(s)]

# Test cases
print("Problem 7: Word Break")
print(word_break("leetcode", ["leet", "code"]))  # True
print(word_break("applepenapple", ["apple", "pen"]))  # True
print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # False
print()


# ============================================================================
# PROBLEM 8: Partition Equal Subset Sum (Subset Sum)
# ============================================================================
# Can array be partitioned into two equal sum subsets?
# Example: [1,5,11,5] → True (1+5+5=11)
# Time: O(n * sum), Space: O(sum)

def can_partition(nums):
    """
    CONCEPT: If total sum is odd, impossible
    Else, find subset with sum = total/2 (0/1 Knapsack variant)
    """
    total = sum(nums)
    if total % 2 != 0:
        return False
    
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in nums:
        # Traverse backwards to avoid using same element twice
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    
    return dp[target]

# Test cases
print("Problem 8: Partition Equal Subset Sum")
print(can_partition([1, 5, 11, 5]))  # True
print(can_partition([1, 2, 3, 5]))   # False
print()



# ============================================================================
# PROBLEM 9: Unique Paths (Grid DP)
# ============================================================================
# Number of unique paths from top-left to bottom-right (only right/down)
# Example: m=3, n=7 → 28
# Time: O(m * n), Space: O(n)

def unique_paths(m, n):
    """
    CONCEPT: dp[i][j] = paths to reach (i,j)
    dp[i][j] = dp[i-1][j] + dp[i][j-1]
    """
    dp = [1] * n
    
    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j-1]
    
    return dp[n-1]

# Test cases
print("Problem 9: Unique Paths")
print(unique_paths(3, 7))  # 28
print(unique_paths(3, 2))  # 3
print()


# ============================================================================
# PROBLEM 10: Edit Distance (Levenshtein Distance)
# ============================================================================
# Minimum operations to convert word1 to word2
# Operations: insert, delete, replace
# Example: "horse" → "ros" = 3 (replace h→r, remove o, remove e)
# Time: O(m * n), Space: O(m * n)

def min_distance(word1, word2):
    """
    CONCEPT: dp[i][j] = operations to convert word1[0:i] to word2[0:j]
    If chars match: dp[i][j] = dp[i-1][j-1]
    Else: min of (insert, delete, replace) + 1
    """
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # Delete
                    dp[i][j-1],    # Insert
                    dp[i-1][j-1]   # Replace
                )
    
    return dp[m][n]

# Test cases
print("Problem 10: Edit Distance")
print(min_distance("horse", "ros"))  # 3
print(min_distance("intention", "execution"))  # 5
print()


# ============================================================================
# SUMMARY - DYNAMIC PROGRAMMING PATTERNS
# ============================================================================
"""
DP PROBLEM IDENTIFICATION:

1. OPTIMAL SUBSTRUCTURE:
   - Problem can be broken into subproblems
   - Optimal solution uses optimal subproblem solutions

2. OVERLAPPING SUBPROBLEMS:
   - Same subproblems solved multiple times
   - Memoization/tabulation helps

DP PATTERNS:

1. LINEAR DP (1D):
   - Climbing stairs, house robber
   - dp[i] depends on dp[i-1], dp[i-2], etc.
   - Often space optimized to O(1)

2. KNAPSACK (0/1 or Unbounded):
   - Coin change, partition sum
   - dp[i][w] for items and weights
   - Space optimize to O(w) by going backwards

3. LCS/LIS (2D):
   - Longest common subsequence
   - Edit distance
   - dp[i][j] for two sequences

4. INTERVAL DP:
   - Burst balloons, matrix chain
   - dp[i][j] for subarray [i:j]

5. STATE MACHINE DP:
   - Stock prices with states
   - dp[i][state] for position and state

DECISION TREE:
- Can break into subproblems? → Consider DP
- Overlapping subproblems? → Use memoization
- Need all values? → Use tabulation (bottom-up)
- Only need few values? → Use recursion + memo

TOP-DOWN (MEMOIZATION):
def solve(params):
    if params in memo:
        return memo[params]
    # Compute result
    memo[params] = result
    return result

BOTTOM-UP (TABULATION):
dp = [0] * n
for i in range(n):
    dp[i] = compute_from_previous(dp)

SPACE OPTIMIZATION:
- If dp[i] only depends on dp[i-1], dp[i-2]
- Use variables instead of array
- Save space from O(n) to O(1)

TIME COMPLEXITIES:
- 1D DP: O(n)
- 2D DP: O(n * m)
- Knapsack: O(n * capacity)
- LCS/Edit Distance: O(m * n)

COMMON MISTAKES:
1. Not identifying base cases correctly
2. Wrong iteration order (especially for space optimization)
3. Off-by-one errors in indices
4. Forgetting to initialize dp array
5. Not considering all transition possibilities

PRACTICE STRATEGY:
1. Start with Fibonacci/Climbing Stairs
2. Move to linear DP (house robber)
3. Try 2D DP (LCS, edit distance)
4. Practice Knapsack variants
5. Master by doing 20+ problems
"""
