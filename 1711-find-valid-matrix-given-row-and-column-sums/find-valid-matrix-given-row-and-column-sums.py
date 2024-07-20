class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        r, c = len(rowSum), len(colSum)
        res = [[0 for _ in range(c)] for _ in range(r)]
        
        for i in range(r):
            for j in range(c):
                candidate = min(rowSum[i],colSum[j])
                res[i][j] = candidate
                rowSum[i] -= candidate
                colSum[j] -= candidate
        return res
                
        

        
        

    


        