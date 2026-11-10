class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        
     

        while top <= bottom:
            mid = (top+bottom)//2
            if (matrix[mid][-1] < target) :
                top = mid + 1
            elif (matrix[mid][0] > target) :
                bottom = mid - 1
            elif (matrix[mid][0] <= target <= matrix[mid][-1]):
                top2 = 0
                bottom2 = len(matrix[mid]) - 1
                while(top2 <= bottom2):
                    mid2 = (top2+bottom2)//2
                    if (target < matrix[mid][mid2]):
                        bottom2 = mid2 - 1
                    elif (target > matrix[mid][mid2]):
                        top2 = mid2+1
                    elif (target == matrix[mid][mid2]):
                        
                        return True
                else :
                   return False
            else:
                return False

        return False