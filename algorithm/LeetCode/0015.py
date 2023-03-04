from typing import List
import itertools


class MyAnswer:
    # ! Time Limit Exceeded
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        comb = itertools.combinations(nums, 3)
        comb = [c for c in comb if sum(c) == 0]
        ans = set()
        for c in comb:
            ans.add(tuple(sorted(c)))
        return list(ans)


class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i in range(len(nums)-2):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # 간격을 좁혀가며 합(s) 계산
            left = i + 1
            right = len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    # s = 0인 경우이므로, 정답 및 스킵 처리
                    results.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return results


if __name__ == "__main__":
    testcase = [-1, 0, 1, 2, -1, -4]
    print(f'My Answer  : {MyAnswer().threeSum(testcase)}')
    print(f'Solution 1 : {Solution1().threeSum(testcase)}')
