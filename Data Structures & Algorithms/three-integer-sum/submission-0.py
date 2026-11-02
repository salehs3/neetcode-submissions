class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        s = sorted(nums)
        for i in range(len(nums) - 1):
            
            k = i + 1
            j = len(nums) - 1
            

            while(k < j):
                if (s[i]+s[k]+s[j] == 0):
                    result.add((s[i],s[j],s[k]))
                    k+=1
                    j-=1
                elif (s[i]+s[k]+s[j] < 0):
                    k+=1
                elif (s[i]+s[k]+s[j] > 0):
                    j-=1
        results = []
        for i in result:
            results.append(list(i))


        return results
                

        