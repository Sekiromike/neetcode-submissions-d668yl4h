class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right=1,max(piles)

        while left<=right:
            k=(left+right)//2

            hours=0

            for p in piles:
                hours+=(p+k-1)//k

            if h<hours:
                left=k+1
            else:
                right=k-1
        
        return left
