class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        need = 0
        bal = 0

        for ch in s:
            if ch == '(':
                bal +=1 
            elif bal > 0:
                bal -= 1
            else:
                need += 1
            
        return need+bal