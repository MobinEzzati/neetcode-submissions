class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix : 
            left, right = 0, len(row) - 1 

            while left <= right :
                mid = (left + right)//2 

                if row[mid] == target:
                    return True
                
                if row[mid] > target : 
                    right = right - 1 
                if row[mid] < target : 
                    left = left + 1
        return False 
        