class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        lucky_numbers = []
        
        # Iterate through each row to find the minimum elements
        for i in range(len(matrix)):
            min_val = min(matrix[i])
            min_index = matrix[i].index(min_val)
            
            # Check if the minimum element in the row is the maximum in its column
            is_lucky = True
            for row in matrix:
                if row[min_index] > min_val:
                    is_lucky = False
                    break
            
            if is_lucky:
                lucky_numbers.append(min_val)
        
        return lucky_numbers
        
"""
	•	Time Complexity:  O(m * n) 
	•	Space Complexity:  O(m)  (including the result list)
"""

        