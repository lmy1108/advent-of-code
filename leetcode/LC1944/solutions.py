class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        monoStack = []
        # stores (index, height)
        for i in range(len(heights)-1, -1, -1):
            cur = heights[i]
            while monoStack and monoStack[len(monoStack)-1][1] < cur:
                monoStack.pop()
            monoStack.append((i, heights[i]))
        
        res = []
        for i in range(len(heights)):
            topi, topHeight = monoStack[len(monoStack)-1][0], monoStack[len(monoStack)-1][1]
            # if index equal top element: pop and return 1
            # if not, iterate throught the stack  to find the next larger, and return the gap+1
            # [11, 8 ,6]
            for j in range(len(monoStack), -1, -1):
                if monoStack[j][1] < heights[i]:
                    continue
                else:
                    res.append(monoStack[j][0] - i)
                    break
            if topi == i:
                monoStack.pop()
        return res