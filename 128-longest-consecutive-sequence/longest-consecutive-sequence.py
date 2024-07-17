class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert the list to a set to remove duplicates and allow O(1) look-up times
        nums_set = set(nums)
        maxVal = 0  # Initialize the maximum length of consecutive sequence
        
        for n in nums:
            cnt = 1  # Start counting with the current number
            # Only start counting if 'n' is the beginning of a sequence
            if (n - 1) not in nums_set:
                # Increment the sequence length if the next number is in the set
                while n+cnt  in nums_set:
                    cnt += 1
                # Update the maximum length found so far
                maxVal = max(maxVal, cnt)
        return maxVal
        # TC :O(n) SC: O(n)









        #[100,4,200,1,3,2]
        # hmap = {}
        
        # for num in nums:
        #     if num - 1 in hmap:
        #         hmap[num-1] = num
        #     if num + 1 in hmap:
        #         hmap[num] = num+1
        #     if num not in hmap:
        #         hmap[num] = float(inf)
        
        # maxVal = 0
        # for k,v in hmap.items():
        #     prev = k
        #     nxt = v
        #     cnt = 1

        #     while nxt in hmap:
        #         cnt += 1
        #         prev, nxt = nxt, hmap[nxt]
        #     maxVal= max(maxVal, cnt)
        # return maxVal


        








        
            