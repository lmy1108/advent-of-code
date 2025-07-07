class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        visited = [False for i in nums]
        res = []

        def dfs(cur, visited):
            if all(visited):
                res.append(cur[:])
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                if not visited[i]:
                    cur.append(nums[i])
                    visited[i] = True
                    dfs(cur, visited)
                    visited[i] = False
                    cur.pop()
        dfs([], visited) 
        return res
                