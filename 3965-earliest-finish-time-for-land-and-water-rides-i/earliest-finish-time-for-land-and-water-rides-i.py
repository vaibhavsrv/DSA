class Solution:
    def earliestFinishTime(self, lst: List[int], ld: List[int], wst: List[int], wd: List[int]) -> int:
        answer = float('inf')
        for i in range(len(lst)):
            t = lst[i] + ld[i]

            for j in range(len(wst)):
                answer = min(answer,max(t,wst[j]) + wd[j])

        
        for i in range(len(wst)):
            t = wst[i] + wd[i]

            for j in range(len(lst)):
                answer = min(answer,max(t,lst[j])+ld[j])

        return answer
