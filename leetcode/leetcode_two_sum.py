
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Method -- One Pass
        dict_ = {}
        for i, num in enumerate(nums):
            # print(i, num)
            diff = target - num
            print(diff)
            if diff in dict_:
                return [dict_[diff], i]
            dict_[num] = i
        return

        # Method -- Brute Force
        # print(nums)
        # list_ = set()
        # for i in range(0, len(nums)):
        #     # print(nums[i])
        #     for j in range(i+1, len(nums)):
        #         print(nums[i], nums[j])
        #         if nums[i] + nums[j] == target:
        #             list_.add(i)
        #             list_.add(j)
        # # print()
        # return list(list_)
