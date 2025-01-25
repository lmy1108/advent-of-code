class Reports:
    def __init__(self):
        return

    def parse(self, filename: str) -> list[list[int]]:
        with open(filename, encoding="utf-8") as f:
            matches = f.read().split("\n")
        
        return [(match.strip().split(" ")) for match in matches]
    
    
    def part1(nums: list[int]):
        def isDesc(nums: list[int]):
            for i in range(1, len(nums)):
                if nums[i] > nums[i-1]:
                    return false
            return true
        def isAsc(nums: list[int]):
            for i in range(1, len(nums)):
                if nums[i] < nums[i-1]:
                    return false
            return true
        def isSafe(nums: list[int]):
            for i in range(1, len(nums)):
                if abs(nums[i] - nums[i-1]) > 3:
                    return false
            return true
        
        if (isDesc(nums) and isSafe(nums)) or (isAsc(nums) and isSafe(nums)):
            return true

        
            



    if __name__  == "__main__":
        
        input_path = "input.txt"
        reports = Reports()
        report = reports.parse(input_path)
        print(report)

        print("---Part One---")
        print(reports.part1(strategies))
        print("---Part Two---")
        # print(elfRockPaperScissors.calculateScores2(strategies))
