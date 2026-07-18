class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        ans = ""
        count = Counter(s)
        if y in count:
            con = count[y]
            for _ in range(con):
                ans += y

            del count[y]
        for key, value in count.items():
            for _ in range(value):
                ans += key
        return ans
        