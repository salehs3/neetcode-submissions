class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       snums = set(nums)
       maxl = 0

       for i in snums:
            if (i - 1 not in snums):
                length = 1
                while(i + 1 in snums):
                    length+=1
                    i+=1
                if (maxl < length):
                    maxl = length
        
       return maxl
        