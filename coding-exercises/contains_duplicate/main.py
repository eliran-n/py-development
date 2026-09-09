
# 217. Contains Duplicate

def contains_duplicate(nums):

    dict_mem = {}
    nums_len = len(nums)

    for i in range(0, nums_len):
        if nums[i] not in dict_mem:
            dict_mem[nums[i]] = 1
        else:
            dict_mem[nums[i]] += 1

    for i in range(0, nums_len):
        if dict_mem[nums[i]] >= 2:
            return True
    return False

if __name__ == '__main__':

    test_list = [3,2,7,5,6,7,8,3]
    res = contains_duplicate(test_list)
    print(res)



