class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # we do this so that we dont need to check whether we the key is there in the dict (res[tuple(count)] = s if we do this it just replaces the list instead of appending

        for i in strs:
            count = [0] * 26 # here it is an array of 26 0s reperesents the letters and and the indexed represesnts each letter so if we find a letter we increase it value by 1
            for j in i:
                count[ord(j) - ord("a")] += 1 
                # HEre we do ord(j) = ord["a"] so that we #get the correct index for count Ex ord a is 80 and j = c we get 82 so 82-80 = 2 which #represents c in count

            result[tuple(count)].append(i) # we change to tuple because keys should be immutable. we append and  = because if we do = it just replaces the existing list instead of adding to it.
        return list(result.values())
        