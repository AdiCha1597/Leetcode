class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        res = 0
        while i<j:
            print(height[i], 'and', height[j])
            curr = min(height[i], height[j]) * (abs(i-j))
            res = max(curr, res)
            if height[i] > height[j]:
                j -= 1
            elif height[j] > height[i]:
                i += 1
            else:
                i += 1
                j -= 1
        return res

        
        