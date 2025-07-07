Looking at your code, I can see the issue. Your approach of using a visited set with tuples works, but it's inefficient and doesn't handle duplicates properly because the order matters when you're building subsets.

The main problem is that you're not sorting the array first, which is crucial for handling duplicates. Here's the corrected version with two approaches:

## Approach 1: Fix your current approach (with visited set)

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # IMPORTANT: Sort first to group duplicates
        res = []
        visited = set()
        
        def dfs(index, cur):
            # Convert to tuple and add to visited/result
            cur_tuple = tuple(cur)
            if cur_tuple not in visited:
                res.append(cur[:])
                visited.add(cur_tuple)
            
            for i in range(index, len(nums)):
                cur.append(nums[i])
                dfs(i + 1, cur)
                cur.pop()
        
        dfs(0, [])
        return res
```

## Approach 2: More efficient solution (avoiding duplicates during generation)

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort to group duplicates together
        res = []
        
        def dfs(index, cur):
            res.append(cur[:])  # Add current subset
            
            for i in range(index, len(nums)):
                # Skip duplicates: if current element equals previous 
                # and we didn't use the previous one
                if i > index and nums[i] == nums[i-1]:
                    continue
                    
                cur.append(nums[i])
                dfs(i + 1, cur)
                cur.pop()
        
        dfs(0, [])
        return res
```

The key improvements:
1. **Sort the array first** - This groups duplicate elements together
2. **Skip duplicates intelligently** - In the second approach, we skip an element if it's the same as the previous one AND we didn't include the previous one in the current branch

The second approach is more efficient because it avoids generating duplicates in the first place, rather than checking against a visited set.

For your example `[1,2,2]`:
- After sorting: `[1,2,2]`
- When we're at the second `2`, if we didn't pick the first `2`, we skip it to avoid duplicates
- This ensures we get `[1,2,2]` but not another `[1,2]` from picking the second `2` alone