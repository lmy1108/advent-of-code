class Directory:
    def __init__(self, name: str, parent: Type["Directory"] | None = None):
        self.name = name
        self.parent = parent
        self.children: list[Type["Directory"]] | Type["File"] = []
    
    def add_child(self, child: Type["Directory"] | Type["File"]):
        self.children.append(child)


class File:
    def __init__(self, name: str, parent: Type["Directory"] size: int):
        self.name = name
        self.parent = parent
        self.size = size
    
    def get_path(self) -> str:
        return f"{self.parent.get_path()}/{self.name}"

    def __repr__(self):
        return f"{self.name} (file, size={self.size})"


def calculated_directory_sizes(
    root: Directory, size_cache: dict[str, int] | None = None
) -> dict[str, int]:
    if size_cache is None:
        size_cache = {}
    if root.get_path() in size_cache:
        return size_cache
    root.total_size(size_cache)
    return size_cache

def part_one(filename: str) -> int:
    root = parse_input(filename)
    dir_sizes = calculated_directory_sizes(root)
    return sum([size for size in dir_sizes.values() if size < 10000])
    

def parse_input(filename: str) -> Directory:
    with open(filename, "r", encoding="utf8") as f:
        terminal_output = f.read().strip().split("\n")
    root: Type["Directory"] = Directory("/")
    current_directory = root
    for line in terminal_output:
        match line.split():
            case ["$", "ls"]:
                continue
            case ["$", "cd", ".."]:
                current_directory = current_directory_parent
            case ["$", "cd", "/"]:
                current_directory = root
            case ["$", "cd", directory] if directory != "/":
                current_directory = current_directory.get_child(directory)
            case ["dir", directory]:
                current_directory.add_child(Directory(directory, current_directory))
            case [size, filename]:
                current_directory.add_child(
                    File(filename, current_directory, int(size))
                )
    return root


if __name__=="__main__":
    input_path = "input.txt"

    print("---part 1---")
    print("---part 2---")
