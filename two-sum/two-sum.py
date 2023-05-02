class Solution(object):
    def twoSum(self, nums, target):
        answer = []
        for num in range(len(nums)):
            for j in range(len(nums) - 1):
                if num == j + 1:
                    pass
                elif nums[num] + nums[j + 1] == target:
                    answer.append(num)
                    answer.append(j + 1)
                    return answer
            

