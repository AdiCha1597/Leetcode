class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        res = 0
        while i<j:
            curr = min(height[i], height[j]) * (abs(i-j))
            if height[i] > height[j]:
                j -= 1
            elif height[j] > height[i]:
                i += 1
            else:
                i += 1
                j -= 1
            res = max(curr, res)
        return res

"""
	•	Approach: Two-pointer technique.
	•	Time Complexity: (O(n)), because each pointer moves at most n times.
	•	Space Complexity: O(1), as only a constant amount of extra space is used.
"""
        
        