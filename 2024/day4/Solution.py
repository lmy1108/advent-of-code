class Solution:
    def __init__(self, filename: str):
        with open(filename, encoding='utf-8') as f:
            self.memory = f.read().strip().split("\n")
    def find_all_xmas(self, grid: list[list[str]], word: str) -> int:
        def valid_number(x: int, y: int) -> int:
            res = 0
            steps = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
            for step in steps:
                for i in range(len(word)):
                    nextX = x + step[0] * i
                    nextY = y + step[1] * i
                    if nextX < 0 or nextX >= len(grid) or nextY < 0 or nextY >= len(grid[0]):
                        break
                    if word[i] != grid[nextX][nextY]:
                        break
                    if i == len(word)-1:
                        res += 1 
            return res     
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                result += valid_number(i, j)
        return result

    def find_all_xmas_part2(self, grid: list[list[str]], word: str) -> int:
        res = 0
        def out_of_bound(x: int, y: int) -> bool:
            return x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0])
        def is_valid(x: int, y: int) -> bool:
            if grid[x][y] != 'A':
                return False
            diagnal_1 = [(1, -1), (-1, 1)]
            diagnal_2 = [(1, 1), (-1, -1)]
            firstX, firstY = x + diagnal_1[0][0], y + diagnal_1[0][1]
            secondX, secondY = x + diagnal_1[1][0], y + diagnal_1[1][1]
            thirdX, thirdY = x + diagnal_2[0][0], y + diagnal_2[0][1]
            fourthX, fourthY = x + diagnal_2[1][0], y + diagnal_2[1][1]

            if out_of_bound(firstX, firstY) or out_of_bound(secondX, secondY) or out_of_bound(thirdX, thirdY) or out_of_bound(fourthX, fourthY):
                return False
            first, second = False, False
            if (grid[firstX][firstY] == 'M' and grid[secondX][secondY] == 'S') or (grid[firstX][firstY] == 'S' and grid[secondX][secondY] == 'M'):
                first =  True
            if (grid[thirdX][thirdY] == 'M' and grid[fourthX][fourthY] == 'S') or (grid[thirdX][thirdY] == 'S' and grid[fourthX][fourthY] == 'M'):
                second = True
            return first and second
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if is_valid(i, j):
                    res += 1
        return res        


'''
    **MSM**
    *A*A*A*
    S**M**S
    SAMXMAS
    **MMM**
    *A*A*A*
    S**S**S

'''
if __name__ == '__main__':
    solution = Solution('input.txt')
    print(solution.find_all_xmas_part2(solution.memory, 'XMAS'))