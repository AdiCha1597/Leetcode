class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        r, c = len(rowSum), len(colSum)
        # initialize the matrix with 0's
        res = [[0 for _ in range(c)] for _ in range(r)]
        
        for i in range(r):
            for j in range(c):
                #put the min value at res[i][j]
                candidate = min(rowSum[i],colSum[j])
                res[i][j] = candidate
                # subtract the min value from rowSum and colSum
                rowSum[i] -= candidate
                colSum[j] -= candidate
        return res

"""
Time Complexity: O(r * c)
Space Complexity: O(r *c)
"""
                
        

        
        

    


        