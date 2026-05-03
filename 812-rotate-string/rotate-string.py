class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        '''if len(s) != len(goal):
            return False
        return goal in (s+s)'''

        #Another solution
        if len(s) != len(goal):
            return False
        result = s + s

        if goal in result:
            return True
        return False