class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        time = 0
        while tickets[k] > 0:
            tickets[0] -= 1
            time +=1

            if tickets[0] == 0:
                tickets.pop(0)

                if k == 0:
                    break

                k -=1
            else:
                p = tickets.pop(0)
                tickets.append(p)

                if k == 0:
                    k = len(tickets)-1
                else:
                    k -=1

        return time