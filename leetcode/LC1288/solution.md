# 1288. Remove Covered Intervals

## Problem Statement
Given an array of intervals where `intervals[i] = [start_i, end_i]`, remove all intervals that are covered by another interval in the list. An interval `[a, b)` is covered by `[c, d)` if and only if `c <= a` and `b <= d`.

## Intuition
To efficiently find covered intervals, we need to process the intervals in a way that allows us to easily compare each interval with the ones that come after it. Sorting helps us achieve this.

## Why Sort by Start Time Increasing and End Time Decreasing?

1. **Start Time Increasing**: By sorting intervals by their start time, we ensure that any interval that could cover another comes after it in the sorted list. This is because a covering interval must have a start time that is less than or equal to the covered interval's start time.

2. **End Time Decreasing (for same start times)**: When two intervals have the same start time, we want the longer interval to come first. This is because the longer interval will cover the shorter one if they start at the same point.

## Solution Code
```python
class Solution:
    def removeCoveredIntervals(self, A: List[List[int]]) -> int:
        res = right = 0
        A.sort(key = lambda a : (a[0], -a[1]))
        for i, j in A:
            res += j > right
            right = max(right, j)
        return res
```

## Explanation
1. **Sorting**: We sort the intervals by start time in ascending order and end time in descending order. This ensures that:
   - Intervals are processed from left to right
   - For intervals with the same start, the longer interval comes first

2. **Tracking Right Boundary**: We maintain a variable `right` that keeps track of the furthest right boundary we've seen so far.

3. **Counting Non-covered Intervals**: For each interval `[i, j]`:
   - If `j > right`, it means this interval is not covered by any previous interval, so we increment our result counter
   - We update `right` to be the maximum of its current value and `j`


## Time and Space Complexity
- **Time Complexity**: O(n log n) due to sorting
- **Space Complexity**: O(1) or O(n) depending on the sorting algorithm used

## Video Explanation
For a visual walkthrough of this problem, check out this video:
[Remove Covered Intervals - Leetcode 1288](https://www.youtube.com/watch?v=ihf8JjQdta0&list=PLbaIOC0vpjNW6V4ZTd5OpURZ6m0mf0G8n)
