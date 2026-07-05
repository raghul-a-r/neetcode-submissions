class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ''
        for i in strs:
            ans += i + 'RaGhUl'
        return ans

    def decode(self, s: str) -> List[str]:
        ans = s.split('RaGhUl')
        return ans[:-1]
