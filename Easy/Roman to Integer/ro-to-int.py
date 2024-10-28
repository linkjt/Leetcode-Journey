class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        Dg0b = list(s)
        total = 0
        for i in range(len(s)):
            if i<len(s)-1:
                if dic[Dg0b[1+i]]>dic[Dg0b[i]]:
                    value = -dic[Dg0b[i]]
                else:
                    value = dic[Dg0b[i]]
            else:
                value = dic[Dg0b[i]]
            total += value
        return total
