
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

            # traverse the string from backwards and compare the previous element with current
            print(s[i])
            if i < len(s)-1 and dict_roman[s[i]] < dict_roman[s[i+1]]:
                print(len(s)-1, dict_roman[s[i]], dict_roman[s[i+1]])
                # if the previous element is less than the current element then,
                # decrement the number by that previous element --
                # example -- current - V previous - I == V[val] - I[val] == 4
                out -= dict_roman[s[i]]
            else:
                # else add the number with the current element -- VI
                # The number I is greater than V so add V to the current I --- 6
                out += dict_roman[s[i]]
            i -= 1
        # print(out)
        # print(out)
        return out


s = Solution()
s.romanToInt('IV')
