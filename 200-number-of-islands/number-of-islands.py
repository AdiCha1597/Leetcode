class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #if empty grid, return 0
        if not grid:
            return 0
        # store the number of rows and columns
        rows, cols = len(grid), len(grid[0])
        # take a set ffor storing all the visited land
        visited = set()
        #take a variable to store the number of islands result
        islands = 0

        def bfs(r,c):
            # take a queue to store the future elements to run bfs on
            q = collections.deque()
            # add the r,c to the visited set and queue
            visited.add((r,c))
            q.append((r,c))

            # while we land element in the queue
            while q:
                # popleft row and col from the queue
                row, col = q.popleft()
                # store all the 4 directions that we can go from any element.
                dirs = [[1,0], [-1, 0], [0,1], [0,-1]]

                # iterate every direction from the current element(row, col)
                for dr, dc in dirs:
                    r, c = row + dr, col + dc
                    # if the new directed element is in range,
                    # is 1 and not visited already, 
                    # append to q and add to visited
                    if(r in range(rows) and
                    c in range(cols) and
                    grid[r][c] == "1" and 
                    (r,c) not in visited):
                        q.append((r,c))
                        visited.add((r,c))

        # iterate through the grid elements             
        for r in range(rows):
            for c in range(cols):
                #and run bfs on the elements that are 
                #land and are not already visited.
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    # increment the island once the entire island is processed.
                    islands += 1
        return islands  
"""
Time Complexity: O(M * N), where M is the number of rows and N is the number of columns, because each cell is processed once.

Space Complexity: O(M * N) due to the visited set and the BFS queue that can potentially store all cells. 
"""      


        


