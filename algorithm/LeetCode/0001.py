from typing import List


class MyAnswer:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            new_target = target - num
            temp_nums = nums[idx+1:]
            if new_target in temp_nums:
                return [idx, idx+1+temp_nums.index(new_target)]


class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i

        for i, num in enumerate(nums):
            complement = target-num
            if (complement in nums_map) and (i != nums_map[complement]):
                return [i, nums_map[complement]]


class Solution2:
    """Solution1 코드의 간결한 버전 (성능은 큰 차이 없음)"""
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            complement = target-num
            if complement in nums_map:
                return [nums_map[complement], i]
            nums_map[num] = i


if __name__ == "__main__":
    testcase_num = [2,7,11,15]
    testcase_tar = 9
    print(f'My Answer  : {MyAnswer().twoSum(testcase_num, testcase_tar)}')
    print(f'Solution 1 : {Solution1().twoSum(testcase_num, testcase_tar)}')
    print(f'Solution 2 : {Solution2().twoSum(testcase_num, testcase_tar)}')
