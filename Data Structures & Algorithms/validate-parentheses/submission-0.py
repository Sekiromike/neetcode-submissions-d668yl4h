class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        matching={
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        for bracket in s:
            if bracket in matching:
                if not stack:
                    return False
                
                if stack[-1]!=matching[bracket]:
                    return False
        
                stack.pop()
            
            else:
                stack.append(bracket)

        return len(stack)==0