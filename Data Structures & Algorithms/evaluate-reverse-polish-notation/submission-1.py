class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.nums = []
        
        for i in tokens:
            if i == "+" or i=="-" or i == "*" or i == "/":
                c = 0
                b = self.nums[-1]
                self.nums.pop()
                a = self.nums[-1]
                self.nums.pop()
                if (i == "+") :
                    c = a+b
                elif (i == "-"):
                    c = a- b
                elif (i == "*"):
                    c = a*b
                elif(i == "/"):
                    c= int(a/b)
                self.nums.append(c)
            else:
                self.nums.append(int(i))

        return self.nums[-1]
                    

        