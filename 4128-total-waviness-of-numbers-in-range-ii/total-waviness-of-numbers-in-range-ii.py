class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def sum_wavy(num):
            digits=[]
            while num:
                digits.append(num%10)
                num=num//10
            m=len(digits)
            memo={}
            def sum_wavy_r(args):
                i,w,prev,prev_2,msd,tight=args
                if i<0:
                    return w
                if args not in memo:
                    memo[args]=0
                    for d in range(digits[i]+1 if tight else 10):
                        new_msd=msd or d>0
                        memo[args]+=sum_wavy_r((
                            i-1,
                            w+(prev is not None and prev_2 is not None and (prev>max(d,prev_2) or prev<min(d,prev_2))),
                            d if new_msd else None,
                            prev,
                            new_msd,
                            tight if d==digits[i] else False
                        ))
                return memo[args]
            ans=sum_wavy_r((m-1, 0, None, None, False, True))
            del memo
            return ans
        return sum_wavy(num2)-sum_wavy(num1-1)