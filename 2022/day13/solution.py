import collections
from typing import Union

def parse_input(filename: str) -> list[list[int]]:
    with open(filename, encoding='UTF-8') as f:
        lines = f.read().split('\n\n') 
        lists = []
        for line in lines:
            left, right = line.split('\n')
            lists.append((left.strip(), right.strip()))
            print(left,right)
    return lists

def separate_nested_lists(listAsStr: str) -> int:
    result = []
    brackets = 0
    pos = 1
    print("listAsStr" + listAsStr)
    for i in range(len(listAsStr)):
        if listAsStr[i] == '[':
            brackets += 1
        elif listAsStr[i] == ']':
            brackets -= 1 
        elif listAsStr[i] == ',':
            print(brackets, listAsStr[i])
            if brackets == 1: 
                result.append(listAsStr[pos:i])
                pos = i+1
            else:
                continue
    result.append(listAsStr[pos:len(listAsStr)])
    print("separate result: " , result)
    return result
 
def part_one(listAsStr: str) -> int:
    res = []
    def parseList(currentListStr: str) -> Union[int,list]:
        print("to parse:" + currentListStr)
        result = []
        if currentListStr and currentListStr[0] == '[':
            print("currentListStr", currentListStr)
            items = separate_nested_lists(currentListStr.strip())
            for item in items:
                result.append(parseList(item))
            return result
        elif currentListStr:
            return int(currentListStr)
    for lista, listb in listAsStr:
        print("lista listb" ,lista, listb)
        a = parseList(lista)
        b = parseList(listb)
        print("left",a , "right", b)        
    return 0
 

if __name__=="__main__":
    input_path = "input.txt"
    print("---part 1---")
    # parsed_list = parse_input(input_path)

    # print(parsed_list)
    # part_one(parsed_list)
    separate_nested_lists("[[[9,[],3],[6],1],[[1],[[9,1],0,7,10],2,0]]")
    print("---part 2---")
