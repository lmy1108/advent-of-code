def solve():

    def update_grid(grid, x, y, value):
        new_row = grid[x][:y] + (value,) + grid[x][y+1:]
        return grid[:x] + (new_row,) + grid[x+1:]

    def walk(grid: tuple[tuple[str, ...], ...]) -> tuple[tuple[str, ...], ...]:
        # Create a new immutable grid
        def update_grid(grid, x, y, value):
            # Create a new row with the updated value
            new_row = grid[x][:y] + (value,) + grid[x][y+1:]
            # Create a new grid with the updated row
            return grid[:x] + (new_row,) + grid[x+1:]

        def in_grid(x: int, y: int) -> bool:
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                return False
            return True

        # Find guard's current position
        x, y = 0, 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in ('1', '2', '3', '4'):
                    x, y = i, j
                    break

        # Guard representation: up = 1, right = 2, down = 3, left = 4
        match grid[x][y]:
            case '1':  # Up
                if in_grid(x-1, y) and (grid[x-1][y] == '.' or grid[x-1][y] == 'X'):
                    # Move up
                    new_grid = update_grid(grid, x, y, 'X')
                    new_grid = update_grid(new_grid, x-1, y, '1')
                    return walk(new_grid)
                elif in_grid(x-1, y) and grid[x-1][y] == '#':
                    # Turn right
                    new_grid = update_grid(grid, x, y, '2')
                    return walk(new_grid)
                else:
                    return grid
            case '2':  # Right
                if in_grid(x, y+1) and (grid[x][y+1] == '.' or grid[x][y+1] == 'X'):
                    # Move right
                    new_grid = update_grid(grid, x, y, 'X')
                    new_grid = update_grid(new_grid, x, y+1, '2')
                    return walk(new_grid)
                elif in_grid(x, y+1) and grid[x][y+1] == '#':
                    # Turn right (now down)
                    new_grid = update_grid(grid, x, y, '3')
                    return walk(new_grid)
                else:
                    return grid
            case '3':  # Down
                if in_grid(x+1, y) and (grid[x+1][y] == '.' or grid[x+1][y] == 'X'):
                    # Move down
                    new_grid = update_grid(grid, x, y, 'X')
                    new_grid = update_grid(new_grid, x+1, y, '3')
                    return walk(new_grid)
                elif in_grid(x+1, y) and grid[x+1][y] == '#':
                    # Turn right (now left)
                    new_grid = update_grid(grid, x, y, '4')
                    return walk(new_grid)
                else:
                    return grid
            case '4':  # Left
                if in_grid(x, y-1) and (grid[x][y-1] == '.' or grid[x][y-1] == 'X'):
                    # Move left
                    new_grid = update_grid(grid, x, y, 'X')
                    new_grid = update_grid(new_grid, x, y-1, '4')
                    return walk(new_grid)
                elif in_grid(x, y-1) and grid[x][y-1] == '#':
                    # Turn right (now up)
                    new_grid = update_grid(grid, x, y, '1')
                    return walk(new_grid)
                else:
                    return grid
            case _:
                return grid

    # Iterative version to avoid recursion depth issues
    def walk_iterative(grid: tuple[tuple[str, ...], ...], max_steps=10000) -> bool:
        steps = 0
        visited_states = set()  # Track (position, direction) to detect cycles
        
        while steps < max_steps:
            # Find guard's position
            guard_pos = None
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] in ('1', '2', '3', '4'):
                        guard_pos = (i, j)
                        direction = grid[i][j]
                        break
                if guard_pos:
                    break
            
            if not guard_pos:
                return False  # No guard found
            
            x, y = guard_pos
            
            # Check if we've seen this state before (position + direction)
            state = (x, y, direction)
            if state in visited_states:
                return True  # Found a loop
            visited_states.add(state)
            
            def update_grid(grid, x, y, value):
                new_row = grid[x][:y] + (value,) + grid[x][y+1:]
                return grid[:x] + (new_row,) + grid[x+1:]
                
            def in_grid(x, y):
                return 0 <= x < len(grid) and 0 <= y < len(grid[0])
            
            # Process based on direction
            if direction == '1':  # Up
                if in_grid(x-1, y) and grid[x-1][y] in ['.', 'X']:
                    grid = update_grid(grid, x, y, 'X')  # Mark current as visited
                    grid = update_grid(grid, x-1, y, '1')
                elif in_grid(x-1, y) and grid[x-1][y] == '#':
                    grid = update_grid(grid, x, y, '2')  # Turn right
                else:
                    return False  # Hit edge of grid
            elif direction == '2':  # Right
                if in_grid(x, y+1) and grid[x][y+1] in ['.', 'X']:
                    grid = update_grid(grid, x, y, 'X')  # Mark current as visited
                    grid = update_grid(grid, x, y+1, '2')
                elif in_grid(x, y+1) and grid[x][y+1] == '#':
                    grid = update_grid(grid, x, y, '3')  # Turn right
                else:
                    return False  # Hit edge of grid
            elif direction == '3':  # Down
                if in_grid(x+1, y) and grid[x+1][y] in ['.', 'X']:
                    grid = update_grid(grid, x, y, 'X')  # Mark current as visited
                    grid = update_grid(grid, x+1, y, '3')
                elif in_grid(x+1, y) and grid[x+1][y] == '#':
                    grid = update_grid(grid, x, y, '4')  # Turn right
                else:
                    return False  # Hit edge of grid
            elif direction == '4':  # Left
                if in_grid(x, y-1) and grid[x][y-1] in ['.', 'X']:
                    grid = update_grid(grid, x, y, 'X')  # Mark current as visited
                    grid = update_grid(grid, x, y-1, '4')
                elif in_grid(x, y-1) and grid[x][y-1] == '#':
                    grid = update_grid(grid, x, y, '1')  # Turn right
                else:
                    return False  # Hit edge of grid
            else:
                return False  # Invalid direction
                
            steps += 1
        if steps >= max_steps:
            print(f"Warning: Reached maximum steps ({max_steps})")
            return False 
        return False 

    with open('input.txt', encoding='utf-8') as f:
        # Convert to tuples for immutability
        lines = f.read().strip().split("\n")
        # Replace ^ with 1 during conversion
        memory = tuple(tuple(c if c != '^' else '1' for c in line) for line in lines)
    
    # Use the iterative version to avoid recursion issues
    res_count = 0

    for i in range(len(memory)):
        for j in range(len(memory[0])):
            if memory[i][j] == '.':
                memory_test = update_grid(memory, i, j, '#') 
                result = walk_iterative(memory_test)
                if result:
                    res_count += 1
                    print(f"Found loop position at ({i}, {j}), count: {res_count}")
        
    print("res_count" , res_count)
    
    # Print the result in a readable format
    for row in memory:
        print(''.join(row))

solve()
