class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        start_color = image[sr][sc]

        if color == start_color:
            return image

        def dfs(i,j):
            if i < 0 or i >=m or j < 0 or j >= n or image[i][j] != start_color:
                return
            image[i][j] = color

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        dfs(sr, sc)
        return image


# Approach: Use DFS to recolor all connected pixels with the same starting color.
# Time Complexity: O(m * n) because each pixel is visited once.
# Space Complexity: O(m * n) due to the recursion stack in the worst case.