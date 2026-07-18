class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        MOD = 10**9 + 7
        count0 = count1 = count2 = 0
        finalans = 0

        for num in nums:
            if num < a:
                label = 0
            elif num <= b:
                label = 1
            else: 
                label = 2
                
            if label == 0:
                finalans += count1 + count2
            elif label == 1:
                finalans += count2

            if label == 0:
                count0 += 1
            elif label == 1:
                count1 += 1
            else:
                count2 += 1

        return finalans % MOD