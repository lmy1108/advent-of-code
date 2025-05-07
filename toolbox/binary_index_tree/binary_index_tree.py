class BIT:
    # Binary index tree for prefix sum
    def __init__(n: int):
        self.treeList = [0] * n+1
        self.n = n
    
    def add(index:int, value:int):
        while index > 0:
            index = index - (index & (-index))
            self.treeList[index] += value
    
    def query():
        res = 0
        while index < self.n:
            res += self.treeList[index & -index]
            index -= index & -index
        return res

class BinaryIndexTreeMaxInterval:
    # This tree can be used for store the maximum range between [0, n] given than there're blockers that divide the range.
    # The maximum range between [0, n] will be stored as treeList[n]
    # Thie tree support updating but only the to a greater value (merge two ranges in this case)
    def __init__(n: int):
        self.n = n
        self.treeList = [0] * n+1
    
    def query(index: int, value: int):
        index += 1
        res = 0
        while index > 0:
            res = max(res, self.treeList[index])
            index -= index & (-index)
        return res
    
    def add(index: int):
        index += 1
        while index < self.n:
            self.treeList[index] = max(self.treeList[index], value)
            index += index & (-index)

class BinaryIndexTreeMaxValue:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * n+1
    def add(self, index, value):
        index += 1
        while index < n:
            self.tree[index] = max(self.tree[index], value)
            index += index & (-index)

    def query(self, index):
        index += 1
        res = 0
        while index > 0:
            res = max(self.tree[index], res)
            index -= index & (-index)

class BIT:
    # Binary index tree for "Greater count"
    # Given a number, find out how many in the array are greater than this number 
    # Build frequency array, and use prefix sum to insert/query
    def __init__(self, n):
        self.n = n
        self.bit = [[0]*(n+2) for _ in range(2)]

    def update(self, idx, which):
        idx += 1
        while idx <= self.n:
            self.bit[which][idx] += 1
            idx += idx & -idx

    def prefixSum(self,idx, which):
        idx += 1
        res = 0
        
        while idx > 0:
            res += self.bit[which][idx]
            idx -= idx & -idx

        return res
    
    def sumRange(self, l, r, which):
        return self.prefixSum(r, which) - self.prefixSum(l-1, which)
    def greaterCount(self, which, val):
        return self.sumRange(val + 1, self.n-1, which)
class main:

