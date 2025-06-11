class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        matrix = [[0 for j in range(n)] for i in range(m)]
        queue = deque()

        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    queue.append((i, j))
        visited = set()
        while queue:
            x, y = queue.popleft()
            visited.add((x,y))
            dirs = [[0,1],[0,-1],[1,0],[-1,0]]
            for dir in dirs:
                nextX, nextY = x + dir[0], y + dir[1]
                if nextX >=0 and nextX < m and nextY >= 0 and nextY < n and isWater[nextX][nextY] != 1 and (nextX, nextY) not in visited:
                    matrix[nextX][nextY] = matrix[x][y]+1
                    visited.add((nextX, nextY))
                    queue.append((nextX, nextY))
        return matrix
