class Solution:
    def canFinish(self, numCourses: int, preq: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in preq:
            preMap[crs].append(pre)

        vs = set()
        def dfs(crs):
            if crs in vs:
                return False
            if preMap[crs] == []:
                return True

            vs.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            vs.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True



                
            

        