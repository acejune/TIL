class MyAnswer:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s

        palindrom = ''
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                temp = s[i:j]
                if len(temp) > len(palindrom) and temp == temp[::-1]:
                    palindrom = temp
        return palindrom


class Solution1:
    def longestPalindrome(self, s: str) -> str:
        # Palindrome 확징 & 투포인터 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        # 해당 사항이 없을 때 빠르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        # 슬라이딩 윈도우 오른쪽으로 이동
        for i in range(len(s) - 1):
            result = max(result,
                         expand(i, i+1),  # 길이가 짝수인 문자열 리턴
                         expand(i, i+2),  # 길이가 홀수인 문자열 리턴
                         key=len)
        return result


if __name__ == "__main__":
    testcase = "jcwwnkwiajicysmdueefqjnrokunucidhgkswbgjkkrujkxkxeanrpjvpliomxztalhmvcldnqmkslkprhgtwlnsnygbzdvtdbsdzsdjggzgmhogknpfhtgjmclrkgfqdbiagwrqqcnagosnqrnpapxfrtrhzlyhszdtgkqggmewqmwugrbufiwfvtjhczqgcwpcyjioeacggiwyinpkyxrpxhglrtojgjmmswxnvirfsrbhmpqgjyyagjqfwkqkjkumywvgfutmiwihwnnhbfxcijaoiyxbdnrckexqfhsmmxflaneccyaoqoxfbaylcvvpfafsikebzcdufvhluldguwsmrtjaljpcjestranfrvgvytozxpcvnwquhnsxlmzkehwopgxvifajmrlwqiqylgxibnypxwpkggxevyfoxywfsfpjbzfxxysgxgwxrzkwdqlkrpajlltzqfqshdokibakkhydizsgwbygqulljqmtxkwepitsukwjlrrmsjptwabtlqytprkkuxtqdmptctkfabxsohrfrqvrbjfbppfkpthosveoppiywkkuoasefviegormlqkqlbhnhblkmglxcbszblfipsyumcrjrkrnzplkveznbtdbtlcptgswhiqsjugqrvujkzuwvoxbjremyxqqzxkgerhgtidsefyemtmstsznvgohexdgetqbhrxaomzsamapxhjibfvtbquhowyrwyxthpwvmfyyqsyibemnfbwkddtyoijzwfxhossylygxmnznpegtgvlrsreepkrcdgbujkghrgtsxwlvxrgrqxnvgqkppbkrxjupjfjcsfzepdemaulfetn"
    print(f'My Answer  : {MyAnswer().longestPalindrome(testcase)}')
    print(f'Solution 1 : {Solution1().longestPalindrome(testcase)}')
