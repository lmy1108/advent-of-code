def solve():
    def walk(grid:list[list[str]]) -> list[list[str]]:
        new_grid = [row.copy() for row in grid]

        def in_grid(x: int, y:int) -> bool:
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                return False
            return True

        # Guard respresentation: up = 1, right = 2, down = 3, left = 4
        # X and . are treated the same
        # if the next step is blocked, the guard will be at the same position and turn right
        # if the next step is not blocked, the guard will move to the next step, and change the current position to X
        # if the guard reaches the end of the grid, return the grid

        x, y = 0, 0
        # find guard current position
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in ('1', '2', '3', '4'):
                    x, y = i, j
                    break


        
        match grid[x][y]:
            case '1':
                if in_grid(x-1, y) and (grid[x-1][y] == '.' or grid[x-1][y] == 'X'):
                    new_grid[x][y] = 'X'
                    new_grid[x-1][y] = '1'
                    return walk(new_grid)
                elif in_grid(x-1, y) and grid[x-1][y] == '#':
                    new_grid[x][y] = '2'
                    return walk(new_grid)
                else:
                    return new_grid
            case '2':
                if in_grid(x, y+1) and (grid[x][y+1] == '.' or grid[x][y+1] == 'X'):
                    new_grid[x][y] = 'X'
                    new_grid[x][y+1] = '2'
                    return walk(new_grid)
                elif in_grid(x, y+1) and grid[x][y+1] == '#':
                    new_grid[x][y] = '3'
                    return walk(new_grid)
                else:
                    return new_grid
            case '3':
                if in_grid(x+1, y) and (grid[x+1][y] == '.' or grid[x+1][y] == 'X'):
                    new_grid[x][y] = 'X'
                    new_grid[x+1][y] = '3'
                    return walk(new_grid)
                elif in_grid(x+1, y) and grid[x+1][y] == '#':
                    new_grid[x][y] = '4'
                    return walk(new_grid)
                else:
                    return new_grid
            case '4':
                if in_grid(x, y-1) and (grid[x][y-1] == '.' or grid[x][y-1] == 'X'):
                    new_grid[x][y] = 'X'
                    new_grid[x][y-1] = '4'
                    return walk(new_grid)
                elif in_grid(x, y-1) and grid[x][y-1] == '#':
                    new_grid[x][y] = '1'
                    return walk(new_grid)
                else:
                    return new_grid
    with open('input.txt', encoding='utf-8') as f:
        memory = [list(line) for line in f.read().strip().split("\n")]

    for s in memory:
        for i in range(len(s)):
            if s[i] == '^':
                s[i] = '1'
    
        print(walk(memory))
solve()
