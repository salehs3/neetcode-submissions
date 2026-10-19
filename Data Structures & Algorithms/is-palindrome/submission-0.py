class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = list(s)
        l2 = []
        for i in l:
            if i.lower().isalnum():
                l2.append(i.lower())
        

        d = l2[::-1]
        if (l2 == d) :
            return True
        return False
        