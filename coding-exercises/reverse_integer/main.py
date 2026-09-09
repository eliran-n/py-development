
# 7. Reverse Integer

class Solution(object):
    def reverse(self, x):

        negative_flag = 0
        if x < 0:
            x = x * (-1)
            negative_flag = 1

        number = x
        reversed_num = 0
        digits_len = self.count_digits(x)
        multiply_factor = self.calc_multiply_base(digits_len)

        while digits_len > 0:
            reversed_num += ((number % 10) * multiply_factor)
            number = number // 10
            multiply_factor = multiply_factor // 10
            digits_len = digits_len - 1

        if negative_flag:
            reversed_num = reversed_num * (-1)

        if reversed_num > ((2**31) - 1) or reversed_num < (-2 ** 31):
            return 0

        return reversed_num

    def count_digits(self, x):
        counter = 0
        num = x
        while num > 0:
            num = num // 10
            counter += 1
        return counter

    def calc_multiply_base(self, digits_num):
        multiply_factor = 1
        i = digits_num - 1
        while i > 0:
            multiply_factor = multiply_factor * 10
            i -= 1
        return multiply_factor


if __name__ == "__main__":

    s1 = Solution()
    res = s1.reverse(123)
    print(res)
