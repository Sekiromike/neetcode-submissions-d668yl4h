class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        max_frequency=0
        left=0
        longest=0

        counts={}

        for right,char in enumerate(s):
            counts[char]=counts.get(char,0)+1
            max_frequency=max(max_frequency,counts[char])

            while (right-left+1)-max_frequency>k:
                counts[s[left]]-=1
                left+=1
            
            longest=max(longest,right-left+1)

        return longest



        