class Solution:
    def stoneGameIII(self, stone_value: List[int]) -> str:
        @cache
        def dp(i: int) -> int:
            take_one = stone_value[i] - dp(i + 1) \
                if i <= n - 1 else 0
            take_two = stone_value[i] + stone_value[i + 1] - dp(i + 2) \
                if i <= n - 2 else -maxsize
            take_three = stone_value[i] + stone_value[i + 1] + stone_value[i + 2] - dp(i + 3) \
                if i <= n - 3 else -maxsize

            return max(take_one, take_three, take_two)

        n = len(stone_value)
        score = dp(0)

        return {
            score > 0: 'Alice',
            score < 0: 'Bob',
        }.get(True, 'Tie')
