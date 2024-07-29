from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], new_i: List[int]) -> List[List[int]]:
        """
        Approach:
        - Iterate through the list of intervals.
        - If the new interval comes before the current interval without overlap, append the new interval and return the rest of the intervals.
        - If the new interval comes after the current interval without overlap, append the current interval to the result.
        - If there is an overlap, merge the new interval with the current interval.
        
        Time Complexity: O(n), where n is the number of intervals. Each interval is processed once.
        Space Complexity: O(n), where n is the number of intervals. The result list stores all intervals
        """
        res = []  # Result list to store merged intervals

        for i in range(len(intervals)):
            # If the new interval comes before the current interval
            if new_i[1] < intervals[i][0]:
                res.append(new_i)  # Append the new interval to the result
                return res + intervals[i:]  # Append the rest of the intervals and return

            # If the new interval comes after the current interval
            elif new_i[0] > intervals[i][1]:
                res.append(intervals[i])  # Append the current interval to the result

            # If there is an overlap with the current interval
            else:
                # Merge the new interval with the current interval
                new_i = [min(new_i[0], intervals[i][0]), max(new_i[1], intervals[i][1])]

        # Append the last merged interval
        res.append(new_i)
        return res  # Return the result list





