
# 13. Roman to Integer

class Solution(object):
    def roman_to_int(self, s):
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        s_sum = 0
        s_len = len(s)
        for i in range(0, s_len):
            if i < s_len-1:
                if roman_dict[s[i]] >= roman_dict[s[i+1]]:
                    s_sum += roman_dict[s[i]]
                else:
                    s_sum -= (roman_dict[s[i]])
            else:
                s_sum += roman_dict[s[i]]
        return s_sum

if __name__ == "__main__":
    
    s1 = Solution()
    res = s1.roman_to_int("LVIII")
    print(res)
