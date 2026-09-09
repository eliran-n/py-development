
# 28. Find the Index of the First Occurrence in a String

class Solution(object):
    def str_str(self, haystack, needle):

        haystack_len = len(haystack)
        needle_len = len(needle)

        match_counter = 0
        match_flag = 0
        last_match_index = 0

        j = 0
        i = 0
        while i < haystack_len:

            if haystack[i] == needle[j]:

                if not match_flag:
                    match_flag = 1
                    last_match_index = i

                match_counter += 1
                j += 1
                i += 1

            else:

                if match_flag:

                    match_flag = 0
                    match_counter = 0
                    i = last_match_index + 1
                    j = 0

                else:
                    i += 1

            if match_counter == needle_len:
                return last_match_index

        return -1


if __name__ == "__main__":

    s1 = Solution()
    index = s1.str_str("sadbutsad", "sad")
    print(index)