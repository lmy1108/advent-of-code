class CalorieFinder:
    def __init__(self):
        return

    def parseCalories(self, filename: str) -> list[list[int]]:
        with open(filename, encoding="utf-8") as f:
            elves = f.read().split("\n\n")
        return [list(map(int, elf.strip().split("\n"))) for elf in elves]

    def findMostCalories(self, calories: list[list[int]]) -> int:
        elfWithMaxCalories = 0
        for elf in calories:
            if sum(elf) > elfWithMaxCalories:
                elfWithMaxCalories = sum(elf)
        return elfWithMaxCalories
    
    def findTop3MostCalories(self, calories: list[list[int]]) -> int:
        totalCaloriesByElf = [sum(elf) for elf in calories]
        return sum(sorted(totalCaloriesByElf, reverse=True)[:3])


if __name__  == "__main__":
    
    input_path = "input.txt"
    caloriesFinder = CalorieFinder()
    caloriesByElf = caloriesFinder.parseCalories(input_path)
    print("---Part One---")
    print(caloriesFinder.findMostCalories(caloriesByElf))
    print("---Part Two---")
    print(caloriesFinder.findTop3MostCalories(caloriesByElf))
