import collections
def parse_input(filename: str) -> list[list[int]]:
    with open(filename, encoding='UTF-8') as f:
        lines = f.read().split('\n') 
        grid = [[c for c in line] for line in lines]
    return grid 

def part_one(grid: list[list[str]]) -> int:
    m, n = len(grid), len(grid[0])
    queue = collections.deque()
    queue.append((0,0))
    visited = set()
    visited.add((0,0))
    steps = 0
    while queue:
        size = len(queue)
        for i in range(size):
            x, y = queue.popleft()
            print(x, y)
            visited.add((x, y))
            if grid[x][y] == 'E':
                return steps
            for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                nextX = x + dx
                nextY = y + dy
                if nextX < 0 or nextX >= m or nextY < 0 or nextY >= n or ord(grid[x][y]) > ord(grid[nextX][nextY]) or (nextX, nextY) in visited:
                    continue
                else:
                    queue.append((nextX, nextY))
        steps+=1
    return steps
                

if __name__=="__main__":
    input_path = "input.txt"
    print("---part 1---")
    grid = parse_input(input_path)
    print(part_one(grid))
    print(grid)
    print("---part 2---")
