class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        times = []
        for hour in range(12):
            for minutes in range(60):
                hour_one = bin(hour).count('1')
                minute_one = bin(minutes).count('1')
                if hour_one+minute_one == turnedOn:
                    times.append(f"{hour}:{minutes:02d}")
        return times
