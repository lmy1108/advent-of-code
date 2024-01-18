class ElfRange:

    def __init__(self):
        return
    
    def parseRanges(self, input):
        with open(input, encoding='UTF-8') as f:
            ranges = f.read().split('\n')                
        return [(twoRange.split(",")[0], twoRange.split(",")[1]) for twoRange in ranges]
    
    def findFullyCovered(self, twoRanges: list[tuple]):
        count = 0
        for ranges in twoRanges:
            firstRange = ranges[0].split("-")
            firstLeft, firstRight = int(firstRange[0]), int(firstRange[1])
            secondRange = ranges[1].split("-")
            secondLeft, secondRight = int(secondRange[0]), int(secondRange[1])
            if (firstLeft >= secondLeft and firstRight <= secondRight) or (firstLeft <= secondLeft and firstRight >= secondRight):
                count+=1
        return count 
    
 
    def findNonOverlapped(self, twoRanges: list[tuple]):
        count = 0
        for ranges in twoRanges:
            firstRange = ranges[0].split("-")
            firstLeft, firstRight = int(firstRange[0]), int(firstRange[1])
            secondRange = ranges[1].split("-")
            secondLeft, secondRight = int(secondRange[0]), int(secondRange[1])
            if not(firstLeft > secondRight or firstRight < secondLeft):
                count+=1
        return count 

if __name__=="__main__":
    input_path = "input.txt"
    elfRange = ElfRange()
    ranges = elfRange.parseRanges(input_path)
    print("---part 1---")
    print(elfRange.findFullyCovered(ranges))
    print("---part 2---")
    print(elfRange.findNonOverlapped(ranges))




