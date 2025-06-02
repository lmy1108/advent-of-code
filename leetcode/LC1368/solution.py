# My solution:

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = []
        # cost 0 to go with the arrow, or cost 1 to go with three other direction
        # state: (cost, x, y)
        queue.append((0, 0, 0))
        visited = set()
        visited.add((0,0))
        while queue:
            cur_cost, x, y = heapq.popleft()
            if x == m-1 and y == n-1:
                return cur_cost
            if (x,y) in visited:
                continue
            dirs = [[0,1],[-1,0],[0,-1],[1,0]]
            dir_by_num = {1:(0,1),2:(0,-1),3:(1,0),4:(-1,0)}
            for dir in dirs:
                next_x = x + dir[0]
                next_y = y + dir[1]
                if dir_by_num[grid[x][y]] == tuple(dir):
                    heapq.pushleft(cur_cost, next_x, next_y)
                    visited.add((next_x,next_y))
                else:
                    heapq.pushleft(cur_cost+1, next_x, next_y)
            
        return "impossible"
            
