Looking at your code, I can see a few issues that need to be fixed:

1. **List mutation problem**: When you append `curList` to `res`, you're appending a reference to the same list object. Since you're modifying `curList` throughout the recursion, all references in `res` will end up pointing to the same empty list.

2. **Incorrect list removal**: `curList.remove(len(curList)-1)` is trying to remove an element with value `len(curList)-1`, not the element at that index. You should use `pop()` instead.

3. **Unused visited set**: You declared a `visited` set but never use it. For this problem, you don't need it since the recursive structure naturally avoids duplicates.

Here's the corrected solution:

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, index, curList, res):
            if index == len(nums):
                res.append(curList[:])  # Create a copy of curList
                return 
            
            # Don't include nums[index]
            dfs(nums, index + 1, curList, res)
            
            # Include nums[index]
            curList.append(nums[index])
            dfs(nums, index + 1, curList, res)
            curList.pop()  # Remove the last element
        
        resList = []
        dfs(nums, 0, [], resList)
        return resList
```

Key changes:
1. `res.append(curList[:])` - Creates a copy of the current list instead of appending a reference
2. `curList.pop()` - Correctly removes the last element from the list
3. Removed the unused `visited` set

The algorithm works by making a binary choice at each index: either include the current element in the subset or don't include it. This naturally generates all 2^n possible subsets without duplicates.

Alternative approach without backtracking (if you're interested):

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(index, path):
            if index == len(nums):
                return [path]
            
            # Don't include nums[index]
            without = dfs(index + 1, path)
            
            # Include nums[index]
            with_current = dfs(index + 1, path + [nums[index]])
            
            return without + with_current
        
        return dfs(0, [])
```

This version creates new lists instead of modifying a shared one, which some find easier to reason about.