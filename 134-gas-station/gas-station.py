class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        else:
            diff = [0] * len(gas)
            for i in range(0, len(cost)): diff[i] = gas[i] - cost[i] 
            total = 0
            start = 0
            i= 0
            while i < len(cost):
                total += diff[i]
                if total < 0:
                    total = 0
                    i += 1
                    start = i
                else:
                    i += 1
        return start



        