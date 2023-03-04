import re


class MyAnswer:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(x for x in s if x.isalpha() or x.isdigit())
        return s == s[::-1]


class Solution1:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]


if __name__ == "__main__":
    testcase = "A man, a plan, a canal: Panama"
    print(f'My Answer  : {MyAnswer().isPalindrome(testcase)}')
    print(f'Solution 1 : {Solution1().isPalindrome(testcase)}')
