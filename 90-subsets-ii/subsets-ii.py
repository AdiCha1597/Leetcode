class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        # sort the nums, to get all the duplicate values next to each other.
        nums = sorted(nums)

        #helper function to process the elements
        def helper(i):
            # base case: if subset is equal to len(nums), append the copy
            if i == len(nums):
                res.append(subset[::])
                return 
            # else append the element in the subset
            subset.append(nums[i])
            #recursively call the function incrementing i
            helper(i + 1)
            #pop from the subset and call once the value is not same while
            # incrementing.
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            # call the helper function once you get the next non-duplicate.
            helper(i + 1)
        
        helper(0)
        return res
                
                


        