class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        visited = [False for i in range(0, n+1)]
        res = []
        def dfs(cur, visited):
            if sum(visited) == k:
                res.append(cur[:])
                return
            for i in range(1, n+1):
                if not visited[i]:
                    visited[i] = True
                    cur.append(i)
                    dfs(cur, visited)
                    cur.pop()
                    visited[i] = False
        dfs([], visited)
        return res