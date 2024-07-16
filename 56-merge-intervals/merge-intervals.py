class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # First, sort the intervals based on the start times
        intervals.sort(key=lambda x: x[0])
        res = []  # This will hold the merged intervals
        s, e = intervals[0]  # Start with the first interval

        for i in range(1, len(intervals)):
            s1, e1 = intervals[i]
            if s1 <= e:  # Overlapping intervals
                e = max(e, e1)  # Merge by extending the end time
                continue
            else:  # Non-overlapping interval, push the previous interval to result
                res.append([s, e])
                s, e = s1, e1  # Update to the new interval
        res.append([s, e])  # Add the last interval to result
        return res

# Time Complexity: O(n log n) due to sorting, where n is the number of intervals.
# Space Complexity: O(n) for the result list in the worst case (no overlaps).

