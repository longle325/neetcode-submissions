import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upperbound = max(piles)
        min_k = float("inf")

        def count_hour(k, piles) :
            count = 0
            for i in piles: 
                count += math.ceil(i/k) 
            return count
            
        left, right = 1, upperbound
        while left <= right: 
            mid = left + (right - left) // 2
            hour = count_hour(mid,piles)
            if hour <= h:
                if mid < min_k : 
                    min_k = mid
                right = mid - 1
            elif hour > h : 
                left = mid + 1
        return min_k