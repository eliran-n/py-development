
# 242. Valid Anagram

def is_anagram(s, t):

    dict_mem = {}
    str_s_len = len(s)
    str_t_len = len(t)

    if str_s_len != str_t_len:
        return False

    for i in range(0, str_s_len):

        if s[i] not in dict_mem:
            dict_mem[s[i]] = 1
        else:
            dict_mem[s[i]] += 1

        if t[i] not in dict_mem:
            dict_mem[t[i]] = -1
        else:
            dict_mem[t[i]] -= 1

    for i in range(0, str_s_len):
        if dict_mem[s[i]] != 0:
            return False

    return True


if __name__ == '__main__':

    res = is_anagram("anagram", "nagaram")
    print(res)

