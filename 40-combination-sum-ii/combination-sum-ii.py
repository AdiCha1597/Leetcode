class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def helper(cur, pos, target):
            if target == 0:
                res.append(cur.copy())
                return  # Add return here to stop further processing
            if target < 0:
                return

            prev = -1
            for i in range(pos, len(nums)):
                if nums[i] == prev:
                    continue
                cur.append(nums[i])
                helper(cur, i + 1, target - nums[i])
                cur.pop()
                prev = nums[i]

        helper([], 0, target)
        return res
