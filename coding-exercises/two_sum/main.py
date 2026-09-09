
# 1. Two Sum

# brute force solution
def two_sum(nums, target):

    # [3, 6, 2, 7]

    # 0,1  0,2  0,3
    # 1,2   1,3
    # 2,3

    nums_len = len(nums)
    for i in range(0, nums_len-1):
        for j in range(i+1, nums_len):
            if nums[i]+nums[j] == target:
                return [i,j]
    return []

# lookup solution
def two_sum_effective(nums, target):

    dict_mem = {}

    nums_len = len(nums)
    for i in range(0, nums_len):
        complement = target - nums[i]
        if complement in dict_mem:
            return [i, dict_mem[complement]]
        else:
            dict_mem[nums[i]] = i
    return []


if __name__ == '__main__':

    nums_list = [3, 6, 2, 7]
    target_num = 13

    res = two_sum(nums_list, target_num)
    print(res)

    res = two_sum_effective(nums_list, target_num)
    print(res)



