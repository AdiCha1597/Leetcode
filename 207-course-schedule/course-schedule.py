class Solution:
    def canFinish(self, numCourses: int, preq: List[List[int]]) -> bool:
        # put all the courses in the hashmap
        preMap = {i: [] for i in range(numCourses)}

        # Append all the corresponding preq
        for crs, pre in preq:
            preMap[crs].append(pre)

        VisitSet = set()

        def dfs(crs):
            # if the course is already visited, loop is detected, hence false.
            if crs in VisitSet:
                return False
            #else if the crs doesn't have any preq, it can be completed.
            if preMap[crs] == []:
                return True

            #else just add the course to visited set to find out loops in future.
            VisitSet.add(crs)

            # iterate through the preq of the current course.
            for pre in preMap[crs]:
                # if dfs returns false, then the 
                #course cannot be completed,hence False.
                if not dfs(pre):
                    return False
            # else remove the course from the visited list.
            VisitSet.remove(crs)
                # Assign [] in preMap[crs] as all preq for crs are processed
            preMap[crs]= []
            return True
        # iterate through the courses, and run dfs on each recursively,
        # if at all, any course returns False, return False.
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        # else return True
        return True

# Time Complexity: O(V + E), where V is the number of courses and E is the number of prerequisites.

# Space Complexity: O(V + E) due to the storage of the adjacency list and the recursion stack in the worst case.