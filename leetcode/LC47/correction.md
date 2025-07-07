Looking at your code, there are a couple of issues that need to be fixed:

1. **Missing sort**: To properly skip duplicates, the array needs to be sorted first.
2. **Incorrect duplicate skipping logic**: The condition `if i > 0 and nums[i] == nums[i-1]: continue` will skip ALL occurrences of duplicates, not just the ones that would create duplicate permutations. You need to check if the previous duplicate was used.

Here's the corrected solution:

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort to group duplicates together
        visited = [False] * len(nums)
        res = []

        def dfs(cur, visited):
            if len(cur) == len(nums):  # More efficient than all(visited)
                res.append(cur[:])
                return
            
            for i in range(len(nums)):
                # Skip if already used
                if visited[i]:
                    continue
                
                # Skip duplicates: if previous duplicate exists and wasn't used
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue
                
                cur.append(nums[i])
                visited[i] = True
                dfs(cur, visited)
                visited[i] = False
                cur.pop()
        
        dfs([], visited) 
        return res
```

Key changes:
1. **Added `nums.sort()`** - Essential for the duplicate-skipping logic to work
2. **Fixed duplicate skipping**: `if i > 0 and nums[i] == nums[i-1] and not visited[i-1]` - This ensures we only use duplicates in a specific order (left to right), preventing duplicate permutations
3. **Optimization**: Changed `all(visited)` to `len(cur) == len(nums)` for better performance

**Why the duplicate skipping works:**
- When we have duplicates like `[1, 1, 2]`, we ensure that the second `1` can only be used if the first `1` is already in use
- This prevents generating the same permutation through different paths
- For example, without this check, we could get `[1,2,1]` by using either the first or second `1` in the first position

Alternative approach using a counter (sometimes cleaner for problems with duplicates):

```python
from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        counter = Counter(nums)
        
        def dfs(cur):
            if len(cur) == len(nums):
                res.append(cur[:])
                return
            
            for num in counter:
                if counter[num] > 0:
                    cur.append(num)
                    counter[num] -= 1
                    dfs(cur)
                    cur.pop()
                    counter[num] += 1
        
        dfs([])
        return res
```

This approach naturally handles duplicates by tracking counts instead of positions.