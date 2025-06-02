I can see the main issues in your solution. Let me help you correct them:

## The Problems:

1. **Reversed graph construction**: You're building the graph backwards
2. **Incorrect indegree calculation**: You're incrementing indegree for the wrong nodes
3. **Wrong direction in topological sort**: You're trying to propagate prerequisites in the wrong direction

## Here's the corrected solution:

```python
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Build adjacency list and indegrees
        adj = defaultdict(list)
        indegrees = [0] * numCourses
        
        # CORRECT: pre[0] is prerequisite of pre[1]
        # So edge goes from pre[0] -> pre[1]
        for pre in prerequisites:
            adj[pre[0]].append(pre[1])  # pre[0] points to pre[1]
            indegrees[pre[1]] += 1      # pre[1] has one more incoming edge
        
        # Find all nodes with no prerequisites
        queue = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
        
        # Track all prerequisites for each course
        prereq_map = defaultdict(set)
        
        # Topological sort
        while queue:
            cur = queue.popleft()
            
            # For each course that depends on cur
            for next_course in adj[cur]:
                # Add cur as a prerequisite of next_course
                prereq_map[next_course].add(cur)
                # Add all prerequisites of cur as prerequisites of next_course
                prereq_map[next_course].update(prereq_map[cur])
                
                indegrees[next_course] -= 1
                if indegrees[next_course] == 0:
                    queue.append(next_course)
        
        # Answer queries
        return [query[0] in prereq_map[query[1]] for query in queries]
```

## Key Fixes:

1. **Graph direction**: 
   - `adj[pre[0]].append(pre[1])` - course `pre[0]` points to course `pre[1]`
   - This means "after taking pre[0], you can take pre[1]"

2. **Indegree**: 
   - `indegrees[pre[1]] += 1` - course `pre[1]` has one more prerequisite

3. **Propagation logic**:
   - When we process a course, we update all courses that depend on it
   - `prereq_map[next_course]` gets all prerequisites from the current course

## Visual Example:
```
If prerequisites = [[0,1], [1,2]]
Graph: 0 → 1 → 2

Processing order:
1. Process 0: prereq_map[1] = {0}
2. Process 1: prereq_map[2] = {1, 0}

Query [0,2]: Is 0 in prereq_map[2]? Yes!
```

The main insight: In topological sort, when processing a node, we propagate its information to all nodes that depend on it (its successors in the graph).