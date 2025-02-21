class Solution:
    def romanToInt(self, s: str) -> int:
        arab = 0
        for i in range(len(s)):
            letter = s[i]
            if letter == 'M':
                if arab % 1000 == 100:
                    arab += 800
                else:
                    arab += 1000
            elif letter == 'D':
                if arab % 500 == 100:
                    arab += 300
                else:
                    arab += 500
            elif letter == 'C':
                if arab % 100 == 10:
                    arab += 80
                else:
                    arab += 100
            elif letter == 'L':
                if arab % 50 == 10:
                    arab += 30
                else:
                    arab += 50
            elif letter == 'X':
                if arab % 10 == 1:
                    arab += 8
                else:
                    arab += 10
            elif letter == 'V':
                if arab % 5 == 1:
                    arab += 3
                else:
                    arab += 5
            elif letter == 'I':
                arab += 1

        return arab
