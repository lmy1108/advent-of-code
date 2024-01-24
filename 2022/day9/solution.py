def part_one(directions: list[str]) -> int:
    start = (0,0)
    currentHead = (0, 0)
    currnetTail = (0, 0)
    setByTail: set[tuple[int, int]] = set()

    def processTail(direction: str):
        if direction == 'L':
            currentTail = (currentHead[0]+1, currentHead[1])
        if direction == 'R':
            currentTail = (currentHead[0]-1, currentHead[1])
        if direction == 'U':
            currentTail = (currentHead[0], currentHead[1]-1)
        if direction == 'D':
            currentTail = (currentHead[0], currentHead[1]+1)

    for direction in directions:
        if isDirectConnected(currentHead, currentTail):
            continue
        match direction:
            case 'L':
                currentHead[0] = currentHead[0]-1
                processTail(direction)
            case 'R': currentHead[0] = currentHead[0]+1
                currentHead[0] = currentHead[0]+1
                processTail(direction)
            case 'U': currentHead[1] = currentHead[1]+1
                currentHead[1] = currentHead[1]+1
                processTail(direction)
            case 'D': currentHead[1] = currentHead[1]-1
                currentHead[1] = currentHead[1]-1
                processTail(direction)
    return
        

def isDirectConnected(head:tuple[int, int], tail:tuple[int, int]):
    return abs(head[0] - tail[0]) < 2 and abs(head[1] - tail[1]) < 2


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
    print(directions)
    print("---part 2---")
