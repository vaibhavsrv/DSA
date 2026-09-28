class Solution:
    def maxDepth(self, s: str) -> int:
        d = 0
        m_d= 0
        for ch in s:
            if ch == "(":
                d += 1
                if d > m_d:
                    m_d = d

            elif ch == ")":
                d -=1
        return m_d