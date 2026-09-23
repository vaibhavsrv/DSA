class Solution:
    def maskPII(self, s: str) -> str:
        if s[0].isalpha():
            s= s.lower()

            at = s.find('@')

            return s[0] + "*****" + s[at-1:]

        digit = ""

        for ch in s:
            if ch.isdigit():
                digit += ch

        countryCode = len(digit) - 10

        if countryCode == 0:
            return "***-***-" + digit[-4:]

        return "+" + "*" * countryCode + "-***-***-" + digit[-4:]