class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while (l < r):
            while (l < r and not s[l].isalnum()):
                l+=1
            while(r > l and not s[r].isalnum()):
                r-=1

            if (s[l].lower() != s[r].lower()) :
                return False
            r-=1
            l+=1
        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # l = 0
        # r = len(s) - 1

        # while l < r:
        #     while l < r and not s[l].isalnum():
        #         l+=1
        #     while r > l and not s[r].isalnum():
        #         r-=1

        #     if (s[l].lower() != s[r].lower()):
        #         return False
        #     r-=1
        #     l+=1
        # return True


        # l = list(s)
        # l2 = []
        # for i in l:
        #     if i.lower().isalnum():
        #         l2.append(i.lower())
        

        # d = l2[::-1]
        # if (l2 == d) :
        #     return True
        # return False
        