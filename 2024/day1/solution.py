from collections import defaultdict 
left = []
right = []

def getResultOne(lista: list[int], listb: list[int]):
    res = 0
    lista.sort()
    listb.sort()
    for a, b in zip(lista, listb):
        res += abs(a-b)
    return res


def getResultTwo(lista: list[int], listb: list[int]):
    res = 0
    right_count = defaultdict(int)
    for num in listb:
        right_count[num]+=1

    similarity_score = 0
    for num in left:
        similarity_score += num * right_count[num]
    
    return similarity_score
    
    
with open('input.txt', 'r') as file:
    for line in file:
        l, r = map(int, line.split())
        left.append(l)
        right.append(r)


res = getResultOne(left, right)
print(res)
res2 = getResultTwo(left, right)
print(res2)
