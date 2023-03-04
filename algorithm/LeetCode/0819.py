from typing import List
import re
import collections


class MyAnswer:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub(r'\W', ' ', paragraph)
        paragraph = paragraph.lower()
        paragraph = paragraph.split()
        counter = collections.Counter(paragraph)
        counter = counter.most_common()
        for k, _ in counter:
            if k not in banned:
                return k


class Solution1:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub(r'[^\w]', ' ', paragraph)
        paragraph = paragraph.lower()
        paragraph = paragraph.split()
        words = [word for word in paragraph if word not in banned]
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]


if __name__ == "__main__":
    testcase_par = "abc abc? abcd the jeff!"
    testcase_ban = ["abc","abcd","jeff"]
    print(f'My Answer  : {MyAnswer().mostCommonWord(testcase_par, testcase_ban)}')
    print(f'Solution 1 : {Solution1().mostCommonWord(testcase_par, testcase_ban)}')
