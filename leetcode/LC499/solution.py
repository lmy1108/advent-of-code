class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        # Define the node in graph: position + current step (represented by char)
        # four transition state: udlr 4 options
        # how long is the edge for each move
        # getNeighbors() to generate possible move positions
        # Dijkstra to find shortest
        # Make sure that ball in the middle will be dropped into the hole
        def find_next(x, y):
            res = []
            if x == hole[x] and y == hole[y]:
                res.append((x,y))
                return res
            # down
            for i in range(x, len(maze)):
                if maze[i+1][y] == 1 and i+1 < len(maze) or (i == hole[x] and y == hole[y]):
                    res.append((i,y))
            for i in range(x-1, -1, -1):
                if maze[i-1][y] == 1 and i-1 >= 0 or (i == hole[x] and y == hole[y]):
                    res.append((i,y))
            for j in range(y, len(maze[0])):
                if maze[x][j+1] == 1 and j+1 < len(maze[0]) or (i == hole[x] and y == hole[y]):
                    res.append((x,j))
            for j in range(y-1, -1, -1):
                if maze[x][j-1] == 1 and j-1 >= 0 or (i == hole[x] and y == hole[y]):
                    res.append((x, j))
            return res

        visited = set()
        visited.add((ball[0], ball[1]))

        m, n = len(maze), len(maze[0])
        q = [(ball[0], ball[1], 0, "")]
        min_distance = Integer.MAXINT 
        min_distance_strs = []
        while q:
            cur_x, cur_y, cur_dist, cur_str = heapq.heappop(q)
            if cur_x == hole[0] and cur_y == hole[1]:
                min_distance = min(min_distance, cur_dist)
                min_distance_strs.append(cur_str)
            if (cur_x, cur_y) in visited:
                continue
            next_pos_list = find_next(cur_x, cur_y)
            for next_pos in next_pos_list:
                distance = abs(cur_pos[0] - next_pos[0]) + abs(cur_pos[1] - next_pos[1])
                dis_char = ''
                if cur_pos[0] < next_pos[0]:
                    dis_char = 'd'
                elif cur_pos[0] > next_pos[0]:
                    dis_char = 'u'
                elif cur_pos[1] > next_pos[1]:
                    dis_char = 'r'
                elif cur_pos[1] < next_pos[1]:
                    dis_char = 'l'
                
                heapq.heappush(q, (next_pos[0], next_pos[1], cur_dist + distance, cur_str + dis_char))
        return sorted(min_distance_strs)[0]


        







def findShortestWay(self, A, ball, hole):
    ball, hole = tuple(ball), tuple(hole)
    R, C = len(A), len(A[0])
    
    def neighbors(r, c):
        for dr, dc, di in [(-1, 0, 'u'), (0, 1, 'r'), 
                           (0, -1, 'l'), (1, 0, 'd')]:
            cr, cc, dist = r, c, 0
            while (0 <= cr + dr < R and 
                    0 <= cc + dc < C and
                    not A[cr+dr][cc+dc]):
                cr += dr
                cc += dc
                dist += 1
                if (cr, cc) == hole:
                    break
            yield (cr, cc), di, dist
    
    pq = [(0, '', ball)]
    seen = set()
    while pq:
        dist, path, node = heapq.heappop(pq)
        if node in seen: continue
        if node == hole: return path
        seen.add(node)
        for nei, di, nei_dist in neighbors(*node):
            heapq.heappush(pq, (dist+nei_dist, path+di, nei) )
        
    return "impossible"
