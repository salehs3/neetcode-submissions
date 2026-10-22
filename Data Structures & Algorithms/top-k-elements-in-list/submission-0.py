class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}

        for i in nums:
            if i in result:
                result[i]+=1;
            else: 
                result[i] = 1
        
        sorted_dict = dict(sorted(result.items(), key=lambda item: item[1],        reverse=True))

        top_k_list = []

        keys = list(sorted_dict.keys())
        
        
        for i in range(k):
            top_k_list.append(keys[i])
            
        return top_k_list

        