class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numlist=set(nums)

        longest=0

        for x in numlist:
            if x-1 not in numlist:
                current = x
                length=1

                while current+1 in numlist:
                    current+=1
                    length+=1
                
                longest=max(longest,length)
        return  longest
        