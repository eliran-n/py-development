
# 20. Valid Parentheses

class Solution(object):

    def __init__(self):
        self.cmp_dict = {')': '(', ']': '[', '}': '{'}

    def is_valid(self, s):

        stack = Stack()

        for ch in s:
            if self.is_open_char(ch):
                stack.push(ch)
            elif not stack.is_empty():
                popped_ch = stack.pop()
                if popped_ch != self.cmp_dict[ch]:
                    return False
            else:
                return False

        if not stack.is_empty():
            return False
        else:
            return True

    @staticmethod
    def is_open_char(char):
        if char in ['(', '{', '[']:
            return True
        else:
            return False


class Stack:

    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val)

    def pop(self):
        if not self.is_empty():
            val = self.data.pop()
            return val
        return None

    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False


if __name__ == "__main__":

    s1 = Solution()

    res = s1.is_valid("()[]{}")
    print(res)

    res = s1.is_valid("([])")
    print(res)

    res = s1.is_valid("([)]")
    print(res)