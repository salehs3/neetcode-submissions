class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0]*len(temperatures)
        index= []

        for i in range (len(temperatures)):
            while(index and temperatures[i]> temperatures[index[-1]]):
                top = index.pop()
                days = i -top
                results[top] = days
            index.append(i)
        return results