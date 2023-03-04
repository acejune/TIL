from typing import List
import collections


class MyAnswer:
    # ! Time Limit Exceeded
    def trap(self, height: List[int]) -> int:
        max_height = max(height)
        rain = 0

        for h in range(1, max_height+1):
            check = ['1' if x >= h else '0' for x in height]
            check = ''.join(check)
            check = check.strip('0')
            count = collections.Counter(check)
            rain += count['0']
        return rain


class Solution1:
    """투 포인터를 최대로 이동"""
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        volume = 0
        left = 0
        right = len(height) - 1
        left_max = height[left]    # 왼쪽의 최대 기둥 높이
        right_max = height[right]  # 오른쪽의 최대 기둥 높이

        # 가장 기둥 높이가 높은 곳에서 좌우 포인터가 만나게 됨
        while left < right:
            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)

            # 더 높은 쪽을 향해 투 포인터 이동
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume


class Solution2:
    """스택 쌓기"""
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for idx, hvalue in enumerate(height):
            # 변곡점을 만나는 경우 (변곡점: 현재 높이가 이전 높이보다 높은 부분)
            while stack and (hvalue > height[stack[-1]]):
                # 스택에서 꺼내기
                top = stack.pop()
                if not stack:
                    break

                # 이전과의 차이만큼을 물 높이 처리
                distance = idx - stack[-1] - 1
                waters = min(hvalue, height[stack[-1]]) - height[top]

                volume += distance * waters
            stack.append(idx)
        return volume


if __name__ == "__main__":
    testcase = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(f'My Answer  : {MyAnswer().trap(testcase)}')
    print(f'Solution 1 : {Solution1().trap(testcase)}')
    print(f'Solution 2 : {Solution2().trap(testcase)}')
