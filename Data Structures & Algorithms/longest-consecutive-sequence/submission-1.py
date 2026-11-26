class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        snums = set(nums)
        maxl = 0

        for num in snums:
            if (num - 1 not in snums) :
                length = 1
                while(num + 1 in snums):
                    length +=1 
                    num = num + 1
                if (length > maxl):
                    maxl = length
        return maxl