
# 9. Palindrome Number

class Solution(object):
    def is_palindrome(self, x):

        if x < 0:
            return False

        digits_list = []
        while x > 0:
            last_digit = x % 10
            digits_list.append(last_digit)
            x = x // 10

        digits_len = len(digits_list)
        compare_len = digits_len // 2
        for i in range(0, compare_len):
            if digits_list[i] != digits_list[digits_len - i - 1]:
                return False
        return True

if __name__ == '__main__':

    s1 = Solution()
    res = s1.is_palindrome(121)
    print(res)
