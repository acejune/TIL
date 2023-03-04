from typing import List


class MyAnswer:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()


if __name__ == "__main__":
    testcase = ["h", "e", "l", "l", "o"]
    MyAnswer().reverseString(testcase)
    print(f'My Answer  : {testcase}')
