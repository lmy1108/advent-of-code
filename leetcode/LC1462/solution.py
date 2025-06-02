class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        pre_map = defaultdict(set)
        indegrees = [0 for i in range(numCourses)]
        queue = deque()
        query_map = defaultdict(set)

        # build pre_map and indegree
        for pre in prerequisites:
            pre_map[pre[1]].add(pre[0])
            indegrees[pre[0]] += 1
        
        for i in range(len(indegrees)):
            if indegrees[i]== 0:
                queue.append(i)
        
        query_map = defaultdict(set)
        # topo sorting
        while queue:
            cur = queue.popleft()
            for item in pre_map[cur]:
                query_map[cur].add(item)
                query_map[cur].update(query_map[item])
                indegrees[item] -=1
                if indegrees[item] == 0:
                    queue.append(item)
        return [query[0] in query_map[query[1]] for query in queries]
                


        