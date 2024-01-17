class ElfRockPaperScissors:
    def __init__(self):
        return

    def parseStrategy(self, filename: str) -> list[list[int]]:
        with open(filename, encoding="utf-8") as f:
            matches = f.read().split("\n")
        
        return [(match.strip().split(" ")) for match in matches]


    def calculateScores(self, strategies: list[tuple[str]]):
        score = 0
        points = {'X':1, 'Y':2, 'Z':3}
        pairsToWin = {'A':'Y', 'B':'Z', 'C':'X'}
        pairsToTie = {'A':'X', 'B':'Y', 'C':'Z'}
        pairsToLose = {'A':'Z', 'B':'X', 'C':'Y'}
        for strategy in strategies:
            score += points[strategy[1]]
            if pairsToWin[strategy[0]] == strategy[1]:
                score += 6 
            elif pairsToTie[strategy[0]] == strategy[1]:
                score += 3
            elif pairsToLose[strategy[0]] == strategy[1]:
                pass
        return score
    

    def calculateScores2(self, strategies: list[tuple[str]]):
        score = 0
        points = {'X':1, 'Y':2, 'Z':3}
        pairsToWin = {'A':'Y', 'B':'Z', 'C':'X'}
        pairsToTie = {'A':'X', 'B':'Y', 'C':'Z'}
        pairsToLose = {'A':'Z', 'B':'X', 'C':'Y'}
        for strategy in strategies:
            if strategy[1] == 'X':
                score += points[pairsToLose[strategy[0]]]
            elif strategy[1] == 'Y':
                score += points[pairsToTie[strategy[0]]]
                score += 3
            elif strategy[1] == 'Z':
                score += points[pairsToWin[strategy[0]]]
                score += 6
        return score



if __name__  == "__main__":
    
    input_path = "input.txt"
    elfRockPaperScissors = ElfRockPaperScissors()
    strategies = elfRockPaperScissors.parseStrategy(input_path)
    # print(strategies)

    print("---Part One---")
    print(elfRockPaperScissors.calculateScores(strategies))
    print("---Part Two---")
    print(elfRockPaperScissors.calculateScores2(strategies))
