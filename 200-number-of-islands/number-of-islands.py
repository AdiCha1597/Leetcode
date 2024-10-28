# Brute Force Approach:
# Traverse each cell in the grid; for each cell that is '1', mark all connected cells as '0' to avoid double-counting.
# Count each traversal as a separate island. This approach modifies the grid in place.
# Time Complexity: O((M * N)^2) because each traversal may visit every cell multiple times.
# Space Complexity: O(1) (no additional space used, but modifies input grid).

# Approach:
# Use Breadth-First Search (BFS) to find all connected cells for each island. For each unvisited land cell, run BFS 
# to mark all connected land cells as visited. Increment the island count after each BFS completes.

from typing import List
import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0  # if grid is empty, return 0 islands

        rows, cols = len(grid), len(grid[0])  # store the number of rows and columns
        visited = set()  # set to store visited land cells
        islands = 0  # variable to store the result, the number of islands

        def bfs(r, c):
            q = collections.deque()  # queue for BFS
            visited.add((r, c))  # add cell to visited set
            q.append((r, c))  # add cell to queue
            while q:  # while there are cells in the queue
                row, col = q.popleft()  # pop leftmost cell from queue
                dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # four possible directions
                for dr, dc in dirs:  # iterate through all directions
                    r, c = row + dr, col + dc
                    if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visited):
                        q.append((r, c))  # add cell to queue if it meets criteria
                        visited.add((r, c))  # mark cell as visited

        for r in range(rows):  # iterate through grid rows
            for c in range(cols):  # iterate through grid columns
                if grid[r][c] == '1' and (r, c) not in visited:  # start BFS on unvisited land
                    bfs(r, c)  # run BFS on the cell
                    islands += 1  # increment island count after BFS

        return islands  # return the total count of islands

"""
Time Complexity: O(M * N), where M is the number of rows and N is the number of columns, because each cell is processed once.
Space Complexity: O(M * N) due to the visited set and the BFS queue that can potentially store all cells.
"""  