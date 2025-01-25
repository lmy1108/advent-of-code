def part_one(directions: list[str]) -> int:
    start = (0,0)
    currentHead = (0, 0)
    currentTail = (0, 0)
    setByTail: set[tuple[int, int]] = set()
    setByTail.add((0,0))

    def processTail(direction: str, head: tuple[int,int], tail:tuple[int,int]):
        if isDirectConnected(head, tail):
            return tail
        if direction == 'L':
            tail = currentTail = (currentHead[0]+1, currentHead[1])
        elif direction == 'R':
            tail = currentTail = (currentHead[0]-1, currentHead[1])
        elif direction == 'U':
            tail = currentTail = (currentHead[0], currentHead[1]-1)
        elif direction == 'D':
            tail = currentTail = (currentHead[0], currentHead[1]+1)
        setByTail.add(currentTail)
        return tail

    for direction in directions:
        match direction:
            case 'L':
                currentHead = (currentHead[0]-1, currentHead[1])
                currentTail = processTail(direction, currentHead, currentTail)
            case 'R': 
                currentHead = (currentHead[0]+1, currentHead[1])
                currentTail = processTail(direction, currentHead, currentTail)
            case 'U': 
                currentHead = (currentHead[0], currentHead[1]+1)
                currentTail = processTail(direction, currentHead, currentTail)
            case 'D': 
                currentHead = (currentHead[0], currentHead[1]-1)
                currentTail = processTail(direction, currentHead, currentTail)
    return len(setByTail)

def isDirectConnected(head:tuple[int, int], tail:tuple[int, int]):
    print(head, tail)
    return abs(head[0] - tail[0]) < 2 and abs(head[1] - tail[1]) < 2

def part_two(directions: list[str]):
    start = (0,0)
    currentKnots = [(0,0) for i in range(10)]
    print(currentKnots)
    setByTail: set[tuple[int, int]] = set()
    setByTail.add((0,0))

    def processTail(direction: str, currentKnots: list[tuple[int, int]]):
        for index in range(9):
            print(currentKnots)
            if isDirectConnected(currentKnots[index], currentKnots[index+1]):
                continue 
            
            if direction == 'L':
                currentKnots[index+1] = (currentKnots[index][0]+1,currentKnots[index][1]) 
            elif direction == 'R':
                currentKnots[index+1] = (currentKnots[index][0]-1,currentKnots[index][1]) 
            elif direction == 'U':
                currentKnots[index+1] = (currentKnots[index][0],currentKnots[index][1]-1) 
            elif direction == 'D':
                currentKnots[index+1] = (currentKnots[index][0],currentKnots[index][1]+1) 
        setByTail.add(currentKnots[9])
        return 

    for direction in directions:
        match direction:
            case 'L':
                currentKnots[0] = (currentKnots[0][0]-1, currentKnots[0][1])
                tailPos = processTail(direction, currentKnots)
            case 'R': 
                currentKnots[0] = (currentKnots[0][0]+1, currentKnots[0][1])
                tailPos = processTail(direction, currentKnots)
            case 'U': 
                currentKnots[0] = (currentKnots[0][0], currentKnots[0][1]-1)
                tailPos = processTail(direction, currentKnots)
            case 'D': 
                currentKnots[0] = (currentKnots[0][0], currentKnots[0][1]+1)
                tailPos = processTail(direction, currentKnots)
    return len(setByTail)


def parse_input(filename: str) -> list[list[int]]:
    with open(filename, encoding='UTF-8') as f:
        ops = f.read().split('\n')
        operations = []
        for line in ops:
            (direction, times) = line.split()
            for i in range(int(times)):
                operations.append(direction)
    return operations 

if __name__=="__main__":
    input_path = "input.txt"
    print("---part 1---")
    directions = parse_input(input_path)
    print(part_one(directions))
    # print(directions)
    print("---part 2---")
    print(part_two(directions))
