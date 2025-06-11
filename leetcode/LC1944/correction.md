Looking at your solution, I can see you're trying to use a monotonic stack approach, which is the right idea! However, there are several issues with the current implementation. Let me help you understand the problem better and provide an improved solution.

## Key Insights

1. Person `i` can see person `j` if:
   - `j` is to the right of `i` (i.e., `j > i`)
   - All people between them are shorter than both `i` and `j`

2. Person `i` stops seeing people when they encounter someone taller than themselves

3. This naturally leads to a monotonic decreasing stack solution

## Issues with Current Solution

1. Your stack building logic is backwards - you're building from right to left but not using it correctly
2. The logic for counting visible people is incorrect
3. You're iterating through the entire stack for each person, which is inefficient

## Improved Solution

Here's a corrected solution using a monotonic decreasing stack:## Explanation of the Improved Solution

### Approach 1: Right to Left
1. We process people from right to left
2. For each person `i`, we count how many people they can see:
   - All people in the stack shorter than them (these get popped)
   - Plus one more if there's a taller person remaining in the stack

### Approach 2: Left to Right
1. We process people from left to right
2. For each new person, we update the count for people who can see them
3. This is more intuitive as we're directly tracking who can see the current person

### Why This Works
- The monotonic decreasing stack maintains people in decreasing order of height
- When we encounter someone taller, we know that all shorter people in between can be seen
- The stack helps us efficiently track visible relationships

### Time & Space Complexity
- Time: O(n) - each person is pushed and popped at most once
- Space: O(n) - for the stack

## Example Walkthrough
For `heights = [10,6,8,5,11,9]`:

Using Approach 1 (right to left):
- i=5: stack=[], count=0, stack=[5]
- i=4: stack=[5], pop 5, count=1, stack=[4]
- i=3: stack=[4], count=1, stack=[4,3]
- i=2: stack=[4,3], pop 3, count=2, stack=[4,2]
- i=1: stack=[4,2], count=1, stack=[4,2,1]
- i=0: stack=[4,2,1], pop all, count=3, stack=[0]

Result: [3,1,2,1,1,0]

Your approach had the right intuition about using a stack, but the implementation needed refinement. The key is understanding that we only need to track people in decreasing order of height, and we can count visible people by checking how many we pop from the stack.
```
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        result = [0] * n
        stack = []  # Monotonic decreasing stack
        
        # Process from right to left
        for i in range(n - 1, -1, -1):
            count = 0
            
            # Pop all people shorter than current person
            # These are the people that person i can see
            while stack and heights[stack[-1]] < heights[i]:
                stack.pop()
                count += 1
            
            # If stack is not empty, person i can also see the next taller person
            if stack:
                count += 1
            
            result[i] = count
            stack.append(i)
        
        return result
```
# Alternative approach: Process from left to right
```
class Solution2:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        result = [0] * n
        stack = []  # Monotonic decreasing stack
        
        for i in range(n):
            # For each person in stack who is shorter than current person,
            # they can see the current person
            while stack and heights[stack[-1]] < heights[i]:
                idx = stack.pop()
                result[idx] += 1
            
            # The person at top of stack (if exists) can also see current person
            if stack:
                result[stack[-1]] += 1
            
            stack.append(i)
        
        return result
```