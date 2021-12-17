
class Solution:
    def romanToInt(self, s: str) -> int:
        dict_roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        out = 0
        i = len(s) - 1

        while i >= 0:
            if i < len(s)-1 and  dict_roman[s[i]] < dict_roman[s[i+1]]:
                out -= dict_roman[s[i]]
            else:
                out += dict_roman[s[i]]
            i -= 1
        # print(out)
        print(out)
        return out

