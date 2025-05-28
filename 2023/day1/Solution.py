import re
class Solution:
    def __init__(self, filename: str):
        with open(filename, encoding='utf-8') as f:
            self.memory = f.read().strip().split("\n")
    
    def find_number(self, line: str)-> int:
        first_num, last_num = self.get_first_num(line), self.get_last_num(line)
        if first_num == '' or last_num == '':
            return 0
        return int(first_num + last_num)

    def get_first_num(self, line:str)-> str:
        for c in line:
            if c.isdigit():
                return c
        return ''

    def get_last_num(self, line:str)-> str:
        for c in line[::-1]:
            if c.isdigit():
                return c
        return ''
    
    def find_all_numbers(self)-> int:
        return sum(self.find_number(line) for line in self.memory)
    
    def find_all_numbers_part2(self)-> int:
        return sum(self.find_number_part2(line) for line in self.memory)

    def find_number_part2(self, line: str) -> int:
        text = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        word_to_digit = {word: str(i+1) for i, word in enumerate(text)}
        digit_reprs = word_to_digit.copy()
        digit_reprs.update({str(i): str(i) for i in range(1, 10)})

        matches = []
        for i in range(len(line)):
            for word, digit in digit_reprs.items():
                if line.startswith(word, i):
                    matches.append(digit)
        if not matches:
            return 0
        return int(matches[0] + matches[-1])

            
if __name__ == '__main__':
    solution = Solution('input.txt')
    print(solution.find_all_numbers_part2())