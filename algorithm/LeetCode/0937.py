from typing import List


class MyAnswer:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for log in logs:
            if log[-1].isalpha():
                letter_logs.append(log)
            else:
                digit_logs.append(log)
        letter_logs.sort(key=lambda x: (x.split()[1:], x))
        return letter_logs + digit_logs


class Solution1:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits


if __name__ == "__main__":
    testcase = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    print(f'My Answer  : {MyAnswer().reorderLogFiles(testcase)}')
    print(f'Solution 1 : {Solution1().reorderLogFiles(testcase)}')
