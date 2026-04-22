class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        if (n:=len(queries[0])) < 3: return queries
        answer = []
        for query in queries:
            for word in dictionary:
                difference = 0 
                for i in range(n):
                    difference += query[i] != word[i]
                    if difference > 2:
                        break
                if difference < 3:
                    answer.append(query); break
            
        return answer