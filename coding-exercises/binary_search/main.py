
class Solution(object):
    def search(self, nums, target):

        low = 0
        high = len(nums) - 1
        mid = int((low + high)/2)

        while low <= high:
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                return mid

            mid = mid = int((low + high)/2)

        return -1


if __name__ == "__main__":

    list_search = [-1,0,3,5,9,12]
    target_num = 9

    s1 = Solution()
    index = s1.search(list_search, target_num)
    print(index)