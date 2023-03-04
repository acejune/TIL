from typing import List
import collections


class MyAnswer:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = collections.defaultdict(list)
        for s in strs:
            count = collections.Counter(s)
            count = sorted(count.items())
            count = tuple(count)
            str_dict[count].append(s)
        return str_dict.values()


class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return anagrams.values()


if __name__ == "__main__":
    testcase = ["eat","tea","tan","ate","nat","bat"]
    print(f'My Answer  : {MyAnswer().groupAnagrams(testcase)}')
    print(f'Solution 1 : {Solution1().groupAnagrams(testcase)}')
