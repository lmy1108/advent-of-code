class ElfRuckSack:
    def __init__(self):
        return

    def parseRuckSack(self, filename: str) -> list[tuple[str]]:
        with open(filename, encoding="utf-8") as f:
            ruckSacks = f.read().split("\n")
        return  [ruckSacks[i:i+3] for i in range(0, len(ruckSacks),3)]

    def calculateSum(self, ruckSacks: list[tuple[str]]):
        score = 0
        count = 0
        for ruckSack in ruckSacks:
            left, right = ruckSack[0], ruckSack[1]
            characterSet = set()
            for c in left:
                characterSet.add(c)
            for c in right:
                if c in characterSet:
                    count+=1
                    print(left, right)
                    if c.islower():
                        score += ord(c) - ord('a') + 1
                    elif c.isupper(): 
                        score += ord(c) - ord('A') + 27
                    break
        return score


    def findCommon(self, ruckSack: str, ruckSack2: str) -> str:
        filterSet = set()
        commonChars = ""
        for c in ruckSack:
            filterSet.add(c)
        for c in ruckSack2:
            if c in filterSet and c not in commonChars:
                commonChars += c
        return commonChars


    def calculateSum2(self, ruckSacks: list[list[str]]):
        score = 0
        for ruckSackByThree in ruckSacks:
            commonStr = self.findCommon(ruckSackByThree[0], ruckSackByThree[1])
            commonChar = self.findCommon(commonStr, ruckSackByThree[2])
            if len(commonChar) != 1:
                print("wrong")
                # throw Exception("common char is none or more than 1")
            if commonChar.islower():
                score += ord(commonChar) - ord('a') + 1
            else:
                score += ord(commonChar) - ord('A') + 27
        return score 


            
    
        
if __name__  == "__main__":
    
    input_path = "input.txt"

    elfRuckSack = ElfRuckSack()
    ruckSacks = elfRuckSack.parseRuckSack(input_path)

    print("---Part One---")
    print(elfRuckSack.calculateSum(ruckSacks))

    print("---Part Two---")
    print(len(ruckSacks))
    print(elfRuckSack.calculateSum2(ruckSacks))
