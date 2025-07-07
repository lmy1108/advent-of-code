class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
            
        # option1: pick current val
        # option2 not pick current val
        res = []
        visited = set()
        def dfs(nums, index, cur, res):
            if index == len(nums):
                if tuple(cur) not in visited:
                    res.append(cur[:])
                    visited.add(tuple(cur))
                return
            dfs(nums, index+1, cur, res)
            cur.append(nums[index])
            dfs(nums, index+1, cur, res)
            cur.pop()
        dfs(nums, 0, [], res)
        return res
            
