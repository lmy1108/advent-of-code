# 127. Word Ladder

## Problem Statement
Given two words (`beginWord` and `endWord`), and a dictionary's word list, find the length of the shortest transformation sequence from `beginWord` to `endWord` such that:

1. Only one letter can be changed at a time.
2. Each transformed word must exist in the word list.

Return 0 if no such transformation sequence exists.

## Approach: Bidirectional BFS with Pattern Matching

### Key Insights
1. **Pattern Matching**: We can represent each word as a set of patterns where each character is replaced by a wildcard (`*`). This helps us efficiently find all words that are one letter apart.
2. **Bidirectional BFS**: Instead of searching from just the beginning, we search from both the start and end words simultaneously. When the two searches meet, we've found the shortest path.
3. **Optimization**: Always expand the smaller queue first to minimize the search space.

### Solution Code
```python
from collections import defaultdict
from typing import List, Set

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # If the target word isn't in our word list, it's impossible to reach
        if endWord not in wordList:
            return 0
        
        # Build a graph where we can find all words that differ by one letter
        # For "hot", we create patterns: "*ot", "h*t", "ho*"
        # This helps us find neighbors efficiently
        pattern_to_words = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                # Replace each position with * to create a pattern
                pattern = word[:i] + "*" + word[i+1:]
                pattern_to_words[pattern].append(word)
        
        # Two-end BFS: We search from both start and end simultaneously
        # This can significantly reduce the search space
        queue_from_begin = {beginWord}  # Words we're exploring from the beginning
        queue_from_end = {endWord}      # Words we're exploring from the end
        visited_words = {beginWord, endWord}  # Keep track of words we've seen
        
        steps = 1  # We start counting from 1 (the beginWord itself)
        
        while queue_from_begin and queue_from_end:
            steps += 1
            
            # Always expand the smaller queue (optimization)
            # This keeps both searches balanced
            if len(queue_from_begin) > len(queue_from_end):
                queue_from_begin, queue_from_end = queue_from_end, queue_from_begin
            
            # Process all words in the current level
            next_level = set()
            for current_word in queue_from_begin:
                # Check all possible one-letter transformations
                for i in range(len(current_word)):
                    pattern = current_word[:i] + "*" + current_word[i+1:]
                    
                    # Get all words matching this pattern
                    for neighbor_word in pattern_to_words.get(pattern, []):
                        # If we found a word that's in the other search, we met!
                        if neighbor_word in queue_from_end:
                            return steps
                        
                        # If we haven't visited this word, add it to explore
                        if neighbor_word not in visited_words:
                            next_level.add(neighbor_word)
                            visited_words.add(neighbor_word)
            
            # Move to the next level
            queue_from_begin = next_level
        
        # No path found
        return 0
```

### Explanation

1. **Pattern Dictionary Creation**:
   - We first create a dictionary that maps patterns to words. For example, for the word "hot", we create patterns "*ot", "h*t", and "ho*".
   - This allows us to quickly find all words that are one letter apart from any given word.

2. **Bidirectional BFS Initialization**:
   - We maintain two sets: `queue_from_begin` and `queue_from_end`.
   - We also maintain a `visited_words` set to avoid cycles.

3. **BFS Execution**:
   - At each step, we process the smaller queue first (optimization).
   - For each word in the current level, we generate all possible patterns and find all neighboring words.
   - If we find a word that exists in the other search's queue, we've found the shortest path.
   - Otherwise, we add the unvisited neighbors to the next level.

4. **Termination**:
   - If we exhaust one of the queues without finding a match, return 0 (no path exists).
   - If we find a match, return the current step count.

### Time and Space Complexity

- **Time Complexity**: O(M² × N)
  - M is the length of each word
  - N is the total number of words in the word list
  - For each word, we generate M patterns, and for each pattern, we might process up to N words

- **Space Complexity**: O(M² × N)
  - We store all possible patterns for all words
  - The BFS queue can store up to N words

### Key Optimizations
1. **Bidirectional BFS**: Reduces the search space from O(b^d) to O(2×b^(d/2)), where b is the branching factor and d is the depth.
2. **Pattern Matching**: Allows O(1) lookup of all words that are one letter apart.
3. **Queue Size Balancing**: Always expanding the smaller queue keeps the search balanced and efficient.

This solution efficiently finds the shortest transformation sequence by leveraging pattern matching and bidirectional BFS, making it optimal for this problem.
