def part_one(trees: list[list[int]]) -> int:
    visible: set[[tuple[int][int]]] = set()
    x_max, y_max = len(nums[0]), len(nums)
    visible.update(
        *(
            [find_visible_in_line(nums, 0, x_max, y, y) for y in range(y_max)]
            + [find_visible_in_line(nums, x_max, 0, y, y) for y in range(y_max)]
            + [find_visible_in_line(nums, x, x, 0, y_max) for x in range(x_max)]
            + [find_visible_in_line(nums, x, x, y_max, 0) for x in range(x_max)]
        )
    )

def parse_input(filename: str) -> list[list[int]]:
    with open(filename, encoding='UTF-8') as f:
        trees = f.read().split('\n')
    return trees 


def find_visible_in_line(
    nums: list[list[int]], x_min, x_max, y_min, y_max: int
) -> set[tuple[int, int]]:
    if x_min != x_max and y_min != y_max:
        raise ValueError(
            "x_min and x_max must be equal or y_min and y_max must be equal"
        )
    visible = set()
    current_max = -1
    if x_min == x_max:
        if y_min < y_max:
            for y in range(y_min, y_max):
                if nums[y][x_min] > current_max:
                    current_max = nums[y][x_min]
                    visible.add((x_min, y))
        else:
            for y in range(y_min - 1, y_max - 1, -1):
                if nums[y][x_min] > current_max:
                    current_max = nums[y][x_min]
                    visible.add((x_min, y))
    else:
        if x_min < x_max:
            for x in range(x_min, x_max):
                if nums[y_min][x] > current_max:
                    current_max = nums[y_min][x]
                    visible.add((x, y_min))
        else:
            for x in range(x_min - 1, x_max - 1, -1):
                if nums[y_min][x] > current_max:
                    current_max = nums[y_min][x]
                    visible.add((x, y_min))
    return visible

if __name__=="__main__":
    input_path = "input.txt"

    print("---part 1---")
    trees = parse_input(input_path)    
    print(part_one(trees))


    print("---part 2---")
