# Approach 0 (Brute Force):
# 1. Calculate the Euclidean distance for each point from the origin.
# 2. Store each point with its distance in a list.
# 3. Sort the list based on the distance in ascending order.
# 4. Return the first k points from the sorted list as the k closest points to the origin.
# Time Complexity: O(n log n), where n is the number of points, due to sorting.
# Space Complexity: O(n), as we store all points with their distances in a list.

# Approach:
# 1. For each point, calculate its Euclidean distance from the origin, which is simply the sum of the squares of its x and y coordinates.
# 2. Store each point in a min-heap along with its distance from the origin.
# 3. After adding all points to the heap, we extract the k smallest elements (closest points to the origin).
# 4. Return the k closest points.

from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        minheap = []

        # Step 1: Calculate distance for each point and add to min-heap
        for x, y in points:
            dist = x**2 + y**2  # Calculate Euclidean distance squared
            minheap.append([dist, x, y])  # Add distance and point coordinates to min-heap
        
        # Step 2: Transform the list into a heap in-place
        heapq.heapify(minheap)

        # Step 3: Extract k closest points
        while k >= 1:
            dist, x, y = heapq.heappop(minheap)  # Pop the point with the smallest distance
            res.append([x, y])  # Append the point coordinates to result list
            k -= 1  # Decrement k
        
        return res

# Time Complexity: O(n log n), where n is the number of points. Building the heap takes O(n), and extracting k points takes O(k log n) in the worst case.
# Space Complexity: O(n), as we store all points in the heap.
